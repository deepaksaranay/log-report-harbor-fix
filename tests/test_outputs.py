import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_exists():
    assert REPORT.exists(), "report.json not found"


def test_report_is_valid_json():
    data = json.loads(REPORT.read_text())

    assert isinstance(data, dict)

    required = {
        "total_requests",
        "unique_ips",
        "top_path",
    }

    assert set(data.keys()) == required


def test_report_values():
    data = json.loads(REPORT.read_text())

    assert isinstance(data["total_requests"], int)
    assert data["total_requests"] > 0

    assert isinstance(data["unique_ips"], int)
    assert data["unique_ips"] > 0

    assert isinstance(data["top_path"], str)
    assert data["top_path"].startswith("/")