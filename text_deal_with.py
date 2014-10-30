import os
print(os.getcwd())
os.chdir('document/')
print(os.getcwd())
try:
    with open("talk.txt") as data,open("talk_to_you.txt","w")as out:
            for each_line in data:
                try:       
                    (man,line)=each_line.split(':',1)
                    print("new",file=out)
                    print(man,end='')
                    print(' said ',file=out)
                    print(' said ',end='')
                    print(line,file=out)
                    print(line,end='')
                
                except:
                    pass
                            
except IOError as err:
    print("File ERROR:"+ str(err))
