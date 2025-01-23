#This is the fuction to delete files
import os

def taskDelete(filename):
    """Function to delete the tasks"""
    os.chdir('tasks')
    toDelete = filename + '.json'
    os.remove(toDelete)
    print(f"task with ID:{filename} is now deleted")


taskDelete(input())

