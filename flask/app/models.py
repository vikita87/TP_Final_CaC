from app.database import get_db

class Client:
    def __init__(self, id_client=None, nombre=None, email=None, telefono=None, asunto=None, mensaje=None, atendido=None, activo=None):
        self.id_client = id_client
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.asunto = asunto
        self.mensaje = mensaje
        self.atendido = atendido
        self.activo = activo

    @staticmethod
    def __get_clients_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
    
        clients = []
        for row in rows:
            clients.append(
                Client(
                    id_client=row[0],
                    nombre=row[1],
                    email=row[2],
                    telefono=row[3],
                    asunto=row[4],
                    mensaje=row[5],
                    atendido=row[6],
                    activo=row[7]
                )
            )
        cursor.close()
        return clients


    @staticmethod
    def get_all_client():
        return Client.__get_clients_by_query(
            """
                SELECT * 
                FROM clientes
                WHERE activo = true AND atendido = false
                ORDER BY nombre DESC
            """
        )
    @staticmethod
    def get_all_atendidos():
        return Client.__get_clients_by_query(
            """
                SELECT * 
                FROM tareas 
                WHERE activo = true AND atendido = true
                ORDER BY nombre DESC
            """
        )
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_client: # Actualizar Cliente existente
            cursor.execute(
                """
                UPDATE clientes
                SET nombre = %s, email = %s, telefono = %s, asunto = %s, mensaje = %s, atendido = %s, activo = %s
                WHERE id = %s
                """,
                (self.nombre, self.email, self.telefono, self.asunto, self.mensaje, self.atendido, self.activo, self.id_client))
        else: # Crear cliente nuevo
            cursor.execute(
                """
                INSERT INTO clientes
                (nombre, email, telefono, asunto, mensaje, atendido, activo)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (self.nombre, self.email, self.telefono, self.asunto, self.mensaje, self.atendido, self.activo))
            self.id_client = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE clientes SET activo = false WHERE id = %s", (self.id_client,))
        db.commit()
        cursor.close()
    
    def serialize(self):
        return {
            'id': self.id_client,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'asunto': self.asunto,
            'mensaje': self.mensaje,
            'atendido': self.atendido,
            'activo': self.activo
        }
