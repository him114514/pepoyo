import os
a=input('Are you sure you want to run it?\nThis is a malicious program!\n N/S ?\n')
if a=='N':
    os.system('start {0}client.exe'.format(os.getcwd()+'pepoyo\\'))
elif a!='N' or a=='S':
    print('Have a good time!')
