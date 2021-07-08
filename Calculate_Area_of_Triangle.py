# This is a sample Python script to find the Area of a triangle.
print("A Program to Calculate the Area of a Triangle")
print("*********************************************")
while True:
    a = float(input("Enter the  First Side\n"))
    b = float(input("Enter the Second Side\n"))
    c = float(input("Enter the Third Side\n"))
    s =(a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print('The Area of the Triangle is = %0.2f'% area)
