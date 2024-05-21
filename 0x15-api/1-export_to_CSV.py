#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys

if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f'{base_url}/users/{employee_id}'

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = f'{base_url}/todos?userId={employee_id}'
    response = requests.get(todo_url)
    tasks = response.json()

    with open('{}.csv'.format(employee_id), 'w') as file:
        csv_file = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            csv_file.writerow([employee_id, username,
                task.get('completed'), task.get('title')])
