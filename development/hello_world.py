import sys

print("Congratulations on installing Python!", '\n')

print("This system is running {}".format(sys.version), '\n')

if "conda" in sys.version:
    print("Hello from Anaconda!")
else:
    print("Hello from system-installed Python!")

print('This is a change in code')