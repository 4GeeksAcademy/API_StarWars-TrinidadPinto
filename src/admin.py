from flask_admin import Admin
from models import db, Usuario, Personajes, Planeta, Vehiculo, Favorito
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    print("✅ Flask Admin configurado")
    admin = Admin(app, name='StarWars Admin', template_mode='bootstrap3')

    admin.add_view(ModelView(Usuario, db.session))
    admin.add_view(ModelView(Personajes, db.session))
    admin.add_view(ModelView(Planeta, db.session))
    admin.add_view(ModelView(Vehiculo, db.session))
    admin.add_view(ModelView(Favorito, db.session))
