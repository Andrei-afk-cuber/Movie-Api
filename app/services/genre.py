from app.dao.models.genres_model import GenreSchema

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

class GenreService:
    def __init__(self, movie_dao):
        self.dao = movie_dao

    def get_all(self):
        return genres_schema.dump(self.dao.get_all())

    def get_one(self, mid):
        try:
            genre = self.dao.get_one(mid)

            if type(genre) == str:
                raise Exception('Genre is not found')

            return genre_schema.dump(self.dao.get_one(mid))
        except Exception as e:
            return str(e), 404