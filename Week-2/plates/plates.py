def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length
    if not (2 <= len(s) <= 6):
        return False

    # Check if all characters are alphanumeric
    if not s.isalnum():
        return False

    # Check if the first two characters are letters
    if not s[0:2].isalpha():
        return False

    # Check if numbers are at the end and the first number is not '0'
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0' and i == 2:
                return False
            if not s[i:].isdigit():
                return False
            break

    return True

if __name__ == "__main__":
    main()
