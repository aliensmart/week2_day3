#!/usr/bin/env python3

#Class
#   Worker
#   Item
#   Factory

class Worker:
    #attribute:
    #   name
    #   job
    #   years
    #   department is None
    def __init__(self, name, job, years):
        self.name = name
        self.job = job
        self.years = years
        self.department = None
    
    #Create methods set_department and increase_tenure
    def set_department(self,depart):

        """
            will take in a string, 
            and re-assign the worker's 
            department for the day

        """
        self.department = depart

    def increase_tenure(self):
        """

            will add one year to the number 
            of years this worker has been 
            at the factory.

        """
        self.years +=1
    



class Item:
    #Attributes:
        #name
        #explosive
        #weight
        #cost
    def __init__(self, name, explosive, weight, cost):
        self.name = name
        self.explosive = explosive
        self.weight = weight
        self.cost = cost

    #create method explod
    def explode(self):
        """
            If explosive == True, our method
            will print Boom!
        """
        if self.explosive == True:
            return "Boom"


battery = Item("battery", True, "4lbs", 200.99)



class Factory:
    #attribut:
    #   workers is the list of worker obj
    #   products is the list of items
    #   days_since_last_incident
    def __init__(self, workers = [], products =[]):
        self.workers = workers
        self.products = products
        self.days_since_last_incident = 0

    #method need:
    #   add_worker
    #   create_product
    #   ship
    #   add_day
    #   incident

    def add_worker(self, worker):
        """
            add a Worker object to our
            self.workers list

        """
        self.workers.append(worker)
    
    def create_product(self, item):
        """
            add an Item object to our 
            self.products list

        """
        self.products.append(item)

    def ship(self):
        """
            should remove everything from our current 

        """
        self.products = []
    
    def add_day(self):
        """
        should add 1 to our 
        self.days_without_incident attribute

        """
        self.days_since_last_incident +=1

    def incident(self):
        """
        re-assign self.days_without_incident to 0
        """
        self.days_since_last_incident = 0













    
