from PIL import Image
from flask import session,render_template, url_for, redirect, flash
from main import app, db, bcrypt
from main.models import Visitor, Place, Hospital, Agent
from main.forms import regvisitor, regplace, reghospital, vislogin, hospitallogin, placelogin, agentlogin, update_visitor_account, update_place_account
from flask_login import login_required, logout_user, login_user, current_user
from flask import request
import secrets
import os

#routes for home
@app.route('/', methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def index():
    return render_template('index.html')

#routes for after successful login
# @login_required is kept so that no one can go directly from URL
@app.route('/golog_vis',methods=['GET','POST'])
@login_required
def govis():
    if session["userType"]!="visitor":
        flash("No access", 'error')
        return redirect(url_for('index'))
    else:
        return render_template('golog_visitor.html')

@app.route('/golog_pla',methods=['GET','POST'])
@login_required
def gopla():
    if session["userType"]!="place":
        flash("No access", 'error')
        return redirect(url_for('index'))
    else:
        return render_template('golog_place.html')

@app.route('/golog_hosp',methods=['GET','POST'])
@login_required
def gohosp():
    if session["userType"]!="hospital":
        flash("No access", 'error')
        return redirect(url_for('index'))
    else:    
        return render_template('golog_hospital.html')

@app.route('/golog_agent',methods=['GET','POST'])
@login_required
def goagent():
    if session["userType"]!="agent":
        flash("No access", 'error')
        return redirect(url_for('index'))
    else:   
        visitor_status = Visitor.query.all() 
        places_status = Place.query.all()
        hospital_status = Hospital.query.all()
        return render_template('golog_agent.html', visitor_status=visitor_status, hospital_status=hospital_status, places_status=places_status)
    
#routes for login form
#is authenticated and session[] are used to keep track of original users.
@app.route('/log_visitor', methods=['GET','POST'])
def log_vis():
    if (current_user.is_authenticated) and (session["userType"]=="visitor"):
        return redirect(url_for('govis'))
    session["userType"]="agent"
    session["userType"]="visitor"
    if current_user.is_authenticated:
        return redirect(url_for('govis'))
    form=vislogin()
    if form.validate_on_submit():
        visit= Visitor.query.filter_by(email=form.email.data).first()
        if visit and bcrypt.check_password_hash(visit.password, form.password.data):
            flash('You are Logged In!','success')
            login_user(visit)
            return redirect(url_for('govis'))
        else:
            flash('Error Occurred. Please check email and password', 'error')
    return render_template('log_visitor.html', form=form)

@app.route('/log_place', methods=['GET','POST'])
def log_place():
    if (current_user.is_authenticated) and (session["userType"]=="place"):
        return redirect(url_for('gopla'))
    session["userType"]="agent"
    session["userType"]="place"
    if current_user.is_authenticated:
        return redirect(url_for('gopla'))
    form=placelogin()
    if form.validate_on_submit():
        place= Place.query.filter_by(email=form.email.data).first()
        if place and bcrypt.check_password_hash(place.password, form.password.data):
            flash('You are Logged In!','success')
            login_user(place)
            return redirect(url_for('gopla'))
        else:
            flash('Error Occurred Please check email and password', 'error')
    return render_template('log_place.html', form=form)

@app.route('/log_hospital', methods=['GET','POST'])
def log_hospital():
    if (current_user.is_authenticated) and (session["userType"]=="hospital"):
        return redirect(url_for('gohosp'))
    session["userType"]="hospital"
    if current_user.is_authenticated:
        return redirect(url_for('gohosp'))
    form=hospitallogin()
    if form.validate_on_submit():
        hosp= Hospital.query.filter_by(email=form.email.data).first()
        if hosp and (hosp.password==form.password.data):
            flash('You are Logged In!','success')
            login_user(hosp)
            return redirect(url_for('gohosp'))
        else:
            flash('Error Occurred Please check email and password', 'error')
    return render_template('log_hospital.html', form=form)

@app.route('/log_agent', methods=['GET','POST'])
def log_agent():
    if (current_user.is_authenticated) and (session["userType"]=="agent"):
        return redirect(url_for('goagent'))
    session["userType"]="agent"
    form=agentlogin()
    if form.validate_on_submit():
        agen= Agent.query.filter_by(email=form.email.data).first()
        if agen and (agen.password==form.password.data):
            flash('You are Logged In!','success')
            login_user(agen)
            return redirect(url_for('goagent'))
        else:
            flash('Error Occurred Please check email and password', 'error')
    return render_template('log_agent.html', form=form)


#registration forms' routes along with addition of data in databases
@app.route('/reg_visitor', methods=['GET','POST'])
def reg_visitor():
    # if current_user.is_authenticated:
    #     return redirect(url_for('logout'))
    form = regvisitor()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.create_all()
        new_visit=Visitor(name=form.name.data, email=form.email.data, password=hashed_password, address=form.address.data, city=form.city.data, phone=form.number.data, device_id=form.device_id.data)
        db.session.add(new_visit)
        db.session.commit()
        flash(f'Account Created for {form.name.data}!', 'success')
        return redirect(url_for('log_vis'))
    return render_template('reg_visitor.html', form=form)

@app.route('/reg_place', methods=['GET','POST'])
def reg_place():
    # if current_user.is_authenticated:
    #     return redirect(url_for('logout'))
    form= regplace()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.create_all()
        new_place=Place(name=form.name.data, email=form.email.data, password=hashed_password, address=form.address.data, city=form.city.data, phone=form.number.data)
        db.session.add(new_place)
        db.session.commit()
        flash(f'Account Created!', 'success')
        return redirect(url_for('log_place'))
    return render_template('reg_place.html', form=form)

@app.route('/reg_hospital', methods=['GET','POST'])
def reg_hospital():
    # if current_user.is_authenticated:
    #     return redirect(url_for('logout'))
    form =reghospital()
    if form.validate_on_submit():
        # hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.create_all()
        new_hos= Hospital(license=form.reg.data, name=form.name.data, email=form.email.data, address=form.address.data, city=form.city.data)
        db.session.add(new_hos)
        db.session.commit()
        flash(f'Request Sent Wait for approval from agent', 'success')
        return redirect(url_for('log_hospital'))
    return render_template('reg_hosp.html', form=form)

def save_picture(image_file):
    random_hex = secrets.token_hex(8)
    _ , f_ext = os.path.splitext(image_file.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/Images', picture_fn)

    output_size = (125, 125)
    i = Image.open(image_file)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn

@app.route('/visitor_account', methods=['GET','POST'])
@login_required
def visitor_account():
    form = update_visitor_account()
    if form.validate_on_submit():
        if form.image_file.data:
            picture_file = save_picture(form.image_file.data)
            current_user.image_file = picture_file
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.device_id = form.device_id.data
        current_user.phone = form.phone.data
        current_user.address = form.address.data
        current_user.city = form.city.data
        db.session.commit()
        flash(f'Account Updated', 'success')
        return redirect(url_for('visitor_account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
        form.device_id.data = current_user.device_id
        form.phone.data = current_user.phone
        form.address.data = current_user.address
        form.city.data = current_user.city

    
    image_file = url_for('static', filename='Images/' + current_user.image_file)
    return render_template('visitor_account.html', image_file=image_file, form=form)

@app.route('/place_account', methods=['GET','POST'])
@login_required
def place_account():
    form = update_place_account()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.phone = form.phone.data
        current_user.address = form.address.data
        current_user.city = form.city.data
        db.session.commit()
        flash(f'Account Updated', 'success')
        return redirect(url_for('visitor_account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
        form.phone.data = current_user.phone
        form.address.data = current_user.address
        form.city.data = current_user.city


    return render_template('place_account.html', form=form)


#routes for logging out
@app.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))
