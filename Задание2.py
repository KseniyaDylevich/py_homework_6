x = int (input('введите координату x: \n')) 
y = int (input('введите координату y: \n'))

which_quadrant = lambda x, y: '1' if x > 0 and y > 0 else '2' if x < 0 and y > 0 else '3' if x < 0 and y < 0 else '4' if x > 0 and y < 0 else '0'
print(which_quadrant(x, y))