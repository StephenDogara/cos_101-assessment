def c ():
    radius=(float(input('Enter the raduis')))
    Pie =(float(input('Enter the pie')))
    area_of_a_circle= 2*Pie*radius
    print(area_of_a_circle)

def a ():
    distance = (float(input("Enter Your Distance")))
    time = (float(input("Enter Your Time")))
    a = distance/time
    print(a)

def b ():
    displacement = (float(input("Enter Your Displacement")))
    time = (float(input("Enter Your Time")))
    b=displacement/time
    print(b)

def d():
    add1 = float(input("enter first number"))
    add2 = float(input("enter second number"))
    addition = add1 + add2
    print(addition)

def e():
    mass = float(input("Enter Your Mass"))
    acceleration = (float(input("Enter Your Acceleration")))
    c = mass * acceleration
    print(c)

def main():
    user=input("what do you want to calculate")
    if user == "a":
        a()
    elif user == "b":
        b()
    elif user == "c":
        c()
    elif user == "d":
        d()
    elif user == "e":
        e()
    else:
        print("invaloid input")
if __name__ == '__main__':
    main()




