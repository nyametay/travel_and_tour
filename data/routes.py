from data import app
from flask import render_template, request, redirect, url_for, flash
from data.modules import *
from data.models import *
from data.models import Booking
from data.utils import *
from datetime import datetime


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
        send_email_smtp(new_booking)
        flash('Booking added', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
        flash('Booking failed', 'danger')
        return redirect(url_for('home'))


@app.route('/destinations', methods=['GET'])
def destinations():
    return render_template('destinations.html')
