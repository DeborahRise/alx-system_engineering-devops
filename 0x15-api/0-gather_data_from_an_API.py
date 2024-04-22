#!/usr/bin/python3

""" Write a Python script that, uses REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys
import json

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    
    # Make a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        tasks = response.json()
        total_tasks = len(tasks)
        
        # Count completed tasks
        completed_tasks = sum(1 for task in tasks if task['completed'])
        
        print("Employee {} is done with tasks ({}/{})".format(user_id, completed_tasks, total_tasks))
        
        # Print titles of completed tasks
        for task in tasks:
            if task['completed']:
                print("\t{}".format(task['title']))