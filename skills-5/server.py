"""server.py

Flask application for Skills 4.
"""

from random import randint
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def show_index():
    """Show the assessment page"""

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
