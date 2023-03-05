import os
if(os.access("C:/Users/user/Documents/pp2/pp2/identity.docx", os.F_OK) and os.access("C:/Users/user/Documents/pp2/pp2/identity.docx", os.R_OK)):
    os.remove("C:/Users/user/Documents/pp2/pp2/identity.docx")
