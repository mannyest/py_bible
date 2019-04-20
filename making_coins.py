### bfd soondays day 15 2018.04.18 ###
### Section 10: Project 10 - Lecture 69 (https://www.udemy.com/the-python-bible) ###

import random

class Pesos:

    def __init__(self, rare = False, clean = True, heads = True, **kwargs):
    ## constructor that is taking in keyword arguments (kwargs) from daughter class
        for key,value in kwargs.items():
            setattr(self,key,value)
        ## setattr command sets attribute 'self' to key and values

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25     ##if coin is rare is should be worth 25% more
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color


    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.original_color

    def flip(self):
        options = [True, False]
        choice = random.choice(options)
        self.heads = choice

    def __del__(self):
        print ('Coin has been spent!')

    def __str__(self):                                                                  ## METHOD __str__
        if self.original_value >= 50:
            return ('${} note'.format(self.value))
        else:
            return ('${} coin'.format(self.value))
    ## printing the object itself (eg. Cincuenta()) would out put something akin to [<__main__. Cincuenta object at ox7f4d81326... This is where the method __str__ is used in parent function. The method is used to return/ouput when the object is called.

class Uno(Pesos):

    def __init__(self):
        data = {
            'original_value': 1,
            'clean_color': 'copper',
            'rusty_color': 'rusty copper',
            'presidente': 'Juan Pablo Duarte',
            'length': 100,
            'width': 20,
            'num_edges': 1,
            'diameter': 2.25,
            'thickness': 3.15,
            'mass': 9.5
            }
        super().__init__(**data)

class Cinco(Pesos):

    def __init__(self):
        data = {
            'original_value': 5,
            'clean_color': 'grey',
            'rusty_color': 'rusty grey',
            'presidente': 'Francisco del Rosario Sánchez',
            'length': 125,
            'width': 20,
            'num_edges': 1,
            'diameter': 2.25,
            'thickness': 3.15,
            'mass': 10.5
            }
        super().__init__(**data)

class Dies(Pesos):

    def __init__(self):
        data = {
            'original_value': 10,
            'clean_color': 'gold & grey',
            'rusty_color': 'rusty gold & grey',
            'presidente': 'Matias Ramon Mella',
            'length': 125,
            'width': 20,
            'num_edges': 1,
            'diameter': 2.25,
            'thickness': 3.15,
            'mass': 10.5
            }
        super().__init__(**data)

class Cincuenta(Pesos):

    def __init__(self):
        data = {
            'original_value': 50,
            'clean_color': 'purple',
            'rusty_color': None,
            'presidente': 'Santa Maria',
            'length': 125,
            'width': 20,
            'num_edges': 1,
            'diameter': 2.25,
            'thickness': 3.15,
            'mass': 2.0
            }
        super().__init__(**data)

    def rust(self):                                                 ## poly-morphism
        self.color = self.clean_color

    def clean(self):                                                ## poly-morphism
        self.color = self.clean_color

class Cien(Pesos):

    def __init__(self):
        data = {
            'original_value': 100,
            'clean_color': 'orange',
            'rusty_color': None,
            'presidente': 'Tres Padres',
            'length': 125,
            'width': 20,
            'num_edges': 1,
            'diameter': 2.25,
            'thickness': 3.15,
            'mass': 2.0
            }
        super().__init__(**data)

    def rust(self):                                                 ## poly-morphism
        self.color = self.clean_color

    def clean(self):                                                ## poly-morphism
        self.color = self.clean_color

class Dos_Cientos(Pesos):

    def __init__(self):
        data = {
            'original_value': 200,
            'clean_color': 'pink',
            'rusty_color': None,
            'presidente': 'Mirabal Sisters',
            'length': 125,
            'width': 20,
            'num_edges': 1,
            'diameter': 2.25,
            'thickness': 3.15,
            'mass': 2.0
            }
        super().__init__(**data)

    def rust(self):                                                 ## poly-morphism
        self.color = self.clean_color

    def clean(self):                                                ## poly-morphism
        self.color = self.clean_color
## poly-morphism is the explicit statement within a daughter-class that 'overrides' the method of the parent class

money = [Uno(), Cinco(), Dies(), Cincuenta(), Cien(), Dos_Cientos()]

for peso in money:
    args = [peso, peso.color, peso.value, peso.mass, peso.presidente]

    output = '{}: Value = {}, Color = {}, Mass = {} and the presidents on the face is/are {}'.format(*args)
    print (output)

