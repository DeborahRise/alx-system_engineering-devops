#!/usr/bin/python3
""" Write a Python script that, uses REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests as r
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    usr = r.get(url + "users/{}".format(user_id)).json()
    username = usr.get("username")
    to_do = r.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, elm.get("completed"),
                          elm.get("title")]) for elm in to_do]
