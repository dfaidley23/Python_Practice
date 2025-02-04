import zipfile

def extract_files(zippath, dest_dir):
    with zipfile.ZipFile(zippath, "r") as zip:
        zip.extractall(dest_dir)


if __name__ == "__main__":
    extract_files("Python Mega\Bonus\dest\compressed.zip", "Python Mega\Bonus\dest")