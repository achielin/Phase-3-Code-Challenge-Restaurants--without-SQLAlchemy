from Restaurant import Restaurant
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

