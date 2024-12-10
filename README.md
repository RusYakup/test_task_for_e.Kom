# FastAPI Project
================

Brief description of the project.

## Description

This web application is designed to identify filled forms based on templates stored in a database. The application accepts a list of fields with values in the body of a POST request and returns the name of the form that best matches the provided list of fields. If a matching form is not found, the application performs on-the-fly typing of the fields and returns a list of fields with their types.

## Functionality

* The application accepts a list of fields with values in the body of a POST request.
* The application searches for a suitable form template in the database.
* If a form template is found, the application returns the name of the form.
* If a form template is not found, the application performs on-the-fly typing of the fields and returns a list of fields with their types.

## Field Types

* email
* phone
* date
* text

## Validation Rules

* Email: must match the pattern `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$`.
* Phone: must match the pattern `^\+7\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2}$`.
* Date: must match the pattern `^\d{4}\.\d{2}\.\d{2}|\d{2}\.\d{2}\.\d{4}$`.

## Example Responses

* If the form template is found: `{"form_name": "form_name"}`
* If the form template is not found: `{"f_name1": "field_type", "f_name2": "field_type"}`

## Test Script

In the `scripts` folder, there is a script `test_requests.py` that sends test requests to the application.

```bash
python scripts/test_requests.py
````

## Requirements
------------

*   **Python 3.12+**: Python 3.12+: Python version 3.12 or higher is required.

*   **FastAPI**: FastAPI: FastAPI is required to create the API.
*   **Pydantic**: Pydantic: Pydantic is required for data validation.
*   **Motor**: Motor: Motor is required for asynchronous interactions with MongoDB.
*   **MongoDB**: MongoDB: MongoDB is required for data storage.

## Installation
------------

### Step 1: Clone the Repository

```bash
git clone git@github.com:RusYakup/test_task.git

````


### Step 2: Start Docker Compose

```
cd /deploy
docker compose up -d
```

