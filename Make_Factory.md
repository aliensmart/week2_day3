## Create a Factory in Python

We're going to make a few classes to model the ACME factory and its workers. You don't need to pay too much attention to the real-world functionality if you don't want to, just focus on writing the methods and attributes as necessary.

Remember, you'll probably be using an instance attribute for anything that's changing from instance to instance, and a class attribute for anything that stays the same between instances (e.g. each worker has a different name, so that'd probably be an instance attribute of the Worker class).

#### Make the following three classes:

* Worker:
    * These are your factory's workers! The build things. Each worker has a `name` (a string), a `job` (a string), a number of `years` worked (an integer), and a `department`, which is initially `None`.
    * We need two methods:
        * `set_department` which will take in a string, and re-assign the worker's department for the day
        * `increase_tenure` which will add one year to the number of years this worker has been at the factory.

* Item:
    * These are the things we're creating at our factory (pianos, sticks of dynamite, anvils, etc.). Each item has a `name` (a string), a property called `explosive` (a bool, whether or not the item will explode), a `weight` (an integer), and a `cost` (a float).
    * We only need one method here, called `explode`. If our property `explosive` == `True`, our method will print `Boom!`. Otherwise, we'll do nothing.

* Factory:
    * This is going to represent our actual factory. We need a few attributes here- `workers`, a list of `Worker` objects (the people currently employed at our factory), `products`, a list of `Item` objects that we've created (this will initially be an empty list, `[]`), and one more, `days_since_last_incident` (an integer, initialized to 0)
    * We need a bunch of methods to get our factory working!
        * `add_worker` should add a `Worker` object to our `self.workers` list
        * `create_product` should add an `Item` object to our `self.products` list
        * `ship` should remove everything from our current `self.products` list (set it back to `[]`)
        * `add_day` should add 1 to our `self.days_without_incident` attribute
        * `incident` should, unforunately, re-assign `self.days_without_incident` to 0
