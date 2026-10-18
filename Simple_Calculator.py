try:
    a = int(input("Enter The First Number : "))
    b = int (input("Enter The Second Number : "))

    print("Enter 1 For Addition ")
    print("Enter 2 For Subtraction ")
    print("Enter 3 For Multiplicationion ")
    print("Enter 4 For Division ")

    o = int(input("Enter Your Selected Option :" ))
    match o :
        case 1:
            print(f"The Result is : {a+b}")
        case 2:
            print(f"The Result is : {a-b}")
        case 3:
            print(f"The Result is : {a*b}")
        case 4:
            print(f"The Result is : {a/b}")
        case default:
            print("There Is Error!")
        
except Exception as e :
    print("Enter The Valid Values Of a and b ")