import math

while True:
    print('Enter a positive whole number to find the square root')
    n = input()
    try:
        n = int(n)
    except:
        print('Please use a whole number')
        continue
    if n < 1:
        print('Please use a positive number')
        continue
    break

y = math.sqrt(int(n))
z = float (y).is_integer()
    
print (y)
if z > 0: 
    print (' Wow! ' + str(n) + ' is a perfect square!')
elif z <= 0:
        print('Oh no, ' + str(n) + ' is not a perfect square.')
        
