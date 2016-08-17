import random as r
import sqlite3
import datetime
from Tkinter import *
import time

'''#def main():

now = datetime.datetime.now()
connection = sqlite3.connect("connection.db")
cursor = connection.cursor()

root = Tk()

# make all the elements
list_name = Listbox(root)
list_name.insert(0, 'name')
name_text = Entry(root, bg = 'white')

#buttons
insert_button = Button(root, text = "Save", command = Insert)

#pack all the elememts
list_name.pack()
name_text.pack()
insert_button.pack()

root.mainloop()
'''
def Insert():
    '''    #add BS 
    print 'in Insert()'
    output.insert(END, 'Calculating Match...')
    time. sleep(.5)
    output.insert(END, 'Calculating IQ...')
    
    time.sleep(.5)
    output.insert(END, 'Comparing Facial Expressions...')
    time.sleep(.5)
    output.insert(END, 'Asking for friend approval...')
    time.sleep(.5)
    print'done with crap'
'''
    #get info from GUI
    name = name_text.get()
    age = int(age_text.get())
    gender = gender_text.get()
    animal = animal_text.get()
    height = int(height_text.get())

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
             output.insert(END,  "Congratulations! You matched with " + str(your_match) + " with a match percentage of " + str(percentmatch) + "%!")
             for person in people_height:
                 people_height.remove(person)
        elif(len(people_age) > 0): # no height requirement
             percentmatch = r.randrange(55,70, 1)
             match_num = r.randrange(len(people_age))
             your_match = people_age[match_num][1]
             output.insert(END, "Congratulations! You matched with " + str(your_match) + " with a match percentage of " + str(percentmatch) + "%!")
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
                output.insert(END, "Congratulations! You matched with " + str(your_match) + " with a match percentage of " + str(percentmatch) + "%!")
                for person in people_age2:
                    print person
                    if(person[1] == your_match):
                        people_age2.remove(person)
            else: # still no one. YOu suck at love
                output.insert(END, "You are forever alone! :(")
                x = 1
                break
  #          print "The Linder team is glad you like your match!"
        x = 1
    connection.commit()
    connection.close()
    
now = datetime.datetime.now()
connection = sqlite3.connect("connection.db")
cursor = connection.cursor()

root = Tk()
root.geometry('1000x500')

# make all the elements
#name
list_name = Listbox(root, height = 1)
list_name.insert(0, 'Enter Name:')
name_text = Entry(root, bg = 'white')
#name
list_age = Listbox(root, height = 1)
list_age.insert(0, 'Enter Birthyear:')
age_text = Entry(root, bg = 'white')
#gender
list_gender = Listbox(root, height = 1)
list_gender.insert(0, 'Gender:')
gender_text = Entry(root, bg='white')
#animal
list_animal = Listbox(root, height = 1)
list_animal.insert(0, 'Dogs or Cats?')
animal_text = Entry(root, bg = 'white')
#height
list_height = Listbox(root, height = 1)
list_height.insert(0, 'Enter Height: in inches')
height_text = Entry(root, bg = 'white')

#buttons
insert_button = Button(root, text = "Find Match", command = Insert)

#make output
output = Listbox(root, width = 100)

#pack all the elememts
list_name.pack()
name_text.pack()
list_age.pack()
age_text.pack()
list_gender.pack()
gender_text.pack()
list_animal.pack()
animal_text.pack()
list_height.pack()
height_text.pack()
insert_button.pack()
output.pack()

root.mainloop()
    
