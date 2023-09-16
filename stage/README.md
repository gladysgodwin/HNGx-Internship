# HNGx STAGE TWO TASK


## Person Management API

This API allows you to perform CRUD (Create, Read, Update, Delete) operations on a "person" resource in a secure and efficient manner. This documentation provides details on setting up, using the API, and understanding its functionalities.


## Getting Started


## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [API Endpoints](#api_endpoints)
- [Request and Response Formats](#response_formats)
- [Sample Usage](#sample_usage)
- [Known Limitations and Assumptions](#known_limitations)
- [UML Diagram](#uml_diagram)

## Prerequisites
Before you begin using the Django Person Management API, make sure you have the following prerequisites in place:

- Python (3.6 or higher) installed on your system.
- Git for cloning the project repository.
- PostgreSQL database or another database of your choice configured and accessible.
- Django framework installed.



## Installation
1. Clone this repository to your local machine:

```bash
git clone https://github.com/Deedeo/HNG_intership.git
cd Stage_two
```
2. Install the project dependencies:

```bash
pip install requiremnents.txt
```

3. Configure the Database connection in the settings.py file:

    >  database_url = URL of your database.

4. Start the server:

```bash
python manage.py runserver
```
Your API should now be running at http://localhost:8000.

## API Endpoints

### READ: Fetching details of Persons
- GET /api/
-  Retrieves the details of Persons by in the database using this URL.

### READ: Fetching details of a person
- GET /api/id
- Retrieve a person's details by providing their unique identifier in the URL.

### CREATE: Adding a Person
- POST /api/
- Create a new person by sending a JSON payload with the person's details in the request body. Required field: name.


### UPDATE: Modifying details of an existing person
- PUT /api/id
- Update a person's details by providing their unique identifier in the URL and sending a JSON payload with the updated details in the request body.

### DELETE: Removing a person
- DELETE /api/id
- Delete a person by providing their unique identifier in the URL.

## Request and Response Formats

- Requests and responses are in JSON format.
- Request payloads should follow the format specified in the API documentation.
- Successful responses will have a status code of 200 OK and 201 created.
- Error responses will have appropriate status codes (e.g. 404 Not Found, 500 Internal Server Error, 201 Created, 204 NO_CONTENT) along with an error message in the response body.

## Sample Usage

### CREATE: Adding a new person
- Request:

```bash
POST http://localhost:8000/api/
Content-Type: application/json

{
  "name": "Gladys Godwin"
}
```
- Response (201 Created):

```bash
{
    "success": true,
    "person": "{
        "id": "1",
        "name": "Gladys Godwin"
        
    }"
}
```
### READ: Fetching details of a persons

- Request:
```bash
GET http://localhost:8000/api/
```

- Response (200 OK):

```bash
{
    "success": true,
    "person": [
        {
            "id": "1",
            "name": "Gladys Godwin"
        },
        {
            "id": "2",
            "name": "Marvelous Godwin"
        }
    ]
}
  
```

### READ: Fetching details of a person

- Request:
```bash
GET http://localhost:8000/api/1
```

- Response (200 OK):

```bash
{
    "success": true,
    "person": {
        "id": "1",
        "name": "Gladys Godwin"
    }"
}
    
```

### UPDATE: Modifying details of an existing person

- Request:
```bash
PUT http://localhost:8000/api/1
Content-Type: application/json

{
  "name": "Gladys Oviawe"
}
```

- Response (200 OK):

```bash
{
    "success": true,
    "person": {
        "id": "1",
        "name": "Gladys Oviawe"
    }"
}
```

### DELETE: Removing a person

- Request:

```bash
DELETE http://localhost:8000/api/1
Response (200 OK):
```
```bash
{
    "success": true
}
```

## Known Limitations and Assumptions

Environment Variable in settings.py:

- Ensure that users are aware of the necessity of setting environment variables in the settings.py file.

- API assumes MySQL as the database and that users need to provide the appropriate database_url in the settings.py file. 

- API performs basic data validation checks, such as checking for required fields and data types. 

- string validation is configured. This could include details on string length restrictions.


## UML Diagram

![UML Diagram]![nameapp drawio](https://github.com/gladysgodwin/HNGx-Internship/assets/99274632/0a52522b-5b7d-4a7f-9e6a-40ac76a91e05)




### Testing Script
