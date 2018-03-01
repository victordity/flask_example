import flask


@flask.current_app.app.route("/")
def hello():
    return "Hello World! pyntonistas"
