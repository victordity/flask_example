from flask import Flask


def create_app():
    app = Flask("training")
    app.config.from_object("app.settings")

    @app.route("/")
    def hello():
        return "Hello World! pyntonistas222"

    @app.route("/victordity")
    def hellovictor():
        return "Mensagem adicionada por Victor Hugo"

    return app