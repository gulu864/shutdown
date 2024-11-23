
def shut_down(z):
  return "Shutting down"

var=input("Do you want the program to shut down?(Yes/No):")

if var=="Yes":
  print(shut_down(var))

elif var=="No":
  print("abort shut")

else:
  print("Sorry your option is not in the list.")  