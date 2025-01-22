import os

cwd = os.getcwd()
print(cwd)
os.chdir('tasks')
nwd = os.getcwd()
print(nwd)

x = open("text.txt", "w")
x.write("content")
x.close