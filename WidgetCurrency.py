import tkinter as tk
import requests
from bs4 import BeautifulSoup
import threading
import time
import os
import sys
import PyInstaller.__main__

class DovizWidget:
    def __init__(self, master):
        self.master = master
        master.title("Döviz Kurları")
        master.geometry("300x150")
        master.resizable(False, False)
        
        self.dolar_label = tk.Label(master, text="Dolar: Yükleniyor...", font=("Consolas", 18))
        self.dolar_label.pack(pady=10)
        
        self.euro_label = tk.Label(master, text="Euro: Yükleniyor...", font=("Consolas", 18))
        self.euro_label.pack(pady=10)
        
        self.guncelleme_label = tk.Label(master, text="Son Güncelleme: -", font=("Consolas", 14))
        self.guncelleme_label.pack(pady=10)
        
        self.guncelle()
        
        threading.Thread(target=self.otomatik_guncelle, daemon=True).start()


    
    def guncelle(self):
        try:
            url = "https://www.doviz.com/"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            dolar = soup.find("span", {"data-socket-key": "USD"}).text
            euro = soup.find("span", {"data-socket-key": "EUR"}).text
            
            self.dolar_label.config(text=f"Dolar: {dolar} TL")
            self.euro_label.config(text=f"Euro: {euro} TL")
            
            simdi = time.strftime("%H:%M:%S")
            self.guncelleme_label.config(text=f"Son Güncelleme: {simdi}")
        except Exception as e:
            print(f"Hata oluştu: {e}")
    
    def otomatik_guncelle(self):
        while True:
            time.sleep(60)
            self.guncelle()

def exe_olustur():
    PyInstaller.__main__.run([
        'atis.py',
        '--onefile',
        '--windowed',
        '--name=DovizWidget',
    ])

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--build":
        exe_olustur()
    else:
        root = tk.Tk()
        widget = DovizWidget(root)
        root.mainloop()
