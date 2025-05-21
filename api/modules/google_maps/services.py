import requests
import os
from rest_framework.exceptions import ValidationError
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY', None)


class services:
    def get_place(self, args):
        if args.get('search', None) is None:
            raise ValidationError({
                'status': 'FAILED',
                'message': 'search params is required',
            })

        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

        params = {
            'query': args.get('search'),
            'key': GOOGLE_MAPS_API_KEY
        }
        response = requests.get(url, params=params)
        data = response.json()

        if data.get('status') == 'OK':
            return {
                'status': "SUCCESS",
                'message': "SUCCESS",
                'payload': data.get('results', [])
            }

        return {
            'status': 'FAILED',
            'message': 'Maps API Request Error',
        }

    def get_place_nearby(self, args):
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

        params = {
            'location': args.get('location'),
            'radius': args.get('radius', 1000),
            'type': args.get('type'),
            'key': GOOGLE_MAPS_API_KEY
        }

        response = requests.get(url, params=params)
        data = response.json()

        if data.get('status') == 'OK':
            return {
                'status': "SUCCESS",
                'message': "SUCCESS",
                'payload': data.get('results', [])
            }

        return {
            'status': 'FAILED',
            'message': 'Maps API Request Error',
        }

    def get_directions(self, args):
        url = 'https://maps.googleapis.com/maps/api/directions/json'

        params = {
            'origin': args.get('origin'),
            'destination': args.get('destination'),
            'mode': args.get('mode'),
            'key': GOOGLE_MAPS_API_KEY
        }

        response = requests.get(url, params=params)
        data = response.json()
        if data.get('status') == 'OK':
            return {
                'status': "SUCCESS",
                'message': "SUCCESS",
                'payload': {
                    'way_points': data.get('geocoded_waypoints', []),
                    'routes': data.get('routes', []),
                }
            }

        return {
            'status': 'FAILED',
            'message': 'Maps API Request Error',
        }

    def get_distance_matrix(self, args):
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json'

        params = {
            'origins': args.get('origins'),
            'destinations': args.get('destinations'),
            'mode': args.get('mode'),
            'key': GOOGLE_MAPS_API_KEY
        }

        response = requests.get(url, params=params)
        data = response.json()

        if data.get('status') == 'OK':
            return {
                'status': "SUCCESS",
                'message': "SUCCESS",
                'payload': {
                    'destination_addresses': data.get('destination_addresses', []),
                    'origin_addresses': data.get('origin_addresses', []),
                    'rows': data.get('rows', []),
                }
            }

        return {
            'status': 'FAILED',
            'message': 'Maps API Request Error',
        }
