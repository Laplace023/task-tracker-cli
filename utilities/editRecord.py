#This will be used to modify the records.
import os
import ast
from datetime import datetime

def taskEdit(filename, status):
    if status in ['to-do', 'in-progress', 'done']:
        homedir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(homedir)
        os.chdir('../')
        os.chdir('tasks')
        task = open(f"{filename}.json", "r") #This is quite challenging
        oldFileName = f"{filename}.json"
        taskDict = ast.literal_eval(task.read()) #This is a new function for me
        #preparation of other parameters
        timenow = datetime.now()
        updated_at = timenow.strftime(("%m/%d/%Y %H:%M"))
        #preparation of the content
        taskDict['Status'] = status
        taskDict['UpdatedAt'] = updated_at
        print(taskDict)
        #creating the file block
        #first tho is prepare the name.
        if status == 'to-do':
            stat = 'td'
        elif status == 'in-progress':
            stat = 'ip'
        elif status == 'done':
            stat = 'dn'
        newFileName = f"{stat}{taskDict['ID']}.json"
        print(newFileName)

        #rewrite the content
        taskData = str(taskDict)
        rewriteContent = open(f"{filename}.json", 'w')
        rewriteContent.write(taskData)
        rewriteContent.close

        #rename the file
        os.rename(oldFileName, newFileName)
        os.chdir('../')

    else:
        print(f"The status({status}) you entered is invalid, please choose between 'to-do, 'in-progress', done'")
if __name__ == "__main__":
    import sys
    taskEdit(str(sys.argv[1]))
#editTask('ip061', 'done')