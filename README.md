# Delivery Hero

## Task

The objective of this code challenge is to develop a backend service or api that returns json over http.
We would like to have a CRUD (create, read, update, delete) on restaurant objects. A restaurant object will have the following fields:

- id: int
- name: string
- opens_at: time
- closes_at: time

For example, a call to the system could be something like:

`GET /restaurant/1`

And the output would be
{
"id": 1,
"name": "Pizza Berlin",
...
}


## Deploy

- install and activate virtual environment
- `pip install requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`

