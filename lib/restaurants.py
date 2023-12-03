class Restaurant:
    all_restaurants = []
    def __init__(self, restaurant_name):
        if type(restaurant_name) not in (str,):
            raise ValueError("Wrong Input")            
        self._name = restaurant_name
        Restaurant.add_all_instances(self)

    def name(self): 
        return(self._name)
    
    def restaurant_name_setter(self, new_rest_name): 
        raise AttributeError("Name cannot be changed after initialization")
        pass    

    def reviews(self):
        pass

    def customers(self):
        
        pass

    @classmethod
    def add_all_instances(cls, new_restaurant):
        cls.all_restaurants.append(new_restaurant)

    restaurant_name = property(name, restaurant_name_setter)


restaurant_0 = Restaurant("12345") 



class Customer:
    all_instances = []
    all_names = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullName = first_name + " " + last_name
        Customer.all(self)
        Customer.allNamesHandler(self)
        
    def given_name(self):
        return(self.first_name)
    
    def family_name(self):
        return(self.last_name)
    
    def full_name(self):
        return(f"{self.first_name} {self.last_name}")
        pass

    def restaurants(self):
        
        pass

    def add_review(restaurant, rating):
        pass

    @classmethod
    def all(cls, new_customer_instance):
        
        cls.all_instances.append(new_customer_instance)
        pass

    @classmethod
    def print_all_instances(cls):
        print([fullname.fullName for fullname in cls.all_instances])

    @classmethod
    def allNamesHandler(cls, new_customer):
        cls.all_names.append(new_customer.fullName)

    @classmethod
    def allNamesPrinter(cls):
        print([fullName for fullName in cls.all_names])



customer1 = Customer("Gweth", "Maduong") 
customer2 = Customer("Hawi", "Mangeny") 
customer3 = Customer("Mor", "Ahinya") 
customer4 = Customer("Ber", "Tee") 

class Review(Customer):
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.rest_customer = customer
        self.rest_restaurant = restaurant
        self._rating = rating
        Review.all(self)
        if type(rating) in (int,):
            self._rating = rating
        else:
            self._rating = None
            print("Rating should be an Integer")

    def rating(self):
        print(self._rating)
    
    def rating_setter(self, rating):
        if type(rating) in (int,):
            self._rating = rating
        else:
            print("Rating should be an Integer")

    rest_rating = property(rating, rating_setter)

    def customer(self):
        
        return(Customer.all_instances)
        pass

    def restaurant(self):
        return(Restaurant.all_restaurants)
        pass

    @classmethod
    def all(cls, new_review):
        cls.all_reviews.append(new_review)

    @classmethod
    def print_all_reviews(cls):
        print([review for review in cls.all_reviews])
        pass


my_restaurant_review_0 = Review("Hawi", "Cjs", 1) 
my_restaurant_review_1 = Review("Gweth", "NSK", 2) 
my_restaurant_review_2 = Review("Mor", "FoodHub", 3) 

