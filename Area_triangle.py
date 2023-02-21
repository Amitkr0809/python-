# Area of a triangle

s1 = float(input('Enter first side value: '))
s2 = float(input('Enter second side value:'))
s3 = float(input('Enter third-side value:'))


sp = (s1 + s2 + s3) / 2

area = (sp*(sp-s1)*(sp-2)*(sp-s3)) ** 0.5


print('The area of the triangle is: ', area)