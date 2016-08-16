import random as r
import sqlite3
import datetime
import sys
from gooey import Gooey, GooeyParser

@Gooey()
def main():

    now = datetime.datetime.now()
    connection = sqlite3.connect("connection.db")
    cursor = connection.cursor()

    parser = GooeyParser(description='Are you ready to find the perfect match?')	
    parser.add_argument("name", type=str, default='Enter Name')
    parser.add_argument("Birthyear", type=int)
    parser.add_argument("gender", choices=["Female","Male"], default="Female")
    parser.add_argument("animal", choices=["Dogs","Cats"], default="Dogs")
    parser.add_argument("feet", type=int, default=5)
    parser.add_argument("inches", type=int, default=3)
    args = parser.parse_args()

    name = args.name
    age = args.Birthyear
    if args.gender == "Female":
        gender = 'f'
    else:
        gender = 'm'
    if args.animal == 'Dogs':
        animal = 'd'
    else:
        animal = 'c'
    height = 12 *  args.feet + args.inches

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

    #find match
    if(len(people_height) >  0): #perfect match
        percentmatch = r.randrange(70, 95, 1)
        match_num = r.randrange(len(people_height))
        your_match = people_height[match_num][1] 
        print "Congratulations! You matched with " + str(your_match) + " with a match percentage of " + str(percentmatch) + "%!"
        for person in people_height:
            people_height.remove(person)
    elif(len(people_age) > 0): # no height requirement
        percentmatch = r.randrange(55,70, 1)
        match_num = r.randrange(len(people_age))
        your_match = people_age[match_num][1]
        print "Congratulations! You matched with " + str(your_match) + " with a match percentage of " + str(percentmatch) + "%!"
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
        else: # still no one. YOu suck at love
            print "You are forever alone! :("
    connection.commit()
    connection.close()
    
    
if __name__ == '__main__':
    main()
