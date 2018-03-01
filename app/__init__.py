from flask import Flask, render_template, session
from os import path
from random import randint

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
        interns = [
            ("Victor1", "/victor1"),
            ("Danilo", "/danilogs"),
            ("Atos", "/atosfm"),
            ("Victor2", "/victordity")
        ]
        return render_template("index.html", interns=interns)

    @app.route("/victor1")
    def zelda():
        return "It's dangerous to go alone! Take This O---{:::::::::::::::>"

    @app.route("/danilogs")
    def hello_danilo():
        return "Hello world! by danilogs"

    @app.route("/atosfm")
    def hello_atos():
        interns = ['Hey!!! Listen!!!', 'Oi eu sou o Goku', 'Ola']
        used_phrases_idx = session['objects']
        index = randint(0, 2)
        if index not in used_phrases_idx:
            used_phrases_idx.append(randint(0, 2))
            session['objects'] = used_phrases_idx
            return render_template("change_phrase.html", interns=interns[randint(0, 2)])
        else:
            return render_template("change_phrase.html", interns='There are no more sentences')

    @app.route("/victordity")
    def hellovictor():
        return "Mensagem adicionada por Victor Hugo"


    return app


