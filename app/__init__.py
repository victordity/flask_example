from flask import Flask


def create_app():
    app = Flask("training")
    app.config.from_object("app.settings")

    @app.route("/")
    def hello():
        return "Hello World! pyntonistas222"

    @app.route("/victor1")
    def zelda():
        return "It's dangerous to go alone! Take This O---{:::::::::::::::>"

    return app
