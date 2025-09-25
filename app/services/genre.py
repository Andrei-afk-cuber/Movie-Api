from app.dao.models.genres_model import GenreSchema

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

class GenreService:
    def __init__(self, movie_dao):
        self.dao = movie_dao

    def get_all(self, data):
        return genres_schema.dump(self.dao.get_all(data))

    def get_one(self, mid):
        return genre_schema.dump(self.dao.get_one(mid))