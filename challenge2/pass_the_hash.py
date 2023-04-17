# This script was created by Matthew Mahan of team Pterodactyl. 
# We discovered the password without the use of this script.
# This script was created after completing the challenge.

import hashlib 

our_guy = '335a10628906e9ef3e5ef3e9100b4768dea0f10ecd091cbdc58bc41bdff5ce2d'
top_list = 'top_list'

# function to make it funny (goofy) ((silly)) 
def he_is(value1, value2):
	return value1 == value2

# organize and clean up the list of passwords
f = open(top_list)
content = f.readlines()
f.close()
clean = []
for password in content:
	clean.append(password.rstrip())

# check if he's our guy (hash matches concatenated)
for i in clean:
	for j in clean:
		l = hashlib.sha256((i+j).encode()).hexdigest()
		if he_is(our_guy, l):
			print("The correct password is", i+j)
	
