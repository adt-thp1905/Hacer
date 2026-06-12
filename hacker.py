def todo():
 t = input("Enter S.no.")
 x = input("Enter event here")
 y = input("Enter date here")
 z = input("Enter time here")
 with open("todo.txt" , "a") as p:
  p.write(f"{t} . {x} {y} {z}\n")
  p.read("todo.txt" )
