from flask import Flask


def create_app():
    app = Flask("training")
    app.config.from_object("app.settings")

    @app.route("/")
    def hello():
        return "Hello World! pyntonistas222"

    @app.route("/victor1")
    def zelda():
        return "It's dangerous to go alone! Take This 8===D"

    @app.route("/danilogs")
    def hello_danilo():
        return "Hello world! by danilogs"

    @app.route("/atosfm")
    def hello_atos():
        return "Hello Atos! Welcome"

    @app.route("/victordity")
    def hellovictor():
        return "Mensagem adicionada por Victor Hugo"


    return app


