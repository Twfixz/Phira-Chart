import requests
from rich.console import Console
from rich.table import Table
from rich.json import JSON
import json
import os
import re

def get_phira_chart_data(page=1):
    """Mengambil data grafik dari API Phira, dengan dukungan halaman."""
    url = f"https://api.phira.cn/chart/?page={page}"
    try:
        response = requests.get(url)
        response.raise_for_status() # Memeriksa status kode respons
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan saat mengambil data: {e}")
        return None

def display_chart_page(page=1):
    """Menampilkan halaman chart dengan pagination."""
    # Clear the screen, but keep the logo
    os.system("cls" if os.name == "nt" else "clear")
    print_logo() # Print the logo again after clearing

    data = get_phira_chart_data(page=page)
    if data:
        display_data(data)

        # Meminta input pengguna untuk navigasi
        navigation = input("Ke halaman (n)ext, (p)revious, atau (q)uit: ").strip().lower()
        if navigation == "n":
            display_chart_page(page + 1)
        elif navigation == "p":
            if page > 1:
                display_chart_page(page - 1)
            else:
                print("Sudah berada di halaman pertama.")
        elif navigation == "q":
            return
        else:
            print("Input tidak valid. Silakan masukkan 'n', 'p', atau 'q'.")
    else:
        print("Tidak ada data chart.")

def search_chart_by_id():
    """Mencari chart berdasarkan ID."""
    os.system("clear")
    print_logo()
    while True:
        chart_id = input("Masukkan ID chart (ketik 'Exit' untuk kembali ke menu): ").strip().lower()
        if chart_id == "exit":
            os.system("cls" if os.name == "nt" else "clear")
            print_logo()
            return # Kembali ke menu utama
        
        url = f"https://api.phira.cn/chart/{chart_id}"
        try:
            response = requests.get(url)
            response.raise_for_status() # Memeriksa status kode respons
            data = response.json()
            display_data(data)
        except requests.exceptions.RequestException as e:
            print(f"Terjadi kesalahan saat mengambil data: {e}")
            os.system("cls" if os.name == "nt" else "clear")
            print_logo()

def display_data(data):
    """Menampilkan data dengan rapi menggunakan rich."""
    console = Console()

    if isinstance(data, dict):
        table = Table(title="Data Grafik Phira")
        table.add_column("Key", style="cyan", no_wrap=True)
        table.add_column("Value", style="cyan") # No link_style here

        for key, value in data.items():
            if isinstance(value, (dict, list)):
                value = JSON(json.dumps(value, indent=2, ensure_ascii=False)).text
            elif isinstance(value, str) and re.match(r'https?://', value): # Mendeteksi tautan
                value = f"[red bold]Link[/]({value})" # Tambahkan gaya link ke text, then create the link
            table.add_row(str(key), str(value))

        console.print(table)

    elif isinstance(data, list):
        for item in data:
            display_data(item)
    else:
        console.print(data)

def print_logo():
    """Menampilkan logo."""
    by = "Twfixz" # Ganti dengan nama creator
    tl = "@Twfixz"

    print()
    print(" \033[1;36m██████  ██   ██ ██ ██████   █████ ")
    print(" \033[1;36m██   ██ ██   ██ ██ ██   ██ ██   ██ ")
    print(" \033[1;36m██████  ███████ ██ ██████  ███████ ")
    print(" \033[1;36m██      ██   ██ ██ ██   ██ ██   ██ ")
    print(" \033[1;36m██      ██   ██ ██ ██   ██ ██   ██ ")
    print(" \033[1;37m──────────────────────────────────")
    print(" \033[1;35m•> \033[1;37mCreator  : \033[1;32m" + by)
    print(" \033[1;35m•> \033[1;37mTelegram : \033[1;32m" + tl)
    print(" \033[1;37m──────────────────────────────────")
    print()

if __name__ == "__main__":
    os.system("clear")
    print_logo() # Print the logo initially
    while True:
        print("\nMenu:")
        print("1. Tampilkan Halaman Chart")
        print("2. Cari Chart Berdasarkan ID")
        print("3. Keluar")

        choice = input("Pilih menu: ")
        if choice == "1":
            display_chart_page()
        elif choice == "2":
            search_chart_by_id()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid.")
