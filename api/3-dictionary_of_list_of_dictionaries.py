#!/usr/bin/python3
"""Script to retrieve data from a REST API
and export it in JSON format."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    # Retrieve user data
    users = requests.get(f"{url}/users").json()

    # Create dictionary to store tasks for each user
    user_tasks = {}
    for user in users:
        # Retrieve tasks for each user
        tasks = requests.get(f"{url}/users/{user['id']}/todos").json()

        # Store tasks in dictionary
        user_tasks[user["id"]] = []
        for task in tasks:
            task_dict = {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            user_tasks[user["id"]].append(task_dict)

    # Export data to JSON file
    with open("todo_all_employees.json", "w") as file:
        json.dump(user_tasks, file)
