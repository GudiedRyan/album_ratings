from flask import render_template, Blueprint

albums = Blueprint('albums', __name__)

@albums.route('/create')

def create():
    return render_template('home.html', title='home')