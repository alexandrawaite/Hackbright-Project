import random

motivational = ['"The most effective way to do it, is to do it" - Amelia Earhart', 
'"We can do no great things, only small things with great love" - Mother Teresa', 
'"The journey of a thousand miles begins with one step" - Lao Tzu', '"Every moment is a fresh beginning" - T.S. Eliot', '"The way to get started is to quit talking and begin doing." - Walt Disney',
'"The pessimist sees difficulty in every opportunity. The optimist sees the opportunity in every difficulty." - Winston Churchill',
'"We generate fears while we sit. We overcome them by action." - Dr. Henry Link', '"Do not wait until the conditions are perfect to begin. Beginning makes the conditions perfect." - Alan Cohen',
'"Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway." - Earl Nightingale', '"Success is nothing more than a few simple disciplines, practiced every day." - Jim Rohn',
'"Even if you\'re on the right track, you\'ll get run over if you just sit there." - Will Rogers', '"When you come to a roadblock, take a detour." - Mary Kay Ash', '"Don\'t wait. The time will never be just right." - Napoleon Hill',
'"Courage doesn\'t always roar. Sometimes courage is the little voice at the end of the day that says I\'ll try again tomorrow." - Mary Anne Radmacher']

inspirational = ['"No matter what you look like or think you look like you\'re special and loved and perfect just the way you are" - Ariel Winter',
'"Life shrinks or expands in proportion to one\'s courage" - Anais Nin', '"Don\'t be the girl who fell. Be the girl who got back up" - Jenette Stanley',
'"Success is going from failure to failure without losing your enthusiasm" - Winston Churchill', '"Keep your face to the sunshine and you can never see the shadow" - Helen Keller',
'"When we are no longer able to change the situation - we are challenged to change ourselves." - Viktor Frankl', '"Learn how to be happy with what you have while you pursue all that you want." - Jim Rohn',
'"Security is mostly a superstition. Life is either a daring adventure or nothing." - Helen Keller', '"You are never too old to set another goal or to dream a new dream" - C.S. Lewis', '"Believe you can and you\'re halfway there." - Theodore Roosevelt',
'"Everything you\'ve ever wanted is on the other side of fear." - George Addair', '"It is never too late to be what you might have been." - George Eliot', '"If there is no struggle, there is no progress." - Frederick Douglass',
'"What we fear doing most is usually what we most need to do." - Tim Ferriss', '"Accept responsibility for your life. Know that it is you who will get you where you want to go, no one else." - Les Brown',
'"Though no one can go back and make a brand new start, anyone can start from now and make a brand new ending." - Carl Bard', '"There are no great people in this world, only great challenges which ordinary people rise to meet." - William Frederick Halsey, Jr.',
'"Life\'s challenges are not supposed to paralyze you; they\'re supposed to help you discover who you are." - Bernice Johnson Reagon', '"Let perseverance be your engine and hope your fuel." - H. Jackson Brown, Jr.',
'"We face up to awful things because we can\'t go around them. The sooner you say Yes it happened, the sooner you can get on with your life." - Annie Proulx']

spiritual = ['"Challenging the meaning of life is the truest expression of the state of being human." - Viktor Frankl', '"The snow goose need not bathe to make itself white. Neither need you do anything but be yourself." - Lao Tzu',
'"We are members of a vast cosmic orchestra in which each living instrument is essential to the complementary and harmonious playing of the whole." - J. Allen Boone',
'"What lies behind us and what lies before us are tiny matters compared to what lies within us." - Ralph Waldo Emerson', 
'"There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle. - Albert Einstein',
'"Step out of the circle of time and into the circle of love." - Rumi', '"It is difficult to find happiness in oneself but it is impossible to find it anywhere else." - Schopenhauer',
'"I believe in God, but not as one thing, not as an old man in the sky. I believe that what people call God is something in all of us." - John Lennon',
'"The possession of knowledge does not kill the sense of wonder and mystery. There is always more mystery." - Anais Nin',
'"How hurtful it can be to deny one\'s true self and live a life of lies just to appease others." - June Ahern', '"I\'m not afraid of death because I don\'t believe in it. It\'s just getting out of one car and into another." - John Lennon',
'"We are not human beings having a spiritual experience. We are spiritual beings having a human experience." - Pierre Teilhard de Chardin','"Re-examine all you have been told. Dismiss what insults your soul." - Walt Whitman']

def main_menu():
	print "Welcome to my feel-good quote generator!"
	print "1 - Motivational"
	print "2 - Inspirational"
	print "3 - Spiritual"
	print "Keep pressing enter to generate quotes\nPress any key to return to this menu\nPress 'x' to exit"
	choice = raw_input("Enter 1-3: ")
	return choice


def main():
	choice = main_menu()
	
	while True:
		if choice == "1":
			print (random.choice(motivational))
			motivational_choice = raw_input("")
			if motivational_choice == "":
				choice == "1"
			elif motivational_choice == "x":
				break
			else:
				main_menu()
				
		elif choice == "2":
			print (random.choice(inspirational))
			inspirational_choice = raw_input("")
			if inspirational_choice == "":
				choice == 2
			elif inspirational_choice == "x":
				break
			else:
				main_menu()
				
		elif choice == "3":
			print (random.choice(spiritual))
			spiritual_choice = raw_input("")
			if spiritual_choice == "":
				choice == "3"
			elif spiritual_choice == "x":
				break
			else:
				main_menu()

		elif choice == "x":
			break
			
		else:
			main_menu()
			

if __name__ == '__main__':
	main()
