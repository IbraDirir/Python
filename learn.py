fw = open("sample.txt", "w")
fw.write("writing stuff in my file\n")
fw.write("cool")
fw.close()
fr = open("sample.txt", "r")
text = fr.read()
print(text)
fr.close()


