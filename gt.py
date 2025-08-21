import csv
import json

# Example log entries
logs = [
    {"email": "user1@example.com", "url": "http://malicious.com"},
    {"email": "user2@example.com", "url": "http://safe.com"}
]

# IOC list
ioc_list = ["malicious.com", "badsite.net"]

alerts = []

for log in logs:
    if any(ioc in log['url'] for ioc in ioc_list):
        alerts.append(log)

# Save alerts to JSON
with open('alerts.json', 'w') as f:
    json.dump(alerts, f, indent=4)

print(f"{len(alerts)} alert(s) detected!")