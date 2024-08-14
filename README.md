CRUD API REST EM PYTHON COM FLASK, SQLALchemy e Postgres

Instalar dependencias:
```bash
pip install Flask
pip install SQLAlchemy
pip install Flask-Migrate
```

EXECUÇÃO:
```bash
flask db init
flask db migrate -m 'init'
flask db upgrade
```

INICIAR O SERVER: 
```bash
python3 app.py
```

API SERÁ INICIADA NESSE LOCAL: 
`http://localhost:8080`