import math
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def funcName(parameter1, parameter2):
    print("dummy funct")
    return 10

def bmi_range(bmi):
    if (bmi < 18.5):
        print("under weight")
    elif (bmi > 25.0):
        print("over weight")
    else:
        print("normal weight")
    return

def calc_bmi(height, weight):
    print("Height = ", height)
    print("Weight = ", weight)
    bmi = weight / pow(height, 2)
    print("bmi =", bmi)
    bmi_range(bmi=bmi)

calc_bmi(weight=57, height=1.73)