
files = open("volby_posl_2017.csv.test","w")


with open("volby_posl_2017.csv") as f:
  while True:
    c = f.read(1)
    if not c:
      print ("End of file")
      break
    if c == ";":
        files.write(",")
    else:
        files.write(c)
