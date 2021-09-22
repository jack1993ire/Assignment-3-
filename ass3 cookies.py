# This program lets you choose the ingredients going into your cookies

# The choices are: sugar, butter and flour


#1. Input
number_of_cookies = int(input('\nHow many cookies would you like to make: '))

# Now These are the classic staple ingredients
# Each one is measured in cups

COOKIES = 48 
SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75 


# If you would like your cookies to be less unhealthy
# You can have half the amount of butter and sugar
# You can adjust it to your liking

half_sugar = 1.5/2 
half_butter = 1/2

# All you have to do is change the output a little
# Simply put those in place of the total amount of butter and sugar! Like this:
# where it says "format", just replace the total number with half!
# Here's an example: format(total_sugar, ',.2f'))
# Now, with half the amount: format(half_sugar, ',.2f'))
# Just do the same for butter and that's it!




total_sugar  = (SUGAR * number_of_cookies) / COOKIES
total_butter = (BUTTER * number_of_cookies) / COOKIES
total_flour  = (FLOUR * number_of_cookies) / COOKIES

#3. Output
print('\nNumber of cookies =', number_of_cookies, end='\n\n')
print('Total sugar =', format(total_sugar, ',.2f'))
print('Total butter =', format(total_butter, ',.2f'))
print('Total flour =', format(total_flour, ',.2f'), end='\n\n')
