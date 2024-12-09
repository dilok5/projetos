from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Configuração da aplicação
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='gtr3253',
        servidor='localhost',
        database='aula'
    )

# Instanciação do banco de dados
db = SQLAlchemy(app)

# Modelo de tabela
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return "<Aluno %r>" % self.nome

# Criar tabelas no banco de dados
with app.app_context():
    db.create_all()

# Rotas
@app.route('/ola')
def mostrar():
    return "<h1>Iniciando aplicação flask</h1>"

@app.route('/lista')
def lista_alunos():
    # Busca os dados na tabela
    lista = Aluno.query.order_by(Aluno.id).all()
    return render_template('lista.html', titulo="Listagem de alunos", todos_alunos=lista)

@app.route("/cadastrar")
def cadastrar_aluno():
    return render_template("cadastrar.html")

@app.route("/adicionar", methods=["POST"])
def adicionar_aluno():
    # Pegando os dados enviados pelo formulário
    nome_aluno = request.form['txtNome']
    telefone_aluno = request.form['txtTelefone']
    email_aluno = request.form['txtEmail']

    # Criando um novo aluno
    novo_aluno = Aluno(nome=nome_aluno, telefone=telefone_aluno, email=email_aluno)

    # Adicionando e salvando no banco de dados
    db.session.add(novo_aluno)
    db.session.commit()

    return redirect('/lista')

# Executar a aplicação
if __name__ == '__main__':
    app.run(debug=True)
