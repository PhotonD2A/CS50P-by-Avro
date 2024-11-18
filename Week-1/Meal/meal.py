def main():
    time = input("What time is it? ")
    timeCheck = convert(time)

    if 7.0 <= timeCheck <= 8.0:
        print("breakfast time")
    elif 12.0 <= timeCheck <= 13.0:
        print("lunch time")
    elif 18.0 <= timeCheck <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    return hours + minutes

if __name__ == "__main__":
    main()
