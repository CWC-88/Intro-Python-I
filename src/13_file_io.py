"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
foo = open('/Users/C/Desktop/Intro-Python-I/src/foo.txt')
print(foo.read())
foo.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar = open('/Users/C/Desktop/Intro-Python-I/bar.txt', 'w+')
bar.writelines(["crypto is not a stonk to be converted to USD \nit is a matter of time before crypto is cancelled \nholding is death... buy, lend and spend...velocity is life"])

with open('/Users/C/Desktop/Intro-Python-I/bar.txt') as b:
    read_data = b.read()
    print(read_data)