from app import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(60))
    email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    logradouro = db.Column(db.String(50), nullable=True)
    numero = db.Column(db.String(20), nullable=True)
    cep = db.Column(db.String(10), nullable=True)
    complemento = db.Column(db.String(60), nullable=True)

    def __init__(self, nome, email, username, password):
        self.nome = nome
        self.email = email
        self.username = username
        self.password = password


class Twitte(db.Model):
    __tablename__ = "twitte"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    conteudo = db.Column(db.String(100), db.ForeignKey("user.id"))


class Like(db.Model):
    __tablename__ = "like"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer)
    twitte = db.Column(db.Integer, db.ForeignKey("id_user"))


class Comentario(db.Model):
    __tablename__ = "comentario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comentario = db.Column(db.String(100), db.ForeignKey("user.id"))


class Seguir(db.Model):
    __tablename__ = "seguir"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer)
    id_friend = db.Column(db.Integer)
    status = db.Column(db.Integer)
