#this can be used to find and get a list of files or filepaths specified. You can even access/modify the contents of said file(s)
import glob

myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())