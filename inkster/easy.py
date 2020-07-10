#Imports
import random
# Variables
number2 = random.randint(1, 100)
# Normal
class Normal:

    def hello(self, name):
        print("Hello " + name + ".")

    def log(self, logged):
        return logged

Normal = Normal()
