import os
path = r"C:/Users/user/Documents/pp2/pp2/identity.docx"
print(os.path.exists(path))
if(os.path.exists(path)):
    print("\nFile name:")
    print(os.path.basename(path))
    print("\nDirectory name:")
    print(os.path.dirname(path))