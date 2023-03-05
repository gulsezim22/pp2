import os
s = "C:/Users/user/Documents/pp2/pp2"
print("Directories:")
print([ i for i in os.listdir(s) if os.path.isdir(os.path.join(s, i)) ])
print("Files:")
print([ i for i in os.listdir(s) if not os.path.isdir(os.path.join(s, i)) ])
print("Directories and files :")
print([ i for i in os.listdir(s)])