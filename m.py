file = open("filename.txt", "w")
file.write("my sister is a loser\n")
file.write("my sister is a big loser\n")
file.close()
file = open("filename.txt","a")
file.write("my sister is weird")
file.close()
file = open("filename.txt", "r")
filen = file.readlines()
print(filen)
with open ("mysisterisaloser.txt", "w") as file:
   file.write("my sister is annoying\n")
with open("mysisterisabigloser.txt", "a") as filen:
   filen.write ("my sister is a shorty\n")
with open("mysisteristooshortforherage.txt", "w") as file:
   file.write("my sister is dumb\n")