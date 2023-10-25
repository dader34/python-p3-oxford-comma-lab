def oxford_comma(it):
    items = [str(item) for item in it]
    if(len(items) == 1):
        return str(items[0])
    elif(len(items) == 2):
        return f'{str(items[0])} and {str(items[1])}'
    elif(len(items) == 3):
        return f'{str(items[0])}, {str(items[1])}, and {str(items[2])}'
    else:
        for item in items:
            if(items.index(item) %2 == 0 and (items.index(item) != len(items) -1)):
                items.insert(items.index(item)+1,", ")
            elif(items.index(item) == len(items)-1):
                items.insert(items.index(item),"and ")
                break
    return(''.join(items))


print(oxford_comma([1,2,3,4,5]))