# Bread Network

## Setup Instructions

### Django Setup
1. Install dependencies.
```shell
python -m venv env
source env/bin/activate
pip install requirements.txt
```

#### MongoDB Setup
1. Create new MongoDB database using the Mongo Console or MongoDB Compass with `bread-network` and keep the initial collection name as `bread-network`
2. Perform migrations
```shell
python manage.py makemigrations
python manage.py migrate
```

## Run Instructions
1. After installing dependencies, run the Django server using the command:
```shell
python manage.py runserver
```
The backend engine will be available at http://localhost:8000/ (8000 is the default port, might change according to the system.)