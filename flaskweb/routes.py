from flask import render_template, url_for, flash, redirect, request, session
from flaskweb import app, db, bcrypt
from flaskweb.forms import RegistrationForm, LoginForm, RatingForm, SearchForm
from flaskweb.getData import getServices, getInfo, pass_today, updateRating, updateFavorite, getFavorite, remFavorite, \
    getServicesPage, ifMap
from flaskweb.search import Search, searchPage
from flask_login import login_user, current_user, logout_user, login_required
from flaskweb.models import User
from flask_paginate import Pagination, get_page_parameter, get_page_args

# The default route
@app.route('/', methods=['GET', 'POST'])

# The route for homepage
@app.route('/home/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        keyword = form.search.data
        return redirect(url_for('searchDisplay', keyword=keyword))
    return render_template('home.html', title='UmbSupport_Home', form=form)

# The route for about page
@app.route('/about/')
def about():
    return render_template('about.html', title='About us')

# The route for service display page
@app.route('/services/<string:service_name>')
def serviceDisplay(service_name):
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    data = getServices(service_name)
    total = len(data)
    pagination_data = getServicesPage(data, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if current_user.is_authenticated:
        email = current_user.email
        favoList = getFavorite(email)
    else:
        favoList=[]
    return render_template('serviceDisplay.html', title='Service Display',
                           service_name=service_name, favoList=favoList,
                           pagination_data=pagination_data,
                           page=page,
                           per_page=per_page,
                           pagination=pagination
                           )

# The route for service display page when add a favorite
@app.route('/services/<service_name>/<service_id>/add')
@login_required
def addFavorite(service_name, service_id):
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    data = getServices(service_name)
    total = len(data)
    pagination_data = getServicesPage(data, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    email = current_user.email
    result = updateFavorite(email, service_name, service_id)
    if result == 'success':
        flash('You have add one favorite successfully!', 'success')
    if current_user.is_authenticated:
        email = current_user.email
        favoList = getFavorite(email)
    else:
        favoList=[]
    return render_template('serviceDisplay.html', title='Service Display',
                           service_name=service_name, favoList=favoList,
                           pagination_data=pagination_data,
                           page=page,
                           per_page=per_page,
                           pagination=pagination
                           )

# The route for service display page when remove a favorite
@app.route('/services/<service_name>/<service_id>/remove')
@login_required
def removeFavorite(service_name, service_id):
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    data = getServices(service_name)
    total = len(data)
    pagination_data = getServicesPage(data, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    email = current_user.email
    result = remFavorite(email, service_name, service_id)
    if result == 'success':
        flash('You have removed one favorite successfully!', 'danger')
    if current_user.is_authenticated:
        email = current_user.email
        favoList = getFavorite(email)
    else:
        favoList=[]
    return render_template('serviceDisplay.html', title='Service Display',
                           service_name=service_name, favoList=favoList,
                           pagination_data=pagination_data,
                           page=page,
                           per_page=per_page,
                           pagination=pagination
                           )

# The route for search display page
@app.route('/searchDisplay/<keyword>', methods=['GET', 'POST'])
def searchDisplay(keyword):
    form = SearchForm()
    if keyword == 'hotline' or keyword == 'hotlines':
        data = getServices('hotlines')
    else:
        data = Search(keyword)
    total = len(data)

    if total != 0:
        map = ifMap(data)
    else:
        map = 'no'

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    pagination_data = searchPage(data, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    if current_user.is_authenticated:
        email = current_user.email
        favoList = getFavorite(email)
    else:
        favoList=[]
    if form.validate_on_submit():
        keyword = form.search.data
        return redirect(url_for('searchDisplay', keyword=keyword))
    return render_template('searchDisplay.html', title='Search Result',
                           form=form, keyword=keyword, favoList=favoList,
                           pagination_data=pagination_data,
                           page=page,
                           per_page=per_page,
                           pagination=pagination, map=map
                           )

# The route for search display when adding a favorite
@app.route('/searchDisplay/<keyword>/<service_name>/<service_id>/add', methods=['GET', 'POST'])
@login_required
def addFavoriteSearch(keyword, service_name, service_id):
    form = SearchForm()
    if keyword == 'hotline' or keyword == 'hotlines':
        data = getServices('hotlines')
    else:
        data = Search(keyword)
    total = len(data)

    if total != 0:
        map = ifMap(data)
    else:
        map = 'no'

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    pagination_data = searchPage(data, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    email = current_user.email
    result = updateFavorite(email, service_name, service_id)
    if result == 'success':
        flash('You have add one favorite successfully!', 'success')
    if current_user.is_authenticated:
        email = current_user.email
        favoList = getFavorite(email)
    else:
        favoList=[]
    if form.validate_on_submit():
        keyword = form.search.data
        return redirect(url_for('searchDisplay', keyword=keyword))
    return render_template('searchDisplay.html', title='Search Result', keyword=keyword,
                           form=form, favoList=favoList,
                           pagination_data=pagination_data,
                           page=page,
                           per_page=per_page,
                           pagination=pagination, map=map
                           )

# The route for search display when removing a favorite
@app.route('/searchDisplay/<keyword>/<service_name>/<service_id>/remove', methods=['GET', 'POST'])
@login_required
def remFavoriteSearch(keyword, service_name, service_id):
    form = SearchForm()
    if keyword == 'hotline' or keyword == 'hotlines':
        data = getServices('hotlines')
    else:
        data = Search(keyword)
    total = len(data)

    if total != 0:
        map = ifMap(data)
    else:
        map = 'no'
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    pagination_data = searchPage(data, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    email = current_user.email
    result = remFavorite(email, service_name, service_id)
    if result == 'success':
        flash('You have removed one favorite successfully!', 'danger')
    if current_user.is_authenticated:
        email = current_user.email
        favoList = getFavorite(email)
    else:
        favoList=[]
    if form.validate_on_submit():
        keyword = form.search.data
        return redirect(url_for('searchDisplay', keyword=keyword))
    return render_template('searchDisplay.html', title='Search Result', keyword=keyword,
                           form=form, favoList=favoList,
                           pagination_data=pagination_data,
                           page=page,
                           per_page=per_page,
                           pagination=pagination, map=map
                           )

# The route for detailed information page for one service
@app.route('/detailedInfo/<string:servicename>/<string:service_id>',
           methods=['GET', 'POST'])
def detailedInfo(servicename, service_id):
    form = RatingForm()
    today = pass_today()
    data = getInfo(servicename, service_id)
    if form.validate_on_submit():
        rating = form.rating.data
        return redirect(url_for('detailedInfoRating', servicename=servicename, service_id=service_id, rating=rating))
    return render_template('detailedInfo.html', title='Service Imformation',
                           data=data, servicename=servicename, today=today, form=form)

# The route for detailed information page for the search result
@app.route('/search/<keyword>/detailedInfo/<string:servicename>/<string:service_id>',
           methods=['GET', 'POST'])
def detailedSearch(servicename, service_id, keyword):
    form = RatingForm()
    today = pass_today()
    data = getInfo(servicename, service_id)
    if form.validate_on_submit():
        rating = form.rating.data
        return redirect(url_for('detailedSearchRating', servicename=servicename, service_id=service_id, rating=rating,
                                keyword=keyword))
    return render_template('detailedInfo.html', title='Service Imformation from Search',
                           data=data, servicename=servicename, today=today, form=form, keyword=keyword)

# The route for rating a service in a detailed information page
@app.route('/detailedInfo/<string:servicename>/<string:service_id>/<rating>',
           methods=['GET', 'POST'])
@login_required
def detailedInfoRating(servicename, service_id, rating):
    form = RatingForm()
    today = pass_today()
    email = current_user.email
    result = updateRating(servicename, service_id, rating, email)
    if result == 'success':
        flash('You have successfully rating it: ' + str(rating) + ' stars', 'success')
    data = getInfo(servicename, service_id)
    if form.validate_on_submit():
        rating = form.rating.data
        session.pop('_flashes', None)
        return redirect(url_for('detailedInfoRating', servicename=servicename, service_id=service_id, rating=rating))
    return render_template('detailedInfo.html', title='Service Imformation',
                           data=data, servicename=servicename, today=today, form=form)

# The route for rating a service in a detailed information page from search result
@app.route('/search/<keyword>/detailedInfo/<string:servicename>/<string:service_id>/<rating>',
           methods=['GET', 'POST'])
@login_required
def detailedSearchRating(servicename, service_id, rating, keyword):
    form = RatingForm()
    today = pass_today()
    email = current_user.email
    result = updateRating(servicename, service_id, rating, email)
    if result == 'success':
        flash('You have successfully rating it: ' + str(rating) + ' stars', 'success')
    data = getInfo(servicename, service_id)
    if form.validate_on_submit():
        rating = form.rating.data
        session.pop('_flashes', None)
        return redirect(url_for('detailedSearchRating', servicename=servicename, service_id=service_id, rating=rating,
                                keyword=keyword))
    return render_template('detailedInfo.html', title='Service Imformation from Search',
                           data=data, servicename=servicename, today=today, form=form, keyword=keyword)

# The route for the register page
@app.route("/register/", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        userjson = {'username': form.username.data, 'email':form.email.data,
                'password': hashed_pw, 'favorite': [], 'rating': {}}
        collection = db.user
        collection.insert_one(userjson)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# The route for the login page
@app.route("/login/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        userjson = db.user.find_one({'email': form.email.data})
        if userjson and bcrypt.check_password_hash(userjson['password'], form.password.data):
            user = User(email=userjson['email'], username=userjson['username'])
            login_user(user, remember=form.remenber.data)
            next_page = request.args.get('next')
            flash('Login successfully!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password:)', 'danger')
    return render_template('login.html', title='Login', form=form)

# The route for logout
@app.route("/logout/")
def logout():
    logout_user()
    flash("You've been logged out!", "success")
    return redirect(url_for('home'))

# The route for favorite page
@app.route("/favorite/")
@login_required
def account():
    email = current_user.email
    data = getFavorite(email)
    return render_template('account.html', title='Account', data=data)

# The route for removing a favorite at favorite page
@app.route("/favorite/rem/<servicename>/<service_id>/")
@login_required
def accountRem(servicename, service_id):
    email = current_user.email
    result = remFavorite(email, servicename, service_id)
    if result == 'success':
        flash('You have removed one favorite successfully', 'success')

    data = getFavorite(email)
    return render_template('account.html', title='Account', data=data)

# The route for financial abuse information page
@app.route("/checklist/")
def checkList():
    return render_template('checklist.html', title='Checklist')

# The route for statistics page
@app.route("/visualization/")
def visualization():
    return render_template('visualization.html', title='Visualization')
