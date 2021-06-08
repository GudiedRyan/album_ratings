from flask import render_template, Blueprint, flash, redirect, url_for, request
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

@albums.route('/update/<int:album_id>', methods = ['GET', 'POST'])
def update(album_id):
    album = AlbumModel.query.get_or_404(album_id)
    form = AlbumForm()
    if form.validate_on_submit():
        album.name = form.album_name.data
        album.artist = form.artist.data
        album.release_year = form.release_year.data
        album.rating = form.rating.data
        db.session.commit()
        flash('Changes have been saved!', 'success')
        return redirect(url_for('albums.home'))
    elif request.method == 'GET':
        form.album_name.data = album.name
        form.artist.data = album.artist
        form.release_year.data = album.release_year
        form.rating.data = album.rating
    return render_template('album.html', title="Edit Album Info", form=form, legend='Update Album Info')


@albums.route('/delete/<album_id>', methods=['GET','POST'])
def delete(album_id):
    album = AlbumModel.query.get_or_404(album_id)
    db.session.delete(album)
    db.session.commit()
    flash('Album deleted.', 'success')
    return redirect(url_for('albums.home'))