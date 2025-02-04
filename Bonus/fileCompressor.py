import FreeSimpleGUI as fsg
from zipCreator import make_archive

label1 = fsg.Text("Select files to compress:")
input1 = fsg.Input()
choose_button1 = fsg.FilesBrowse("Choose Files", key="files")

label2 = fsg.Text("Select destination folder:")
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse("Choose Folder", key="folder")

compress_button = fsg.Button("Compress Files")
output_label = fsg.Text(key = "output", text_color="black")
layout = [[label1, input1, choose_button1], 
          [label2, input2, choose_button2], 
          [compress_button, output_label]]


window = fsg.Window("File Compressor", layout=layout)


while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed!")


window.close()