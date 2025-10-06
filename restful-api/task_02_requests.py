#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    parsed = r.json()
    for elements in parsed:
        for key, value in elements.items():
            if key == 'title':
                print(value)


def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    parsed = r.json()
    my_list = []
    for elements in parsed:
        my_dict = {}
        for key, value in elements.items():
            if key in ('id', 'title', 'body'):
                my_dict[key] = value
        my_list.append(my_dict)
    fieldnames = ['id', 'title', 'body']
    with open('posts.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(my_list)
