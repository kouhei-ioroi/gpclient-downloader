import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
import xml.etree.ElementTree as ET
import os
import gettext

BASE_URL = "https://pan-gp-client.s3.amazonaws.com/"

def get_user_language_from_env():
    lang = os.environ.get('LANG', None)
    if lang:
        return lang.split('.')[0]
    return None

def set_language(lang):
    locales_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locales')
    translation = gettext.translation('messages', locales_dir, languages=[lang])
    translation.install()
    return translation.gettext

def fetch_file_list():
    response = requests.get(BASE_URL)
    if response.status_code != 200:
        messagebox.showerror("Error", f"{_("listnotfound")}: {response.status_code}")
        return []

    xml_root = ET.fromstring(response.content)
    contents = xml_root.findall('{http://s3.amazonaws.com/doc/2006-03-01/}Contents')
    
    files = []
    for content in contents:
        key = content.find('{http://s3.amazonaws.com/doc/2006-03-01/}Key').text
        size = int(content.find('{http://s3.amazonaws.com/doc/2006-03-01/}Size').text)
        if not key.endswith('/'):
            files.append((key, size))
    
    return files

def download_file(url, save_path, total_size, progress_callback):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        downloaded = 0
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    progress_callback(downloaded / total_size * 100)
        return True
    else:
        return False

def check_file_exists(url):
    response = requests.head(url)
    return response.status_code == 200

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title(_("title"))

        self.file_label = ttk.Label(self, text=f"{_("fileselect")}:")
        self.file_label.grid(row=0, column=0, padx=5, pady=5)

        self.file_combo = ttk.Combobox(self, width=50)
        self.file_combo.grid(row=0, column=1, padx=5, pady=5)
        self.file_combo.bind("<<ComboboxSelected>>", self.update_size_label)

        self.size_label = ttk.Label(self, text=f"{_("size")}: N/A")
        self.size_label.grid(row=0, column=2, padx=5, pady=5)
        
        self.download_button = ttk.Button(self, text=_("download"), command=self.on_download_button)
        self.download_button.grid(row=1, column=2, padx=5, pady=5, sticky="e")
        
        self.progress_bar = ttk.Progressbar(self, orient="horizontal", mode="determinate")
        self.progress_bar.grid(row=2, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

        self.files = fetch_file_list()
        self.file_combo['values'] = [file[0] for file in self.files]

    def update_size_label(self, event):
        selected_file = self.file_combo.get()
        for file in self.files:
            if file[0] == selected_file:
                size_mb = file[1] / 1024 / 1024
                self.size_label.config(text=f"{_("size")}: {size_mb:.2f} MB")
                break

    def on_download_button(self):
        selected_file = self.file_combo.get()
        if not selected_file:
            messagebox.showerror("Error", _("filenotselect"))
            return

        download_url = BASE_URL + selected_file
        
        if not check_file_exists(download_url):
            messagebox.showerror("Error", _("filenotfound"))
            return

        file_extension = os.path.splitext(selected_file)[1]
        file_types = [(f"{file_extension} files", f"*{file_extension}"), ("All files", "*.*")]

        save_path = filedialog.asksaveasfilename(initialfile=os.path.basename(selected_file), defaultextension=file_extension, filetypes=file_types)
        if not save_path:
            return

        total_size = next(file[1] for file in self.files if file[0] == selected_file)

        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

        def progress_callback(percentage):
            self.progress_bar["value"] = percentage
            self.update_idletasks()

        if download_file(download_url, save_path, total_size, progress_callback):
            messagebox.showinfo("Success", _("downloadfinish"))
            os.startfile(os.path.dirname(save_path))
        else:
            messagebox.showerror("Error", _("downloadfailed"))

if __name__ == "__main__":
    lang = get_user_language_from_env()
    if lang not in ['ja', 'en', 'zh']: 
        lang = 'en' #ja:日本語 en:English zh:Chinese ja_aa:???
    _ = set_language(lang)
    app = App()
    app.mainloop()