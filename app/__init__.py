from random import randint
import random
from os import path

from flask import Flask, render_template, session, request, redirect

from app.modules.utils import logged
from models.user import User
import json
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
        interns = ['M1', 'M2', 'M3']
        if 'used_sentences' not in session:
            session['used_sentences'] = interns
        index = randint(0, 2)
        try:
            session['used_sentences'].pop(index)
            return render_template("change_phrase.html", interns=interns[randint(0, 2)])
        except Exception :
            return render_template("change_phrase.html", interns='There are no more sentences')


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
        return render_template('login.html')

    @app.route("/user")
    @logged
    def user():
        return "Logged"

    @app.route("/cad_user", methods=["POST", "GET"])
    def cad_user():
        print(request.form)
        return "cadastrado"

    @app.route("/cad_user_atos", methods=["POST", "GET"])
    def cad_user_atos():

        if 'user' not in session:
            new_user = User(request.form.get('nome'),request.form.get('email'))
            session['user'] = new_user.serialize()
            print session['user']
        else:
            new_user = json.loads(session['user'])
            if (not new_user.get('nome')):
                new_user = User(request.form.get('nome'),request.form.get('email'))
                session['user'] = json.dumps(new_user.__dict__)
        return redirect('user')

    return app
