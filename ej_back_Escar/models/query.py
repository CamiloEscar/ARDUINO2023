from graphene import (
    ObjectType,
    Field,
    String,
    Boolean,
    List,
    Int
)

from .persona import Persona as PersonaModel
from .objects import LugarTrabajo, Persona#, Departamento
from .objects import Trabajo, TrabajoModel
# from .departamento import Departamento as DepartamentoModel
from .objects import LugarTrabajo, LugarTrabajoModel


class Query(ObjectType):
    personas = List(lambda: Persona, last_name=String(), id=Int(), has_email=Boolean(), order_by_name=Boolean())
    # departamentos = List(lambda: Departamento)
    # departamento = Field(lambda: Departamento, id=Int())
    trabajo = List(Trabajo)
    # lugar_trabajo = Field(lambda: LugarTrabajo, id=Int())
    lugar_trabajo = List(LugarTrabajo)


    def resolve_personas(self, info, id=None, last_name=None, has_email=None, order_by_name=None):
        query = Persona.get_query(info=info)
        if id:
            query = query.filter(PersonaModel.id==id)
        if last_name:
            query = query.filter(PersonaModel.last_name==last_name)
        if has_email is not None:
            if has_email:
                query = query.filter(PersonaModel.email != None)
            else:
                query = query.filter(PersonaModel.email == None)
        if order_by_name:
            query = query.order_by(PersonaModel.name)
        return query.all()
    
    # def resolve_departamentos(self, info):
    #     query = Departamento.get_query(info=info)
    #     return query.all()
    
    # def resolve_departamento(self, info, id):
    #     dpto = DepartamentoModel.query.get(id)
    #     return dpto

    def resolve_trabajo(self, info):
        query2 = Trabajo.query
        return query2.all()

    def resolve_trabajo(self, info):
        job = TrabajoModel.query
        return job

    def resolve_lugar_trabajo(self, info):
        query3 = LugarTrabajo.query
        return query3.all()

    def resolve_lugar_trabajo(self, info):
        place = LugarTrabajoModel.query
        return place