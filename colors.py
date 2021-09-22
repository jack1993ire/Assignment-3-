# This program is designed to allow you to mix primary colors
# And make more colors!
# These are the colors: red, blue and yellow
# Now, a way of telling Python which colors you would like to mix
# And a way of inputting the code

#first color
first_color = input("Please choose a primary color of your choice:")
# second color
second_color = input("Please choose a primary color of your choice:")

#Primary colors: red, blue and yellow
color_list = ["red", "blue", "yellow"]

#Check to make sure the colors are in the color_list
if(first_color in color_list and second_color in color_list):

#If you would like to mix red and blue, it will print purple
    if((first_color == "red" and second_color == "blue") or (first_color == "blue" and second_color == "red")):
        print("When you mix {} and {}, you get purple".format(first_color,second_color))

#If you chose red and yellow, you will see a lovely orange
elif((first_color == "red" and second_color == "yellow") or (first_color == "yellow" and second_color == "red")):
    print("When you mix {} and {}, you get orange".format(first_color,second_color))

#Or, if you would like blue and yellow, it will print green
elif((first_color == "blue" and second_color == "yellow") or (first_color == "yellow" and second_color == "blue")):
    print("When you mix {} and {}, you get green".format(first_color,second_color))

#If none of the colors you like are on the list
# It will give you an error message

else:
    print("You didn't input two primary colors.")

