from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates , relationship
from sqlalchemy import CheckConstraint
from datetime import date

db = SQLAlchemy()

# Define Models here

class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'
    
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    sets = db.Column(db.Integer,default=0)
    reps = db.Column(db.Integer,default=0)
    duration_seconds = db.Column(db.Integer, default=0)
    
    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")
    
    
    
    _table_args__ = (
        CheckConstraint('reps >= 0'),
        CheckConstraint('sets >= 0'),
        CheckConstraint('duration_seconds >= 0'),
    )
   
        
class Workout(db.Model):
    __tablename__ = 'workouts'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text) 
    workout_exercises = db.relationship('WorkoutExercise', back_populates='workout', cascade='all, delete-orphan')
    exercises = db.relationship('Exercise', secondary='workout_exercises', back_populates='workouts')
    
    __table_args__ = (CheckConstraint('duration_minutes > 0'),)
    
    @validates('duration_minutes')
    def validate_duration(self, key, value):
        if value <= 0:
            raise ValueError('duration must be greater than 0')
        return value
    
    
class Exercise(db.Model):
    __tablename__ = 'exercises'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(100), nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)
    workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise', cascade='all, delete-orphan')
    workouts = db.relationship('Workout', secondary='workout_exercises', back_populates='exercises')
    
    @validates('name')
    def validate_name(self, key, value):
        if not value or len(value.strip()) < 2:
            raise ValueError('name must be at least 2 characters')
        return value.strip()
    
    