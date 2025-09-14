# initiate a class
class Employee:
    # special method/magic method/dunder method - constructer
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/data initialized")

        def travel(self, destination):
            print("This travel function was called manually")
            print(f"Employee travelling to {destination}")


#create an object/instance of a class
sam = Employee()
sam.name = "Sam Kumar"
print(sam.name)
sam = Employee()
print(id(sam))
# print(sam.salary)
# sam.travel("Kerala")

print(type(sam))

