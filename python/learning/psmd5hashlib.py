import hashlib

checksum = hashlib.md5(open('D:\PythonTraining\day1\passwd.txt').read())
print dir(checksum)
print checksum.hexdigest()