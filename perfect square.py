import math

n = input("Enter a number to find the square root:")
y = math.sqrt(int(n))
z = float (y).is_integer()
    
print (y)
if z > 0: 
    print (' Wow! ' + str(n) + ' is a perfect square!')
elif z <= 0:
        print('Oh no, ' + str(n) + ' is not a perfect square.')