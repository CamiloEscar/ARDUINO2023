from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
)
from api_config import (
    db,
)

from .objects import (
        Persona
)

from .objects import (
        Trabajo
)

from .objects import (
        LugarTrabajo
)


from .persona import Persona as PersonaModel

from .Trabajo import Trabajo as TrabajoModel

from .lugarTrabajo import LugarTrabajo as LugarTrabajoModel


class createPersona(Mutation):
    class Arguments:
        
        name = String(required=True)
        last_name = String(required=True)
        email = String(required=False)
    
    persona = Field(lambda: Persona)

    def mutate(self, info, name, last_name, email=None):
        persona = PersonaModel(name=name, last_name=last_name, email=email)

        db.session.add(persona)
        db.session.commit()

        return createPersona(persona=persona)

class createTrabajo(Mutation):
    class Arguments:
        job = String(required=True)

    Trabajo = Field(lambda: Trabajo)

    def mutate(self, info, job):
        Trabajo = TrabajoModel(job=job)

        db.session.add(Trabajo)
        db.session.commit()

        return createTrabajo(Trabajo=Trabajo)
    
class CreateLugarTrabajo(Mutation):
    class Arguments:
        nombre = String(required=True)
        direccion = String(required=True)

    lugar_trabajo = Field(lambda: LugarTrabajo)

    def mutate(self, info, nombre, direccion):
        lugar_trabajo = LugarTrabajoModel(nombre=nombre, direccion=direccion)

        db.session.add(lugar_trabajo)
        db.session.commit()

        return CreateLugarTrabajo(lugar_trabajo=lugar_trabajo)

class updatePersona(Mutation):
    class Arguments:
        persona_id = Int(required=True)
        email = String()
        name = String()
        last_name = String()

    persona = Field(lambda: Persona)

    def mutate(self, info, persona_id, email=None, name=None, last_name=None):
        persona = PersonaModel.query.get(persona_id)
        if persona:
            if email:
                persona.email = email
            if name:
                persona.name = name
            if last_name:
                persona.last_name = last_name
            db.session.add(persona)
            db.session.commit()

        return updatePersona(persona=persona)

class updateTrabajo(Mutation):
    class Arguments:
        Trabajo_id = Int(required=True)
        job = String()

    Trabajo = Field(lambda: Trabajo)

    def mutate(self, info, Trabajo_id, job=None):
        Trabajo = TrabajoModel.query.get(Trabajo_id)
        if Trabajo:
            if job:
                Trabajo.job = job
            db.session.add(Trabajo)
            db.session.commit()

        return updateTrabajo(Trabajo=Trabajo)

class UpdateLugarTrabajo(Mutation):
    class Arguments:
        lugar_trabajo_id = Int(required=True)
        nombre = String()
        direccion = String()

    lugar_trabajo = Field(lambda: LugarTrabajo)

    def mutate(self, info, lugar_trabajo_id, nombre=None, direccion=None):
        lugar_trabajo = LugarTrabajoModel.query.get(lugar_trabajo_id)
        if lugar_trabajo:
            if nombre:
                lugar_trabajo.nombre = nombre
            if direccion:
                lugar_trabajo.direccion = direccion
            db.session.add(lugar_trabajo)
            db.session.commit()

        return UpdateLugarTrabajo(lugar_trabajo=lugar_trabajo)

class deletePersona(Mutation):
    class Arguments:
        persona_id = Int(required=True)

    persona = Field(lambda: Persona)

    def mutate(self, info, persona_id):
        persona = PersonaModel.query.get(persona_id)
        if persona:
            db.session.delete(persona)
            db.session.commit()

        return deletePersona(persona=persona)

class deleteTrabajo(Mutation):
    class Arguments:
        Trabajo_id = Int(required=True)
    
    Trabajo = Field(lambda: Trabajo)

    def mutate(self, info, Trabajo_id):
        Trabajo = TrabajoModel.query.get(Trabajo_id)
        if Trabajo:
            db.session.delete(Trabajo)
            db.session.commit()

        return deleteTrabajo(Trabajo=Trabajo)
    
class DeleteLugarTrabajo(Mutation):
    class Arguments:
        lugar_trabajo_id = Int(required=True)

    lugar_trabajo = Field(lambda: LugarTrabajo)

    def mutate(self, info, lugar_trabajo_id):
        lugar_trabajo = LugarTrabajoModel.query.get(lugar_trabajo_id)
        if lugar_trabajo:
            db.session.delete(lugar_trabajo)
            db.session.commit()

        return DeleteLugarTrabajo(lugar_trabajo=lugar_trabajo)
    

class Mutation(ObjectType):
    create_persona = createPersona.Field()
    update_persona = updatePersona.Field()
    delete_persona = deletePersona.Field()
    create_trabajo = createTrabajo.Field()
    update_trabajo = updateTrabajo.Field()
    delete_trabajo = deleteTrabajo.Field()
    create_lugar_trabajo = CreateLugarTrabajo.Field()
    update_lugar_trabajo = UpdateLugarTrabajo.Field()
    delete_lugar_trabajo = DeleteLugarTrabajo.Field()







