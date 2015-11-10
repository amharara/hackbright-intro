name = raw_input("What is your name?")
color = raw_input("What is your favorite color?")
hobby = raw_input ("what is your favorite hobby?")
movie = raw_input ("what is your favorite movie?")

def print_survey_results(name, color, hobby, movie):
	print name + "'s favorite color is " + color 
	print name + "'s favorite hobby is " + hobby 
	print name + "'s favorite movie is " + movie 

print_survey_results(name, color, hobby, movie)

