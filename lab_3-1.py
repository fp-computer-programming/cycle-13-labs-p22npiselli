# Nolan Piselli

def r_max(nestedlst): # Defines function
     max = 0 # stores 
     for num in nestedlst: # specifies nums
         if type(num) == list:
             num = r_max(num)
             if num > max: # num > max set max = to num
                 max = num
         else:
             if num > max: 
                 max = num
     return max # returns

print(r_max([0,2,2,[23,60],24])) # test