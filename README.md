# HackerNews Top 10 New Stories

## Overview
This application retrieves the Top 10 new stories from the HackerNews API using a FastAPI backend and displays them on a React.js frontend.

## Technologies
- **Backend:** FastAPI (Python)
- **Frontend:** React.js (JavaScript)
- **Docker:** For containerization
- **Docker Compose:** For managing multi-container Docker applications

## How to Run

### Prerequisites
Ensure you have the following installed:
- Docker
- Docker Compose

### Steps to run this application locally:
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/techwithradhika/HackerNews.git
    ```
    After cloning repo, Navigate to the project directory:
    ```bash
    cd HackerNews
    ```

2. **Build and Start Services:**
    Run the following command to start the backend and frontend services using Docker Compose:
    ```bash
    docker-compose up --build
    ```
    Wait until the Docker containers to started and the frontend development server is running. This may take a few moments.

3. **Access the Application:**
    To access the application in your browser, navigate to "http://localhost:3000" and view the React application displaying the Top 10 new stories.
