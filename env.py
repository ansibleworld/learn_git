import os 
for key in ["HOME" , "SHELL"]:
    value = os.getenv(key)
    print(value)