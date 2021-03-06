import random

motivational = ['\n"The most effective way to do it, is to do it." - Amelia Earhart', 
'\n"We can do no great things, only small things with great love." - Mother Teresa', 
'\n"The journey of a thousand miles begins with one step." - Lao Tzu', '\n"Every moment is a fresh beginning." - T.S. Eliot', '\n"The way to get started is to quit talking and begin doing." - Walt Disney',
'\n"The pessimist sees difficulty in every opportunity. The optimist sees the opportunity in every difficulty." - Winston Churchill',
'\n"We generate fears while we sit. We overcome them by action." - Dr. Henry Link', '\n"Do not wait until the conditions are perfect to begin. Beginning makes the conditions perfect." - Alan Cohen',
'\n"Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway." - Earl Nightingale', '\n"Success is nothing more than a few simple disciplines, practiced every day." - Jim Rohn',
'\n"Even if you\'re on the right track, you\'ll get run over if you just sit there." - Will Rogers', '\n"When you come to a roadblock, take a detour." - Mary Kay Ash', '\n"Don\'t wait. The time will never be just right." - Napoleon Hill',
'\n"Courage doesn\'t always roar. Sometimes courage is the little voice at the end of the day that says I\'ll try again tomorrow." - Mary Anne Radmacher', '\n"We have more possibilities available in each moment than we realize." - Thich Nhat Hanh',
'\n"Ideas won\'t keep; something must be done about them." - Alfred North Whitehead','\n"It\'s time to start living the life you\'ve imagined." - Henry James',
'\n"It does not matter how slowly you go as long as you do not stop." - Confucius', '\n"If you\'re going through hell, keep going." - Winston Churchill']

inspirational = ['\n"No matter what you look like or think you look like, you\'re special and loved and perfect just the way you are." - Ariel Winter',
'\n"Life shrinks or expands in proportion to one\'s courage." - Anais Nin', '\n"Don\'t be the girl who fell. Be the girl who got back up." - Jenette Stanley',
'\n"Success is going from failure to failure without losing your enthusiasm." - Winston Churchill', '\n"Keep your face to the sunshine and you can never see the shadow." - Helen Keller',
'\n"When we are no longer able to change the situation - we are challenged to change ourselves." - Viktor Frankl', '\n"Learn how to be happy with what you have while you pursue all that you want." - Jim Rohn',
'\n"Security is mostly a superstition. Life is either a daring adventure or nothing." - Helen Keller', '\n"You are never too old to set another goal or to dream a new dream" - C.S. Lewis', '\n"Believe you can and you\'re halfway there." - Theodore Roosevelt',
'\n"Everything you\'ve ever wanted is on the other side of fear." - George Addair', '\n"It is never too late to be what you might have been." - George Eliot', '"If there is no struggle, there is no progress." - Frederick Douglass',
'\n"What we fear doing most is usually what we most need to do." - Tim Ferriss', '\n"Accept responsibility for your life. Know that it is you who will get you where you want to go, no one else." - Les Brown',
'\n"Though no one can go back and make a brand new start, anyone can start from now and make a brand new ending." - Carl Bard', '\n"There are no great people in this world, only great challenges which ordinary people rise to meet." - William Frederick Halsey, Jr.',
'\n"Life\'s challenges are not supposed to paralyze you; they\'re supposed to help you discover who you are." - Bernice Johnson Reagon', '\n"Let perseverance be your engine and hope your fuel." - H. Jackson Brown, Jr.',
'\n"We face up to awful things because we can\'t go around them. The sooner you say, Yes it happened, the sooner you can get on with your life." - Annie Proulx']

