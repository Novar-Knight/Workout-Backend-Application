#!/usr/bin/env python3

from app import app
from models import db, Workout, Exercise, WorkoutExercise
from datetime import date

with app.app_context():
# reset data and add new example data, committing to db 
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    exercise1 = Exercise(name='Push Up', category='Strength', equipment_needed=False)
    exercise2 = Exercise(name='Squat', category='Legs', equipment_needed=False)
    workout1 = Workout(date=date.today(), duration_minutes=45, notes='Morning session')

    db.session.add_all([exercise1, exercise2, workout1])
    db.session.commit()

    link = WorkoutExercise(workout_id=workout1.id, exercise_id=exercise1.id, reps=15, sets=3, duration_seconds=60)
    db.session.add(link)
    db.session.commit()
    print('Seeded!')