import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter.ttk import Separator
import subprocess
import webbrowser
import urllib.request
import os

# Create the main window
window = tk.Tk()
window.title("Wget Downloader")

# Function to handle the "Paste URL" button


def paste_url():
    url_entry.delete(0, tk.END)
    url_entry.insert(tk.END, window.clipboard_get())


# Function to handle the browse button


def select_output_dir():
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(tk.END, output_dir)


# Function to handle the download process


def download_file():
    url = url_entry.get()
    output_dir = output_dir_entry.get()
    if url and output_dir:
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            command = ["wget", url, "-P", output_dir, "-N"]
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                startupinfo=startupinfo,
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
            for line in iter(process.stdout.readline, ""):
                update_status(line.strip())
            update_status("Download completed.")
            show_completion_popup()
        except Exception as e:
            update_status("Error occurred during download: " + str(e))
    else:
        update_status("Please enter a valid URL.")


# Function to update the status label


def update_status(text):
    status_label.config(text=text)
    status_label.update()


# Function to display a pop-up window for completion status


def show_completion_popup():
    messagebox.showinfo(
        "Download Complete", "The download has been completed successfully."
    )


# Function to handle the "About" menu item


def show_about():
    messagebox.showinfo(
        "About", "Wget Downloader\nVersion 1.1\n\nCreated by pudsz\n\n... TTIOT ..."
    )


# Function to handle the "How to use..." menu item


def show_usage():
    messagebox.showinfo(
        "How to use...",
        "1. Enter the URL of the file to download.\n2. Select the output directory.\n3. Click on the 'Download' button to start the download.\n\nNote: For detailed instructions on how to use please open the 'Help File'",
    )


# Function to open the help file documentation


def open_help_file():
    # Replace with the actual path to your help file
    help_file_path = "G:/Software/py/Python Creations/Completed/Projects/Wget Downloader/Version 1.0/readme.txt"
    webbrowser.open(help_file_path)


# Function to open the version info file documentation


def open_version_info_file():
    # Replace with the actual path to your version info file
    version_info_file_path = "G:/Software/py/Python Creations/Completed/Projects/Wget Downloader/Version 1.1/Release Notes Version 1.1.txt"
    webbrowser.open(version_info_file_path)


# Function to exit the program


def exit_program():
    window.destroy()


# Function to handle the "Check Version" command


def check_version():
    messagebox.showinfo("Version", "Wget Downloader v1.1")


# Create the menu bar
menu_bar = tk.Menu(window)

# Create the "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create the "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="• How to use", command=show_usage)
# Command to open the local help file
help_menu.add_command(label="• Help File", command=open_help_file)
help_menu.add_separator()  # Add a separator
help_menu.add_command(label="About...", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Create the "Version" submenu
version_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Version", menu=version_menu)
version_menu.add_command(
    label="• Check Version", command=check_version
)  # Add your command here
version_menu.add_command(label="• Release Notes", command=open_version_info_file)
version_menu.add_separator()  # Add a separator
version_menu.add_command(label="Wget Downloader", command=None)

# Add the menu bar to the window
window.config(menu=menu_bar)

# Add a label to display instructions
instructions_label = tk.Label(
    window,
    text="Enter the URL of the file to download:",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 11),
)
instructions_label.pack(fill="both", expand=True, pady=(10, 0))

# Add an entry field for the URL
url_entry = tk.Entry(window, width=50, bg="#F7FCFC")
url_entry.pack(fill="both", expand=True, pady=(4, 5))

# Add a "Paste URL" button
paste_button = tk.Button(
    window,
    text="Paste URL",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 11),
    command=paste_url,
)
paste_button.pack(expand=True, pady=(4, 10))

# Add a separator line
separator = Separator(window, orient=tk.HORIZONTAL)
separator.pack(fill=tk.X, padx=(10))

# Add a label to display the output directory
output_dir_label = tk.Label(
    window,
    text="Select output directory:",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 11),
)
output_dir_label.pack(fill="both", expand=True, pady=(10, 0))

# Add an entry field to display the selected output directory
output_dir_entry = tk.Entry(window, width=50, bg="#F7FCFC", justify="center")
output_dir_entry.pack(fill="both", expand=True, pady=(4, 5))

# Add a button to browse and select the output directory
browse_button = tk.Button(
    window,
    text="Browse",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 11),
    command=select_output_dir,
)
browse_button.pack(expand=True, pady=(4, 10))

# Add a separator line
separator = Separator(window, orient=tk.HORIZONTAL)
separator.pack(fill=tk.X, padx=(10))

# Add a button to start the download
download_button = tk.Button(
    window,
    text="Download",
    bg="#E7E9EA",
    fg="#20211A",
    justify="center",
    font=("Tahoma", 12),
    command=download_file,
)
download_button.pack(fill="both", expand=True, pady=(10, 0))

# Add a label to display the download status
status_label = tk.Label(window, text="")
status_label.pack(fill="both", expand=True, pady=(5, 10))

# Background color
window.configure(bg="#80b3ff")

# Run the main event loop
window.mainloop()
