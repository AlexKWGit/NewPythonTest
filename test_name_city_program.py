import unittest
from unittest.mock import patch
from name_city import name_user, city_user, result

class TestNameCity(unittest.TestCase):
    @patch('builtins.input', side_effect=['John', 'New York'])
    def test_name_city(self, mock_input):
        self.assertEqual(name_user, 'John')
        self.assertEqual(city_user, 'New York')
        self.assertEqual(result, "Your name is John. Your city is New York")