from sys import argv

script, file = argv

print "we are going to erase file %r" % file

print "Opening the file...."
target = open(file,'w')

print "truncating the file"
target.truncate()

print "write some more content to the file"
row1 = raw_input("line 1:")
row2 = raw_input("line 2:")
row3 = raw_input("line 3:")

target.write(row1)
target.write("\n")
target.write(row2)
target.write("\n")
target.write(row3)
target.write("\n")

print "the writting operation done"
target.close()