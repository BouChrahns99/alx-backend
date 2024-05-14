#!/usr/bin/env python3
"""
Uses the _ or gettext function to parametrize your templates.
Uses the message IDs home_title and home_header.
"""
from flask_babel import Babel, gettext, request
from flask import Flask, render_template

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """gets the best match from the supported languages
    """
    return request.accept_languages.best_match(["en", "fr"])


@app.route('/')
def get_index() -> str:
    """initializes the paremeters for index.html
    """
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template(
        "3-index.html", home_title=home_title, home_header=home_header
    )


if __name__ == "__main__":
    app.run()
