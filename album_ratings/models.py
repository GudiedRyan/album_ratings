from album_ratings import db

class AlbumModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    artist = db.Column(db.String(50))
    release_year = db.Column(db.Integer)
    rating = db.Column(db.String(1))

    def __repr__(self):
        return f"AlbumModel('{self.name}', '{self.artist}')"