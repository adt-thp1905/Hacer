t = input("Enter S.no.")
x = input("Enter event here")
y = input("Enter date here")
z = input("Enter time here")
with open("todo.pdf" ,"w") as f:
 for x in f:
  f.write(f"{t} . {x} {y} {z}")
 
