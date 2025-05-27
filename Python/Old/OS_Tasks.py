# with OS we can execute the bash commands/script on linux server
import os
#print(dir(os)) # It's going to return all the modules.
#print(os.system("dir"))
'''
path="/Users/dilee/python/"

if os.path.isdir(path):
    print("It's a directory")
elif os.path.isfile(path):
    print("It's a file")
else:
    print("File or directory doesn't exit")
'''

#Below script will create the users in Linux machine. Please use the script in Linux.

userlist=("Dileep", "Rajesh", "Ravi")

for user in userlist:
    exitcode = os.system("id {}".format(user))
   # print(f"{exitcode}")
    if exitcode != 0:
        print(f"User {user} doesn't exist. Creating it")
        os.system(("useradd {}".format(user)))
    else:
        print("user already exist")

#Note: Python Fabric is like Ansible kind of thing to run the any scriot from the parent server to the child server. Mostly it deals automation tasks of the servers.
#Better we can learn the Anisble.