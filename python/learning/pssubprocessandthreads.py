import subprocess

op = subprocess.check_output(['dir', 'D:'], shell=True)
print op

#this below part will work only with linux
p1 = subprocess.Popen(['cat','/etc/passwd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p2 = subprocess.Popen(['tr','a-z', 'A-Z'], stdout=p1.stdout, stderr=subprocess.PIPE)

for line in p2.communicate():
    if line:
        print(line)