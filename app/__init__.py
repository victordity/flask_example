from flask import Flask, render_template, session
from os import path
from random import randint
import random
from os import path

from flask import Flask, render_template, session

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
        msg = [
            'Hello world by Danilo',
            "Message 2",
            "I'm out of ideas already",
            "Still writing something"
        ]
        return render_template("template_danilo",
                               msg=msg[random.randint(0, len(msg) - 1)])

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

    return app
