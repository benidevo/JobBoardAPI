# Jobs Board REST API 

This is a simple REST API for listing and viewing job offerings. Clients wil be able to communicate with this Web API from 2 endpoints:
api/jobs/ - accepts GET and POST methods, allowing a user to create new instances and retrieve a list with all the available job offers. 
api/jobs/<id>/ - accepts GET and PUT and DELETE methods, allowing a user to retrieve, update or delete an object instance.

## Technologies 

The following technologies were used in this project:

- [Python](https://www.python.org/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [SQLite3](https://www.sqlite.org/index.html)

## Requirements

Before starting, you need to have [Git](https://git-scm.com) and [Python 3.9](https://www.python.org/)installed. Alternatively, you can download the code as a zip file

## Clone this project

    git clone https://github.com/benidevo/JobBoardAPI.git

## Create virtual environment

    python3 -m venv env

## Activate virtual environment

    . env/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate

## Run tests

    python manage.py test

## Start server

    python manage.py runserver


# Endpoints

The endpoints and responses are described below.

## Get list of Jobs

### Request

`GET api/jobs/`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/jobs

### Response

    {
        "message": "success",
        "data": {
            "job offers": {
                "id": <UUID>,
                "company_name": <string>,
                "company_email": <string>,
                "job_title": <string>,
                "job_description": <string>,
                "salary": <integer>,
                "city": <string>,
                "state": <string>,
                "created_at": <string>,
                "is_available": <boolean>
            }
        },
        "errors": null
    }

## Create a new job listing

### Request

`POST api/jobs/`

    curl -i -H 'Accept: application/json' -d 'name=Foo&status=new' http://localhost:8000/api/s

### Response

    {
        "message": "success",
        "data": {
            "job offers": {
                "id": <UUID>,
                "company_name": <string>,
                "company_email": <string>,
                "job_title": <string>,
                "job_description": <string>,
                "salary": <integer>,
                "city": <string>,
                "state": <string>,
                "created_at": <string>,
                "is_available": <boolean>
            }
        },
        "errors": null
    }

## Get a specific job listing by ID

### Request

`GET api/jobs/id`

    curl -i -H 'Accept: application/json' http://localhost:8000/jobs/<id>

### Response

    {
        "message": "success",
        "data": {
            "job offers": {
                "id": <UUID>,
                "company_name": <string>,
                "company_email": <string>,
                "job_title": <string>,
                "job_description": <string>,
                "salary": <integer>,
                "city": <string>,
                "state": <string>,
                "created_at": <string>,
                "is_available": <boolean>
            }
        },
        "errors": null
    }

## Update a job offer

### Request

`PUT api/jobs/<id>`

    curl -i -H 'Accept: application/json' http://localhost:8000/jobs/<id>

### Response

    {
        "message": "success",
        "data": {
            "job offers": {
                "id": <UUID>,
                "company_name": <string>,
                "company_email": <string>,
                "job_title": <string>,
                "job_description": <string>,
                "salary": <integer>,
                "city": <string>,
                "state": <string>,
                "created_at": <string>,
                "is_available": <boolean>
            }
        },
        "errors": null
    }

## Delete a job offerring

### Request

`DELETE api/jobs/api`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/jobs/<id>

### Response

    {
        "message": "success",
        "data": {
            "data": {}
        },
        "errors": null
    }
