'''
This file contains secrets 
for the SSO to work

Edit secrets.py to match your setup.
This file is an example.

Secrets.py is imported into the test script

'''

userid ='myuserid1' # the userid of the person

host='https://your.learn.com'

# shared secret is configured in
# in the auth provider settings
sharedSecret='AddThisToYourOSLTConfigToo'

# example query string
# Something like:
url='/webapps/oslt-auth-provider-autosignon-BB<something>/service/login/_254_1'

# course redirect
qcourse ='&courseId=YOURCOURSEID'
