# Learn Python the Hard Way
# Exercise 33: While Loops

start = 0
numbers =[]

def while_loop_list(end, increment):
    """Prints the elements in a list until the end variable is reached."""
    global start
    while start < end:
        print "At the top i is %d" % start
        numbers.append(start)
        start += increment

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % start

while_loop_list(int(raw_input("Enter the end number:\n")),
        int(raw_input("Enter the number to increment in:\n")))

print "The numbers: "

for num in numbers:
    print num
