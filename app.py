"""Flask app for Cupcakes."""

import os
from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///cupcakes')
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.get("/api/cupcakes")
def get_all_cupcakes():
    """returns all cupcakes"""

    serialized = [cupcake.serialized() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<int:cupcake_id>")
def get_all_cupcakes(cupcake_id):
    """returns all cupcakes"""

    serialized = [cupcake.serialized() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes=serialized)