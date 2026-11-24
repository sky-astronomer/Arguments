print("welcome to my program")
def finder(number_changer):
    return number_changer*number_changer*number_changer
def diviser(number_store):
    if number_store%3==0:
        print(finder(number_store))
    else:
        return False
num=int(input("Enter the number to claculate the cube of a number"))
diviser(num)