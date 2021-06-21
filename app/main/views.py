from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Blog, User,BlogComments,Upvotes,Downvotes
from .forms import BlogForm,BlogCommentsForm,UpvotesForm,DownvotesForm,UpdateProfile
from flask.views import View,MethodView
from .. import db,photos
from ..request import getQuotes
import markdown2 
#views

@main.route('/', methods=['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data.
    ''' 
    blog=Blog.query.filter_by().first()
    quotes=getQuotes()

    title='Home'

    technologyblog=Blog.query.filter_by(category="technologyblog")
    sportsblog=Blog.query.filter_by(category="sportsblog")
    academicblog=Blog.query.filter_by(category="academicblog")
    researchblog=Blog.query.filter_by(category="researchblog")
    politicablog=Blog.query.filter_by(category="politicablog")

    upvotes=Upvotes.get_all_upvotes(id)


    return render_template('home.html',title=title,blog=blog,technologyblog=technologyblog,sportsblog=sportsblog,academicblog=academicblog,researchblog=researchblog,politicablog=politicablog,quotes=quotes) 



@main.route('/blogs/new/', methods=['GET','POST']) 
@login_required
def new_blog():
    form= BlogForm() 
    my_upvotes=my_upvotes=Upvotes.query.filter_by(blog_id=Blog.id)
    if form.validate_on_submit():
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





@main.route('/blog/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
@login_required
def upvote(blog_id):
    blog = Blog.query.get(pitch_id)
    user = current_user
    blog_upvotes = Upvote.query.filter_by(blog_id= blog_id)
    
    if Upvote.query.filter(Upvote.user_id==user.id,Upvote.blog_id==blog_id).first():
        return  redirect(url_for('main.index'))


    new_upvote = Upvote(blog_id=blog_id, user = current_user)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))



#    new_upvote = Upvote(user=current_user, pitch=pitch, vote_number=1)
#    new_vote.save_vote()
# return redirect(url_for('main.index'))


@main.route('/blog/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(blog_id):
    blog = Blog.query.get(blog_id)
    user = current_user
    blog_downvotes = Downvote.query.filter_by(blog_id= blog_id)
    
    if Downvote.query.filter(Downvote.user_id==user.id,Downvote.blog_id==blog_id).first():
        return  redirect(url_for('main.index'))


    new_downvote = Downvote(blog_id=blog_id, user = current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index')) 

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)  



@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))





