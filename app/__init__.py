import random
from os import path

from flask import Flask, render_template, session, request, redirect, jsonify

from app.models.user import User as UserMain
from app.models.user_danilogs import User
from app.models.user_victor import UserVictor
from app.modules.utils import logged


def create_app():
    instance_path = path.join(
        path.abspath(path.dirname(__file__))
    )
    print(instance_path)
    app = Flask(
        __name__,
        instance_path=instance_path,
        instance_relative_config=True
    )
    app.config.from_object("app.settings")

    @app.route("/")
    def hello():
        session['interns'] = [
            ("Victor1", "/victor1"),
            ("Danilo", "/danilogs"),
            ("Atos", "/atosfm"),
            ("Victor2", "/victordity")
        ]
        return render_template("index.html")

    @app.route("/victor1")
    def zelda():
        sorted_phrases = {"0": "It's dangerous to go alone! Take This 8=====D",
                          "1": "Hey, listen!",
                          "2": "Ocarina of time ftw!",
                          "3": "Majora's Mask is the better"}

        return sorted_phrases[str(random.randint(0, 3))]

    @app.route("/danilogs")
    def hello_danilo():
        if 'messages' not in session:
            session["messages"] = [
                'Hello world by Danilo',
                "Message 2",
                "I'm out of ideas already",
                "Still writing something"
            ]
        popped = session['messages'].pop(
            random.randint(0, 1)
        )
        print "test"
        print session
        return render_template("template_danilo", msg=popped)

    @app.route("/atosfm")
    def hello_atos():
        return "Hello Atos! Welcome"

    @app.route("/victordity")
    def hellovictor():
        from random import randint
        mensagens = ["Mensagem 1", "Mensagem 2", "Mensagem 3", "Mensagem 4",
                     "Mensagem 5"]
        idx = randint(0, 4)
        print(mensagens[idx])

        return render_template("victor2.html", mensagem=mensagens[idx])

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        session.clear()
        return render_template('login.html')

    @app.route("/user")
    @logged
    def user():
        logged_user = UserMain(**session['user'])
        return str(logged_user)

    @app.route("/cad_user", methods=["POST", "GET"])
    def cad_user():
        if not all([request.form.get(i) for i in ['nome', 'email']]):
            return "Parametros invalidos"

        if 'user' not in session:
            name = request.form.get("nome")
            email = request.form.get("email")
            new_user = UserMain(name, email)
            session['user'] = new_user.__dict__
        return redirect('user')

    @app.route("/cad_user_danilogs", methods=["POST", "GET"])
    def cad_user_danilogs():

        if "user" not in session:
            session["user"] = [[]]

        created_user = User(request.form.get('nome'),
                            request.form.get('email'))
        session["user"].append([created_user.name, created_user.email])

        return redirect("/user")

    @app.route("/cad_user_victor1", methods=["POST", "GET"])
    def cad_user_victor1():
        new_user = UserVictor(request.form.get('nome'),
                              request.form.get('email'))

        session['user'] = new_user.toJSON()

        return redirect("user")

    @app.route("/list_user", methods=["GET"])
    def list_user():
        logged_user = UserMain(**session['user'])
        return jsonify({
            'data': logged_user.__dict__,
            'resp': True
        })

    return app
