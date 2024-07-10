from app.database import get_db

class Client:
    def __init__(self, id_client=None, nombre=None, email=None, telefono=None, asunto=None, mensaje=None):
        self.id_client = id_client
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.asunto = asunto
        self.mensaje = mensaje

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
                    mensaje=row[5]
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
                SET nombre = %s, email = %s, telefono = %s, asunto = %s, mensaje = %s
                WHERE id = %s
                """,
                (self.nombre, self.email, self.telefono, self.asunto, self.mensaje, self.id_client))
        else: # Crear cliente nuevo
            cursor.execute(
                """
                INSERT INTO clientes
                (nombre, email, telefono, asunto, mensaje)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (self.nombre, self.email, self.telefono, self.asunto, self.mensaje))
            self.id_client = cursor.lastrowid
        db.commit()
        cursor.close()

    
    def serialize(self):
        return {
            'id': self.id_client,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'asunto': self.asunto,
            'mensaje': self.mensaje
        }
