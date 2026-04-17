from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates , relationship

from datetime import date

db = SQLAlchemy()

# Define Models here

class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'
    
    id = db.column(db.Integer, primary_key=True)
    work_out_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    sets = db.Column(db.Integer,default=0)
    reps = db.Column(db.Integer,default=0)
    duration_seconds = db.Column(db.Integer, default=0)
    
    
    
class Workout(db.Model):
    __tablename__ = 'workouts'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text) 
    workout_exercises = relationship('WorkoutExercise', back_populates='workout', cascade='all, delete-orphan')
    exercises = relationship('Exercise', secondary='workout_exercises', back_populates='workouts')
    
class Exercise(db.Model):
    __tablename__ = 'exercises'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(100), nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)
    workout_exercises = relationship('WorkoutExercise', backref='exercise', cascade='all, delete-orphan')
    workouts = relationship('Workout', secondary='workout_exercises', back_populates='exercises')
    
    
    
    