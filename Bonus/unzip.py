import FreeSimpleGUI as fsg
from unzipExtractor import extract_files

fsg.theme("Black")

label1 = fsg.Text("Select Zipped File:")
input1 = fsg.Input()
choose_button1 = fsg.FileBrowse("Choose Files", key="file")

label2 = fsg.Text("Select destination folder:")
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse("Choose Folder", key="folder")

extract_button = fsg.Button("Extract Files")
output_label = fsg.Text(key = "output", text_color="blue")

layout = [[label1, input1, choose_button1], 
          [label2, input2, choose_button2], 
          [extract_button, output_label]]


window = fsg.Window("File Extractor", layout=layout)


while True:
    event, values = window.read()
    print(event, values)
    zippedpath = values["file"]
    dest_dir = values["folder"]
    extract_files(zippedpath, dest_dir)
    window["output"].update(value="Extraction Completed!")

window.close()