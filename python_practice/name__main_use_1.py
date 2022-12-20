import name__main_use 
"""To use uncomment line 4 to check """

# print(name__main_use.animal("Elephant"))

#Output will be 
# PS D:\Repositories\Daily-practice-> & C:/Users/ASUS/AppData/Local/Programs/Python/Python310/python.exe d:/Repositories/Daily-practice-/name__main_use_1.py
# My name is Bajrang and I am Human
# None
# My name is Elephant and I am Animal.
# None

"""It Called all the function in name_main_use.py file while importing
But If we use "if __name == '__main__' " it will first call the main in
the main file then execute it"""

print(name__main_use.animal("Elephant"))

"""
So the above line will only call the specific function that we want to call
from main file"""
