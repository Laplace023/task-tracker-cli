#This will be used to modify the records.
import os
import ast
from datetime import datetime

def editTask(filename, status):
    if status in ['to-do', 'in-progress', 'done']:
        os.chdir('tasks')
        task = open(f"{filename}.json", "r") #This is quite challenging
        taskDict = ast.literal_eval(task.read()) #This is a new function for me
        #preparation of other parameters
        timenow = datetime.now()
        updated_at = timenow.strftime(("%m/%d/%Y %H:%M"))

        taskDict['Status'] = status
        taskDict['UpdatedAt'] = updated_at
        print(taskDict)
    else:
        print(f"The status({status}) you entered is invalid, please choose between 'to-do, 'in-progress', done'")

editTask('ip061', 'to-do')