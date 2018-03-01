from flask import Flask, render_template
from os import path


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
        return "Hello Atos! Welcome"

    @app.route("/victordity")
    def hellovictor():
        from random import randint
        mensagens = ["Mensagem 1", "Mensagem 2", "Mensagem 3", "Mensagem 4", "Mensagem 5"]
        idx = randint(0, 4)
        print(mensagens[idx])

        return render_template("victor2.html", mensagem = mensagens[idx])

    return app


