from flask import Flask


def create_app():
    app = Flask("training")
    app.config.from_object("app.settings")

    @app.route("/")
    def hello():
        return "Hello World! pyntonistas222"

    @app.route("/danilogs")
    def hello_danilo():
        return "Hello world! by danilogs"

    @app.route("/atosfm")
    def hello_atos():
        return "Hello Atos! Welcome"
    
    return app
