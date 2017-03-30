import datetime


def years(age):
    now = datetime.datetime.now()
    current = now.year
    result = 99 - age + current
    return result


def main():
    name = input("Your name?: ")
    age = int(input("Your age: "))
    turn = int(input("Give a number: "))
    for i in range(turn): 
        print(name, "\b, you will be 100 in", years(age))
    return


if __name__ == '__main__':
    main()
