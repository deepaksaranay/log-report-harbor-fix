
Analyze the Apache-style access log located at /app/access.log.

Generate a JSON report and save it as:

/app/report.json

The report must be valid JSON and contain exactly these fields:

- total_requests: Total number of requests in the log.
- unique_ips: Number of unique client IP addresses.
- top_path: The most frequently requested URL path.

The solution will be evaluated automatically. Ensure the JSON file is written to the correct location and contains the required fields.