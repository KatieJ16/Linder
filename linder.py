import random as r
import sqlite3
import datetime
import sys
import argparse
from gooey import Gooey, GooeyParser

@Gooey(advanced=False)
def main():
	parser = GooeyParser(prog= 'Are you ready to find your perfect match?')


	now = datetime.datetime.now()
	connection = sqlite3.connect("connection.db")
	cursor = connection.cursor()

	# get info from person
	'''name = str(raw_input("Enter your name: "))
	age = int(input("Enter your birthyear: "))
	gender = str(raw_input("Gender (m/f): "))
	animal = str(raw_input ("Dogs or Cats: "))
	height = int(input("Enter height (in inches): "))
	taller = str(raw_input("Do you prefer you matches to be taller or shorter than you? (t/s): "))
'''

	#make list of ages
	ages = []
	for i in range(100):
		ages.append(now.year - i)

	parser.add_argument("name", type=str, default='Enter Name')
	parser.add_argument("age", choices=ages, default=1997)
	parser.add_argument("gender", choices=["Female","Male"], default="Female")
	parser.add_argument("animal", choices=["Dogs","Cats"], default="Dogs")
	parser.add_argument("feet", choices=[1,2,3,4,5,6,7], default=5)
	parser.add_argument("inches", choices=[0,1,2,3,4,5,6,7,8,9,10,11], default=3)
	args = parser.parse_args()
	print args.name
	sql_command = """
	CREATE TABLE IF NOT EXISTS database (
	id INTEGER PRIMARY KEY,
	name STRING,
	age INT,
	gender STRING,
	animal STRING,
	height INT)"""

	#add person to database
	cursor.execute(sql_command)

	format_str = """INSERT INTO database (id, name, age, gender, animal, height) VALUES (NULL, "{thisname}", "{thisage}", "{thisgender}", "{thisanimal}", "{thisheight}");"""

	sql_command = format_str.format(thisname = name, thisage = age, thisgender = gender, thisanimal = animal, thisheight=height)

	cursor.execute(sql_command)

	#get people from database
	sql_command = ("""SELECT * FROM database """)

	cursor.execute(sql_command)
	result = cursor.fetchall()
	people = []
	#sort based on gender
	for person in result:
	    try:
		if(person[3].lower() != gender.lower()):
		    people.append(person)
	    except:
		pass

	#sort based on animal
	people_animal = []
	for person in people:
	     try:
		 if(animal[0].lower() == person[4][0].lower()):
		     people_animal.append(person)
	     except:
		 pass


	#sort based on age
	people_age = []
	age = now.year - age
	for person in people_animal:
	    try:
		other_age = now.year - person[2]
		if((other_age > (.9 * age)) and (other_age < (1.1 * age))):
		    people_age.append(person)
	    except:
		pass

	#sort for height
	people_height = []
	for person in people_age:
	    try:
		if(taller.lower() == "t"):
		    if(height < person[5]):
			people_height.append(person)
		else:
		    if(height < person[5]):
			people_height.append(person)
	    except:
		pass


	x = 0
	while x < 1:
	    #find match
	    if(len(people_height) >  0): #perfect match
		percentmatch = r.randrange(70, 95, 1)
		match_num = r.randrange(len(people_height))
		your_match = people_height[match_num][1] 
		print "Congratulations! You matched with " + str(your_match) + " with a match percentage of " + str(percentmatch) + "%!"
		for person in people_height:
		    print person
		    if(person[1] == your_match):
			print 'removed'
			people_height.remove(person)
	    elif(len(people_age) > 0): # no height requirement
		percentmatch = r.randrange(55,70, 1)
		match_num = r.randrange(len(people_age))
		your_match = people_age[match_num][1]
		print "Congratulations! You matched with " + str(your_match) + " with a match percentage of " + str(percentmatch) + "%!"
		for person in people_age:
		    print person
		    if(person[1] == your_match):
			people_age.remove(person)
	    else:
		people_age2 = []
		for person in people_animal: # bigger age range
		    other_age = now.year - person[2]
		    if((other_age > (.75 * age)) and (other_age < (1.25 * age))):
			people_age2.append(person)
		if(len(people_age2) > 0):
		    percentmatch = r.randrange(40, 55, 1)
		    match_num = r.randrange(len(people_age2))
		    your_match = people_age2[match_num][1]
		    print "Congratulations! You matched with " + str(your_match) + " with a match percentage of " + str(percentmatch) + "%!"
		    for person in people_age2:
			print person
			if(person[1] == your_match):
			    people_age2.remove(person)
		else: # still no one. YOu suck at love
		    print "You are forever alone! :("
		    x = 1
		    break
	    swipe = raw_input("Do you like your match? (yes/no)")
	    if(swipe[0] == 'y'):
		print "The Linder team is glad you like your match!"
		x = 1

if __name__ == '__main__':
	main()

	"""girls = ["Danielle", "Katie", "Delaney", "Emily", "Manal", "Carina", "Elizabeth"]

	boys = ["Andrew", "Theo", "Shingo", "Chris", "Justin"]

	random_girl = r.randrange(7)
	random_boy = r.randrange(5)

	print boys[random_boy] + " loves " + girls[random_girl] + "!!! <3"
	"""


	connection.commit()
	connection.close()

