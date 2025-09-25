from flask_restx import Namespace, Resource
from flask import request

from app.setup_db import db
from app.container import movie_service
movies_ns = Namespace('movies')

# Класс обработки данных всех фильмов
@movies_ns.route('/')
class MoviesView(Resource):
    # Метод получения всех фильмов
    def get(self):
        data = request.args
        return movie_service.get_all(data), 200

    # Метод создания фильма
    def post(self):
        json_data = request.json
        return movie_service.create(json_data)

# Класс обработки данных одного фильма
@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    # Метод получения фильма по его id
    def get(self, mid):
        return movie_service.get_one(mid)


    # Метод полного изменения информации о фильме
    def put(self, mid):
        data = request.json
        data['mid'] = mid
        return movie_service.update(data)

    # Метод для удаления данных о фильме
    def delete(self, mid):
        return movie_service.delete(mid)