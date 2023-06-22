from api_config import db

class LugarTrabajo(db.Model):
    __tablename__ = "lugar_trabajo"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    direccion = db.Column(db.String(500))