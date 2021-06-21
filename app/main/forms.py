from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class BlogForm(FlaskForm):
    title = StringField('Blog title', validators=[Required()])
    description=TextAreaField("What would you like to write on?",validators=[Required()])
    category=RadioField('Label',choices=[('technologyblog','technologyblog'),('sportsblog','sportsblog'),('academicblog','academicblog'),('researchblog','researchblog'),('politicalblog','politicalblog')],validators=[Required()])
    submit=SubmitField('Submit') 


class BlogCommentsForm(FlaskForm):
    description = TextAreaField('Add comment', validators=[Required()])
    Submit= SubmitField()

class UpvotesForm(FlaskForm):
    Submit=SubmitField() 

class DownvotesForm(FlaskForm):
    Submit=SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you', validators=[Required()])
    submit=SubmitField('submit')
