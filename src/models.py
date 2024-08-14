from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


    
class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    favorite_characters = db.relationship("Character", backref = "favorites")
    favorite_planets = db.relationship("Planet", backref = "favorites")
    user = db.relationship("User", backref = "favorites")

    def serialize(self):
         return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "character_id": self.character_id, 
            "planet_id": self.planet_id
        }


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email 
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.name,
            "favorites": [favorite.serialize() for favorite in self.favorites]
        }



class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birth_year = db.Column(db.String(50))
    height = db.Column(db.String(50))
    gender = db.Column(db.String(50))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "height": self.height, 
            "gender": self.gender
        }

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique = True)
    population = db.Column(db.BigInteger, nullable=True)
    rotation_period = db.Column(db.String(50))
    terrain = db.Column(db.String(50), nullable=True)
    gravity = db.Column(db.String(50), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "rotation_period": self.rotation_period,
            "terrain": self.terrain,
            "gravity": self.gravity
        }

