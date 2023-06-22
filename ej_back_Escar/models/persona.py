from api_config import db


class Persona(db.Model):
    __tablename__ = "persona"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(500))
    email  = db.Column(db.String(150), nullable=True)
    # depto_fk = db.Column(db.Integer, db.ForeignKey("departamento.id"))
    # departamento = db.relationship('Departamento', backref='personas_depto')
    trabajo_fk = db.Column(db.Integer, db.ForeignKey("departamento.id"))
    trabajo = db.relationship('Trabajo', backref='trabajo')
