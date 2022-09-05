import PySimpleGUI as sg
import os
from file_reader import FileReader


def main():
    sg.theme("SystemDefault")

    layout = [
        [sg.Text("Choose a file with all the youtube links to convert:")],
        [sg.InputText(key="FILE_PATH"), sg.FileBrowse(
            initial_folder=os.getcwd(), file_types=[("Text Files", "*.txt")])],
        [sg.Text(text="Download Status:", key="status")],
        [sg.Button("Submit"), sg.Exit()]
    ]

    window = sg.Window("Youtomp3 Script", layout)

    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == "Exit":
            break

        elif event == "Submit":
            f = FileReader(values["FILE_PATH"])
            run_status = " Done" if f.run_cmds() else " Error Data Not Found"
            window["status"].update(f"Download Status: {run_status}")

    window.close()


if __name__ == '__main__':
    main()
