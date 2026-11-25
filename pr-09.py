
# Problem 1: Zipper File()

def zipper_file(filename, strings):
    with open(filename, 'w') as file:
        for i in range(0, len(strings), 2):
            zipped = strings[i] + strings[i+1]
            file.write(zipped + '\n')

    print("File created successfully!")


# Example
strings = ["Hello", "World", "Good", "Morning"]
zipper_file("output.txt", strings)


# Problem 2: Reformat Date()

def reformat_date(dates):
    months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }

    result = []

    for date in dates:
        month, day, year = date.split('/')

        formatted = "Office Hours on " + months[month] + " " + day + ", " + year

        result.append(formatted)

    return result


# Example
dates = ["01/15/2025", "03/09/2024", "12/25/2023"]

print("\nReformatted Dates:")
print(reformat_date(dates))
