 
import mathematics                                       # access to all modules inside the package
from mathematics import transcendentals                  # access to all modules inside the package 
from mathematics.algebraic import sum as addition       # access to all modules inside the package

print("2 * 6 = ", mathematics.algebraic.product(2,6))
print("2^4 = ", transcendentals.power_of_two(4))
print("PI approximation: ", transcendentals.PI)
print("9 + 11 = ", addition(9,11))
