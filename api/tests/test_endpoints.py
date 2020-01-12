from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from ..models import *


class TestPost(APITransactionTestCase):
    def test(self):
        cases = [
            # MEDAL
            {
                'url': 'medal-list',
                'data': {'name': 'test'},
                'model': 'Medal',
                'status': status.HTTP_201_CREATED,
                'method': 'POST'
            },
            {
                'url': 'medal-list',
                'data': {'wrong': 'test'},
                'model': 'Medal',
                'status': status.HTTP_400_BAD_REQUEST,
                'method': 'POST'
            },
            {
                'url': 'medal-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Medal',
                'status': status.HTTP_200_OK,
                'method': 'PUT'
            },
            {
                'url': 'medal-list',
                'data': {},
                'model': 'Medal',
                'status': status.HTTP_200_OK,
                'method': 'GET'
            },
            {
                'url': 'medal-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Medal',
                'status': status.HTTP_204_NO_CONTENT,
                'method': 'DELETE'
            },

            # GAMES
            {
                'url': 'games-list',
                'data': {'name': 'test'},
                'model': 'Games',
                'status': status.HTTP_201_CREATED,
                'method': 'POST'
            },
            {
                'url': 'games-list',
                'data': {'wrong': 'test'},
                'model': 'Games',
                'status': status.HTTP_400_BAD_REQUEST,
                'method': 'POST'
            },
            {
                'url': 'games-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Games',
                'status': status.HTTP_200_OK,
                'method': 'PUT'
            },
            {
                'url': 'games-list',
                'data': {},
                'model': 'Games',
                'status': status.HTTP_200_OK,
                'method': 'GET'
            },
            {
                'url': 'games-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Games',
                'status': status.HTTP_204_NO_CONTENT,
                'method': 'DELETE'
            },

            # TEAM
            {
                'url': 'team-list',
                'data': {'name': 'test'},
                'model': 'Team',
                'status': status.HTTP_201_CREATED,
                'method': 'POST'
            },
            {
                'url': 'team-list',
                'data': {'wrong': 'test'},
                'model': 'Team',
                'status': status.HTTP_400_BAD_REQUEST,
                'method': 'POST'
            },
            {
                'url': 'team-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Team',
                'status': status.HTTP_200_OK,
                'method': 'PUT'
            },
            {
                'url': 'team-list',
                'data': {},
                'model': 'Team',
                'status': status.HTTP_200_OK,
                'method': 'GET'
            },
            {
                'url': 'team-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Team',
                'status': status.HTTP_204_NO_CONTENT,
                'method': 'DELETE'
            },

            # SEASON
            {
                'url': 'season-list',
                'data': {'name': 'test'},
                'model': 'Season',
                'status': status.HTTP_201_CREATED,
                'method': 'POST'
            },
            {
                'url': 'season-list',
                'data': {'wrong': 'test'},
                'model': 'Season',
                'status': status.HTTP_400_BAD_REQUEST,
                'method': 'POST'
            },
            {
                'url': 'season-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Season',
                'status': status.HTTP_200_OK,
                'method': 'PUT'
            },
            {
                'url': 'season-list',
                'data': {},
                'model': 'Season',
                'status': status.HTTP_200_OK,
                'method': 'GET'
            },
            {
                'url': 'season-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Season',
                'status': status.HTTP_204_NO_CONTENT,
                'method': 'DELETE'
            },

            # CITY
            {
                'url': 'city-list',
                'data': {'name': 'test'},
                'model': 'City',
                'status': status.HTTP_201_CREATED,
                'method': 'POST'
            },
            {
                'url': 'city-list',
                'data': {'wrong': 'test'},
                'model': 'City',
                'status': status.HTTP_400_BAD_REQUEST,
                'method': 'POST'
            },
            {
                'url': 'city-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'City',
                'status': status.HTTP_200_OK,
                'method': 'PUT'
            },
            {
                'url': 'city-list',
                'data': {},
                'model': 'City',
                'status': status.HTTP_200_OK,
                'method': 'GET'
            },
            {
                'url': 'city-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'City',
                'status': status.HTTP_204_NO_CONTENT,
                'method': 'DELETE'
            },

            # SPORT
            {
                'url': 'sport-list',
                'data': {'name': 'test'},
                'model': 'Sport',
                'status': status.HTTP_201_CREATED,
                'method': 'POST'
            },
            {
                'url': 'sport-list',
                'data': {'wrong': 'test'},
                'model': 'Sport',
                'status': status.HTTP_400_BAD_REQUEST,
                'method': 'POST'
            },
            {
                'url': 'sport-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Sport',
                'status': status.HTTP_200_OK,
                'method': 'PUT'
            },
            {
                'url': 'sport-list',
                'data': {},
                'model': 'Sport',
                'status': status.HTTP_200_OK,
                'method': 'GET'
            },
            {
                'url': 'sport-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Sport',
                'status': status.HTTP_204_NO_CONTENT,
                'method': 'DELETE'
            },

            # EVENT
            {
                'url': 'event-list',
                'data': {'name': 'test'},
                'model': 'Event',
                'status': status.HTTP_201_CREATED,
                'method': 'POST'
            },
            {
                'url': 'event-list',
                'data': {'wrong': 'test'},
                'model': 'Event',
                'status': status.HTTP_400_BAD_REQUEST,
                'method': 'POST'
            },
            {
                'url': 'event-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Event',
                'status': status.HTTP_200_OK,
                'method': 'PUT'
            },
            {
                'url': 'event-list',
                'data': {},
                'model': 'Event',
                'status': status.HTTP_200_OK,
                'method': 'GET'
            },
            {
                'url': 'event-detail',
                'data': {'id': 1, 'name': 'test'},
                'model': 'Event',
                'status': status.HTTP_204_NO_CONTENT,
                'method': 'DELETE'
            },

            # ATTRIBUTES
            {
                'url': 'attributes-list',
                'data': {
                    "age": 50,
                    "height": 15.5,
                    "weight": 5.5,
                    "year": 2222
                },
                'model': 'Attributes',
                'status': status.HTTP_201_CREATED,
                'method': 'POST'
            },
            {
                'url': 'attributes-list',
                'data': {'wrong': 'test'},
                'model': 'Attributes',
                'status': status.HTTP_400_BAD_REQUEST,
                'method': 'POST'
            },
            {
                'url': 'attributes-detail',
                'data': {'id': 1,
                         'name': 'test',
                         "age": 15,
                         "height": 15.5,
                         "weight": 5.5,
                         "year": 5555
                         },
                'model': 'Attributes',
                'status': status.HTTP_200_OK,
                'method': 'PUT'
            },
            {
                'url': 'attributes-list',
                'data': {},
                'model': 'Attributes',
                'status': status.HTTP_200_OK,
                'method': 'GET'
            },
            {
                'url': 'attributes-detail',
                'data': {'id': 1},
                'model': 'Attributes',
                'status': status.HTTP_204_NO_CONTENT,
                'method': 'DELETE'
            },

            # ATHLETES
            {
                'url': 'athlete-list',
                'data': {
                    "id": 1,
                    "name": "Lucas",
                    "sex": "M",
                    "attributes": {
                        "age": 50,
                        "height": 15.5,
                        "weight": 5.5,
                        "year": 2222
                    },
                    "games": {
                        "name": "Teste"
                    },
                    "team": {
                        "name": "Teste"
                    },
                    "season": {
                        "name": "Teste"
                    },
                    "city": {
                        "name": "Teste"
                    },
                    "sport": {
                        "name": "Teste"
                    },
                    "event": {
                        "name": "Teste"
                    },
                    "medal": {
                        "name": "Teste"
                    }
                },
                'model': 'Athlete',
                'status': status.HTTP_201_CREATED,
                'method': 'POST'
            },
            {
                'url': 'athlete-list',
                'data': {'wrong': 'test'},
                'model': 'Athlete',
                'status': status.HTTP_400_BAD_REQUEST,
                'method': 'POST'
            },
            {
                'url': 'athlete-detail',
                'data': {
                    "id": 1,
                    "name": "Edgar Lindenau Aabye",
                    "sex": "M",
                    "attributes": {
                        "id": 1,
                        "age": 34,
                        "height": "0.00",
                        "weight": "0.00",
                        "year": 1900
                    },
                    "games": {
                        "id": 1,
                        "name": "1900 Summer"
                    },
                    "team": {
                        "id": 1,
                        "name": "Denmark/Sweden"
                    },
                    "season": {
                        "id": 1,
                        "name": "Summer"
                    },
                    "city": {
                        "id": 1,
                        "name": "Paris"
                    },
                    "sport": {
                        "id": 1,
                        "name": "Tug-Of-War"
                    },
                    "event": {
                        "id": 1,
                        "name": "Tug-Of-War Men's Tug-Of-War"
                    },
                    "medal": {
                        "id": 1,
                        "name": "Gold"
                    }
                },
                'model': 'Athlete',
                'status': status.HTTP_200_OK,
                'method': 'PUT'
            },
            {
                'url': 'athlete-list',
                'data': {},
                'model': 'Athlete',
                'status': status.HTTP_200_OK,
                'method': 'GET'
            },
            {
                'url': 'athlete-detail',
                'data': {'id': 1},
                'model': 'Athlete',
                'status': status.HTTP_204_NO_CONTENT,
                'method': 'DELETE'
            },

        ]
        for case in cases:
            data = case['data']
            if case['method'] == 'POST':
                url = reverse(case['url'])
                response = self.client.post(url, data, format='json')
            elif case['method'] == 'PUT':
                url = reverse(case['url'], args=[case['data']['id']])
                response = self.client.put(url, data, format='json')
            elif case['method'] == 'GET':
                url = reverse(case['url'])
                response = self.client.get(url, format='json')
            elif case['method'] == 'DELETE':
                url = reverse(case['url'], args=[case['data']['id']])
                response = self.client.delete(url, data, format='json')
            else:
                self.fail("No specified Http Method!")

            self.assertEqual(response.status_code, case['status'], msg="Fail in case: {}".format(case))
            if bool(data) and response.status_code in [200, 201]:
                string_eval = "{}.objects.get().{}".format(case['model'], list(data.keys())[0])
                self.assertEqual(eval(string_eval), list(data.values())[0])

    def test_athlete_filter(self):
        url = reverse('athletes_search')
        response = self.client.get(url, format='json', params={"medal":"Silver","season":"Summer"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)