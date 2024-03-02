import getopt
import sys
(opts, args) = getopt.getopt(sys.argv[1:], "f:m:", ["filename", "message"])

print(opts)
print(args)

for opt, message in opts:
    print (f"{opt}, {message}") 
