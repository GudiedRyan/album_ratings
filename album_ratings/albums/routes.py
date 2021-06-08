from flask import render_template, Blueprint, flash, redirect, url_for
from album_ratings.albums.forms import AlbumForm
from album_ratings.models import AlbumModel
from album_ratings import db

albums = Blueprint('albums', __name__)

@albums.route('/')
def home():
    albums = AlbumModel.query.all()
    return render_template('home.html', title='home', albums=albums)

@albums.route('/create', methods=['GET', 'POST'])
def create():
    form = AlbumForm()
    if form.validate_on_submit():
        album = AlbumModel(
            name = form.album_name.data,
            artist = form.artist.data,
            release_year = form.release_year.data,
            rating = form.rating.data
        )
        db.session.add(album)
        db.session.commit()
        flash('Album added!', 'success')
        return redirect(url_for('albums.home'))
    return render_template('album.html', title='Add Album', form=form, legend="Add a new Album")

@albums.route('/update')
def update():
    pass

@albums.route('/delete')
def delete():
    pass