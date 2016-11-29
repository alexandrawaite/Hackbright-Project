def menu_choice():
	print "Welcome to my quote generator!"
	print "1 - Motivational"
	print "2 - Inspirational"
	print "3 - Spiritual"
	choice = int(raw_input("Please enter 1, 2 or 3 for the type of quote you'd like to see:"))
# Include options to return to menu and to press enter to generate new random quote

def main():
	choice = menu_choice()
# Write function to display random quote from the category user inputs
# Currently have three txt files that contain quotes from each category but unsure
# of how to use import random function to print a random string from those files
	

if __name__ == '__main__':
	main()

