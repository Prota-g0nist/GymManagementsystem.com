
-- Table for Members
CREATE TABLE Members (
    member_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    membership_type TEXT NOT NULL
);

-- Table for Attendance
CREATE TABLE Attendance (
    attendance_id INTEGER PRIMARY KEY,
    member_id INTEGER,
    attendance_date DATE NOT NULL,
    attendance_status TEXT NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- Table for Equipment
CREATE TABLE Equipment (
    equipment_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

-- Insert data into the Equipment table
INSERT INTO Equipment (name, description)
VALUES
    ('Treadmill', 'Cardio equipment for running or walking.'),
    ('Weights', 'Dumbbells and barbells for strength training.'),
    ('Elliptical Machine', 'Low-impact cardio equipment.'),
    ('Stationary Bike', 'Indoor cycling for cardio workouts.');

-- Table for Trainers
CREATE TABLE Trainers (
    trainer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    specialization TEXT NOT NULL
);

-- Table for Appointments
CREATE TABLE Appointments (
    appointment_id INTEGER PRIMARY KEY,
    trainer_id INTEGER REFERENCES Trainers(trainer_id),
    member_id INTEGER REFERENCES Members(member_id),
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL
);
