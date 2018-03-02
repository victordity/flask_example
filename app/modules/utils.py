from flask import session, redirect, url_for


def logged(func):
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for("login", msg="Voce precisa logar"))
        return func(*args, **kwargs)

    return wrapper
