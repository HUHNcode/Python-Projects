print('Punkt A:')
x1 = int(input('X: '))
y1 = int(input('Y: '))
print('Punkt B:')
x2 = int(input('X: '))
y2 = int(input('Y: '))


m = (y2 - y1) / (x2 - x1)

y1f = m * x1

y1f2 = y1 - y1f         # was drauf adirt wird

print(f'f(x) = {m} * x + {y1f2}')

input()