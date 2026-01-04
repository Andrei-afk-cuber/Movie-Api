# My mini API
## Description
This API is my homework. I made it using Flask, flask-restx, flask-sqlalchemy and Marshmallow. 
This API is designed to work with interconnected movies, modes, and genres.
## Running in IDE
Clone git repository:

`git clone https://github.com/Andrei-afk-cuber/homework_lesson_18.git`

Create a virtual environment:

`python -m venv .venv`

Install dependencies:

`pip install -r requirements.txt`

Run the application:

`python main.py`
## Running in Docker
Build the Docker image:

`docker build -t [IMAGE_NAME] .`

Run the container:

`docker run [IMAGE_NAME]`

Alternatively, pull and run the pre-built image:

`docker run andreilyakh/movie-api`