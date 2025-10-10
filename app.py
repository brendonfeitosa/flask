from flask import Flask, request, render_template

app = Flask(__name__) #objeto que vai rodar na função main do python

alunos = [
    {"id": 1, "nome": "Brendon", "idade": 29, "endereco": "rua xpto, 123"},
    {"id": 2, "nome": "Debora", "idade": 41, "endereco": "rua xpto, 1234"},
    {"id": 3, "nome": "Helena", "idade": 3, "endereco": "rua xpto, 12345"}
]

@app.route('/')
def home():
    return render_template('index.html')

#parametros na rota
#exibe o aluno e o id passado na url
@app.route('/buscar/<int:user_id>/<string:nome>/<int:idade>/string:endereco', methods=['GET', 'POST']) #decorator para passar uma rota, ele deve sempre estar em cima da sua função
def buscar(user_id, nome, idade, endereco):
    return f"Usuário: id: {user_id} - Nome: {nome} - Idade: {idade} - Endereço: {endereco}"

#parametros na rota como QueryString
@app.route('/cadastrar', methods=['GET'])
def cadastrar():
    user_id = request.args.get('id')
    nome = request.args.get('nome')
    idade = request.args.get('idade')
    endereco = request.args.get('endereco')
    return f"Usuário cadastrado: id: {user_id} - Nome: {nome} - Idade: {idade} - Endereço: {endereco}"

#endpoint buscar todos os alunos
@app.route('/listar', methods=['GET'])
def listar():
    return alunos


#buscar aluno por id
@app.route('/buscaraluno/<int:id>', methods=['GET'])
def buscar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return aluno
    
    return "Aluno não localizado"

#remover aluno parametros na url
@app.route('/remover/<int:id>', methods=['DELETE'])
def remover_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)   # remove o dicionário da lista
            return "Aluno removido com sucesso!"

    return "Aluno não localizado"

@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    dados = request.get_json()
    id_alterado = dados.get('id')
    for aluno in alunos:
        if aluno["id"] == id:
            aluno.update({
                "nome": dados.get("nome", aluno.get("nome")),
                "idade": dados.get("idade", aluno.get("idade")),
                "endereco": dados.get("endereco", aluno.get("endereco"))
            })

            return f"Aluno {id} atualizado com sucesso! \nNovos dados do aluno: {aluno} \nTodos os alunos: {alunos}"

    return "Aluno não encontrado"



#parametros na rota como QueryString
@app.route('/cadastrarjson', methods=['POST'])
def cadastrar_json():
    novo = request.get_json()
    novo["id"] = len(alunos) + 1
    alunos.append(novo)
    return alunos


if __name__ == '__main__': #checando se main existe no __name__
    app.run(debug=True)


