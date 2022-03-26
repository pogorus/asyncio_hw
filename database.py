from gino import Gino


PG_DSN = 'postgres://asyncio:1234@127.0.0.1:5432/asyncio'
db = Gino()


class Person(db.Model):

    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    birth_year = db.Column(db.String)
    eye_color = db.Column(db.String)
    films = db.Column(db.String)
    gender = db.Column(db.String)
    hair_color = db.Column(db.String)
    height = db.Column(db.String)
    homeworld = db.Column(db.String)
    mass = db.Column(db.String)
    name = db.Column(db.String)
    skin_color = db.Column(db.String)
    species = db.Column(db.String)
    starships = db.Column(db.String)
    vehicles = db.Column(db.String)
