while True :
    x = 1
    oper = input("What is the mathmatical operation being preformed. (Put opperators in in python notation)")
    n1 = float(input("What is the first number in the equation."))
    n2 = float(input("What is the second number in the equation."))
    if oper == "+" :
        answer = n1 + n2
    elif oper == "-" :
        answer = n1 - n2
    elif oper == "*" :
        answer = n1 * n2
    elif oper == "/" :
        answer = n1 / n2
    elif oper  == "**" :
        answer = n1 ** n2
    else :
        x = 2
        print("Invaled operation")
    while x == 1 :
        print(n1,oper,n2,"=",answer)
        x = 2
