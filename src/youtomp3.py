import PySimpleGUI as sg
import os
from file_reader import FileReader

# '''
# NEXT UP:
# - Parse youtube links to before downloading (remove the apersand after the link itself)
# - Add spotify links functionality (either convert spotify -> or spotify_dl)
# - After downloading and processing, put directly into Music with artist metadata and mp3 img
# '''


def main():
    sg.theme("SystemDefault")

    layout = [
        [sg.Text("Choose a file with the youtube link(s) to convert:")],
        [sg.InputText(key="FILE_PATH"), sg.FileBrowse(
            initial_folder=os.getcwd(), file_types=[("Text Files", "*.txt")])],
        [sg.Text(text="Download Status:", key="status")],
        [sg.Button("Download"), sg.Exit()]
    ]

    window = sg.Window("Youtomp3 Script", layout)

    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == "Exit":
            break

        elif event == "Download":
            f = FileReader(values["FILE_PATH"])
            run_status = " Done" if f.run_cmds() else " Error Data Not Found"
            window["status"].update(f"Download Status: {run_status}")

    window.close()


if __name__ == '__main__':
    main()
