#adds record to the detination folder via add command
from datetime import datetime
import os 
import random


def taskAdd(desc):
    """function to add an entry"""
    #prepare the directory
    os.chdir('tasks')
    #calling datetime to set the current date
    time_now = datetime.now()
    #change format to m/d/y h:m for CreatedAy
    created_at = time_now.strftime("%m/%d/%Y %H:%M")
    #create an ID with second created and a random number form 100-999
    id = str(time_now.strftime("%S")) + str(random.randrange(100, 1000))
    
    #This is the entry composition part
    task_entry = dict() #this is where the entry is composed
    
    task_entry['ID'] = id
    task_entry['Description'] = desc
    task_entry['Status'] = "to-do"
    task_entry['CreatedAt'] = created_at
    task_entry['UpdatedAt'] = created_at

    #Creating the file
    task_data = str(task_entry) #changing the data to string to make it writable
    #creating the file name
    filename = "td" + task_entry['ID'] #
    mkfile = open(f"{filename}.json", "w")
    mkfile.write(task_data)
    mkfile.close
    
    print(f"file {filename}.txt created")
    return task_entry

#Debugging/Testing section

#entry = taskAdd(input())

#entry.update({'UpdatedAt':'I AM ATOMIC'})
#print("Here is the file content. for debugging sake")
#for key, value in entry.items():
#    print(f"{key} : {value}")



