import time

from kaggle.rest import ApiException
from django.test import TestCase, TransactionTestCase
from django.core.exceptions import ValidationError

from ..services import *


class TestDownloadCsvFileFromKaggle(TestCase):
    def test(self):
        self.assertIsNone(download_csv_file_from_kaggle(path='../api/csvfile/test'))
        time.sleep(3)
        self.assertTrue(os.path.isfile('api/csvfile/test/athlete_events.csv'))
        os.remove('api/csvfile/test/athlete_events.csv')

    def test_wrong_name_of_dataset(self):
        with self.assertRaises(ApiException):
            download_csv_file_from_kaggle(name_of_dataset="blablabla", path='../api/csvfile/test')
        time.sleep(3)
        self.assertFalse(os.path.isfile('api/csvfile/test/athlete_events.csv'))


class TestFormatData(TestCase):
    def test(self):
        results = format_data()
        self.assertIsInstance(results[2], dict)
        self.assertListEqual(['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games', 'Year',
                              'Season', 'City', 'Sport', 'Event', 'Medal'],
                             list(results[2].keys()))

    def test_wrong_file_name(self):
        with self.assertRaises(FileNotFoundError):
            format_data(file_name="asssaa")


class TestCreateObjects(TransactionTestCase):
    def test(self):
        dict_test = {'ID': '999999', 'Name': 'Mohamed Fathallah Abdel Rahman', 'Sex': 'M', 'Age': '21', 'Height': 0.0,
                     'Weight': 0.0, 'Team': 'Egypt', 'NOC': 'EGY', 'Games': '1936 Summer', 'Year': '1936',
                     'Season': 'Summer', 'City': 'Berlin', 'Sport': 'Fencing',
                     'Event': "Fencing Men's Sabre, Individual", 'Medal': 'empty'}
        self.assertIsNone(create_objects(dict_test))

    def test_wrong_dict(self):
        cases = [
            {"dict_test": {'bla': '999999', 'bla2': 'Mohamed Fathallah Abdel Rahman', 'Sex': 'M', 'Age': '21',
                           'Height': 0.0,
                           'Weight': 0.0, 'Team': 'Egypt', 'NOC': 'EGY', 'Games': '1936 Summer', 'Year': '1936',
                           'Season': 'Summer', 'City': 'Berlin', 'Sport': 'Fencing',
                           'Event': "Fencing Men's Sabre, Individual", 'Medal': 'empty'},
             "exception": KeyError},
            {"dict_test": {'ID': 'bla', 'Name': 'Mohamed Fathallah Abdel Rahman', 'Sex': 'M', 'Age': '21',
                           'Height': 0.0,
                           'Weight': 0.0, 'Team': 'Egypt', 'NOC': 'EGY', 'Games': '1936 Summer', 'Year': '1936',
                           'Season': 'Summer', 'City': 'Berlin', 'Sport': 'Fencing',
                           'Event': "Fencing Men's Sabre, Individual", 'Medal': 'empty'},
             "exception": ValueError},
            {"dict_test": {'ID': '999999', 'Name': 'Mohamed Fathallah Abdel Rahman', 'Sex': 'M', 'Age': '21',
                           'Height': "bla",
                           'Weight': 0.0, 'Team': 'Egypt', 'NOC': 'EGY', 'Games': '1936 Summer', 'Year': '1936',
                           'Season': 'Summer', 'City': 'Berlin', 'Sport': 'Fencing',
                           'Event': "Fencing Men's Sabre, Individual", 'Medal': 'empty'},
             "exception": ValidationError}
        ]
        for case in cases:
            with self.assertRaises(case["exception"], msg="Case: {}".format(case)):
                create_objects(case["dict_test"])


class TestFactoryToCheckExists(TransactionTestCase):
    def test(self):
        cases = [(Games, {'Games': '1936 Summer'})]
        for case in cases:
            factory_to_check_exists(case[0], case[1])

    def test_wrong_models(self):
        cases = [
            (Games, {'Bla': '1936 Summer'}, KeyError),
        ]
        for case in cases:
            with self.assertRaises(case[2]):
                factory_to_check_exists(case[0], case[1])

