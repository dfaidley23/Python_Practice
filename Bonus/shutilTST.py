import shutil

#this will take all of the files in said directory, make them a zip, and compile them in the output file
shutil.make_archive("output", "zip", "files/")