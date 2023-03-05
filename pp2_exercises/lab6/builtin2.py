def upper_lower(str):
    m1,m2=0,0
    for i in str:
        if(i.isupper()):
            m1+=1
        else:
            m2+=1
    return m1,m2
print(upper_lower("GFjxhhshGytx"))
