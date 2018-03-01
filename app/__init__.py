from flask import Flask, render_template
from os import path
import random

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
        sorted_phrases = {"0": "It's dangerous to go alone! Take This O---{:::::::::::::::>", "1": "Hey, listen!",
                          "2": "Ocarina of time ftw!", "3": "Majora's Mask is the better"}

        return sorted_phrases[str(random.randint(0, 3))]

    @app.route("/danilogs")
    def hello_danilo():
        return "Hello world! by danilogs"

    @app.route("/atosfm")
    def hello_atos():
        return "Hello Atos! Welcome"

    @app.route("/victordity")
    def hellovictor():
        from random import randint
        from flask import session
        mensagens = ["Mensagem 1", "Mensagem 2", "Mensagem 3", "Mensagem 4", "Mensagem 5"]
        idx = randint(0, 4)
        session.pop('username', None)
        print(mensagens[idx])

        return render_template("victor2.html", mensagem = mensagens[idx])

    return app


