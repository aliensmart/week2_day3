#!/usr/bin/env python3
from unittest import TestCase
from factory_app import Worker, Item, Factory

class TestFactory(TestCase):

    def testWorker(self):
        abdoul = Worker("Abdoul", "CTO", 1)
        self.assertEqual(abdoul.name, "Abdoul")
        self.assertEqual(abdoul.job, "CTO")
        self.assertEqual(abdoul.years, 1)
        self.assertEqual(abdoul.department, None)
        abdoul.set_department("today")
        self.assertEqual(abdoul.department, "today")
        abdoul.increase_tenure()
        self.assertEqual(abdoul.years, 2)
        self.assertIsInstance(abdoul, Worker)

    def testItem(self):
        piano = Item("piano", False, "2lbs", 1000.0)
        self.assertEqual(piano.name, "piano")
        self.assertEqual(piano.explosive, False)
        self.assertEqual(piano.weight, "2lbs")
        self.assertEqual(piano.cost, 1000.0)
        battery = Item("battery", True, "4lbs", 200.99)
        self.assertEqual(battery.explode(), "Boom")
        self.assertIsInstance(battery, Item)

    def testFactory(self):
        ACME = Factory()
        self.assertEqual(ACME.workers, [])
        self.assertEqual(ACME.products, [])
        self.assertEqual(ACME.days_since_last_incident, 0)
        abdoul = Worker("Abdoul", "CTO", 1)
        piano = Item("piano", False, "2lbs", 1000.0)
        ACME.add_worker(abdoul)
        ACME.create_product(piano)
        self.assertEqual(ACME.workers[0].name, "Abdoul")
        self.assertEqual(ACME.products[0].name, "piano")
        ACME.add_day()
        ACME.add_day()
        self.assertEqual(ACME.days_since_last_incident, 2)
        ACME.incident()
        self.assertEqual(ACME.days_since_last_incident, 0)
        self.assertIsInstance(ACME, Factory)
        


        
