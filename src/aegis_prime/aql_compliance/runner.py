import subprocess
import yaml
from pathlib import Path
import sys
import argparse


def run_query(input_data: str, query: str):
    proc = subprocess.run(
        ["aegis", "query", query],
        input=input_data.encode(),
        capture_output=True,
    )
    return {
        "stdout": proc.stdout.decode().strip(),
        "stderr": proc.stderr.decode().strip(),
        "exit_code": proc.returncode,
    }


def load_cases(cases_dir: Path):
    files = list(cases_dir.glob("*.yaml"))

    if not files:
        print(f"❌ No test files found in {cases_dir}")
        sys.exit(1)

    cases = []
    for file in files:
        with open(file, "r") as f:
            data = yaml.safe_load(f)

            if not isinstance(data, list):
                print(f"❌ Invalid format in {file} (expected list)")
                sys.exit(1)

            cases.extend(data)

    return cases


def run_case(case):
    result = run_query(case["input"]["data"], case["query"])
    expected = case.get("expected", {})

    ok = True

    if result["stdout"].strip() != expected.get("stdout", "").strip():
        ok = False

    if result["exit_code"] != expected.get("exit_code", 0):
        ok = False

    return ok, result


def main():
    parser = argparse.ArgumentParser(description="AQL Compliance Suite")
    parser.add_argument(
        "--cases",
        type=str,
        help="Path to test cases directory",
    )

    args = parser.parse_args()

    # Default location (fallback)
    if args.cases:
        cases_dir = Path(args.cases)
    else:
        cases_dir = Path(__file__).parent / "cases"

    print("AQL Compliance Suite v0.1\n")
    print(f"Using cases from: {cases_dir}\n")

    cases = load_cases(cases_dir)

    passed = 0

    for case in cases:
        ok, _ = run_case(case)

        if ok:
            print(f"🟢 {case['id']}")
            passed += 1
        else:
            print(f"🔴 {case['id']}")

    total = len(cases)

    print("\n" + "=" * 50)
    percent = (passed / total) * 100 if total else 0

    status = "🟢 COMPLIANT" if percent == 100 else "🔴 NON-COMPLIANT"

    print(status)
    print(f"Passed: {passed}/{total} ({percent:.1f}%)")
    print("=" * 50)


if __name__ == "__main__":
    main()