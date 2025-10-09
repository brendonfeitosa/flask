from flask import Flask, request, render_template

app = Flask(__name__) #objeto que vai rodar na função main do python

alunos = [
    {"id": 1, "nome": "Brendon"},
    {"id": 2, "nome": "Debora"},
    {"id": 3, "nome": "Helena"}
]

@app.route('/')
def home():
    return render_template('index.html')

#parametros na rota
@app.route('/buscar/<int:user_id>/<string:nome>', methods=['GET', 'POST']) #decorator para passar uma rota, ele deve sempre estar em cima da sua função
def buscar(user_id, nome):
    return f"Usuário: id: {user_id} - Nome: {nome}"

#parametros na rota como QueryString
@app.route('/cadastrar', methods=['GET'])
def cadastrar():
    user_id = request.args.get('id')
    nome = request.args.get('nome')
    return f"Usuário cadastrado: id: {user_id} - Nome: {nome}"

#endpoint buscar todos os alunos
@app.route('/listar', methods=['GET'])
def listar():
    return alunos


#buscar aluno
@app.route('/buscaraluno/<int:id>', methods=['GET'])
def buscar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return aluno
    
    return "Aluno não localizado"

#remover aluno
@app.route('/remover/<int:id>', methods=['DELETE'])
def remover_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)   # remove o dicionário da lista
            return "Aluno removido com sucesso!"

    return "Aluno não localizado"


#parametros na rota como QueryString
@app.route('/cadastrarjson', methods=['POST'])
def cadastrar_json():
    novo = request.get_json()
    novo["id"] = len(alunos) + 1
    alunos.append(novo)
    return alunos


if __name__ == '__main__': #checando se main existe no __name__
    app.run(debug=True)


