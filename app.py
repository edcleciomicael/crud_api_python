from flask import Flask, request, jsonify
from flask_migrate import Migrate
from db import db
from models.pessoa import Pessoa

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/meudb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/pessoa', methods=['POST'])
def add_pessoa():
  data = request.get_json()
  newPessoa = Pessoa(nome=data['nome'],
                      data_nascimento=data['data_nascimento'],
                        salario=data['salario'],
                          observacoes=data['observacoes'],
                            nome_mae=data['nome_mae'],
                            nome_pai=data['nome_pai'],
                            cpf=data['cpf'])
  db.session.add(newPessoa)
  db.session.commit()
  return jsonify({'message': 'Pessoa cadastrada'}), 201

@app.route('/pessoa', methods=['GET'])
def get_all():
  pessoa = Pessoa.query.all()
  return jsonify([pessoa.as_dict() for pessoa in pessoa])

@app.route('/pessoa/<uuid:pessoa_id>', methods=['GET'])
def get_pessoa(pessoa_id):
  pessoa = Pessoa.query.get_or_404(pessoa_id)
  return jsonify(pessoa.as_dict())

@app.route('/pessoa/<uuid:pessoa_id>', methods=['PATCH'])
def update_pessoa(pessoa_id):
  pessoa = Pessoa.query.get_or_404(pessoa_id)
  data = request.get_json()

  for key, value in data.items():
    setattr(pessoa, key, value)
  
  db.session.commit()
  return jsonify({'message': 'Cadastro atualizado com sucesso'})

@app.route('/pessoa/<uuid:pessoa_id>', methods=['DELETE'])
def delete(pessoa_id):
  pessoa = Pessoa.query.get_or_404(pessoa_id)
  db.session.delete(pessoa)
  db.session.commit()
  return jsonify({'message': 'Cadastro removido do com sucesso'})

if __name__ == '__main__':
  app.run(debug=True, port=8080, host='0.0.0.0')