#input
text = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything?" ))

#convert to lower case, remove hyphen, no space either side
answer = text.replace("-"," ").lower().strip()

# print
if answer == "42":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")
