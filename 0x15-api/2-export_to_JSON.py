#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees """
import json
import requests
import sys


def get_user_name(id) -> str:
    """fetch username"""
    uri = f"https://jsonplaceholder.typicode.com/users/{id}"
    name = requests.get(uri).json().get("username")
    return name


def main():
    """main fun"""
    url_for_all_todos = 'https://jsonplaceholder.typicode.com/todos/'
    user_id = int(sys.argv[1])
    userName = get_user_name(user_id)

    all_todos = requests.get(url_for_all_todos).json()
    user_todos = [i for i in all_todos if i.get("userId") == user_id]

    todos = []

    for todo in user_todos:
        obj = {"task": f'{todo.get("title")}', "completed":
               todo.get("completed"), "username": userName}
        todos.append(obj)

    data = {f"{user_id}": todos}
    dt = json.dumps(data)

    with open(f"{user_id}.json", "w") as f:
        f.write(dt)


if __name__ == "__main__":
    main()
