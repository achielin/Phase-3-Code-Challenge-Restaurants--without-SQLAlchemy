from Customer import Customer
from Restaurant import Restaurant

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