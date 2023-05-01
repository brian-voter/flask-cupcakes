"""Flask app for Cupcakes."""

import os
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake, DEFAULT_CUPCAKE_IMAGE_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///cupcakes')
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.get('/')
def get_homepage():
    """returns homepage html"""

    return render_template("home.html")

@app.get("/api/cupcakes")
def get_all_cupcakes():
    """returns all cupcakes
    returns JSON:
        {cupcakes: [
            {id, flavor, size, rating, image_url},
            ...]
        }
    """

    serialized = [cupcake.serialize() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """returns a cupcake
    returns JSON:
        {cupcake:
            {id, flavor, size, rating, image_url}
        }
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post("/api/cupcakes")
def create_cupcake():
    """creates a cupcake
    returns JSON:
        {cupcake:
            {id, flavor, size, rating, image_url}
        }
    """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image_url = request.json["image_url"] or None #have to give None to use default from model


    new_cupcake = Cupcake(
                    flavor=flavor,
                    size=size,
                    rating=rating,
                    image_url=image_url
                  )

    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake(cupcake_id):
    """updates a cupcake (not all cupcake fields are required in request)
    returns JSON:
        {cupcake:
            {id, flavor, size, rating, image_url}
        }
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)


    # Support resetting to the default cupcake image if we receive an empty string:

    # image_url is a URL, an empty string, or None
    image_url = request.json.get("image_url")

    new_image_url = ""
    if image_url is None:
        new_image_url = cupcake.image_url
    elif image_url == "":
        new_image_url = DEFAULT_CUPCAKE_IMAGE_URL
    else:
        new_image_url = image_url

    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image_url = new_image_url

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """deletes a cupcake
    returns JSON:
        {deleted:
            [cupcake-id]
        }
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(deleted = [cupcake_id])