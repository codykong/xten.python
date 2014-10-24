movies=["The Holy Grail","The Life of Brian","The Meaning of Life",['python',[1988,['kong','qing','yu']]]]

def print_lol(the_list,level=0):

    if isinstance(the_list,list):
        for each_item in the_list:            
            print_lol(each_item,level+1)
            print(the_list)
    else:
        for level_num in range(level):
            print("\t",end='')
        print(the_list)

print_lol(movies)
