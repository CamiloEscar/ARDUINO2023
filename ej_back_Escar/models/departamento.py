# from api_config import db


# class Departamento(db.Model):
#     __tablename__ = "departamento"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     fk_persona = db.Column(db.Integer, db.ForeignKey("persona.id"))
    # persona_id = db.Column(db.Integer, db.ForeignKey("persona.id"))
    # persona = db.relationship("Persona", backref='persona')

#antes
    # fk_persona = db.Column(db.Integer, db.ForeignKey("persona.id"))
    # persona = db.relationship("Persona")


# class Departamento(db.Model):
#     __tablename__ = "departamento"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     # fk_persona = db.Column(db.Integer, db.ForeignKey("persona.id"))
#     # persona = db.relationship("Persona")
#     trabajo = db.relationship("Trabajo", backref="departamento")
#     lugar_trabajo_id = db.Column(db.Integer, db.ForeignKey("lugar_trabajo.id"))
#     lugar_trabajo = db.relationship("LugarTrabajo")