import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, scrolledtext
import tkinter.ttk as ttk
from tkinter.ttk import Separator, Style
import urllib.request
import os
import webbrowser
from PIL import Image, ImageTk
import time
import pywebview


# Create the main window
window = tk.Tk()
window.title("Wget Downloader v1.3")
window.iconbitmap("G:\Software\py\Python Creations\Completed\Projects\Wget Downloader\Version 1.2\wget logo 1.ico")  # Set the path to your icon file

# Add an image label at the top center
# Replace with the actual path to your image file
image_path = "G:\Software\py\Python Creations\Completed\Projects\Wget Downloader\Images\wget cover 1.png"
image = Image.open(image_path)

# Replace width and height with your desired dimensions
image = image.resize((130, 120))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=image)
image_label.pack(pady=(15, 0))


# Function to handle the "Paste URL" button
def paste_url():
    url_entry.delete(0, tk.END)
    url_entry.insert(tk.END, window.clipboard_get())


# Function to handle the browse button
def select_output_dir():
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(tk.END, output_dir)
    # Set the current working directory to the selected output directory
    os.chdir(output_dir)


# Function to handle the download process
def download_files():
    urls = url_entry.get().split("\n")
    output_dir = output_dir_entry.get()
    if urls and output_dir:
        for url in urls:
            if url:
                try:
                    file_name = os.path.basename(url)
                    file_path = os.path.join(output_dir, file_name)
                    status_widget.update_status(f"Downloading: {file_name}...")
                    urllib.request.urlretrieve(url, file_path, reporthook=download_progress)
                    update_status(f"Downloaded: {file_name}")
                except Exception as e:
                    update_status(f"Error occurred during download: {str(e)}")
        show_completion_popup()
    else:
        update_status("Please enter a valid URL and output directory.")


# Callback function to update the download progress
def download_progress(count, block_size, total_size):
    percentage = int(count * block_size * 100 / total_size)
    status_widget.update_progress(percentage)
    window.update()


# Function to update the status label
def update_status(text):
    status_widget.update_status(text)


# Function to display a pop-up window for completion status
def show_completion_popup():
    messagebox.showinfo("Download Complete", "All files have been downloaded successfully.")


# Function to handle the "About" menu item
def show_about():
    messagebox.showinfo("About", "Wget Downloader\nVersion 1.3\n\nCreated by pudsz\n\n... TTIOT ...")


# Function to handle the "How to use" menu item
def show_usage():
    messagebox.showinfo("How to use", "1. Enter the URL of the file to download.\n2. Select the output directory.\n3. Click on the 'Download' button to start the download.\n\nNote: For detailed instructions on how to use please open the 'Help File'")


# Function to handle the "Help File" menu item
def open_help_file():
    # Replace with the actual path to your help file
    help_file_path = "G:\Software\py\Python Creations\Completed\Projects\Wget Downloader\Version 1.2\Wget Help File.pdf"
    webbrowser.open(help_file_path)


# Function to handle the "Exit" menu item
def exit_app():
    window.destroy()

# Create the menu bar
menu_bar = tk.Menu(window)

# Create the "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_app)

# Create the "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
help_menu.add_command(label="How to use", command=show_usage)
help_menu.add_command(label="Help File", command=open_help_file)

# Add the menus to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Set the menu bar
window.config(menu=menu_bar)


# Custom widget to display status and progress
class StatusWidget(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.status_label = tk.Label(self, text="", font=("Tahoma", 11))
        self.progress_bar = ttk.Progressbar(self, mode="determinate")
        self.status_label.pack(pady=(10, 0))
        self.progress_bar.pack(fill="x", padx=10)

    def update_status(self, text):
        self.status_label.config(text=text)
        self.update()

    def update_progress(self, value):
        self.progress_bar["value"] = value
        self.update()


# Create the status widget
status_widget = StatusWidget(window)
status_widget.pack(pady=(15, 10))


# Add a label and entry for URL input
url_label = tk.Label(
    window,
    text="URL:",
    bg="#80b3ff",
    font=("Tahoma", 11),
)
url_label.pack(pady=(0, 5))

url_entry = scrolledtext.ScrolledText(
    window,
    width=50,
    height=4,
    font=("Tahoma", 11),
)
url_entry.pack(pady=(0, 10))


# Add a label and entry for output directory selection
output_dir_label = tk.Label(
    window,
    text="Output Directory:",
    bg="#80b3ff",
    font=("Tahoma", 11),
)
output_dir_label.pack(pady=(0, 5))

output_dir_entry = tk.Entry(
    window,
    width=50,
    font=("Tahoma", 11),
)
output_dir_entry.pack(pady=(0, 10))


# Add buttons for "Paste URL", "Browse", and "Download"
button_frame = tk.Frame(window)
button_frame.pack(pady=(0, 10))

paste_url_button = tk.Button(
    button_frame,
    text="Paste URL",
    bg="#FF4D4D",
    fg="#FFFFFF",
    justify="center",
    font=("Tahoma", 11),
    command=paste_url,
)
paste_url_button.pack(side="left", padx=(0, 5))

browse_button = tk.Button(
    button_frame,
    text="Browse",
    bg="#FF4D4D",
    fg="#FFFFFF",
    justify="center",
    font=("Tahoma", 11),
    command=select_output_dir,
)
browse_button.pack(side="left", padx=(0, 5))

download_button = tk.Button(
    button_frame,
    text="Download",
    bg="#FF4D4D",
    fg="#FFFFFF",
    justify="center",
    font=("Tahoma", 11),
    command=download_files,
)
download_button.pack(side="left")


# Add a separator
separator = Separator(window, orient="horizontal")
separator.pack(fill="x", pady=(15, 10))

# Function to open the URL in a webview window
def open_url():
    url = "https://pudszttiot.blogspot.com/"

    # Open the URL in a webview window
    webview = pywebview.create_window("Web View", url)
    pywebview.start()


# Add a button to open URL using pywebview
open_url_button = tk.Button(
    window,
    text="Open URL",
    bg="#FF4D4D",
    fg="#FFFFFF",
    justify="center",
    font=("Tahoma", 11),
    command=open_url,
)
open_url_button.pack()


# Run the Tkinter event loop
window.mainloop()
