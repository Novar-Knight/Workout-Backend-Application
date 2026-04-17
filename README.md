# Workout-Backend-Application

# Project Title

Workout-Backend-Application

# Project Description

This is a Flask REST API for managing workouts and exercises.
It allows users to create workouts, create exercises, and link exercises to workouts using a many-to-many relationship with additional data such as reps, sets, and duration

# The system is built by ;
Flask
Flask-SQLAlchemy
Flask-Migrate
Marshmallow for serialization/validation

# Tech Stack
Python 3.8+
Flask 2.2.2
Flask-SQLAlchemy 3.0.3
Flask-Migrate 3.1.0
Marshmallow 3.20.1
Pipenv

# Installation Instructions
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
flask db init
flask db migrate -m "init"
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

Server runs at:

http://127.0.0.1:5555

# API Endpoints
1. Workouts

GET /workouts
Returns all workouts

GET /workouts/<id>
Returns a single workout with exercises

POST /workouts
Creates a workout

Example body:

```bash
{
  "date": "2026-04-17",
  "duration_minutes": 45,
  "notes": "Morning workout"
}
```

DELETE /workouts/<id>
Deletes a workout

2. Exercises

GET /exercises
Returns all exercises

GET /exercises/<id>
Returns a single exercise with workouts

POST /exercises
Creates an exercise

Example body:

```bash
{
  "name": "Push Up",
  "category": "Strength",
  "equipment_needed": false
}
```

DELETE /exercises/<id>
Deletes an exercise

3. Workout Exercises (Join Table)

POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
Adds an exercise to a workout

Example body:

```bash
{
  "reps": 15,
  "sets": 3,
  "duration_seconds": 60
}
```

# Testing

You can test endpoints using:

Postman
curl
Flask shell

Example:

```bash
curl http://127.0.0.1:5555/workouts
```

# Project Structure

```bash
.
├── instance
│   └── app.db
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── e37e8a70c02a_rebuild_tables.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
└── server
    ├── app.py
    ├── instance
    │   └── app.db
    ├── model.py
    ├── schemas.py
    └── seed.py
```    



