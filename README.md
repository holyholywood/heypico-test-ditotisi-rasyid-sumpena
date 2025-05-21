# Hey Pico Technical Pre-Technical Test

Simple API Application with Google Maps API Integration.

## Tech

- python3
- django
- djangorestframework

## Requirements

- python 3.10 or later and pip
- MySql

## Installation

After cloned this repository. you can try these steps for installing application:

1. Copy `.env.example` to `.env`
2. Put your Google API Key to `GOOGLE_MAPS_API_KEY` in `.env`
3. Make a python virtual environment `python3 venv myvenv` then `source venv/bin/activate` to activate virtual environment
4. run `pip install -r requirements.txt`
5. run `python manage.py makemigrations`
6. run `python manage.py migrate`
7. run `python manage.py createsuperuser` and follow these steps to create user to authenticate later.
8. run server with `python manage.py runserver` and your apps will started in http://localhost:8000

# Available endpoints

### Search Places

`/api/google-maps/places/find`

example:

`http://locallhost:8000/api/google-maps/places/find?search=Coffee Shop in Hang tuah South Jakarta`

### Get Place Nearby

`/api/google-maps/places/nearby`

example:

`http://locallhost:8000/api//google-maps/places/nearby?location=-6.230002194424081,106.79752693264508&radius=1000&type=restaurant`

### Get Directions

`/api/google-maps/directions`

example:

`http://locallhost:8000/api/google-maps/directions?origin=Plaza Senayan&destination=Monumen Nasional&mode=transit`

### Get Get Distance Matrix

`/api/google-maps/distance-matrix`

example:

`http://locallhost:8000/api/google-maps/distance-matrix?origins=Kopi Mandja Hang Tuah|Blok M PLaza&destinations=Praktis&mode=driving`
