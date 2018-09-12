import sys

print("This system is running", sys.version, '\n')

if "conda" in sys.version:
    print("Hello from Anaconda!")
else:
    print("Hello from System-installed Python!")
