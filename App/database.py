import sqlite3 
from flask import request
gymdb='Gym_management_system.db'

# Connect to SQLite database

def createtable():
    conn=sqlite3.connect(gymdb)
    c = conn.cursor()
    # Create a Members table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            membership_type TEXT NOT NULL
        )
    ''')

    # Create a trainer_name Appointmet Table if it doesn't exist 
    c.execute('''
        CREATE TABLE IF NOT EXISTS Appointment(
                trainer TEXT NOT NULL, 
                member_id Integer NOT NULL,
                appointment_date DATE ,
                appointment_time TIME,
                FOREIGN KEY (member_id) REFERENCES Members (member_id)
        )           
                
        ''')

    # Create an Attendance table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS Attendance (
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            attendance_date TEXT NOT NULL,
            attendance_status TEXT NOT NULL,
            FOREIGN KEY (member_id) REFERENCES Members (member_id)
        )
    ''')

    conn.commit()
    conn.close()


def register_member(name, email, phone, membership_type):
        conn=sqlite3.connect(gymdb)
        c = conn.cursor()
  # Insert data into the Members table
        c.execute("INSERT INTO Members (name, email, phone, membership_type) VALUES (?, ?, ?, ?)",
                       (name, email, phone, membership_type))

        conn.commit()
        conn.close()




def mark_attendance(member_id, attendance_date,attendance_status):
        conn=sqlite3.connect(gymdb)
        c = conn.cursor()

        # Insert data into the Attendance table
        c.execute('''
            INSERT INTO Attendance (member_id, attendance_date, attendance_status)
            VALUES (?, ?, ?)
        ''', (member_id, attendance_date, attendance_status))

        conn.commit()
        conn.close()

    


def trainer_appointment(trainer, appointment_date, appointment_time, member_id):
    conn = sqlite3.connect(gymdb)
    c = conn.cursor()

    # Insert data into the Appointment table
    c.execute('''
        INSERT INTO Appointment (trainer, appointment_date, appointment_time, member_id)
        VALUES (?, ?, ?, ?)
    ''', (trainer, appointment_date, appointment_time, member_id))

    conn.commit()
    conn.close()