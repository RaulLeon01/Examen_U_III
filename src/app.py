"""
Examen Unidad III 
Autor: Raul Corcino Leon
Fecha: 29 de octubre de 2025
"""
# INSTALACIÓN DE FLASK:
# 1. cd C:/Users/TuUsuario/Documents/Flask_
# 2. python -m venv venv
# 3. venv\Scripts\activate
# 4. pip install flask
# 5. pip show flask
# 6. python app.py

"""
Desarrollar una API básica con Flask que permita:
- Crear un diccionario de dispositivos de red.
- Agregar nuevos dispositivos.
- Modificar dispositivos existentes.
- Mostrar un listado de todos los dispositivos en formato HTML, 
- donde cada dispositivo se muestre en un <div> con nombre, 
- descripción y características
"""

from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

# Diccionario inicial de dispositivos
dispositivos = {
    "router01": {
        "id": "router01",
        "nombre": "Router Principal",
        "descripcion": "Router de borde para salida a Internet",
        "ip": "192.168.1.1",
        "mac": "00:1A:2B:3C:4D:5E",
        "ubicacion": "Sala de servidores",
        "tipo": "Router",
        "otros": ""
    },
    "switch01": {
        "id": "switch01",
        "nombre": "Switch de Acceso",
        "descripcion": "Switch para conectar equipos de usuarios",
        "ip": "192.168.1.2",
        "mac": "00:1A:2B:3C:4D:5F",
        "ubicacion": "Planta 1",
        "tipo": "Switch",
        "otros": "24 puertos PoE"
    }
}

# Muestrea todos los dispositivos para HTMl
@app.route('/dispositivos_html', methods=['GET'])
def mostrar_dispositivos_html():
    return render_template('dispositivos.html', dispositivos=dispositivos)

# Agrega un nuevo dispositivo
@app.route('/dispositivos', methods=['POST'])
def agregar_dispositivo():
    
    # Valida que se envien los datos
    if not request.json:
        # Si no hay datos, retorna un error
        return jsonify({"error": "No se proporcionaron datos"}), 400
    # Obtiene los datos
    data = request.json
    
    # Valida que el ID esté presente
    if 'id' not in data:
        return jsonify({"error": "Falta el ID del dispositivo"}), 400
    id_dispositivo = data['id']
    
    # Verifica si el ID ya existe
    if id_dispositivo in dispositivos:
        return jsonify({"error": "El ID del dispositivo ya existe"}), 400
    dispositivos[id_dispositivo] = data
    return jsonify({"mensaje": "Dispositivo agregado con éxito", "dispositivo": data}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    