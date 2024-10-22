from Assignment1 import question1, question2

def qustion1_run():
    while True:
        try:
            a = float(input("a = "))
            if a <= 0:
                print("Error, all inputs must be positive numbers")
                continue
            b = float(input("b = "))
            if b <= 0:
                print("Error, all inputs must be positive numbers")
                continue
            c = float(input("c = "))
            if c <= 0:
                print("Error, all inputs must be positive numbers")
                continue

            if a <= 0 or b <= 0 or c <= 0:
                print("Error, all inputs must be positive numbers")
                continue

            print(a, b, c)
            equation, ans = question1(a, b, c).run()
            print(f"your equation is:", equation)
            print("The answer is:", ans)

        except ValueError:
            print("Error, please enter a valid number")
            continue

        redo = input("Do you want to redo? (y/n): ").strip().lower()
        if redo != 'y':
            break


def qustion2_run():
    while True:
        try:
            print("Note: Please input the number list in the format like 1,2,3,4,5")
            numberlist = input("Please input the number list: ")
            numberlist = numberlist.split(",")
            numberlist = [float(i) for i in numberlist]
            print (numberlist)
            print (question2(numberlist).my_sum())
            print (question2(numberlist).my_mean())
            print (question2(numberlist).my_median())
            print (question2(numberlist).my_stdev())
            print (question2(numberlist).my_max())

        except ValueError:
            print("Error, please enter a valid number")
            continue

        redo = input("Did you want to redo? (y/n)")
        if redo == "y":
            continue
        else:
            break


def main():
    print("Welcome to the assignment 1")
    print("question 1 is for quadratic equation, press 1 to run")
    print("question 2 is for statistics, press 2 to run")
    print("press q to quit")
    chouse = input("Which question do you want to run? (1/2/q)")

    if chouse == "1":
        qustion1_run()
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
