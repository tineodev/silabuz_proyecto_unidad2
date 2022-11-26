from flask import Blueprint, render_template, redirect, url_for, flash
from app import mongo
from utils.request_api import consume
from models.rickoso import Rickoso
from bson.objectid import ObjectId #filtrar por id (id: ObjectId(id)))


home = Blueprint('home', __name__)


@home.route('/')
def index():
    return render_template('index.html')


@home.route('/add_character')
def add_character():

    datos = consume()
    for x in datos:

        insert_Rickoso = Rickoso(
            
            x["nombre"],
            x["estado"],
            x["especie"],
            x["avatar"],
            x["ultimaVez"],
            x["primeraVez"],
            x["episodios"]
        )
        mongo.db.rickoso.insert_one(insert_Rickoso.to_json())

    flash('Added characters')
    return redirect(url_for('home.index'))


@home.route('/list_characters')
def list_characters():

    list_query = mongo.db.rickoso.aggregate([
        {
            "$sort": {"_id": -1}
        }
    ])
    return render_template('characters.html', lista = list_query)

@home.route('/delete_characters')
def delete_characters():
    mongo.db.rickoso.drop()
    flash('Deleted characters')
    return redirect(url_for('home.index'))


@home.route('/detail_character/<id>')
def detail_character(id):
    unique = mongo.db.rickoso.find_one({"_id": ObjectId(id)})
    return render_template('/detail.html', character_unique=unique)
    

