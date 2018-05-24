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

## Project info
- Python 3.6
- Django 1.11 LTS
- GraphQL
- Factories (factory boy) to create init data


## Deploy

- install and activate virtual environment(`virtualenv -p python3.6 venv`)
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`

OR
- install and activate virtual environment(`virtualenv -p python3.6 venv`)
- use make file (`make <command>`). Use `make help` for help

## Use
- Get restaurant by ID: `/restaurant/<id>`
- Delete restaurant: send DELETE request to url `/restaurant/` with JSON data `{id: <restaurant_id>}`
- Create restaurant: use graphql (url `/graphql/`).
Request example:
```
mutation{
  createRestaurant(restaurantData: {name: "TestGraphQl", opensAt: "01:00:00", closesAt:"23:00:00"})
  {
    ok
    message
    restaurant {
      id
      name
      opensAt
      closesAt
    }
  }
}
```
- Update restaurant: use graphql (url `/graphql/`). ID is a must input, 
other fields are optional
Request example:
```
mutation{
  updateRestaurant(restaurantUpdateData: {id: 2, name: "New Name 2", opensAt:"23:59"}){
    ok
    message
    restaurant {
      name
      opensAt
      closesAt
    }
  }
}
```
- Get all restaurants (additional option). Use graphql. Request example:
```
query{
  getAllRestaurants {
    id
    name
    opensAt
    closesAt
  }
}
```


