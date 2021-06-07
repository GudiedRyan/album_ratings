from flask import render_template, Blueprint, flash, redirect, url_for
from album_ratings.albums.forms import AlbumForm

albums = Blueprint('albums', __name__)

@albums.route('/create', methods=['GET', 'POST'])
def create():
    form = AlbumForm()
    if form.validate_on_submit():
        flash('Album added!', 'success')
        return redirect(url_for('main.home'))
    return render_template('album.html', title='Add Album', form=form, legend="Add a new Album")

@albums.route('/update')
def update():
    pass

@albums.route('/delete')
def delete():
    pass