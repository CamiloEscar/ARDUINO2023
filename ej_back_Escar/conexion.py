import psycopg2
# import contextlib

db_params = dict(
    host="localhost",
    database="postgres",
    port=5432,
    user="postgres",
    password="abcd1234"
)

def conect_to_db(db_params):
    print("Connecting to PostgreSQL database...")
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    cur.close()
    conn.close()


def get_db(db_params):
    print("Connecting to PostgreSQL database...")
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    return cur, conn


def get_all_persons():
    connection, con = get_db(db_params)
    connection.execute("select * from persona")
    respuesta = []    
    for persona in connection.fetchall():
        datos = {}
        datos['id'] = persona[0]
        datos['nombre'] = persona[1]
        datos['apellido'] = persona[2]
        datos['email'] = persona[3]
        respuesta.append(datos)
    
    return respuesta

def get_by_id(id):
    connection, con = get_db(db_params)
    connection.execute(f"select * from persona where id = {id}")
    persona = connection.fetchone()
    datos = {}
    datos['id'] = persona[0]
    datos['nombre'] = persona[1]
    datos['apellido'] = persona[2]
    datos['email'] = persona[3]
    
    return datos


def get_person_deptos(id):
    connection, con = get_db(db_params)
    connection.execute(f"select * from departamento d join persona p on (d.fk_persona = p.id) where p.id ={id}")
    personas = connection.fetchall()
    datos_persona = {}
    if len(personas) > 0:
        datos_persona['id'] = personas[0][3]
        datos_persona['nombre'] = personas[0][4]
        datos_persona['apellido'] = personas[0][5]
        datos_persona['email'] = personas[0][6]
        datos_persona['deptos'] = []
        deptos = []
        for persona in personas:
            datos_depto = {}
            datos_depto['id'] = persona[0]
            datos_depto['nombre'] = persona[1]
            datos_persona['deptos'].append(datos_depto)
    
    return datos_persona
    
def delete_by_id(id):
    connection, con = get_db(db_params)
    connection.execute(f"delete from persona where id = {id}")
    con.commit()

def insert_person(name, last_name, email):
    connection, con = get_db(db_params)
    connection.execute(f"insert into persona (name, last_name, email) values ('{name}', '{last_name}', '{email}') returning id")
    persona = connection.fetchone()
    con.commit()
    return persona[0]

def update_person_email(id, email):
    connection, con = get_db(db_params)
    connection.execute(f"update persona set email = '{email}' where id = {id}")
    con.commit()
# @contextlib.contextmanager
# def database(params):
#     print("Connecting to PostgreSQL database...")
#     # Setup script
#     conn = psycopg2.connect(**params)
#     cur = conn.cursor()
#     try:
#         yield cur
#     finally:
#         # Teardown script
#         cur.close()
#         conn.commit()
#         conn.close()
#         print("Database connection closed.")



def get_trabajos_by_persona(persona_id):
    connection, con = get_db(db_params)
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM trabajo WHERE persona_id = {persona_id}")
    trabajos = cur.fetchall()
    cur.close()
    connection.close()

    response = []
    for trabajo in trabajos:
        datos = {
            "id": trabajo[0],
            "nombre": trabajo[1],
            "persona_id": trabajo[2]
        }
        response.append(datos)

    return response

def get_lugar_trabajo_by_id(lugar_trabajo_id):
    connection, con = get_db(db_params)
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM lugar_trabajo WHERE id = {lugar_trabajo_id}")
    lugar_trabajo = cur.fetchone()
    cur.close()
    connection.close()

    datos = {
        "id": lugar_trabajo[0],
        "nombre": lugar_trabajo[1]
    }

    return datos

def create_trabajo(nombre, persona_id):
    connection, con = get_db(db_params)
    cur = connection.cursor()
    cur.execute(f"INSERT INTO trabajo (nombre, persona_id) VALUES ('{nombre}', {persona_id}) RETURNING id")
    trabajo = cur.fetchone()
    connection.commit()
    cur.close()
    connection.close()
    return trabajo[0]

def create_lugar_trabajo(nombre):
    connection, con = get_db(db_params)
    cur = connection.cursor()
    cur.execute(f"INSERT INTO lugar_trabajo (nombre) VALUES ('{nombre}') RETURNING id")
    lugar_trabajo = cur.fetchone()
    connection.commit()
    cur.close()
    connection.close()
    return lugar_trabajo[0]

