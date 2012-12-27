from random import randint

from django.db.utils import IntegrityError
from django.test import TestCase

from tx_locations import models


def generate_random_state(**overrides):
    abbreviations = ['TX', 'LA', 'OK']
    r = randint(0, len(abbreviations) - 1)
    kwargs = {
        'name': 'Name %s' % randint(1000, 2000),
        'abbreviation': abbreviations[r],
    }
    kwargs.update(overrides)
    return kwargs, models.State(**kwargs)


class StateTestCase(TestCase):
    def test_has_name(self):
        kwargs, s = generate_random_state()
        self.assertEqual(kwargs['name'], s.name)

    def test_has_abbreviate(self):
        kwargs, s = generate_random_state()
        self.assertEqual(kwargs['abbreviation'], s.abbreviation)

    def test_unicode_returns_name(self):
        kwargs, s = generate_random_state()
        self.assertEqual(kwargs['name'], str(s))


class CityTestCase(TestCase):
    def test_requires_a_state(self):
        c = models.City()
        with self.assertRaises(IntegrityError) as e:
            c.save()
        expected = 'tx_locations_city.state_id may not be NULL'
        self.assertEqual(expected, e.exception.message)

    def test_has_a_name(self):
        random_name = 'Random City %s' % randint(1000, 2000)
        c = models.City(name=random_name)
        self.assertEqual(random_name, c.name)

    def test_unicode_returns_name_and_state(self):
        random_name = 'Random City %s' % randint(1000, 2000)
        _, s = generate_random_state()
        c = models.City(name=random_name, state=s)
        self.assertEqual('%s, %s' % (random_name, s.name), str(c))
