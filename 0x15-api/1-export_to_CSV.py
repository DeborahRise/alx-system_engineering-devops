#!/usr/bin/python3
""" Write a Python script that, uses REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    # Make a GET request to the API
    response = requests.get(url + "users/{}".format(user_id))

    # Check if the request was successful
    if response.status_code == 200:
        user = response.json()
        params = {"userId": user_id}
        todos_response = requests.get(url + "todos", params=params)
        tasks = todos_response.json()
        total_tasks = len(tasks)

        # Count completed tasks
        completed_tasks = sum(1 for task in tasks if task['completed'])

        """ print("Employee {} is done with tasks ({}/{})"
              .format(user['username'], completed_tasks, total_tasks))"""

        
        csv_file = "{}.csv".format(user_id)

        with open(csv_file, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
           
            for task in tasks:
                csv_writer.writerow([user_id, user['username'],
                                     task['completed'], task['title']])
