from sqlalchemy.dialects.postgresql import UUID, TEXT, DATE
from sqlalchemy import func
from db import db

class Pessoa(db.Model):
  __tablename__ = 'pessoa'

  id_nome = db.Column(UUID(as_uuid=True), primary_key=True, default=func.uuid_generate_v4())
  nome = db.Column(db.String(255), nullable=False)
  data_nascimento = db.Column(DATE(), nullable=False)
  salario = db.Column(db.String(255), default=False)
  observacoes = db.Column(TEXT(), nullable=False)
  nome_mae = db.Column(db.String(255), nullable=False)
  nome_pai = db.Column(db.String(255), nullable=False)
  cpf = db.Column(db.String(255), nullable=False)
  
  def as_dict(self):
    return {
      'id_nome': str(self.id_nome),
      'nome': self.nome,
      'data_nascimento': self.data_nascimento,
      'salario': self.salario,
      'observacoes': self.observacoes,
      'nome_mae': self.nome_mae,
      'nome_pai': self.nome_pai,
      'cpf': self.cpf
    }