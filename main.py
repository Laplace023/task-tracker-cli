#hope I can pull this off
#These are my awesome modules
from utilities.addRecord import taskAdd as tAdd
from utilities.deleteRecord import taskDelete as tDel
from utilities.editRecord import taskEdit as tEdit
from utilities.listRecords import taskList as tList
from utilities.updateRecord import updateTask as tUpdate

import argparse
import os

#tAdd('I am Atomic')
curdir = os.getcwd()
print(curdir)
tList('done')
tUpdate('dn061', 'I am all range Atomic')
