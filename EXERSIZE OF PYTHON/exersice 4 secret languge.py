# # SECRET LANGUGE

print('welcome to sectet laungauge')
code = input('if you have to code world enter a: \nif you have to decode code input b:')
if (code == "a") :
    a = input("enter the world you have to code it")
    a =a.upper()
    print(a[1:len(a)]+a+a[::-1])

# if you have decode it
elif (code == "b"):
    b = input("enter the world in code format if we have to decode it ")
    b=b.lower()
    if len(b)==5: #2
        print(b[1:3])
    elif len(b)==8: #3
        print(b[2:5])
    elif len(b)==11: #4
        print(b[3:8])
    elif len(b) == 14: #5
        print(b[4:9])
    elif len(b) == 17: #6
        print(b[5:11])
    elif len(b) == 20: #7
        print(b[6:13])
    elif len(b) == 23: #8
        print(b[7:15])
    elif len(b) == 26: #9
        print(b[8:17])
    elif len(b) == 29: #10
        print(b[9:19])
    else:
        print('sorry we cant process your world')

