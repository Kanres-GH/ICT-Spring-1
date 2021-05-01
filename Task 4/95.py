from random import randint
def old_license():
    print(randint(100,999), chr(randint(65,90)), chr(randint(65,90)), chr(randint(65,90)), sep='')
def new_license():
    print(chr(randint(65,90)), chr(randint(65,90)), chr(randint(65,90)), randint(1000,9999), sep='')
old_license()
print()
new_license()