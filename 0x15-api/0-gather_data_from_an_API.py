#!/usr/bin/python3
""" Accessing a REST API for a todo list of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = int(sys.argv[1])
    baseUrl = "https://jsonplaceholder.typicode.com"
    url = baseurl + "/users/" + employeeId


    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = baseurl + "/todos?userId=" + employeeId
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
            .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
