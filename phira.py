import requests
from rich.text import Text, Style
from rich.console import Console
from rich.table import Table
from rich.json import JSON
import json
import os
import re
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import subprocess
import requests
import io
import pyfiglet
import datetime

def get_phira_chart_data(page=1):
    url = f"https://api.phira.cn/chart/?page={page}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{Back.RED}An error occurred while retrieving data: {e}")
        print_logo()
        return

def display_chart_page(page=1):
    os.system("cls" if os.name == "nt" else "clear")
    print_logo()

    data = get_phira_chart_data(page=page)
    if data:
        update_links(data)
        display_data(data)

    while True:
        print()
        print(f"{Style.BRIGHT}──────────────────────────────────")
        print(f"{Style.BRIGHT}1.{Fore.GREEN} Next")
        print(f"{Style.BRIGHT}2.{Fore.CYAN} Previous")
        print(f"{Style.BRIGHT}3.{Fore.RED} Back")
        print(f"{Style.BRIGHT}──────────────────────────────────")
        print()
        navigation = input("Choose: ").strip().lower()
        if navigation == "1":
            if page < 34:
                pass
                display_chart_page(page + 1)
            else:
                print(f"{Back.CYAN}Already on the last page.")
        elif navigation == "2":
            if page > 1:
                pass
                display_chart_page(page - 1)
            else:
                print(f"{Back.CYAN}Already on the first page.")
        elif navigation == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print_logo()
            print_info()
            return
        else:
            print(f"{Back.RED}Invalid input. Please enter '1', '2', or '3'.")
    else:
        print(f"{Back.RED}No chart data.")
        os.system("cls" if os.name == "nt" else "clear")
        print_logo()
        print_info()
        
def get_phira_troll_chart_data(page=1):
    url = f"https://api.phira.cn/chart/?page={page}&division=troll"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{Back.RED}An error occurred while retrieving data: {e}")
        print_logo()
        return

def display_troll_chart_page(page=1):
    os.system("cls" if os.name == "nt" else "clear")
    print_logo()

    data = get_phira_troll_chart_data(page=page)
    if data:
        update_links(data)
        display_data(data)

    while True:
        print()
        print(f"{Style.BRIGHT}──────────────────────────────────")
        print(f"{Style.BRIGHT}1.{Fore.GREEN} Next")
        print(f"{Style.BRIGHT}2.{Fore.CYAN} Previous")
        print(f"{Style.BRIGHT}3.{Fore.RED} Back")
        print(f"{Style.BRIGHT}──────────────────────────────────")
        print()
        navigation = input("Choose: ").strip().lower()
        if navigation == "1":
            if page < 14:
                pass
                display_troll_chart_page(page + 1)
            else:
                print(f"{Back.CYAN}Already on the last page.")
        elif navigation == "2":
            if page > 1:
                pass
                display_troll_chart_page(page - 1)
            else:
                print(f"{Back.CYAN}Already on the first page.")
        elif navigation == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print_logo()
            print_info()
            return
        else:
            print(f"{Back.RED}Invalid input. Please enter '1', '2', or '3'.")
    else:
        print(f"{Back.RED}No chart data.")
        os.system("cls" if os.name == "nt" else "clear")
        print_logo()
        print_info()
        
def get_phira_plain_chart_data(page=1):
    url = f"https://api.phira.cn/chart/?page={page}&division=plain"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{Back.RED}An error occurred while retrieving data: {e}")
        print_logo()
        return

def display_plain_chart_page(page=1):
    os.system("cls" if os.name == "nt" else "clear")
    print_logo()

    data = get_phira_plain_chart_data(page=page)
    if data:
        update_links(data)
        display_data(data)

    while True:
        print()
        print(f"{Style.BRIGHT}──────────────────────────────────")
        print(f"{Style.BRIGHT}1.{Fore.GREEN} Next")
        print(f"{Style.BRIGHT}2.{Fore.CYAN} Previous")
        print(f"{Style.BRIGHT}3.{Fore.RED} Back")
        print(f"{Style.BRIGHT}──────────────────────────────────")
        print()
        navigation = input("Choose: ").strip().lower()
        if navigation == "1":
            if page < 34:
                pass
                display_plain_chart_page(page + 1)
            else:
                print(f"{Back.CYAN}Already on the last page.")
        elif navigation == "2":
            if page > 1:
                pass
                display_plain_chart_page(page - 1)
            else:
                print(f"{Back.CYAN}Already on the first page.")
        elif navigation == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print_logo()
            print_info()
            return
        else:
            print(f"{Back.RED}Invalid input. Please enter '1', '2', or '3'.")
    else:
        print(f"{Back.RED}No chart data.")
        os.system("cls" if os.name == "nt" else "clear")
        print_logo()
        print_info()
        
