from flask import render_template, request, redirect,flash, url_for, abort
from . import main
from .forms import BlogForm, CommentForm, UpdateProfile
from ..models import User, Comment, Blog
from flask_login import login_required, current_user
from .. import db, photos
import datetime
from ..requests import getQuotes

@main.route('/')
def index():
    blogs = Blog.query.all()
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to the best Blog Website'
    quote = getQuotes()
    quote1 = getQuotes()
    quote2 = getQuotes()
    quote3 = getQuotes()
    #quote4 = getQuotes()
    #quote5 = getQuotes()
    #quote6 = getQuotes()

    return render_template('index.html' title=title, blogs=blogs, quote=quote, quote1=quote1, quote2=quote2, quote3=quote3 )

 @main.route('/blog/new', methods = ['GET','PODT'])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog = blog_form.text.data

        #Update blog instance
        