import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox

#choose file(s)
def select_files():
    file_paths = filedialog.askopenfilenames(title="Choose file(s) to rename", filetypes=(("All Files", "*.*"),))
    print(file_paths)
    return file_paths

def select_output_directory():
    output_directory = filedialog.askdirectory(title="renaming file output path(s)")
    return output_directory

def remove_string_and_save(files, output_dir, remove_str):
    for file in files:
        dir_name, file_name = os.path.split(file)
        new_file_name = file_name.replace(remove_str, '')
        new_file_path = os.path.join(output_dir, new_file_name)
        
        try:
            with open(file, 'rb') as f_src:
                with open(new_file_path, 'wb') as f_dst:
                    f_dst.write(f_src.read())
            print(f"file saved in: {new_file_path} !")
        except Exception as e:
            tkinter.messagebox.showerror("Unexpected Error",f"Error while saving files, quit with: {e}")

def main():
    root = tk.Tk()
    root.title("RCSF v1.0.0")

    root.geometry("400x200")
    label = tk.Label(root, text="Welcome RCSF:Replacing Certain String in Filename")
    label.pack(pady=10)

    label = tk.Label(root, text="Type Replacing String")
    label.pack(pady=10)


    remove_entry = tk.Entry(root, width=50)
    remove_entry.pack(pady=10)

    label = tk.Label(root, text="@0x14C6")
    label.pack(side="right")

    def process_files():
        remove_str = remove_entry.get()
        
        if not remove_str:
            tkinter.messagebox.showerror("Unexpected Error","Empty Replacing String!")
            return
        files = select_files()
        if not files:
            tkinter.messagebox.showerror("Unexpected Error","No Selected Files")
            return
        output_dir = select_output_directory()
        if not output_dir:
            tkinter.messagebox.showerror("Unexpected Error","Invaild Paths")
            return
        remove_string_and_save(files, output_dir, remove_str)
    
    process_button = tk.Button(root, text="Start", command=process_files)
    process_button.pack(pady=20)
    
    root.mainloop()

main()
