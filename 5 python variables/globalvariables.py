x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

x = "fantastic"
print("Python is" + x)

myfunc()

print("python is"  + x)

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)