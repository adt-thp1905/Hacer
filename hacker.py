t = input("Enter S.no.")
x = input("Enter event here")
y = input("Enter date here")
z = input("Enter time here")
with open("todo.txt" ,"w") as f:
 f.write(f"{t} . {x} {y} {z}")
 for o in f:
  f.append(f"{t} . {x} {y} {z}")
