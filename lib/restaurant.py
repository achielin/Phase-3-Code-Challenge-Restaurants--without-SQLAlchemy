from Restaurants import Review
from Restaurants import Customer
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
        return(Review.all_reviews)
        pass

    def customers(self):
        
        unique_names = list(set(Customer.all_names))
        
        print(unique_names)
        pass

    @classmethod
    def add_all_instances(cls, new_restaurant):
        cls.all_restaurants.append(new_restaurant)

    restaurant_name = property(name, restaurant_name_setter)


restaurant_0 = Restaurant("Cjs") 
restaurant_1 = Restaurant("NSK") 
restaurant_2 = Restaurant("FoodHub") 
