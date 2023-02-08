import time
import sys
import math
import os


def check_password():
    count_enter = 0
    password_enter = input("Enter a password: ")
    password_correct = "chaubao"
    while password_enter != password_correct:
        print("Incorrect password !!!")
        if count_enter > 1:
            for i in range(5):
                print("Wait ", 5-i, " second ...")
                time.sleep(1)
        count_enter += 1
        password_enter = input("Enter a password: ")
    print()
    print()


def choose_option():
    ##########################
    # Mấy này anh tra gg dịch á
    #########################

    # Clearing the Screen
    os.system('cls')

    print("Hi... Wellcome my program.")

    print("   Option 1: Birthday dictionaries")
    print("   Option 2: Calculate quadratic equation 2")
    print("   Option 3: Calculate perimeter and area of triangle")
    print("   Option 4: Exit")

    while True:
        option = int(input("Please choose option: "))
        if option == 1:
            option1()
        if option == 2:
            option2()
        if option == 3:
            option3()
        if option == 4:
            option4()


def option1():
    list_name = [
        'Albert Einstein',
        'Benjamin Franklin',
        'Ada Lovelace',
        'Donald Trump',
        'Rowan Atkinson'
    ]
    list_birthday = [
        '03/14/1879',
        '01/17/1706',
        '12/10/1815',
        '06/14/1946',
        '01/6/1955'
    ]

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for i in range(len(list_name)):
        print("   ", list_name[i])
    print('Whose birthday do you want to look up?')
    name = input()
    if name in list_name:
        # index of name on list_name
        index_name = list_name.index(name)
        print(name, " birthday is ", list_birthday[index_name])
    else:
        print("Sorry I don't have ", name ," birthday.")


def option2():
    a = float(input("Enter number a: "))
    b = float(input("Enter number b: "))
    c = float(input("Enter number c: "))

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("The equation has no solution")
    elif delta == 0:
        print("The equation has solution x1 = x2 = ", -(b / (2 * a)))
    else:
        print("The equation has two solution:")
        print("x1 = ", (-b + math.sqrt(delta)) / (2 * a))
        print("x1 = ", (-b - math.sqrt(delta)) / (2 * a))


def option3():
    a = int(input("Enter edge a :"))
    b = int(input("Enter edge b :"))
    c = int(input("Enter edge c :"))
    cv = a + b + c
    p = (a + b + c) / 2
    s = (float)(math.sqrt(p * (p - a) * (p - b) * (p - c)))
    print("Perimeter of triangle :", cv)
    print("Area of triangle :", s)


def option4():
    print("Exit program (-_-)")
    time.sleep(5)
    sys.exit()


# program main
check_password()
choose_option()
