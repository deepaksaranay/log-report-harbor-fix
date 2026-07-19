There is an Apache-style access log at /app/access.log. Parse it and write a
summary report as JSON to /app/report.json.

The report must be a single JSON object with exactly these three keys:

1. "total_requests" — the total number of log lines (requests) in the file.
2. "unique_ips" — the number of distinct client IP addresses that appear.
3. "top_path" — the request path (e.g. "/index.html") that appears most often
   across all requests. If there is a tie, any of the tied paths is acceptable.

Write the file to the exact path /app/report.json. Do not create any other
output files.

You have 120 seconds to complete this task.
