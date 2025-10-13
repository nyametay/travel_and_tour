from data import app
from flask import render_template, request, redirect, url_for, flash, session
from data.modules import *
from data.models import *
from data.models import Booking
from data.utils import *
from datetime import datetime


@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if 'admin' in session:
        return redirect(url_for('admin_home'))
    if request.method == 'GET':
        return render_template('admin/login.html')
    try:
        admin_email = request.form['email']
        admin_password = request.form['password']
        admin = get_admin(admin_email)
        if not admin:
            flash('Admin Not Found', 'danger')
            return redirect(url_for('login'))
        if admin and not admin.check_password(admin_password):
            flash('Wrong Admin Credentials', 'danger')
            return redirect(url_for('login'))
        session['admin'] = admin.to_dict()
        flash('Login Successfully', 'success')
        return redirect(url_for('admin_home'))
    except Exception as e:
        print(e)
        flash('Admin Login Failed', 'danger')
        return redirect(url_for('login'))


@app.route('/admin/home', methods=['GET', 'POST'])
def admin_home():
    if 'admin' not in session:
        return redirect(url_for('login'))
    try:
        destinations_ = Locations.query.all()
        bookings_ = Booking.query.order_by(Booking.id.desc()).all()
        return render_template('admin/home.html', destinations=destinations_, bookings=bookings_)
    except Exception as e:
        print(e)
        flash('Error Occurred', 'danger')
        return redirect(url_for('admin_home'))


@app.route('/admin/add_destination', methods=['POST'])
def add_destination():
    try:
        name = request.form['name']
        description = request.form['description']
        file = request.files['image']

        if not file:
            flash("No image uploaded!", "danger")
            return redirect(url_for('admin_home'))

        new_destination = Locations(
            location_name=name,
            description=description,
            image_data=file.read(),  # Store binary data
            image_mimetype=file.mimetype  # Save MIME type (e.g., image/png)
        )

        db.session.add(new_destination)
        db.session.commit()

        flash("Destination added successfully!", "success")
        return redirect(url_for('admin_home'))
    except Exception as e:
        print(e)
        flash('Error Occurred', 'danger')
        return redirect(url_for('admin_home'))


@app.route('/admin/delete/<int:id>')
def delete_destination(id):
    try:
        dest = Locations.query.get_or_404(id)
        db.session.delete(dest)
        db.session.commit()
        flash('Destination deleted.', 'danger')
        return redirect(url_for('admin_home'))
    except Exception as e:
        print(e)
        flash('Error Occurred', 'danger')
        return redirect(url_for('admin_home'))


@app.route('/admin/edit_destination/<int:id>', methods=['POST'])
def edit_destination(id):
    try:
        destination = Locations.query.get_or_404(id)
        destination.location_name = request.form['name']
        destination.description = request.form['description']

        file = request.files.get('image')
        if file:
            destination.image_data = file.read()
            destination.image_mimetype = file.mimetype

        db.session.commit()
        flash("Destination updated successfully!", "success")
        return redirect(url_for('admin_home'))
    except Exception as e:
        print(e)
        flash('Error Occurred', 'danger')
        return redirect(url_for('admin_home'))


@app.route('/admin/logout')
def logout():
    if 'admin' in session:
        session.pop('admin')
        flash('Logout Successfully', 'success')
        return redirect(url_for('home'))
    return None


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/bookings', methods=['POST'])
def bookings():
    try:
        print(request.form)
        name, email, phone, destination, date_str, special_note = get_bookings(request.form)
        travel_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        new_booking = Booking(name, email, phone, destination, travel_date, special_note)
        db.session.add(new_booking)
        db.session.commit()
        send_email_sendgrid(new_booking)
        flash('Booking added', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
        flash('Booking failed', 'danger')
        return redirect(url_for('home'))


@app.route('/destinations', methods=['GET'])
def destinations():
    try:
        destinations_ = Locations.query.all()
        return render_template('destinations.html', destinations=destinations_)
    except Exception as e:
        print(e)
        flash('Error Occurred', 'danger')
        return redirect(url_for('home'))
