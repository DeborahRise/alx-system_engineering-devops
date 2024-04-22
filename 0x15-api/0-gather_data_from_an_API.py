#!/usr/bin/python3

""" Write a Python script that, uses REST API, for a given employee ID,
returns information about his/her TODO list progress.
Requirements:
You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output of
the employee TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
completed and non-completed tasks

Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
employee_id = sys.argv[1]

    response = requests.get('https://jsonplaceholder.typicode.com/todos/{}'.format(employee_id))

    user = response.json()

    print("Employee {} is done with tasks({}/{})".format(user['name'], user['completed'], user['total_tasks']))
"""

import requests
import sys
import json

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = ('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
    response = requests.get(url)
    user = response.json
    name = user.get('name')
    total_tasks = len(user.get('title'))
    complete_task = [ tasks for task in (user.get('title')), if task.get("completed") ]
    completed_task = len(complete_task)

    print("Employee {} is done with tasks({}/{})".format(name, completed_task, total_tasks))
    for task in (user.get('title')):
        if task.get("completed"):
            print("\t{}".format(task.get("title")))