def get_phira_visual_chart_data(page=1):
    url = f"https://api.phira.cn/chart/?page={page}&division=visual"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{Back.RED}An error occurred while retrieving data: {e}")
        print_logo()
        return

def display_visual_chart_page(page=1):
    os.system("cls" if os.name == "nt" else "clear")
    print_logo()

    data = get_phira_visual_chart_data(page=page)
    if data:
        update_links(data)
        display_data(data)

    while True:
        print()
        print(f"{Style.BRIGHT}──────────────────────────────────")
        print(f"{Style.BRIGHT}1.{Fore.GREEN} Next")
        print(f"{Style.BRIGHT}2.{Fore.CYAN} Previous")
        print(f"{Style.BRIGHT}3.{Fore.RED} Back")
        print(f"{Style.BRIGHT}──────────────────────────────────")
        print()
        navigation = input("Choose: ").strip().lower()
        if navigation == "1":
            if page < 3:
                display_visual_chart_page(page + 1)
            else:
                print(f"{Back.CYAN}Already on the last page.")
        elif navigation == "2":
            if page > 1:
                pass
                display_visual_chart_page(page - 1)
            else:
                print(f"{Back.CYAN}Already on the first page.")
        elif navigation == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print_logo()
            print_info()
            return
        else:
            print(f"{Back.RED}Invalid input. Please enter '1', '2', or '3'.")
    else:
        print(f"{Back.RED}No chart data.")
        os.system("cls" if os.name == "nt" else "clear")
        print_logo()
        print_info()

def update_links(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str) and "https://api.phira.cn/files" in value:
                data[key] = value.replace("https://api.phira.cn/files", "https://files-cf.phira.cn")
            elif isinstance(value, (dict, list)):
                update_links(value)
    elif isinstance(data, list):
        for item in data:
            update_links(item)

def search_chart_by_id():
    os.system("clear")
    print_logo()
    while True:
        print()
        print(f"{Style.BRIGHT}{Fore.WHITE}──────────────────────────────────")
        print(f"    {Style.BRIGHT}Type {Fore.RED}Back {Fore.WHITE}to menu")
        print(f"{Style.BRIGHT}{Fore.WHITE}──────────────────────────────────")
        print()
        chart_id = input(f"{Style.BRIGHT}Enter chart ID: ").strip().lower()
        if chart_id == "back":
            os.system("cls" if os.name == "nt" else "clear")
            print_logo()
            print_info()
            return
        
        url = f"https://api.phira.cn/chart/{chart_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            update_links(data)
            display_data(data)
        except requests.exceptions.RequestException as e:
            print(f"Terjadi kesalahan saat mengambil data: {e}")
            os.system("cls" if os.name == "nt" else "clear")
            print_logo()
            print_info()
            

def search_chart_by_name():
    os.system("clear")
    print_logo()
    while True:
        print()
        print(f"{Style.BRIGHT}{Fore.WHITE}──────────────────────────────────")
        print(f"    {Style.BRIGHT}Type {Fore.RED}Back {Fore.WHITE}to menu")
        print(f"{Style.BRIGHT}{Fore.WHITE}──────────────────────────────────")
        print()
        
        chart_name = input(f"{Style.BRIGHT}Type the chart name: ").strip().lower()
        url = f"https://api.phira.cn/chart?search={chart_name}"
        if chart_name == "back":
            os.system("cls" if os.name == "nt" else "clear")
            print_logo()
            print_info()
            return
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            update_links(data)
            display_data(data)
        except requests.exceptions.RequestException as e:
            print(f"Terjadi kesalahan saat mengambil data: {e}")
            os.system("cls" if os.name == "nt" else "clear")
            print_logo()
            print_info()

