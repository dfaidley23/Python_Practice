filenames = ["1.test.txt", "2.test.txt", "3.test.txt"]

for filename in filenames:
    #this finds the first occurence of . in the string and replaces it with a dash
    filename = filename.replace('.', '-', 1)
    print(filename)

# filename() this is a turple.