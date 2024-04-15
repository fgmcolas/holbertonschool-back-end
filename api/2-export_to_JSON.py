#!/usr/bin/python3
"""Script to fetch and export employee TODO list
progress from a REST API to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employeeId(int)")
        sys.exit(1)

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

    user_tasks = {employeeId: []}
    for task in data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": task["user"]["username"]
        }
        user_tasks[employeeId].append(task_dict)

    with open(f"{employeeId}.json", "w") as file:
        json.dump(user_tasks, file)
