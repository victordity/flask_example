from flask import Flask, render_template
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
        return "It's dangerous to go alone! Take This 8===D"

    @app.route("/danilogs")
    def hello_danilo():

        msg = [
            'Hello world by Danilo',
            "Message 2",
            "I'm out of ideas already",
            "Still writing something"
        ]
        return render_template("template_danilo", msg=msg[randint(0, len(msg)-1)])

    @app.route("/atosfm")
    def hello_atos():
        return "Hello Atos! Welcome"

    @app.route("/victordity")
    def hellovictor():
        return "Mensagem adicionada por Victor Hugo"


    return app


