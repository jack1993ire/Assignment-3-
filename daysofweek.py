    # This program is designed to display the day of the week
    # The numbers one to seven stand for each day






    # First, a way of inputting the numbers to give the day
    day = int(input('Enter a number from one to seven to display the day:'))

    # Determine the name of the day of the week, and display it.
    if day == 1:
        print('Monday')
    elif day == 2:
        print('Tuesday')
    elif day == 3:
        print('Wednesday')
    elif day == 4:
        print('Thursday')
    elif day == 5:
        print('Friday')
    elif day == 6:
        print('Saturday')
    elif day == 7:
        print('Sunday')
    else:
        print('Error: Please enter a number in the range 1-7.')

