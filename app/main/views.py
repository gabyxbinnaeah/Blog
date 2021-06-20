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



@main.route('/blogs/new/', methods=['GET','POST']) 
@login_required
def new_pitcher():
    form= BlogForm() 
    my_upvotes.query.filter_by(blog_id=Blog.id)
    if form.validate_on_submi():
        description=form.description.data
        title=form.title.data
        user_id=current_user
        category=form.category.data 

        new_blog = Blog(user_id=current_user._get_current_object().id, title=title, description=description, category=category)
        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('blogs.html',form=form)

@main.route('/comment/new/<int:blog_id>', methods=['GET','POST'])
def new_comment(blog_id):
    form = BlogCommentsForm()
    blog=Blog.query.get(blog_id)
    if form.validate_on_submit():
        description=form.description.data

        new_comment=BlogComments(description=description,user_id=current_user._get_current_object().id,blog_id=blog_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment', blog_id=blog_id))


    all_comments=BlogComments.query.filter_by(blog_id=blog_id).all()
    return render_template('comments.html', form = form, comment = all_comments, blog = blog)



