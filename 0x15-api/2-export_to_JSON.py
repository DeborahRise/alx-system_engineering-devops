#!/usr/bin/python3
""" Write a Python script that, uses REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys
import json

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    # Make a GET request to the API
    response = requests.get(url + "users/{}".format(user_id))

    # Check if the request was successful
    if response.status_code == 200:
        user = response.json()
        params = {"userId": user_id}
        username = user['username']
        todos_response = requests.get(url + "todos", params=params)
        tasks = todos_response.json() 
        
        task_dict = {user_id: []}
        for task in tasks:
            task_info = {"task": task["title"], "completed": task["completed"],
                "username": username}
            task_dict[user_id].append(task_info)

        json_filename = "{}.json".format(user_id)
        with open(json_filename, "w") as jsonfile:
            json.dump(task_dict, jsonfile, indent=4)