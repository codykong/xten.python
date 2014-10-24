import os
print(os.getcwd())
os.chdir("D:")
print(os.getcwd())
data=open("words.txt")
print(data.readline(),end='')
print(data.readline(),end='')
print(data.readline(),end='')
print(data.readline(),end='')

data.seek(0)
for each_line in data:
    print(each_line,end='')

data.close()
         
