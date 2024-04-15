#!/usr/bin/python3
"""Script to fetch and export employee TODO list
progress from a REST API to CSV"""
import csv
import requests
import sys


url = "https://jsonplaceholder.typicode.com"
employeeId = sys.argv[1]

response = requests.get(
    f"{url}/users/{employeeId}/todos",
    params={"_expand": "user"}
)
data = response.json()

if not len(data):
    print("RequestError:", 404)
    sys.exit(1)

username = data[0]["user"]["username"]

with open(f"{employeeId}.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    for task in data:
        writer.writerow(
            [employeeId, username, str(task["completed"]), task["title"]]
        )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employeeId(int)")
        sys.exit(1)
