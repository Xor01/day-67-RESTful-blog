from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

ckeditor = CKEditor()


class PostForm(FlaskForm):
    title = StringField(label='Post Title')
    subtitle = StringField(label='Post Subtitle')
    author = StringField(label='Your Name')
    img_url = URLField(label='Post Image URL')
    body = CKEditorField(label='Body Content')
    submit = SubmitField(label='Submit')
