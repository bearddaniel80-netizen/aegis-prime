import re
from typing import List
from aegis_prime.models.failure import FailureCluster
from aegis_prime.core.model_enums import ErrorType

def from_value(enum_cls, value: str):
    return next((e for e in enum_cls if e.value == value), None)

def parse_pytest_failures(data: dict) -> List[FailureCluster]:
    failures = []

    for test in data.get("tests", []):
        if test.get("outcome") != "failed":
            continue

        nodeid = test["nodeid"]
        line_no = test["lineno"]
        file = test["keywords"]

        call = test.get("call", {})
        longrepr = call.get("longrepr", "")

        error_type = "Unknown"
        message = longrepr

        if "AssertionError" in longrepr:
            error_type = "AssertionError"

        failures.append(
            FailureCluster(
                error_type=from_value(ErrorType, error_type),
                message=message,
                files=file,
                line=line_no,
                tests=nodeid,
                stack_traces=[longrepr],
            )
        )

    return failures