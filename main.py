#hope I can pull this off
#These are my awesome modules
from utilities.addRecord import taskAdd as tAdd
from utilities.deleteRecord import taskDelete as tDel
from utilities.editRecord import taskEdit as tEdit
from utilities.listRecords import taskList as tList
from utilities.updateRecord import updateTask as tUpdate

import argparse
import os

pars = argparse.ArgumentParser()

pars.add_argument("--add", help="add a new entry", action="store_true")
pars.add_argument("inp1", help="content of the call",nargs='?', default="test")
#pars.add_argument("inp2", help="another input, I'm still learning pos args")
pars.add_argument("--delete", help="deletes an entry", action="store_true")
pars.add_argument("--list", help="list tasks",nargs='?', choices=["to-do", "in-progress", "done", "all"], const="all")
pars.add_argument("--update", help="update description")
pars.add_argument("--mark", help="this is used to update the status")
arg = pars.parse_args()

entry = arg.inp1

#entry2 = arg.inp2
file = arg.update
file2 = arg.mark

stats = arg.list

if arg.add:
    tAdd(entry)
elif arg.delete:
    tDel(entry)
elif arg.update:
    tUpdate(file, entry)
elif arg.list:
    tList(stats)
elif arg.mark:
    tEdit(file2, entry)
else:
    print("gomenasai")
