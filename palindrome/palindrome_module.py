def palindrome(str):
    if "".join((str.lower()).split(" ")) == "".join(((str[::-1]).lower()).split(" ")):
        return True
    return False


def main():
    string = input("Enter a string: ")
    return palindrome(string)


if __name__ == '__main__':
    main()
