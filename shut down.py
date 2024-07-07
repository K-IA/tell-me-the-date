import os
shut_down =input("do you want to shotdown your computer(yes/no): ")
if shut_down == "yes":
    os.system("shutdown /s /t 0")
else:
    print("shut down is not requasted")
    
