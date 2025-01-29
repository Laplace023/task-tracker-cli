import os
import ast
from datetime import datetime

def updateTask(filename, description):
    homedir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(homedir)
    os.chdir('../')
    os.chdir('tasks')
    #pull up the file
    task = open(f'{filename}.json', 'r')
    taskDict = ast.literal_eval(task.read())
    timeNow = datetime.now()
    updatedAt = timeNow.strftime(("%m/%d/%Y %H:%M"))

    taskDict['Description'] = description
    taskDict['UpdatedAt'] = updatedAt

    taskData = str(taskDict)
    rewrite = open(f'{filename}.json', 'w')
    rewrite.write(taskData)
    rewrite.close()

    os.chdir('../')

    return taskDict

