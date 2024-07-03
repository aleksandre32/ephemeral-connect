from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, FileField,TextAreaField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileAllowed
from models import User
from flask_login import current_user





class RegisterForm(FlaskForm):
    username = StringField(label="username")
    password = PasswordField(label = "password")
    register = SubmitField(label ="register")
    
class LoginForm(FlaskForm):
    username = StringField(label="username")
    password = PasswordField(label = "password")
    login = SubmitField(label ="login")

class PostForm(FlaskForm):
    text = StringField('Text', validators=[DataRequired()])
    file = FileField('File', validators=[FileAllowed(['jpg', 'png', 'pdf', 'docx'], 'Images and documents only!')])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ReplyForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Reply')

class SearchForm(FlaskForm):
    query = StringField('Search for Users', validators=[DataRequired()])
    submit = SubmitField('Search')



class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    profile_image = FileField('Profile Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        user = User.query.filter_by(user_name=username.data).first()
        if user and user.id != current_user.id:
            raise ValidationError('Username already taken.')