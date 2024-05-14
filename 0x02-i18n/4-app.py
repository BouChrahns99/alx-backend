#!/usr/bin/env python3
"""
In this task, you will implement a way
to force a particular locale by passing
the locale=fr parameter to your apps URLs.
"""
from flask import Flask, render_template
from flask_babel import Babel, gettext, request

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """gets locale from the headers"""
    lang = request.args.get("locale")
    print(lang)
    if lang:
        return lang
    return request.accept_languages.best_match(["en", "fr"])


@app.route('/')
def get_index():
    """initializes the paremeters for index.html
    """
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template(
        "4-index.html", home_title=home_title, home_header=home_header
    )


if __name__ == "__main__":
    app.run()
