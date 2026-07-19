import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report():
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"
    assert REPORT_PATH.stat().st_size > 0, "report.json is empty"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_report_has_required_keys():
    """The report is a JSON object with exactly the three required keys."""
    data = _load_report()
    assert isinstance(data, dict), "report.json must contain a JSON object"
    assert set(data.keys()) == {"total_requests", "unique_ips", "top_path"}, (
        f"expected keys total_requests, unique_ips, top_path — got {sorted(data.keys())}"
    )


def test_total_requests_correct():
    """total_requests matches the number of lines in access.log (6)."""
    data = _load_report()
    assert data["total_requests"] == 6, (
        f"expected total_requests == 6, got {data.get('total_requests')}"
    )


def test_unique_ips_correct():
    """unique_ips matches the number of distinct client IPs in access.log (3)."""
    data = _load_report()
    assert data["unique_ips"] == 3, (
        f"expected unique_ips == 3, got {data.get('unique_ips')}"
    )


def test_top_path_correct():
    """top_path is the most-requested path in access.log (/index.html, 3 hits)."""
    data = _load_report()
    assert data["top_path"] == "/index.html", (
        f"expected top_path == '/index.html', got {data.get('top_path')}"
    )
