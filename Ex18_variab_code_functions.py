# thi one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just take one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no argument
def print_none():
    print("Nothing.")

print_two("Martin","Bazzolo")
print_two_again("Martin","Bazzolo")
print_one("First")
print_none()
