# Flask Docker Skeleton Project

## Overview
This skeleton project provides a foundation for building a RESTful API using Flask and containerizing it with Docker. It's designed to test your skills in web development, API design, machine learning integration, and containerization.

## Tech Stack
- Python 3.11
- Flask: A lightweight WSGI web application framework
- Gunicorn: A Python WSGI HTTP Server for UNIX
- Docker: A platform for developing, shipping, and running applications

## Prerequisites
- Docker installed on your local machine

## Project Structure
```
project_root/
├── Dockerfile
├── requirements.txt
├── app.py
└── README.md
```

## Your Task
1. Implement the API in `app.py`, including an inference endpoint for a machine learning model
2. Build and run the Docker container
3. Make successful requests to your API

## Detailed Requirements
- Create an inference endpoint that accepts input data and returns predictions using a machine learning model of your choice
- Implement proper error handling and input validation
- Ensure the API follows RESTful principles

## Getting Started

### 1. API Implementation
- Open `app.py` and implement the required endpoints and logic
- Ensure your code follows PEP 8 style guidelines
- Add any necessary dependencies to `requirements.txt`

### 2. Building the Docker Image
```
docker build -t <image-name>:<version> .
```

### 3. Running the Container
```
docker run -p 50505:50505 <image-name>:<version>
```

### 4. Testing Your API
Use curl or any API testing tool to make requests to your endpoints. For example:
```
curl http://localhost:50505
```

## Evaluation Criteria
Your submission will be evaluated based on:
- Correctness of API implementation, including the ML inference endpoint
- Code quality, organization, and adherence to best practices
- Proper use of Docker
- API functionality and adherence to RESTful principles
- Error handling and input validation

## Bonus Features
While not required, implementing any of the following will be viewed favorably:
- JWT authentication
- Comprehensive logging
- API documentation (e.g., using Swagger/OpenAPI)
- Unit tests
- Data validation and sanitization
- Rate limiting
- Caching mechanisms

## Submission and Review Process

1. When ready, we will schedule a meeting with you to review your implementation.

2. During this meeting, you will have the opportunity to walk us through your code live. Be prepared to:
   - Explain your design decisions
   - Demonstrate the functionality of your API
   - Discuss any challenges you faced and how you overcame them
   - Answer questions about your implementation

3. This live review allows us to better understand your thought process and gives you a chance to showcase your communication skills and technical knowledge.

We look forward to seeing your implementation and discussing it with you!