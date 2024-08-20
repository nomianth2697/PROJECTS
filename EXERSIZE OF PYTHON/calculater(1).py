print("--creating calculater--")

print('enter wich calculation do you have to do!. ( + , - , * , / )')

a = input("enter here!")

num1 = float(input("enter your first num"))
num2 = float(input("enter your second num"))
try:
    if a =='+':
        print(num1 + num2)

    elif a =="-":
        print(num1-num2)

    elif a =='*':
        print(num1 *num2)

    elif a ==' /':
        print(num1/num2)

    # else :
        # print('enter the valid input')

except Exception as e :
    print(e)




