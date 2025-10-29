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


from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
   return "Hola mundo" 
   
if __name__ == '__main__':
    app.run(debug=True)
    