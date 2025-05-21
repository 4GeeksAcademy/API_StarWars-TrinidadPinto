from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    nombre = db.Column(db.String(120))
    apellido = db.Column(db.String(120))
    favoritos = db.relationship('Favorito', backref='usuario', lazy=True)
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
        }

class Personajes(db.Model):
    __tablename__ = 'personajes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    genero = db.Column(db.String(20))
    altura = db.Column(db.String(10))
    peso = db.Column(db.String(10))
    color_pelo = db.Column(db.String(10))
    color_ojos = db.Column(db.String(10))
    nacimiento = db.Column(db.String(20))
    favoritos = db.relationship('Favorito', back_populates='personajes', lazy=True)
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "altura": self.altura,
            "peso": self.peso,
            "color_pelo": self.color_pelo,
            "color_ojos": self.color_ojos,
            "nacimiento": self.nacimiento,
        }

class Planeta(db.Model):
    __tablename__ = 'planeta'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    clima = db.Column(db.String(120))
    terreno = db.Column(db.String(120))
    diametro = db.Column(db.String(120))
    poblacion = db.Column(db.String(120))
    favoritos = db.relationship('Favorito', back_populates='planeta', lazy=True)
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "terreno": self.terreno,
            "diametro": self.diametro,
            "poblacion": self.poblacion,
        }

class Vehiculo(db.Model):
    __tablename__ = 'vehiculo'
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(120), nullable=False)
    max_velocidad = db.Column(db.String(20))
    tipo = db.Column(db.String(20))
    capacidad = db.Column(db.String(20))
    favoritos = db.relationship('Favorito', back_populates='vehiculo', lazy=True)
    def serialize(self):
        return {
            "id": self.id,
            "modelo": self.modelo,
            "max_velocidad": self.max_velocidad,
            "tipo": self.tipo,
            "capacidad": self.capacidad
        }
    
class Favorito(db.Model):
    __tablename__ = 'favorito'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    personajes_id = db.Column(db.Integer, db.ForeignKey('personajes.id'), nullable=True)
    planeta_id = db.Column(db.Integer, db.ForeignKey('planeta.id'), nullable=True)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculo.id'), nullable=True)

    personajes = db.relationship('Personajes', back_populates='favoritos')
    planeta = db.relationship('Planeta', back_populates='favoritos')
    vehiculo = db.relationship('Vehiculo', back_populates='favoritos')

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personajes_id": self.personajes_id.serialize() if self.personajes_id else None,
            "planeta_id": self.planeta_id.serialize() if self.planeta_id else None,
            "vehiculo_id": self.vehiculo_id.serialize() if self.vehiculo_id else None
        }