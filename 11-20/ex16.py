# Learn Python the Hard Way
# Exercise 16: Reading and Writing

from sys import argv

script, filename = argv

def write_line(line):
    target.write(line)
    target.write('\n')

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input('?')

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

write_line(line1)
write_line(line2)
write_line(line3)

print "And finally, we close it."
target.close()
