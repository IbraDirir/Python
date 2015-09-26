#continue
numbersTaken =[9, 4, 11, 7, 8]
print("here are the numbers still available")

for n in range(1,20):
    if n in numbersTaken:
      continue
    print(n)