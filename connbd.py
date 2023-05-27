from flask import Flask, jsonify
import json
import requests
import mysql.connector

app = Flask(__name__)


bancoDeDados = mysql.connector.connect(host="localhost",user="root",password="Gab@202300",database="funcionarios")

#http://127.0.0.1:5000/v1/funcionarios
@app.route('/v1/funcionarios', methods=["GET"])
def listar():
    selectAllSql = f"select * from id_funcionarios"
    cursor = bancoDeDados.cursor()
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()
    if resultado is None:
        api_url = "http://localhost:5000/funcionarios"
        response = requests.get(api_url)
        retornaApi = response.json()
    else:
        retornaApi = None

    return jsonify(retornaApi)

if __name__ == '__main__':
    app.run(port=5001)
    
 
















