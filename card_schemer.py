#!/usr/bin/env python3
import sys, shutil, argparse
from time import sleep
import requests
from colorama import init, Fore, Back, Style

init(autoreset=True)

def show_banner():
    width = shutil.get_terminal_size().columns
    big_banner = [
" ██████╗ █████╗ ██████╗ ██████╗     ██╗   ██╗ █████╗ ██╗███╗   ██╗    ",
"██╔════╝██╔══██╗██╔══██╗██╔══██╗    ██║   ██║██╔══██╗██║████╗  ██║    ",
"██║     ███████║██████╔╝██║  ██║    ██║   ██║███████║██║██╔██╗ ██║    ",
"██║     ██╔══██║██╔══██╗██║  ██║    ╚██╗ ██╔╝██╔══██║██║██║╚██╗██║    ",
"╚██████╗██║  ██║██║  ██║██████╔╝     ╚████╔╝ ██║  ██║██║██║ ╚████║    ",
" ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝       ╚═══╝  ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    "
    ]
    colors = [Fore.MAGENTA, Fore.CYAN, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.RED]

    print("\n")
    for i, line in enumerate(big_banner):
        try: print(colors[i % 6] + line.center(width))
        except: print(colors[i % 6] + line)

    title = "  CARD SCHEMER V1.0  "
    box_width = len(title) + 4
    left = max((width - box_width) // 2, 0)
    print("\n" + " " * left + Back.WHITE + Fore.BLACK + title.center(box_width) + Style.RESET_ALL + "\n")

    dev = "⚡ Developed by 777AMANAT ⚡"
    try: print(Fore.WHITE + dev.center(width))
    except: print(Fore.WHITE + dev)
    print("\n")

def clean_card(x): return x.replace(" ", "").replace("-", "").strip()

def luhn_is_valid(num):
    if not num.isdigit() or len(num) < 2: return False
    total = 0
    rev = num[::-1]
    for i, ch in enumerate(rev):
        n = int(ch)
        if i % 2 == 1:
            n *= 2
            if n > 9: n -= 9
        total += n
    return total % 10 == 0

def extract_bin(num, length=6):
    if len(num) < length:
        raise ValueError("Card number too short for BIN.")
    return num[:length]

def fetch_bin_info(b):
    url = f"https://api.juspay.in/cardbins/{b}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()

def pretty(label, val, emoji):
    print(Fore.CYAN + f"{emoji} {label:11}" + Style.RESET_ALL + Fore.YELLOW + f" : {val}")

def process(card):
    c = clean_card(card)
    if not c:
        print(Fore.RED + "❌ Empty input\n"); return
    if not c.isdigit():
        print(Fore.RED + "❌ Digits only\n"); return

    ok = luhn_is_valid(c)
    print("\n📘 Luhn Check:", (Fore.GREEN if ok else Fore.RED) + ("VALID ✓" if ok else "INVALID ✗"))

    try:
        b = extract_bin(c)
        print(Fore.BLUE + "🔢 BIN:", Fore.WHITE + b)
    except Exception as e:
        print(Fore.RED + f"{e}\n"); return

    try:
        j = fetch_bin_info(b)
        BRAND = j.get("card_sub_type", "N/A")
        TYPE = j.get("extended_card_type", "N/A")
        COUNTRY = j.get("country", "N/A")
        BANK = j.get("bank", "N/A")
        SCHEME = j.get("brand", "N/A")

        print("\n" + Fore.MAGENTA + "--- 🔎 BIN DETAILS ---")
        pretty("BRAND", BRAND, "🏷️")
        pretty("TYPE", TYPE, "🔖")
        pretty("COUNTRY", COUNTRY, "🌍")
        pretty("BANK", BANK, "🏦")
        pretty("SCHEME", SCHEME, "🔁")
        print()
    except Exception as e:
        print(Fore.RED + f"Error: {e}\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("card", nargs="?", help="Card number")
    a = parser.parse_args()
    show_banner()
    if a.card: process(a.card)
    else:
        while True:
            try:
                x = input(Fore.WHITE + "💳 Enter card number (or q): ").strip()
            except: sys.exit()
            if x.lower() in ("q","quit","exit"):
                print(Fore.GREEN + "Goodbye ✨"); break
            process(x)
            sleep(0.3)

if __name__ == "__main__": main()
