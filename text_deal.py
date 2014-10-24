import os
print(os.getcwd())
os.chdir('document/')
print(os.getcwd())
data=open("talk.txt")

for each_line in data:
    (man,line)=each_line.split(':')
    print(man,end='')
    print(' said ',end='')
    print(line,end='')

data.close()
         
