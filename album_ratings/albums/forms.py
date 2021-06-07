from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AlbumForm(FlaskForm):
    album_name = StringField('Album Name', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])
    release_year = IntegerField('Release Year (numbers only)', validators=[DataRequired()])
    rating = SelectField(u'Rating (out of 5)', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    submit = SubmitField('Submit')
