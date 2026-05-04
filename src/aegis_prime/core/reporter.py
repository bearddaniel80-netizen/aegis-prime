from datetime import datetime
from pathlib import Path
import json
from aegis_prime.core.settings import CLUSTER, REPORT

def load_merged_clusters():
    with open(CLUSTER, "r") as f:
        data = json.load(f)
    return data

def generate_html_report(output_path=REPORT):
    output = load_merged_clusters()

    if not output:
        print("❌ No test run data found")
        return

    failures = [ item['files'] for item in output ]

    html = f"""
    <html>
    <head>
        <title>Aegis Report</title>
        <style>
            body {{ font-family: Arial; padding: 20px; }}
            .fail {{ color: red; }}
        </style>
    </head>
    <body>
        <h1>Aegis Report</h1>
        <p>Generated: {datetime.now()}</p>

        <h2>Failures ({len(failures)})</h2>
        <ul>
            {''.join(f'<li class="fail">{f}</li>' for f in failures)}
        </ul>
    </body>
    </html>
    """

    Path(output_path).write_text(html)

    print(f"📄 Report generated: {output_path}")