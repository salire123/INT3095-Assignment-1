from Assignment1 import question1, question2

def qusetion1_run():
    qusetion1_runing = True
    while qusetion1_runing == True:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        if a == 0 or b == 0 or c == 0:
            print("Error, input not valid")
        else:
            print(a, b, c)
            ans = question1(a, b, c).run()

            print("The answer is: ", ans)
        redo = input("Did you want to redo? (y/n)")

        if redo == "y":
            continue
        else:
            qusetion1_runing = False

def qustion2_run():
    qusetion1_runing = True
    while qusetion1_runing == True:
        numberlist = input("Please input the number list: ")
        numberlist = numberlist.split(",")
        numberlist = [float(i) for i in numberlist]
        print (numberlist)
        print (question2(numberlist).my_sum())
        print (question2(numberlist).my_mean())
        print (question2(numberlist).my_median())
        print (question2(numberlist).my_stdev())
        print (question2(numberlist).my_max())
        redo = input("Did you want to redo? (y/n)")
        if redo == "y":
            continue
        else:
            qusetion1_runing = False

def main():
    print("Welcome to the assignment 1")
    print("question 1 is for quadratic equation, press 1 to run")
    print("question 2 is for statistics, press 2 to run")
    print("press q to quit")
    chouse = input("Which question do you want to run? (1/2/q)")

    if chouse == "1":
        qusetion1_run()
    elif chouse == "2":
        qustion2_run()
    elif chouse == "q":
        print("Thank you for using the assignment 1")
        exit()
    else:
        print("Error, input not valid")

if __name__ == "__main__":
    while True:
        main()
