#Activity: Define a function to take a string as input and display all the distinct letters in the string in Upper case.
def convert(name1):
  x = []
  for i in name1:
    x.append(i.upper())
  print(x)
  x = set(x)
  return x

n = input("Enter your value: ")
a = convert(n)
print(a)




  