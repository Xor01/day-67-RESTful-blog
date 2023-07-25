from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

ckeditor = CKEditor()


class PostForm(FlaskForm):
    title = StringField(label='Post Title', validators=[DataRequired()])
    subtitle = StringField(label='Post Subtitle', validators=[DataRequired()])
    author = StringField(label='Your Name', validators=[DataRequired()])
    img_url = URLField(label='Post Image URL', validators=[DataRequired()])
    body = CKEditorField(label='Body Content', validators=[DataRequired()])
    submit = SubmitField(label='Submit', validators=[DataRequired()])
