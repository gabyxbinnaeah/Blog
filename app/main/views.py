from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Blog, User,BlogComments,Upvotes,Downvotes
from .forms import BlogForm,BlogCommentsForm,UpvotesForm,DownvotesForm,UpdateProfileForm
from flask.views import View,MethodView
from .. import db,photos
import markdown2 
#views

@main.route('/', methods=['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data.
    ''' 
    blog=Blog.query.filter_by().first()

    title='Home'

    technologyblog=Blog.query.filter_by(category="technologyblog")
    sportsblog=Blog.query.filter_by(category="sportsblog")
    academicblog=Blog.query.filter_by(category="academic")
    researchblog=Blog.query.filter_by(category="research")
    politicblog=Blog.query.filter_by(category="politicalblog")

    upvotes=Upvotes.get_all_upvotes(id)


    return render_template('home.htnl',title=title,blog=blog,technologyblog=technologyblog,sportsblog=sportsblog,academic=academic,researchblog=researchblog,politicblog=politicalblog) 
    