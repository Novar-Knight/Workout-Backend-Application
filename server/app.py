from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from marshmallow import  ValidationError
from server.model import db, Workout, Exercise, WorkoutExercise
from server.schemas import WorkoutSchema, ExerciseSchema, WorkoutExerciseSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define Routes here
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_exercise_schema = WorkoutExerciseSchema()

@app.errorhandler(ValidationError)
def handle_validation(err):
    return jsonify(err.messages), 400

@app.route('/workouts', methods=['GET'])
def get_workouts():
    return workouts_schema.dump(Workout.query.all())

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    data = workout_schema.dump(workout)
    data['exercises'] = [{
        'id': workout_exercise.exercise.id,
        'name': workout_exercise.exercise.name,
        'reps': workout_exercise.reps,
        'sets': workout_exercise.sets,
        'duration_seconds': workout_exercise.duration_seconds
    } for workout_exercise in workout.workout_exercises]
    return data

@app.route('/workouts', methods=['POST'])
def create_workout():
    data = workout_schema.load(request.json)
    workout = Workout(**data)
    db.session.add(workout)
    db.session.commit()
    return workout_schema.dump(workout), 201


@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return make_response({'message':'deleted'}, 200)

@app.route('/exercises', methods=['GET'])
def get_exercises():
    return exercises_schema.dump(Exercise.query.all())

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    data = exercise_schema.dump(exercise)
    data['workouts'] = [{'id': w.id, 'date': str(w.date)} for w in exercise.workouts]
    return data

@app.route('/exercises', methods=['POST'])
def create_exercise():
    data = exercise_schema.load(request.json)
    exercise = Exercise(**data)
    db.session.add(exercise)
    db.session.commit()
    return exercise_schema.dump(exercise), 201

@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    db.session.delete(exercise)
    db.session.commit()
    return {'message':'deleted'}

@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise(workout_id, exercise_id):
    Workout.query.get_or_404(workout_id)
    Exercise.query.get_or_404(exercise_id)
    data = workout_exercise_schema.load(request.json)
    join = WorkoutExercise(workout_id=workout_id, exercise_id=exercise_id, **data)
    db.session.add(join)
    db.session.commit()
    return workout_exercise_schema.dump(join), 201



if __name__ == '__main__':
    app.run(port=5555, debug=True)
