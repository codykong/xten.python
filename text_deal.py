import os
print(os.getcwd())
os.chdir('document/')
print(os.getcwd())
try:
    data=open("talk.txt")
    out=open("talk_to_you.txt","w")
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
finally:
    if 'data' in locals():
        data.close()
    if 'out' in locals():
        out.close()

         
