# Robot API Test Execution

This project is a Django application designed to execute Robot Framework test cases via HTTP requests. It provides a simple API endpoint that accepts JSON data containing test cases, dynamically generates Robot Framework test files, executes the tests, and returns the results in JSON format.

## Installation

1. Clone the repository:

    ```
    git clone <repository_url>
    ```

2. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

3. Make migrations and apply them:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

## Usage

1. Start the Django development server:

    python manage.py runserver

2. Send POST requests to the `/http://127.0.0.1:8000/testai/tests/v1/execute` endpoint with JSON data containing test cases.

3. Receive the test results in JSON format.

## Project Structure

- `api/`: Django application directory.
    - `views.py`: Contains the view function for executing test cases.
    - `models.py`: Contains the models for the application (currently not utilized).
- `README.md`: This file providing instructions and information about the project.
- `requirements.txt`: Contains the required Python packages for the project.
- `manage.py`: Django project management script.
- `temp_files/`: Temporary directory for storing dynamically generated test files.

## Dependencies

- Django: Web framework for building the API.
- Robot Framework: Test automation framework for writing and executing test cases.
- SeleniumLibrary: Robot Framework library for web browser automation.

