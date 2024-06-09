import unittest
from name_city import name_city 

class TestNameCity(unittest.TestCase):
  def setUp(self):
    self.name_city = name_city()
  def test_one(self):
    self.assertEqual(self.name_city.add('John','New York'), 'Your name is John. Your city is New York')

  def test_two(self):
    self.assertEqual(self.name_city.add('Alex','Minsk'), 'Your name is Alex. Your city is Minsk')

if __name__ == "__main__":
  unittest.main()
