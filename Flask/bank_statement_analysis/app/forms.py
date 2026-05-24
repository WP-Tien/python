from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import Email, InputRequired, Length, EqualTo

# FLASK FORM CLASSES
class LoginForm(FlaskForm):
    username = StringField(
        'Username', 
        validators = [
            InputRequired(),
            Length(min=4, max=15)
        ]
    )
    
    password = PasswordField(
        'Password',
        validators = [
            InputRequired(),
            Length(min=8, max=80)
        ]
    )
    
    remember = BooleanField('Remember me')
    
    submit = SubmitField(
        'Log In',
        render_kw={
            "class": "btn btn-secondary w-100 btn-lg"
        }
    )

class RegisterForm(FlaskForm):
    email = StringField(
        'Email',
        validators = [
            InputRequired(),
            Email(message="Invalid Email"),
            Length(max = 80)
        ]
    )
    
    username = StringField(
        'Username',
        validators = [
            InputRequired(),
            Length(min=4, max=15)
        ]
    ) 
    
    password = PasswordField(
        'Password',
        validators = [
            InputRequired(),
            Length(min=8, max=80),
        ]
    )
    
    confirm = PasswordField(
        'Password',
        validators = [
            InputRequired(),
            Length(min=8, max=80),
            EqualTo('password', 'Password must match')
        ]
    )
    
    submit = SubmitField(
        'Register',
        render_kw={
            "class": "btn btn-secondary w-100 btn-lg"
        }
    )