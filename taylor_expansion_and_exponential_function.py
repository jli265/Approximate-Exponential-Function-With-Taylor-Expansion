#approximate exponential function with taylor expansion
import math

def app_expo(x,n,a=0):
    """x is the input x of original exponential function.
       n is the number of terms in taylor expansion.
       a is the parameter in taylor expansion with default value of 0.   """
    output=0
    for i in range(n):
        output += math.exp(a)*(x-a)**i/math.factorial(i)
    return output

try:
    x = float(input("Please enter a number as the input x of original exponential function: "))
    n = int(input("Please enter a positive integer as the number of terms in taylor expansion: "))
    a = float(input("Please enter the parameter in taylor expansion with default value of 0: "))
    output=app_expo(x,n,a)
except:
    try:
        output=app_expo(x,n)

    except:
      print("Error! x is the input x of original exponential function. n is the number of terms in taylor expansion. a is the parameter in taylor expansion with default value of 0. Try again!")
      quit()

print("The approximate value of the original exponential function is %.4f."%(output))
