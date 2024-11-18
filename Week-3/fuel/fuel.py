def main():
    gauge = get_input()
    percentage = round(gauge * 100)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def get_input():
    while True:
        try:
            text = input("Fraction: ")
            nums = text.split('/')
            firstNum = int(nums[0])
            secondNum = int(nums[1])

            if firstNum > secondNum or secondNum == 0:
                raise ValueError

            result = firstNum / secondNum

            return result

        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction.")

if __name__ == "__main__":
    main()
