# server/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    })

db = SQLAlchemy(metadata=metadata)

# Association table to store many-to-many relationship between emmployees and meetings
employees_meetings = db.Table(
    'employees_meetings', metadata,
    db.Column('employee_id',
              db.Integer,
              db.ForeignKey('employees.id'),
              primary_key=True),
    db.Column('meeting_id',
              db.Integer,
              db.ForeignKey('meetings.id'),
              primary_key=True))


class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    hire_date = db.Column(db.Date)

    meetings = db.relationship('Meeting',
                               back_populates='employees',
                               secondary=employees_meetings)

    def __repr__(self):
        return f'<Employee {self.id}, {self.name}, {self.hire_date}>'


class Meeting(db.Model):
    __tablename__ = 'meetings'

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String)
    scheduled_time = db.Column(db.DateTime)
    location = db.Column(db.String)

    employees = db.relationship('Employee',
                                back_populates='meetings',
                                secondary=employees_meetings)

    def __repr__(self):
        return f'<Meeting {self.id}, {self.topic}, {self.scheduled_time}, {self.location}>'


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    budget = db.Column(db.Integer)

    def __repr__(self):
        return f'<Review {self.id}, {self.title}, {self.budget}>'
