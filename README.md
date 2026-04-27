# Workout-Backend-Application

## Project Description

This is a Flask REST API for managing workouts and exercises.
It allows users to create workouts, create exercises, and link exercises to workouts using a many-to-many relationship with additional data such as reps, sets, and duration

## The system is built by ;

```bash
Flask
Flask-SQLAlchemy
Flask-Migrate
Marshmallow for serialization/validation
```
## Tech Stack

```bash
Python 3.12
Flask 2.2.2
Flask-SQLAlchemy 3.0.3
Flask-Migrate 3.1.0
Marshmallow 3.20.1
Pipenv
```

## Installation Instructions
1. Clone repository

```bash
git clone <git@github.com:Novar-Knight/Workout-Backend-Application.git>
cd Workout-Backend-Application
```

2. Install dependencies

```bash
pipenv install
pipenv shell
```
3. Run Migrations

```bash
export FLASK_APP=server.app
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```
4. Seed Database

```bash
python -m server.seed
```
5. Run Server

```bash
python -m server.app
```
6. Flask Shell
```bash
flask --app server.app shell
```
Server runs at:

http://127.0.0.1:5555

## API Endpoints
1. Workouts

A.GET /workouts
Returns all workouts

B.GET /workouts/<id>
Returns a single workout with exercises

C.POST /workouts
Creates a workout


D.DELETE /workouts/<id>
Deletes a workout

2. Exercises

A.GET /exercises
Returns all exercises

B.GET /exercises/<id>
Returns a single exercise with workouts

C.POST /exercises
Creates an exercise


D.DELETE /exercises/<id>
Deletes an exercise

3. Workout Exercises (Join Table)

A.POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
Adds an exercise to a workout



## Testing

You can test endpoints using:

```bash
Postman
curl
Flask shell
```
Example:

```bash
curl http://127.0.0.1:5555/workouts
```

## Project Structure

```bash
.
.
├── instance
│   └── app.db
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── 175024d78462_initial_migration.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
└── server
    ├── app.py
    ├── __init__.py
    ├── instance
    ├── model.py
    ├── schemas.py
    └── seed.py
```    



