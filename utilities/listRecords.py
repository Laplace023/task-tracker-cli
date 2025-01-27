#this function lists records
import os

def taskList(status):
    """This function lists the files depending on the status"""
    os.chdir('tasks')
    records = os.listdir()
    
    print(records) #this is a debug code
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
        print(lst[:-5])
    
    os.chdir('../')
    return tasks

if __name__ == "__main__":
    import sys
    taskList(str(sys.argv[1]))
#tasksList = listTask('in-progress')

#for lst in tasksList:
#    print(lst[:-5])