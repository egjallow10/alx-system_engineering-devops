#!/usr/bin/python3
'''
Using the JSONPlaceholder API, returns the TODO list
corresponding to a given employee ID.
USAGE:
>$ ./0-gather_data_from_an_API.py <NUMERIC_ID>
Employee [EMPLOYEE_NAME] is done with tasks(#_DONE_TASKS/TOTAL_#_TASKS):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
'''


if __name__ == '__main__':
    import requests
    from sys import argv

    try:
        employee_id = int(argv[1])
        api_url = 'https://jsonplaceholder.typicode.com'
        users = requests.get(
            '{}/users/{}'.format(api_url, employee_id))
        name = users.json()['name']
        todos = requests.get(
            '{}/todos?userId={}'.format(api_url, employee_id))
        total_tasks = len(todos.json())
        done_tasks = 0
        done_titles = ""
        for i in todos.json():
            if i['completed'] is True:
                done_tasks += 1
                done_titles += "\n\t {}".format(i['title'])
        print('Employee {} is done with tasks({}/{}):{}'.format(
            name, done_tasks, total_tasks, done_titles))
    except(RuntimeError, TypeError, NameError):
        pass
