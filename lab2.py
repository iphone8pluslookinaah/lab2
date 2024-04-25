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

def display_main_menu(): 
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    return

def get_user_input():
    print("get_user_input")
    temp = input("input? ")
    temp_split = temp.split(",")
    for i in temp_split:
        temp_split[temp_split.index(i)] = float(i)
    return temp_split

def calc_average(list): 
    print("calc_average")
    new_float = 69.420
    return new_float

def find_min_max(list):
    print("find_min_max")
    min_temp = 69.420
    max_temp = 0.600
    return min_temp, max_temp

def sort_temperature(list):
    print("sort_temperature")
    return

def calc_median_temperature(list):
    print("calc_median_temperature")
    new_float = 0.600
    return new_float

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

if __name__ == "__main__":
    main()

def calc_average_temperature():
    print("To return a float value of the calculated average value of all temperature readings.")
    temp = input("input? ")
    temp_split = temp.split(",")
    for i in temp_split:
        temp_split[temp_split.index(i)] = float(i)
    calc = sum(temp_split) / len(temp_split)
    return calc

def calc_min_mac_temperature():
    print("To return an integer list with 2 values for minimum and maximum temperature.")
    temp = input("input? ")
    temp_split = temp.split(",")
    for i in temp_split:
        temp_split[temp_split.index(i)] = int(i)
    temp_split.sort()
    return temp_split