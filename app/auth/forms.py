from flask_wtf import FlaskForm 
from wtforms import stringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from .. models import User 
from wtforms import ValidatorError 


class RegistrationForm(FlaskForm):
    '''
    class that defines registration prerequisites 
    '''

    email= StringField('Your email address', validators=[Required(),Email()])
    username= StringField('Enter your username', validators=[Required(),])
    password= PasswordField('Enter your password',validators=[Required(),EqualTo('password_confirm', message = 'Password must match')])
    password_confirm= PasswordField('Confirm passwords', validators=[Required()])
    submit= SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email= data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username= data_field.data).first():
            raise ValidationError('There is an account with that username')

class LoginForm(FlaskForm):
    email = StringField('Your email address',validators=[Required(),Email()]) 
    password = PasswordField('Your password',validators=[Required(),Password()]) 
    remember= BooleanField('Remember me')
    submit= SubmitField('Sign In')

    

