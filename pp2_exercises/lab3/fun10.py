def unique_list(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2