import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import tkinter.ttk as ttk
from tkinter.ttk import Separator
import urllib.request
import os
import webbrowser
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Wget Downloader")
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


def download_file():
    url = url_entry.get()
    output_dir = output_dir_entry.get()
    if url:
        try:
            file_name = os.path.basename(url)
            file_path = os.path.join(output_dir, file_name)
            # Disable the download button during the download
            download_button.config(state=tk.DISABLED)
            status_widget.update_status("Downloading...")
            urllib.request.urlretrieve(url, file_path, reporthook=download_progress)
            update_status("Download completed.")
            show_completion_popup()
        except Exception as e:
            update_status(f"Error occurred during download: {str(e)}")
        finally:
            # Enable the download button after the download
            download_button.config(state=tk.NORMAL)
            status_widget.update_status("Ready")
    else:
        update_status("Please enter a valid URL.")


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
    messagebox.showinfo(
        "Download Complete", "The download has been completed successfully."
    )


# Function to handle the "About" menu item


def show_about():
    messagebox.showinfo(
        "About", "Wget Downloader\nVersion 1.2\n\nCreated by pudsz\n\n... TTIOT ..."
    )


# Function to handle the "How to use" menu item


def show_usage():
    messagebox.showinfo(
        "How to use",
        "1. Enter the URL of the file to download.\n2. Select the output directory.\n3. Click on the 'Download' button to start the download.\n\nNote: For detailed instructions on how to use please open the 'Help File'",
    )


# Function to open the help file documentation


def open_help_file():
    # Replace with the actual path to your help file
    help_file_path = r"G:\Software\py\Python Creations\Completed\Projects\Wget Downloader\Docs\readme.txt"
    webbrowser.open(help_file_path)


# Function to open the release notes file documentation


def open_release_notes_file():
    # Replace with the actual path to your release notes file
    release_notes_file_path = "G:\Software\py\Python Creations\Completed\Projects\Wget Downloader\Version 1.2\Release Notes Version 1.2.txt"
    webbrowser.open(release_notes_file_path)


# Function to exit the program


def exit_application():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        window.destroy()


# Function to handle the "Check Version" command


def check_version():
    messagebox.showinfo("Version", "Wget Downloader v1.2")


# Create the menu bar
menu_bar = tk.Menu(window)

# Create the "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_application)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create the "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="How to use", command=show_usage)
# Command to open the local help file
help_menu.add_command(label="Help File...", command=open_help_file)
help_menu.add_separator()  # Add a separator
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Create the "Version" submenu
version_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Version", menu=version_menu)
version_menu.add_command(
    label="Check Version", command=check_version
)  # Add your command here
version_menu.add_command(label="Release Notes...", command=open_release_notes_file)
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
# Adjust the width and height as desired
paste_button.config(width=9, height=0)
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
# Adjust the width and height as desired
browse_button.config(width=9, height=0)
browse_button.pack(expand=True, pady=(4, 10))

# Add a separator line
separator = Separator(window, orient=tk.HORIZONTAL)
separator.pack(fill=tk.X, padx=(10))

# Add a button to start the download
download_button = tk.Button(
    window,
    text="Download",
    bg="#8D80FF",
    fg="#F2F7FF",
    justify="center",
    font=("Closeness Regular", 19),
    command=download_file,
)
# Adjust the width and height as desired
download_button.config(width=12, height=1)
download_button.pack(pady=(10, 1))

# Create a custom widget that combines the status label and progress bar


class StatusLabelWithProgressBar(tk.LabelFrame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.status_label = tk.Label(
            self,
            text="Ready",
            bg="#E7E9EA",
            fg="#20211A",
            justify="center",
            font=("Tahoma", 11),
        )
        self.status_label.pack(fill="both", expand=True, pady=(4, 0))
        self.progress_frame = tk.Frame(self, bg="#E7E9EA")
        self.progress_bar = ttk.Progressbar(
            self.progress_frame, orient=tk.HORIZONTAL, length=200, mode="determinate"
        )
        self.progress_label = tk.Label(
            self.progress_frame, text="0%", bg="#E7E9EA", fg="#20211A"
        )
        self.progress_label.pack(side=tk.RIGHT)
        self.progress_bar.pack(fill="both", expand=True, pady=(0, 4))
        self.progress_frame.pack(fill="both", expand=True)

    def update_status(self, text):
        self.status_label.config(text=text)

    def update_progress(self, value):
        self.progress_bar["value"] = value
        self.progress_label.config(text=f"{int(value)}%")


# Add the custom status label with progress bar
status_widget = StatusLabelWithProgressBar(window, text="Status")
status_widget.pack(fill="both", expand=True, pady=(5, 20))

# Watermark label
watermark_label = tk.Label(
    window, text="pudszTTIOT", font=("Corbel", 9), bg="#2A292B", fg="#46F953"
)
watermark_label.place(relx=1.0, rely=1.0, anchor="se", x=0, y=0)

# Calculate the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the window position
window_width = window.winfo_width()
window_height = window.winfo_height()
x = screen_width // 3 - window_width // 4
y = screen_height // 24 - window_height // -3

# Set the window position
window.geometry(f"+{x}+{y}")

# Background color
window.configure(bg="#80b3ff")

# Run the main event loop
window.mainloop()
