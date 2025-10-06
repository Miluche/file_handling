with open("input.txt", "w") as file:
    file.write("Python is a powerful programming language.\n")
    file.write("Power Learn project Teaches Python.\n")
    file.write("Learning Python opens up many career opportunities.\n")
    file.write("This week challenge is for practicing file handling in Python.\n")
    file.write("And improving my coding skills!\n")

with open("input.txt", "r") as file:
    content = file.read()

word_count = len(content.split())

uppercase_content = content.upper()

with open("output.txt", "w") as file:
    file.write("PROCESSED TEXT:\n")
    file.write(uppercase_content)
    file.write("\n\nWORD COUNT: " + str(word_count))
