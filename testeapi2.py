from flask import Flask, jsonify, request




app = Flask(__name__)

funcionarios = [
    {
        'id': 1,
        'Nome': 'Gabriel',
        'Sexo': 'Masculino'
    },
    {
        'id': 2,
        'Nome': 'Guilherme',
        'Sexo': 'Feminino '
    },
    {
        'id': 3,
        'Nome': 'Marco',
        'Sexo': 'Masculino'
    },
    {
        'id': 4,
        'Nome': 'berê',
        'sexo': 'Feminino'
    },
]

@app.route('/funcionarios',methods=['GET'])
def obter_funcionarios():
    return jsonify(funcionarios)


@app.route('/funcionarios/<int:id>',methods =['GET'])
def obter_funcionarios_por_id(id):
    for funcionarios in funcionarios:
        if funcionarios.get('id') == id:
            return jsonify(funcionarios)



app.run(port=5000,host='localhost',debug=True)


