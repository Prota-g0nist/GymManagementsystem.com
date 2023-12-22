from flask import Flask,Blueprint,render_template, request,redirect,url_for,jsonify,flash
import sqlite3 
from database import trainer_appointment,mark_attendance,register_member

dp= Blueprint('main', __name__)
@dp.route('/')
def index():
    return render_template('index.html')
@dp.route('/register')
def register():
    return render_template ("Member_registration.html")
@dp.route('/attandance_s')
def attandance_s():
    return render_template("attandancesucessfull.html")
@dp.route('/attendance')
def attendance():
    return render_template("attendance.html")
@dp.route('/equipment')
def equipment():
    return render_template("equipment.html")
@dp.route('/register_s')
def register_s():
    return render_template("registerationsucessfull.html")
@dp.route('/trainer')
def trainer():
    return render_template("trainer.html")
@dp.route('/appointment_s')
def appointment_s():
    return render_template("appointmentsucessfull.html")
@dp.route('/appointmentl')
def appointmentl():
    return render_template("appointmentl.html")

@dp.route('/add_member', methods=['GET','POST'])
def addmemberroute():
    name = request.form.get('name')
    email = request.form.get('email')
    phone_number = request.form.get('phone')
    membership_type = request.form.get('membership_type')

    if not all([name, email, phone_number, membership_type]):
        flash('Missing data', 'error')
        return redirect(url_for('main.register'))

    try:
        register_member(name, email, phone_number, membership_type)
        flash('Member added successfully', 'success')
        return redirect(url_for('main.register_s'))

    except sqlite3.IntegrityError:
        flash('Member already exists', 'error')
        return redirect(url_for('main.register'))
    
@dp.route('/add_attandance', methods=['GET','POST'])
def addattandance():
    member_id = request.form.get('member_id')
    attendance_date = request.form.get('attendance_date')
    attendance_status = request.form.get('attendance_status')

    if not all([member_id, attendance_date, attendance_status]):
        flash('Missing data', 'error')
        return redirect(url_for('main.attendance'))

    try:
        mark_attendance(member_id, attendance_date, attendance_status)
        flash('Attendance added successfully', 'success')
        return redirect(url_for('main.attandance_s'))

    except sqlite3.IntegrityError:
        flash('Attandance already exists', 'error')
        return redirect(url_for('main.attendance'))
    
@dp.route('/make_appointment', methods=['GET','POST'])
def appointment():
    trainer = request.form.get('trainer_name')
    appointment_date = request.form.get('appointment_date')
    appointment_time = request.form.get('appointment_time')
    member_id = request.form.get('member_id')  # Get member_id from form data

    if not all([trainer, appointment_date, appointment_time, member_id]):
        flash('Missing data', 'error')
        return redirect(url_for('main.appointment'))

    try:
        trainer_appointment(trainer, appointment_date, appointment_time, member_id)
        flash('Appointment added successfully', 'success')
        return redirect(url_for('main.appointment_s'))

    except sqlite3.IntegrityError:
        flash('Appointment already exists', 'error')
        return redirect(url_for('main.appointment'))
    

