import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from admin import setup_admin
from models import db, Usuario, Personajes, Planeta, Vehiculo, Favorito

app = Flask(__name__)
app.url_map.strict_slashes = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
MIGRATE = Migrate(app, db)
CORS(app)
setup_admin(app)

@app.route('/')
def index():
    return jsonify({"msg": "API de Star Wars activa"}), 200

@app.route('/personajes', methods=['GET'])
def get_personajes():
    personajes = Personajes.query.all()
    return jsonify([p.serialize() for p in personajes]), 200

@app.route('/personajes/<int:personajes_id>', methods=['GET'])
def get_un_personaje(personajes_id):
    personaje = Personajes.query.get(personajes_id)
    if not personaje:
        return jsonify({"msg": "Personaje no encontrado"}), 404
    return jsonify(personaje.serialize()), 200

@app.route('/planetas', methods=['GET'])
def get_planetas():
    planetas = Planeta.query.all()
    return jsonify([p.serialize() for p in planetas]), 200

@app.route('/planetas/<int:planeta_id>', methods=['GET'])
def get_un_planeta(planeta_id):
    planeta = Planeta.query.get(planeta_id)
    if not planeta:
        return jsonify({"msg": "Planeta no encontrado"}), 404
    return jsonify(planeta.serialize()), 200

@app.route('/vehiculos', methods=['GET'])
def get_vehiculos():
    vehiculos = Vehiculo.query.all()
    return jsonify([v.serialize() for v in vehiculos]), 200

@app.route('/vehiculos/<int:vehiculos_id>', methods=['GET'])
def get_un_vehiculo(vehiculo_id):
    vehiculo = Vehiculo.query.get(vehiculo_id)
    if not vehiculo:
        return jsonify({"msg": "Planeta no encontrado"}), 404
    return jsonify(vehiculo.serialize()), 200

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.serialize() for u in usuarios]), 200

@app.route('/usuarios/favoritos', methods=['GET'])
def get_usuario_favoritos():
    favoritos = Favorito.query.all()
    return jsonify([f.serialize() for f in favoritos]), 200

@app.route('/favorito/planeta/<int:planeta_id>', methods=['POST'])
def add_fav_planeta(planeta_id):
    favorito = Favorito(usuario_id=1, planeta_id=planeta_id)  # Simula usuario 1
    db.session.add(favorito)
    db.session.commit()
    return jsonify({"msg": "Planeta añadido a favoritos"}), 201

@app.route('/favorito/personajes/<int:personajes_id>', methods=['POST'])
def add_fav_personajes(personajes_id):
    favorito = Favorito(usuario_id=1, personajes_id=personajes_id)
    db.session.add(favorito)
    db.session.commit()
    return jsonify({"msg": "Personaje añadido a favoritos"}), 201

@app.route('/favorito/vehiculo/<int:vehiculo_id>', methods=['POST'])
def add_fav_vehiculos(vehiculo_id):
    favorito = Favorito(usuario_id=1, vehiculo_id=vehiculo_id)
    db.session.add(favorito)
    db.session.commit()
    return jsonify({"msg": "Vehiculo añadido a favoritos"}), 201

@app.route('/favorito/planeta/<int:planeta_id>', methods=['DELETE'])
def delete_fav_planeta(planeta_id):
    favorito = Favorito.query.filter_by(usuario_id=1, planeta_id=planeta_id).first()
    if favorito:
        db.session.delete(favorito)
        db.session.commit()
        return jsonify({"msg": "Favorito eliminado"}), 200
    return jsonify({"msg": "No se encontró el favorito"}), 404

@app.route('/favorito/personajes/<int:personajes_id>', methods=['DELETE'])
def delete_fav_personajes(personajes_id):
    favorito = Favorito.query.filter_by(usuario_id=1, personajes_id=personajes_id).first()
    if favorito:
        db.session.delete(favorito)
        db.session.commit()
        return jsonify({"msg": "Favorito eliminado"}), 200
    return jsonify({"msg": "No se encontró el favorito"}), 404

@app.route('/favorito/vehiculo/<int:vehiculo_id>', methods=['DELETE'])
def delete_fav_vehiculo(vehiculo_id):
    favorito = Favorito.query.filter_by(usuario_id=1, vehiculo_id=vehiculo_id).first()
    if favorito:
        db.session.delete(favorito)
        db.session.commit()
        return jsonify({"msg": "Favorito eliminado"}), 200
    return jsonify({"msg": "No se encontró el favorito"}), 404

# MAIN --------------
if __name__ == '__main__':
    app.run(debug=True)