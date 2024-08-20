def att():
    print("select your streme")
    print("enter 1 for science")
    print("enter 2 for comerce")
    print("enter 3 for arts")
    print("enter 4 for NCC")
    streme = int(input())
    match streme:
        case 1:
            print("enter your class ")
            print("for bcs enter 1 ")
            print("for bca enter 2 ")
            print("for bsc IT enter 3 ")
            print("for bsc DATA SCI. enter 4 ")
            class_stu = int(input())
            match class_stu:
                case 1:
                    input("enter your roll no ")



print("DEOGIRI COLLAGE CHH. SAMBHAJI NAGAR")
print("Welcome to attendence section")
print("to enter your today's attendence enter ('att')")
print("to check your this months attendece enter ('stu')")
inp1 = input("enter here !")
if(inp1 == "att"):
    att()
