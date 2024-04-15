#!usr/bin/bash/python3
"""Python script to fetch and display TODO list
progress for a given employee ID using a REST API"""
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

completed_tasks = [task for task in data if task["completed"]]
total_tasks = len(data)
total_done_tasks = len(completed_tasks)
employee_name = data[0]["user"]["name"]

print(f"Employee {employee_name} is done with tasks"
      f"({total_done_tasks}/{total_tasks}):")
for task in completed_tasks:
    print(f"\t {task["title"]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__} employee_id(int)")
        sys.exit(1)
