import os
print("Existance:", os.access("C:/Users/user/Documents/pp2/pp2/identity.docx", os.F_OK))
print("Readability:", os.access("C:/Users/user/Documents/pp2/pp2/identity.docx", os.R_OK))
print("Writability:", os.access("C:/Users/user/Documents/pp2/pp2/identity.docx", os.W_OK))
print("Executability:", os.access("C:/Users/user/Documents/pp2/pp2/identity.docx", os.X_OK))