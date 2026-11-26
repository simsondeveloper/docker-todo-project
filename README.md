
# Dockerized Full-Stack To-Do Application

## Project Overview

A full-stack To-Do application using Node.js, Express,
Python Flask, MongoDB, Docker and Docker Compose.

## Technologies Used

- Frontend: Node.js, Express, EJS
- Backend: Python, Flask
- Database: MongoDB
- Containerization: Docker
- Orchestration: Docker Compose
- Version Control: Git and GitHub

## Project Structure

- frontend/ - Express frontend application
- backend/ - Flask backend API
- docker-compose.yml - Container orchestration
- .gitignore - Ignored files

## Features

- To-Do item submission
- Express to Flask API integration
- MongoDB data storage
- Dockerized frontend and backend
- Docker Compose networking

## Run Application

Build containers:

    docker compose build

Start application:

    docker compose up -d

Open frontend:

    http://localhost:3000

Backend API:

    http://localhost:5000

View saved items:

    http://localhost:5000/items

Stop containers:

    docker compose down

## Docker Hub Images

Frontend:
simson1009/todo-frontend:1.0

Backend:
simson1009/todo-backend:1.0