spiritual = ['\n"Challenging the meaning of life is the truest expression of the state of being human." - Viktor Frankl', '\n"The snow goose need not bathe to make itself white. Neither need you do anything but be yourself." - Lao Tzu',
'\n"We are members of a vast cosmic orchestra in which each living instrument is essential to the complementary and harmonious playing of the whole." - J. Allen Boone',
'\n"What lies behind us and what lies before us are tiny matters compared to what lies within us." - Ralph Waldo Emerson', 
'\n"There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle. - Albert Einstein',
'\n"Step out of the circle of time and into the circle of love." - Rumi', '\n"It is difficult to find happiness in oneself but it is impossible to find it anywhere else." - Schopenhauer',
'\n"I believe in God, but not as one thing, not as an old man in the sky. I believe that what people call God is something in all of us." - John Lennon', '\n"Music is the mediator between the spiritual and the sensual life." -Ludwig van Beethoven',
'\n"The possession of knowledge does not kill the sense of wonder and mystery. There is always more mystery." - Anais Nin', '\n"The quieter you become, the more you can hear." - Ram Dass',
'\n"How hurtful it can be to deny one\'s true self and live a life of lies just to appease others." - June Ahern', '\n"I\'m not afraid of death because I don\'t believe in it. It\'s just getting out of one car and into another." - John Lennon',
'\n"We are not human beings having a spiritual experience. We are spiritual beings having a human experience." - Pierre Teilhard de Chardin','\n"Re-examine all you have been told. Dismiss what insults your soul." - Walt Whitman',
'\n"It is important to expect nothing, to take every experience, including the negative ones, as merely steps on the path, and to proceed." - Ram Dass',
'\n"Life is movement. The more life there is, the more flexibility there is. The more fluid you are, the more you are alive." - Arnaud Desjardins']

mindfulness = ['\n"Don\'t believe everything you think. Thoughts are just that - thoughts." - Allan Lokos',
'\n"Feelings come and go like clouds in a windy sky. Conscious breathing is my anchor." - Thich Nhat Hanh', '\n"If you want to conquer the anxiety of life, live in the moment, live in the breath." - Amit Ray',
'\n"Our worst enemy cannot harm us as much as our unwise thoughts. No one can help us as much as our own compassionate thoughts." - Buddha',
'\n"The most fundamental aggression to ourselves, the most fundamental harm we can do to ourselves, is to remain ignorant by not having the courage and the respect to look at ourselves honestly and gently." - Pema Chodran',
'\n"Between stimulus and response there is a space. In that space is our power to choose our response. In our response lies our growth and our freedom." - Viktor Frankl',
'\n"Surrender to what is. Let go of what was. Have faith in what will be." - Sonia Ricotti', '\n"Mindfulness isn\'t difficult. We just need to remember to do it." Sharon Salzberg',
'\n"If you want others to be happy, practice compassion. If you want to be happy, practice compassion." - Dalai Lama', '\n"Your vision will become clear only when you look into your heart. Who looks outside, dreams. Who looks inside, awakens." - Carl Jung',
'\n"Impermanence is a principle of harmony. When we don\'t struggle against it, we are in harmony with reality." - Pema Chodron', '\n"Each morning we are born again. What we do today is what matters most." - Buddha',
'\n"Western laziness consists of cramming our lives with compulsive activity, so that there is no time to confront real issues." - Sogyal Rinpoche']

def main_menu():
	print "Welcome to my feel-good quote generator!"
	print "1 - Motivational"
	print "2 - Inspirational"
	print "3 - Spiritual"
	print "4 - Mindfulness"
	print "Type 'x' to exit at anytime\n"
	choice = raw_input("Enter 1-4: ").lower()
	return choice


def main():
	choice = main_menu()
	
	while True:
		if choice == "1":
			print (random.choice(motivational))
			motiv_choice = raw_input("\nPress enter to see another quote or type 'm' to return to menu\n").lower()
			if motiv_choice == "":
				continue
			elif motiv_choice == "m":
				choice = main_menu()
			elif motiv_choice == "x":
				break
				
		elif choice == "2":
			print (random.choice(inspirational))
			inspir_choice = raw_input("\nPress enter to see another quote or type 'm' to return to menu\n").lower()
			if inspir_choice == "":
				continue
			elif inspir_choice == "m":
				choice = main_menu()
			elif inspir_choice == "x":
				break

		elif choice == "3":
			print (random.choice(spiritual))
			spirit_choice = raw_input("\nPress enter to see another quote or type 'm' to return to menu\n").lower()
			if spirit_choice == "":
				continue
			elif spirit_choice == "m":
				choice = main_menu()
			elif spirit_choice == "x":
				break

		elif choice == "4":
			print (random.choice(mindfulness))
			mindful_choice = raw_input("\nPress enter to see another quote or type 'm' to return to menu\n").lower()
			if mindful_choice == "":
				continue
			elif mindful_choice == "m":
				choice = main_menu()
			elif mindful_choice == "x":
				break

		elif choice == "x":
			break
		
		else:
			print "Oops, invalid entry. Try again!\n"
			choice = main_menu()


if __name__ == '__main__':
	main()
