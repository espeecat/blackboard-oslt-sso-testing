# OSLT Auth testing
# To test the B2 plugin availabe from:
# https://github.com/AllTheDucks/oslt-autosignon
# Version with ultra support (TBC)
# https://github.com/AllTheDucks/oslt-autosignon/tree/feature/ultra-support

# Run this script to produce a URL for SSO
# You will need to create/edit secrets.py
# -host
# -url
# -shared secret
# -userid e.g. abc123
# -courseid e.g. CHEM101 (courseid is optional)
# Test with a long timedelta setting
# to allow you to copy and paste
#
# Turn on debug in authprovider for help
# tested with autsignon V3
# Not tested with Ultra
#
# 20190905 first attempt -jason
import time
import hashlib 
from secrets import * #server info and secrets

'''
Example URL
https://mycourses.myschool.edu/webapps/
oslt-auth-provider-autosignon-BBLEARN/service/login/_328_1/
?auth=d78c<hash>ca3c6d&userId=abc1234&timestamp=1458501560&courseId=AB123_2019
'''
timestamp = int(time.time()) 

# string to be hashed =
# timestamp+userid+secret
string = str(timestamp)+userid+sharedSecret
md5hash = hashlib.md5(string)
md5String = md5hash.hexdigest()

queryString ='?auth='+md5String+'&userId='+userid+'&timestamp='+str(timestamp)

# qcourse is optional for redirect to course area
sso =host+url+queryString+qcourse

# SSO without course redirect/linking
# sso =host+url+queryString
print 'Copy and paste the URL into browser'
print 'Be quick if your timedelta is small!'
print
print
print " "+sso
print
print
print "The end."