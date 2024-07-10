from flask import jsonify, request
from app.models import Client

from datetime import date

def index():
    return jsonify(
        {
            'mensaje': 'Esta es la lista de Clientes Actuales'
        }
    )

def get_all_client():
    clients = Client.get_all_client()
    return jsonify([client.serialize() for client in clients])


def create_client():
    data = request.json
    new_client = Client(
        nombre=data['nombre'],
        email=data['email'],
        telefono=data['telefono'],
        asunto=data['asunto'],
        mensaje=data['mensaje']
    )
    new_client.save()
    return jsonify({'message': 'Client created successfully'}), 201

def update_client(client_id):
    client = Client.get_by_id(client_id)
    if not client:
        return jsonify({'message': 'Client not found'}), 404
   
    data = request.json
    client.nombre = data['nombre']
    client.email = data['email'],
    client.telefono = data['telefono'],
    client.asunto = data['asunto'],
    client.mensaje = data['mensaje']
    client.save()
    return jsonify({'message': 'Client updated successfully'})

