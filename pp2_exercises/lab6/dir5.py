list1 = ['0', '1', '2', '3', '4']
with open('gulsezim2.txt', "w") as myfile:
        for i in list1:
                myfile.write("%s\n" % i)

c = open('gulsezim2.txt')
print(c.read())