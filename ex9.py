from sys import argv

script, user_name = argv

prompt = "123"

print "Hi I'm the %s script." % script

print "Do you like me %s" % user_name

like = raw_input(prompt)

print "Where do you live %s" % user_name

lives = raw_input(prompt)

print "What kind of computer you have %s" % user_name
computer = raw_input(prompt)
print """
Alright, so you  said %r about liking me.
You live in %r. Not sure where that is.
and you have %r computer model
""" % (like, lives, computer)