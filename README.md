# Upnyx-Innovative-Solutions

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [APIUSAGE](#apiusage)


## Introduction
  Building REST APIs for an AI Chat System
  You have been tasked with developing REST APIs using Django for an AI chat system. The system allows users to register, login, and interact with an AI-powered chatbot. The chatbot provides responses to user queries and deducts tokens from the user's account for each question asked. Below are the models for the system:

## Features
- **Task 1**: User Registration API: Django REST API endpoint that allows users to register with the chat system. Users should provide a unique username and a password. Upon successful registration, a new user should be created with 4000 tokens assigned to their account. Return an appropriate response indicating the success or failure of the registration process.
- **Task 2**: Django REST API endpoint that allows users to log in to the chat system. Users should provide their username and password. Upon successful login, return an authentication token that will be used for subsequent API calls. You can generate a random token or use any appropriate token generation method available in Django.
- **Task 3**: Implement a Django REST API endpoint that accepts user messages and returns AI-generated responses. Users should provide their authentication token and the message they want to send. The API should deduct 100 tokens from the user's account for each question asked. For the sake of simplicity, you can hardcode a dummy value as the response for each question. Save the chat history in the Chat model, including the user, message, response, and a timestamp.
- **Task 4**: Django REST API endpoint that allows users to check their token balance. Users should provide their authentication token, and the API should return the remaining number of tokens in the user's account.


## Installation
To get started with Toota, follow these steps:

### Backend (Django)
1. Clone the repository:
    ```bash
    git clone https://github.com/MfundoDon/toota.git
    ```
2. Navigate to the backend directory:
    ```bash
    cd server 
    ```
3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Apply migrations and start the server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```
6. Access the Swagger API documentation:
    - Open your browser and go to `http://127.0.0.1:8000/swagger/` to view the API documentation.
