#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
successful = 0
ipAdd = {}

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            ipAdd = line.split(" ")[-1] 
        elif "-] Authorization failed" in line:
            successful += 1

print(f"The number of failed log in attempts is {loginfail} from the following IP addresses:  {ipAdd}")
print("The number of successful log ins is ", successful)
