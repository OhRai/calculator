'''
Student: Raiyan
Teacher: Mr. Ghorvei
Date: May 4rd, 2020
Program: Input-Output Calculator
'''

# defines what name is
def name():
  name = input('Please enter your name: ')
  return name 

# defines each function
def sum(x,y):
  return float(x) + float(y)
def diff(x,y):
  return float(x) - float(y)
def product(x,y):
  return float(x) * float(y)
def quotient(x,y):
  return float(x) / float(y)
def modulo(x,y):
  return float(x) % float(y)
def floordiv(x,y):
  return float(x) // float(y)
def exponent(x,y):
  return float(x) ** float(y)
def factorial(x):
  factorial = 1
  for i in range(1,int(x)+1): 
    factorial = factorial * i
  return factorial

# user input
firstName = name()

# a loop so that the calculator can be used until the user stops it
while True:
  
    # use chooses which function they want to perform
    chooseFunc = input('What would you like to do with these numbers?: \nAdd: + \nSubtract: -  \nMultiply: * \nDivide: / \nModulo: % \nFloor Division: // \nExponent: ** \nFactorial: ! \n{0}, enter your choice: ' .format(firstName))

    # if the user decides to choose these function, input two numbers
    if chooseFunc == '+' or chooseFunc == '-' or chooseFunc == '*' or chooseFunc == '/' or chooseFunc == '%' or chooseFunc == '**' or chooseFunc == '//':

     #user inputs first number
     x = input(firstName + ', enter your first number: ')

     # user inputs second number
     y = input(firstName + ', enter your second number: ')

    #addition
    if chooseFunc == '+':
      print('The sum of {0} and {1} is '.format(x, y, sum(x,y)))

    #subtraction
    elif chooseFunc == '-':
      print('The difference of {0} and {1} is {2}'.format(x, y, diff(x,y)))

    #multiplication
    elif chooseFunc == '*':
      print('The product of {0} and {1} is {2}'.format(x, y, product(x,y)))

    #division
    elif chooseFunc == '/':
      print('The quotient of {0} and {1} is {2}'.format(x, y, quotient(x,y)))

    #modulo
    elif chooseFunc == '%':
      print('The modulo of {0} and {1} is {2}'.format(x, y, modulo(x,y)))

    #exponentiation
    elif chooseFunc == '**':
      print('{0} to the power of {1} is {2}'.format(x, y, exponent(x,y)))
      
    #floor division
    elif chooseFunc == '//':
      print('The floor division of {0} and {1} is {2}'.format(x, y, floordiv(x,y)))
    
    #factorial
    elif chooseFunc == '!':
      x = float(input(firstName + ', please enter a positive integer: '))

      y = int(x)

    # if the use chose a negative number or a decimal number, it gives them an error
      while True:
        if x - y != 0: 
          print('Uh oh... What you entered is either a negative integer or a non-integral. ')
          x = float(input(firstName + ', please enter a positive integer: '))

        #if the user chose a positive integer, it prints the the answer
        elif x >= 0: 
          print('The factorial of {0} is {1}' .format(x, factorial(x)))
          break

    # if the user wants to continue to use the calc
    endStatus = input("Do you want to exit? y/n: ")
    if endStatus == "y" or endStatus == "yes":
      print("See you next time! :)")
      break
  
