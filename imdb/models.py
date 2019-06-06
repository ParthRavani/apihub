from imdb import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    production = db.Column(db.String(60), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    popularity = db.Column(db.String(20), nullable=False)
    year = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Movie('{self.name}', '{self.production}, '{self.genre}', '{self.popularity}', '{self.year}')"
