#this function lists records
import os
import ast

def taskList(status):
    """This function lists the files depending on the status"""
    homedir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(homedir)
    os.chdir('../')
    os.chdir('tasks')
    records = os.listdir()
    
    #print(records) #this is a debug code
    #preparing the code to fetch the files
    if status == 'to-do':
        stat = "td"
    elif status == 'in-progress':
        stat = "ip"
    elif status == 'done':
        stat = "dn"
    else:
        stat = "**" #adding a wildcard option for all
    #This will list the filtered files
    tasks = []
    for st in records:
        if stat == st[:2]:
            tasks.append(st)
        elif stat == "**":
            tasks.append(st)
        else:
            pass
    for lst in tasks:
        x = open(lst)
        item = x.read()
        itemdict = ast.literal_eval(item)
        name = lst[:-5]
        description = itemdict['Description']
        print(f"{name}:{description}")
    
    os.chdir('../')
    return tasks

if __name__ == "__main__":
    import sys
    taskList(str(sys.argv[1]))
#tasksList = listTask('in-progress')

#for lst in tasksList:
#    print(lst[:-5])