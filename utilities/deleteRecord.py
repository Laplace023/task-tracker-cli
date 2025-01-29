#This is the fuction to delete files
import os

def taskDelete(filename):
    """Function to delete the tasks"""
    homedir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(homedir)
    os.chdir('../')
    os.chdir('tasks')
    toDelete = filename + '.json'
    os.remove(toDelete)
    print(f"task with ID:{filename} is now deleted")
    os.chdir('../')

if __name__ == "__main__":
    import sys
    taskDelete(str(sys.argv[1]))
#taskDelete(input())

#This somehow works but I need to clean this up.