#adds record to the detination folder via add command
from datetime import datetime


def task_add(desc):
    """function to add an entry"""
    time_now = datetime.now()
    #change format to m/d/y h:m
    created_at = time_now.strftime("%m/%d/%Y %H:%M")
    id = time_now.strftime("%m%d%Y-%H%M%S")


    task_entry = dict() #this is where the entry is composed
    task_entry['ID'] = id
    task_entry['Description'] = desc
    task_entry['Status'] = "to-do"
    task_entry['CreatedAt'] = created_at
    task_entry['UpdatedAt'] = created_at
    return task_entry

entry = task_add(input())

for key, value in entry.items():
    print(f"{key} : {value}")

