import sys
import pprint

#one way to import libs from a folder location but suitable only when limited packages
sys.path.append('lib')
import psutils

#this will throw an error
#import psutils

print psutils.__name__
#help(psutils)
print psutils.author
psutils.author = "new author"
print psutils.author

reload(psutils)
print psutils.author