# meriFile = open("testing.txt", "w")
# meriFile.write("Yeh meri file hai or mein is mein likh rha hn!\n")
# meriFile.write("Yeh nayi line ka text hai\n")
# meriFile.close()

# fileReadKaro = open("testing.txt", "r")
# content = fileReadKaro.read()
# print(content)
# fileReadKaro.close()

# File I/O
with open("files/sampleThree.txt", "w") as f:
    f.write("This is AgentCraft (Test 3)!\n")
    f.write("Welcome to File Handling (Test 3)!\n")

with open("files/sampleThree.txt", "r") as f:
    content = f.read()
    print(content)