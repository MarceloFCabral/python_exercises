import random


class Cellphone:

    #  Defining a Class Object Attribute:
    type = 'mobile'

    #  Defining the classes' attributes:

    def __init__(self, model, brand, smartphone):
        self.model = model
        self.brand = brand
        self.smartphone = smartphone

    # Defining the classes' methods:

    def getBrandModel(self):
        return f'This is a {self.brand} {self.model} {self.type}.'

    def isSmartphone(self):
        if self.smartphone == 'yes':
            return 'This cellphone is a smartphone.'
        else:
            return 'This cellphone is not a smartphone.'

#  Testing the class and it's methods:


mi8 = Cellphone(model='Mi 8 Lite', brand='Xiaomi', smartphone='yes')

cellphone_info = mi8.getBrandModel()
print(cellphone_info)

smart = mi8.isSmartphone()
print(smart)

#  Creation of a random cellphone number generator:


def gencpnum():
    print('Generating cellphone number...')
    cellphone_number = '9'
    while len(cellphone_number) < 5:
        cellphone_number += str(random.randint(0, 10))
    cellphone_number += '-'
    while len(cellphone_number) < 10:
        cellphone_number += str(random.randint(0, 10))
    return cellphone_number

#  Creation of a function that generates a random cellphone brand, model and number:


def rand_phone_gen():
    brand_list = ['Xiaomi', 'Samsung', 'Apple']
    model_list = [('Mi 8 Lite', 'Mi 7 SE', 'Mi 9'), ('Galaxy S5', 'Galaxy S8', 'Galaxy S10'),
                  ('iPhone 5', 'iPhone 6', 'iPhone 8')]

    brand = random.choice(brand_list)

    if brand == 'Xiaomi':
        model = random.choice(model_list[0])
    elif brand == 'Samsung':
        model = random.choice(model_list[1])
    else:
        model = random.choice(model_list[2])

    random_cellphone = Cellphone(model=model, brand=brand, smartphone='yes')
    smart = random_cellphone.isSmartphone()
    cpnum = gencpnum()

    print(f'Your cellphone is a {random_cellphone.brand} {random_cellphone.model}. Your cellphone number is {cpnum}. '
          f'{smart}')


rand_phone_gen()