def display_data(data, value_color="cyan bold"):
    console = Console()

    if isinstance(data, dict):
        table = Table(title="Phira Chart Data")
        table.add_column("Key", style=f"magenta bold", no_wrap=True)
        table.add_column("Value", style=f"yellow bold")

        for key, value in data.items():
            if isinstance(value, (dict, list)):
                json_str = json.dumps(value, indent=2, ensure_ascii=False)
                table.add_row(str(key), JSON(json_str))
            elif isinstance(value, str) and re.match(r'https?://files-cf.phira.cn', value):
                # Tambahkan warna ke link
                link = Text.from_markup(f"[{value}]{value}", style=f"{value_color}") 
                table.add_row(str(key), link)
            else:
                table.add_row(str(key), str(value))

        console.print(table)
        print(f"{Style.BRIGHT}Copy Link and Paste in Browser to download")

    elif isinstance(data, list):
        for item in data:
            display_data(item)
    else:
        console.print(data)

def print_logo():
    ascii_banner = pyfiglet.Figlet(font='slant')

    ascii_banner_text = ascii_banner.renderText('Phira Chart Downloader')
    blue_ascii_banner_text = Style.BRIGHT + Fore.CYAN + ascii_banner_text
    print(blue_ascii_banner_text)
    
def print_info():
    by = "Twfixz"
    tl = "\033[4m\033[1mhttps://t.me/twfixz\033[0m"
    vr = "0.0.5"
    now = datetime.datetime.now()
    tanggal = now.strftime("%d/%m/%Y")
    waktu = now.strftime("%H:%M:%S")

    print(f"{Style.BRIGHT}                     \033[3mPhira Chart Downloader\033[0m")
    print(f"{Style.BRIGHT}────────────────────────────────────────────────────────────────────")
    print(f"    {Style.BRIGHT}{Fore.MAGENTA}•>    {Fore.CYAN}Creator    {Fore.WHITE}:               {Fore.YELLOW}"+ by)
    print()
    print(f"    {Style.BRIGHT}{Fore.MAGENTA}•>    {Fore.CYAN}Version    {Fore.WHITE}:               {Fore.YELLOW}"+ vr)
    print()
    print(f"    {Style.BRIGHT}{Fore.MAGENTA}•>    {Fore.CYAN}Telegram   {Fore.WHITE}:        {Fore.GREEN}"+ tl)
    print()
    print(f"    {Style.BRIGHT}{Fore.MAGENTA}•>    {Fore.CYAN}Date       {Fore.WHITE}:              {Fore.YELLOW}"+ tanggal)
    print()
    print(f"    {Style.BRIGHT}{Fore.MAGENTA}•>    {Fore.CYAN}Time       {Fore.WHITE}:              {Fore.YELLOW}"+ waktu)            
    print(f"{Style.BRIGHT}────────────────────────────────────────────────────────────────────")

if __name__ == "__main__": 
    os.system("clear")
    print_logo()
    print_info()
    while True:
        print(f"\n{Style.BRIGHT}Main Menu:")
        print()
        print(f"1. {Fore.GREEN}{Style.BRIGHT}Show Reguler Chart Page ")
        print(f"2. {Fore.YELLOW}{Style.BRIGHT}Show Troll Chart Page ")
        print(f"3. {Fore.YELLOW}{Style.BRIGHT}Show Plain Chart Page ")
        print(f"4. {Fore.YELLOW}{Style.BRIGHT}Show Visual Chart Page ")
        print(f"5. {Fore.BLUE}{Style.BRIGHT}Search Chart By ID")
        print(f"6. {Fore.CYAN}{Style.BRIGHT}Search Chart By Name")
        print(f"7. {Fore.RED}{Style.BRIGHT}Exit")
        print()

        choice = input(f"{Style.BRIGHT}Select Menu: ")
        if choice == "1":
            pass
            display_chart_page()
        elif choice == "2":
            pass
            display_troll_chart_page()
        elif choice == "3":
            pass
            display_plain_chart_page()
        elif choice == "4":
            pass
            display_visual_chart_page()
        elif choice == "5":
            pass
            search_chart_by_id()
        elif choice == "6":
            pass
            search_chart_by_name()
        elif choice == "7":
            break
        else:
            print("Invalid selection.")
            os.system("cls" if os.name == "nt" else "clear")
            print_logo()
            print_info()