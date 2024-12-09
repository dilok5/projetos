from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

# a linha abaixo é a minha variavel de aplicação
app = Flask(__name__)

# a linha abaixo é a configuração do banco
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'gtr3253',
        servidor = 'localhost',
        database = 'aula'
    )

# a linha abaixo instancia o banco de dados
db = SQLAlchemy(app)

# a linha abaixo cria uma classe modelo
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return "<Name %r>"% self.nome

@app.route('/ola')
def mostrar():
    return "<h1>Iniciando aplicação flask</h1>"

@app.route('/Lista')
def lista_alunos():

    # a linha abaixo busca os dados na tabela 
    lista = Aluno.query.order_by(Aluno.id)

    return render_template('lista.html', titulo="Listagem de alunos", todos_alunos = lista)



app.run(debug=True)