from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length
from books_app.models import Audience, Book, Author, Genre

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title', validators=[DataRequired(), Length(min=3, max=80)])
    publish_date = DateField('Date Published')
    author = QuerySelectField('Author', query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres', query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')


class AuthorForm(FlaskForm):
    """Form to create an author."""

    # : Fill out the fields in this class for:
    # - the author's name
    # - the author's biography (hint: use a TextAreaField)
    # - a submit button
    name = StringField("Author's Name", validators=[
                       DataRequired(), Length(min=3, max=80)])
    biography = TextAreaField("Biography", validators=[DataRequired()])
    submit = SubmitField('Submit')

    # STRETCH CHALLENGE: Add more fields here as well as in `models.py` to
    # collect more information about the author, such as their birth date,
    # country, etc.
    


class GenreForm(FlaskForm):
    """Form to create a genre."""

    # - the genre's name (e.g. fiction, non-fiction, etc)
    # - a submit button
    genre = StringField("Genre:", validators=[DataRequired(), Length(min=3, max=80)])

    submit = SubmitField('Submit')
    
