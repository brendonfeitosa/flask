from flask import Flask, request

app = Flask(__name__) #objeto que vai rodar na função main do python

#parametros na rota
@app.route('/buscar/<int:user_id>/<string:nome>', methods=['GET', 'POST']) #decorator para passar uma rota, ele deve sempre estar em cima da sua função
def buscar(user_id, nome):
    return f"Usuário: id: {user_id} - Nome: {nome}"

#parametros na rota como QueryString
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    user_id = request.args.get('id')
    nome = request.args.get('nome')
    return f"Usuário cadastrado: id: {user_id} - Nome: {nome}"


if __name__ == '__main__': #checando se main existe no __name__
    app.run(debug=True)


