months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    formattedDate = validate_date()
    print(formattedDate)

def validate_date():
    while True:
        try:
            date = input("Date: ").strip()

            if ',' in date and '/' not in date:
                date = date.split(', ')
                year = date[1]
                monthDay = date[0].split(" ")
                day = monthDay[1].zfill(2)
                monthIndex = months.index(monthDay[0]) + 1

                if int(day) > 31:
                    continue
                formatted = f"{year}-{monthIndex:02}-{day:02}"
                return formatted

            elif '/' in date:
                date = date.split('/')

                if len(date) != 3:
                    continue

                month = date[0].zfill(2)
                day = date[1].zfill(2)
                year = date[2]

                if int(day) > 31 or int(month) > 12:
                    continue

                formatted = f"{year}-{month}-{day}"
                return formatted

        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()
