import easygui as eg
from fractions import Fraction
import sys
import operator
import random as ran

#Dekai Rohlsen
#U50753261

#Function for home window
def homewindow():
    title = "Main Window"
    choices = ["Solver","Quizzer","Quit"]
    home_msg="Welcome to Practice Fractions! What would you like to do?"
    home = eg.buttonbox(home_msg, title, choices)
    return home

#function for solver window
def solver():
    title = "Solver Window"
    s_msg = "Enter an arbitrary fraction expression"
    solve = eg.enterbox(s_msg)
    print("solve is %s" % solve)
    if solve == None:
        return False

    ops = ["+","-","*"]

    op_count = 0
    op_chose = 0

    #remove spaces from entry
    for i in ops:
        if i in solve:
            new = solve.split(i)
            f1 = new[0].replace(" ","")
            lf = f1.split("/")
            lf[0] = int(lf[0])
            lf[1] = int(lf[1])
            f2 = new[1].replace(" ","")
            rf = f2.split("/")
            rf[0] = int(rf[0])
            rf[1] = int(rf[1])
            
            op_count += 1
            break
        op_chose += 1

    if op_count == 0:
        msg = "Invalid Fraction expression! Operator not found"
        s_choice = ["Try Another","Return to Main Window"]
        try_again = eg.ccbox(msg,choices = s_choice)
        return try_again

    try:
        frac1 = Fraction(lf[0],lf[1])
        frac2 = Fraction(rf[0],rf[1])

        print(frac1)
        print(frac2)
        print(ops[op_chose])
        if(ops[op_chose] == "+"):
            frac = operator.add(frac1,frac2)
        elif(ops[op_chose] == "-"):
            frac = operator.sub(frac1,frac2)
        else:
            frac = operator.mul(frac1,frac2)
        
    except ValueError:
        msg = "Invalid Fraction!"
        s_choice = ["Try Another","Return to Main Window"]
        try_again = eg.ccbox(msg,choices = s_choice)
        return try_again
    except ZeroDivisionError:
        msg = "Invalid Fraction.. Cannot have Zero in Denominator!"
        s_choice = ["Try Another","Return to Main Window"]
        try_again = eg.ccbox(msg,choices = s_choice)
        return try_again
        
    
    msg = "The result of your fractions is " + str(frac) 
    s_choice = ["Try Another","Return to Main Window"]
    try_again = eg.ccbox(msg,choices = s_choice)
    return try_again


#Function for Quizzer Window
def quizzer():
    temp = "Not selected yet"
    while 1:
        title = "Quizzer Window"
        choice = ["+","-","*","Create Expression"]
        msg = "Lets test your skills! Select an operator, then create your expression to solve"
        q_msg = eg.buttonbox(msg = msg,title = title,choices = choice)
        print(temp)
        
        if q_msg == "Create Expression":
            if temp == "Not selected yet":
                e_msg = "Oooops... You forgot to select an operator!"
                pick = ["Try again", "Return to Main Window"]
                err_msg = eg.ccbox(msg = e_msg,choices = pick)
                
                if err_msg == False:
                    return err_msg
            
            else:
                q = question(temp)
                if q == False:
                    return q
        temp = q_msg
        if temp == "Create Expression":
            temp = "Not selected yet"


#Function for Question Window
def question(op):

    #create random numbers for equation
    left = [ran.randint(-15,15),ran.randint(-15,15)]
    right = [ran.randint(-15,15),ran.randint(-15,15)]

    #make sure denominator != 0
    while 1:
        if left[1] != 0 and right[1] != 0:
            break
        else:
            left[1] = ran.randint(-15,15)
            right[1] = ran.randint(-15,15)
    
    frac1 = Fraction(left[0],left[1])
    frac2 = Fraction(right[0],right[1])

    if(op == "+"):
        frac = operator.add(frac1,frac2)
    elif(op == "-"):
        frac = operator.sub(frac1,frac2)
    else:
        frac = operator.mul(frac1,frac2)

    try:
        msg = str(frac1) + op + str(frac2) + "="
        result = eg.enterbox(msg)
        if result == None:
            return 1
        check = Fraction(result)
    except ValueError:
        msg = "Invalid Fraction!"
        s_choice = ["Try Another","Return to Main Window"]
        try_again = eg.ccbox(msg,choices = s_choice)
        return try_again
    except ZeroDivisionError:
        msg = "Invalid Fraction.. Cannot have Zero in Denominator!"
        s_choice = ["Try Another","Return to Main Window"]
        try_again = eg.ccbox(msg,choices = s_choice)
        return try_again

    result_str = result

    #convert result to value
    if "/" in result:
        string = result.split("/")
        l = int(string[0])
        r = int(string[1])
        result = l / r
        
        
    if float(frac) == float(result):
        
        if str(frac) == result_str:
            msg = "CONGRATULATIONS, you've answered correctly!"    
            s_choice = ["Try Another","Return to Main Window"]
            try_again = eg.ccbox(msg,choices = s_choice)
            return try_again
        else:
            msg = "While your answer is correct, you do not have it in the reduced form! \n" + "expected result: " + str(frac) + "\nyour result: " + result_str
            s_choice = ["Try Another","Return to Main Window"]
            try_again = eg.ccbox(msg,choices = s_choice)
            return try_again
    else:
            msg = "Sorry, that is the wrong answer \nexpected result: " + str(frac) + "\nyour result: " + result_str
            s_choice = ["Try Another","Return to Main Window"]
            try_again = eg.ccbox(msg,choices = s_choice)
            return try_again




if __name__ == "__main__":    

    while 1:
        home = homewindow()
        if home == "Solver":
            print("solver was selected")
            while 1:
                solve = solver()
                if solve == False:
                    break
        
        if home == "Quizzer":
            print("Quizzer was selected")
            while 1:
                quiz = quizzer()
                if quiz == False:
                    break
        if home == "Quit":
            break

    

