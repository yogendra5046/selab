# Student Test To-Do List Management

This is a simple Flask-based to-do list application to help students manage their test-related tasks.

## Features
- Add tasks to the to-do list.
- Delete tasks from the list.
- View tasks through a web interface or via API.

## How to Run

### Locally:
1. Clone the repository:
    ```bash
    git clone https://github.com/yogendra5046/selab.git
    cd student-todo-app
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

4. Access the app at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Docker:
1. Build the Docker image:
    ```bash
    docker build -t student-todo-app .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 student-todo-app
    ```

## API Endpoints
- `GET /api/tasks` - Fetch all tasks.
- `POST /api/tasks` - Add a new task. Example payload: `{ "name": "Sample Task" }`

## License
MIT
