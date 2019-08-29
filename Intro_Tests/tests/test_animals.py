from unittest import TestCase
from app import Tiger, Cow, Dog, Zoo


class TestAnimals(TestCase):

    def testTiger(self):
        test_tiger = Tiger("Tony")
        self.assertEqual(test_tiger.species, "tiger")
        self.assertEqual(test_tiger.name, "Tony")
        self.assertIsInstance(test_tiger, Tiger)

    def testCow(self):
        test_cow = Cow("Molly")
        self.assertEqual(test_cow.species, "cow")
        self.assertEqual(test_cow.name, "Molly")
        self.assertIsInstance(test_cow, Cow)

    def testDog(self):
        test_dog = Dog("Ollie")
        self.assertEqual(test_dog.species, "dog")
        self.assertEqual(test_dog.name, "Ollie")
        self.assertIsInstance(test_dog, Dog)

    def testZoo(self):
        zoo = Zoo()
        self.assertIsInstance(zoo, Zoo)
        self.assertEqual(zoo.animals, [])
        zoo.add(Cow("Bessie"))
        # self.assertNotEqual(zoo.animals, [])
        self.assertEqual(zoo.animals[0].name, "Bessie")
