# Nolan Piselli

def factorial(num): # defines function
     if num != 0: # test 
         total = 1 # base values
         counter = 1
         while counter <= num: 
             total *= counter # equation for factorial
             counter += 1 
         return total
     else:
         print("This function cannot handle zero as an input") 

print(factorial(0)) # test 
print(factorial(5)) 