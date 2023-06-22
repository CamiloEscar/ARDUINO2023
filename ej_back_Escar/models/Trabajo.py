from api_config import db

class Trabajo(db.Model):
    __tablename__ = "trabajo"
    idt = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.String(100))
    cargo = db.Column(db.String(100))
    persona_fk = db.Column(db.Integer, db.ForeignKey("persona.id"))
    lugar_trabajo_fk = db.Column(db.Integer, db.ForeignKey("lugar_trabajo.id"))
    lugar_trabajo = db.relationship('LugarTrabajo', backref='trabajo')