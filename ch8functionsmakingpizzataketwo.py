import ch8functionspizzataketwo as pizza
pizza.makepizza("small","pepperoni") #return Making a small pizza with the following toppings:\n - pepperoni
pizza.makepizza("medium","mushrooms","green peppers","extra cheese") #return Making a medium pizza with the following toppings:\n - mushrooms\n - green peppers\n - extra cheese
pizza.makepizza("large","salami","sausage","pepperoni","bell peppers") #return Making a large pizza with the following toppings:\n- salami\n - sausage\n - pepperoni\n - bell peppers

#also import a specific function from a module
#template--> from module_name import function_0, function_1, function_2
from ch8functionspizzataketwo import makepizza
makepizza("small","pepperoni") #return Making a small pizza with the following toppings:\n - pepperoni
makepizza("medium","mushrooms","green peppers","extra cheese") #return Making a medium pizza with the following toppings:\n - mushrooms\n - green peppers\n - extra cheese
makepizza("large","salami","sausage","pepperoni","bell peppers") #return Making a large pizza with the following toppings:\n- salami\n - sausage\n - pepperoni\n - bell peppers

from ch8functionspizzataketwo import makepizza as mp
mp("small","pepperoni") #return Making a small pizza with the following toppings:\n - pepperoni
mp("medium","mushrooms","green peppers","extra cheese") #return Making a medium pizza with the following toppings:\n - mushrooms\n - green peppers\n - extra cheese
mp("large","salami","sausage","pepperoni","bell peppers") #return Making a large pizza with the following toppings:\n- salami\n - sausage\n - pepperoni\n - bell peppers

#import every function in a module type import *
from ch8functionspizzataketwo import *
makepizza("small","pepperoni") #return Making a small pizza with the following toppings:\n - pepperoni
makepizza("medium","mushrooms","green peppers","extra cheese") #return Making a medium pizza with the following toppings:\n - mushrooms\n - green peppers\n - extra cheese
makepizza("large","salami","sausage","pepperoni","bell peppers") #return Making a large pizza with the following toppings:\n- salami\n - sausage\n - pepperoni\n - bell peppers