from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from app import app, db
# from flask_mail import Mail, Message
from app.model.tables import User


@app.route("/")
def index():
    user = User.query.all()
    return render_template("index.html", user=user)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(request.form['nome'],
                    request.form['email'],
                    request.form['username'],
                    request.form['password']
                    )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("register.html")


@app.route("/recover")
def recover():
    return render_template("recover.html")


@app.route("/home")
def home():
    user = User.query.all()
    return render_template("home.html", user=user)


@app.route("/followers")
def followers():
    user = User.query.all()
    return render_template("followers.html", user=user)


@app.route("/following")
def following():
    user = User.query.all()
    return render_template("following.html", user=user)


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/my-profile")
def myprofile():
    return render_template("my-profile.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


# @app.route("/add", methods=['GET', 'POST'])
# def add():
#     if request.method == 'POST':
#         user = User(request.form['nome'],
#                     request.form['email'],
#                     request.form['username'],
#                     request.form['password']
#                     )
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template("add.html")


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    user = User.query.get(id)
    if request.method == 'POST':
        user.nome = request.form['nome']
        user.email = request.form['email']
        user.username = request.form['username']
        user.cep = request.form['cep']
        user.logradouro = request.form['logradouro']
        user.numero = request.form['numero']
        user.complemento = request.form['complemento']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", user=user)


@app.route("/delete/<int:id>")
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
