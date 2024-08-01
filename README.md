# Chat API

A Django REST API that allows users to send messages and receive AI-generated responses. The API supports user authentication, token management, and chat history logging.

## Features

- User registration and login
- JWT authentication
- Token deduction for each message sent
- Predefined AI responses
- Chat history logging

## Setup

### Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework
- Django REST Framework SimpleJWT

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vinnywalker96/Upnyx-Innovative-Solutions
    cd Upnyx-Innovative-Solutions
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### User Registration

- **Endpoint:** `/api/signup/`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
        "username": "your_username",
        "password": "your_password",
    }
    ```

- **Response:**

    ```json
    {
        "id": 1,
        "username": "your_username",
    }
    ```

### User Login

- **Endpoint:** `/api/login/`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```

- **Response:**

    ```json
    {
        "refresh": "your_refresh_token",
        "access": "your_access_token"
    }
    ```

### Send Message

- **Endpoint:** `/api/chat/`
- **Method:** `POST`
- **Headers:**
  - `Authorization: Bearer <your_access_token>`
- **Request Body:**

    ```json
    {
        "message": "hi"
    }
    ```

- **Response:**

    ```json
    {
        "id": 1,
        "user": 1,
        "message": "hi",
        "response": "Hello! How can I help you today?",
        "timestamp": "2024-08-01T12:00:00Z"
    }
    ```

### Check Token Balance

- **Endpoint:** `/api/token-balance/`
- **Method:** `GET`
- **Headers:**
  - `Authorization: Bearer <your_access_token>`
- **Response:**

    ```json
    {
        "username": "your_username",
        "tokens": 900
    }
    ```

## Running Tests

To run tests, use the following command:

```bash
python manage.py test
