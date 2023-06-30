import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# Create the main window
window = tk.Tk()
window.title("Wget Downloader")

# Add a label to display instructions
instructions_label = tk.Label(
    window, text="Enter the URL of the file to download:")
instructions_label.grid(row=0, column=0, padx=10, pady=10)

# Add an entry field for the URL
url_entry = tk.Entry(window, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Function to handle the "Paste URL" button


def paste_url():
    url_entry.delete(0, tk.END)
    url_entry.insert(tk.END, window.clipboard_get())


# Add a "Paste URL" button
paste_button = tk.Button(window, text="Paste URL", command=paste_url)
paste_button.grid(row=0, column=2, padx=10, pady=10)

# Add a label to display the output directory
output_dir_label = tk.Label(window, text="Select output directory:")
output_dir_label.grid(row=1, column=0, padx=10, pady=10)

# Function to handle the browse button


def select_output_dir():
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(tk.END, output_dir)


# Add a button to browse and select the output directory
browse_button = tk.Button(window, text="Browse", command=select_output_dir)
browse_button.grid(row=1, column=2, padx=10, pady=10)

# Add an entry field to display the selected output directory
output_dir_entry = tk.Entry(window, width=50)
output_dir_entry.grid(row=1, column=1, padx=10, pady=10)

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
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            for line in iter(process.stdout.readline, ''):
                update_status(line.strip())
            update_status("Download completed.")
            show_completion_popup()
        except subprocess.CalledProcessError:
            update_status("Error occurred during download.")
    else:
        update_status("Please enter a valid URL and output directory.")


# Add a button to start the download
download_button = tk.Button(window, text="Download", command=download_file)
download_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Add a label to display the download status
status_label = tk.Label(window, text="")
status_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Function to update the status label


def update_status(text):
    status_label.config(text=text)
    status_label.update()

# Function to display a pop-up window for completion status


def show_completion_popup():
    messagebox.showinfo("Download Complete",
                        "The download has been completed successfully.")


# Run the main event loop
window.mainloop()
