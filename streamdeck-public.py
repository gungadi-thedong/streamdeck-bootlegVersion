import tkinter as tk
from tkinter import ttk
import serial
import json
import os
import pyautogui
import webbrowser
from pygame import mixer

# =====================================================================
# 1. LOCAL SONG PATHS (PLACEHOLDERS FOR GITHUB)
# =====================================================================
# Change these paths to your own local .mp3 files
LAGU_BG_1 = r"C:\path\to\your\background_song1.mp3"
LAGU_BG_2 = r"C:\path\to\your\background_song2.mp3"
LAGU_BG_3 = r"C:\path\to\your\background_song3.mp3"
LAGU_BG_4 = r"C:\path\to\your\background_song4.mp3"

LAGU_GROOVE_1 = r"C:\path\to\your\groove_song1.mp3"
LAGU_GROOVE_2 = r"C:\path\to\your\groove_song2.mp3"
LAGU_GROOVE_3 = r"C:\path\to\your\groove_song3.mp3"
LAGU_GROOVE_4 = r"C:\path\to\your\groove_song4.mp3"

# Initialize Audio Player
mixer.init()

# =====================================================================
# 2. HARDCODED ACTIONS LIST (UI DROPDOWN MENU)
# =====================================================================
DAFTAR_AKSI = {
    "Kosong": "NONE",
    # --- Local Music ---
    "Play BG: Song 1": "BG_1",
    "Play BG: Song 2": "BG_2",
    "Play BG: Song 3": "BG_3",
    "Play BG: Song 4": "BG_4",
    "Open Groove: Song 1": "GRV_1",
    "Open Groove: Song 2": "GRV_2",
    "Open Groove: Song 3": "GRV_3",
    "Open Groove: Song 4": "GRV_4",
    "STOP ALL BG MUSIC": "STOP_BG",
    # --- Shortcuts ---
    "Copy (Ctrl + C)": "CTRL_C",
    "Paste (Ctrl + V)": "CTRL_V",
    "Bold (Ctrl + B)": "CTRL_B",
    "Italic (Ctrl + I)": "CTRL_I",
    "Underline (Ctrl + U)": "CTRL_U",
    "Undo (Ctrl + Z)": "UNDO",
    "Redo (Ctrl + Y)": "REDO",
    # --- Media Controls ---
    "Play / Pause": "PLAY_PAUSE",
    "Back (Prev Track)": "TRACK_PREV",
    "Next Track": "TRACK_NEXT",
    "Volume Up": "VOL_UP",
    "Volume Down": "VOL_DOWN",
    "Mute Audio": "VOL_MUTE",
    # --- Open System Apps ---
    "Open Groove Music": "APP_GROOVE",
    "Open Notepad": "APP_NOTEPAD",
    "Open Calculator": "APP_CALCULATOR",
    "Open Task Manager": "APP_TASKMGR",
    "Open Chrome": "APP_CHROME"
}

def eksekusi_aksi(id_aksi):
    try:
        # --- BACKGROUND AUDIO LOGIC ---
        if id_aksi == "BG_1" and os.path.exists(LAGU_BG_1):
            mixer.music.load(LAGU_BG_1); mixer.music.play()
        elif id_aksi == "BG_2" and os.path.exists(LAGU_BG_2):
            mixer.music.load(LAGU_BG_2); mixer.music.play()
        elif id_aksi == "BG_3" and os.path.exists(LAGU_BG_3):
            mixer.music.load(LAGU_BG_3); mixer.music.play()
        elif id_aksi == "BG_4" and os.path.exists(LAGU_BG_4):
            mixer.music.load(LAGU_BG_4); mixer.music.play()
        elif id_aksi == "STOP_BG":
            mixer.music.stop()

        # --- GROOVE PLAYER AUDIO LOGIC ---
        elif id_aksi == "GRV_1" and os.path.exists(LAGU_GROOVE_1):
            os.startfile(LAGU_GROOVE_1)
        elif id_aksi == "GRV_2" and os.path.exists(LAGU_GROOVE_2):
            os.startfile(LAGU_GROOVE_2)
        elif id_aksi == "GRV_3" and os.path.exists(LAGU_GROOVE_3):
            os.startfile(LAGU_GROOVE_3)
        elif id_aksi == "GRV_4" and os.path.exists(LAGU_GROOVE_4):
            os.startfile(LAGU_GROOVE_4)

        # --- SHORTCUTS LOGIC ---
        elif id_aksi == "CTRL_C": pyautogui.hotkey('ctrl', 'c')
        elif id_aksi == "CTRL_V": pyautogui.hotkey('ctrl', 'v')
        elif id_aksi == "CTRL_B": pyautogui.hotkey('ctrl', 'b')
        elif id_aksi == "CTRL_I": pyautogui.hotkey('ctrl', 'i')
        elif id_aksi == "CTRL_U": pyautogui.hotkey('ctrl', 'u')
        elif id_aksi == "UNDO": pyautogui.hotkey('ctrl', 'z')
        elif id_aksi == "REDO": pyautogui.hotkey('ctrl', 'y')

        # --- MEDIA CONTROLS LOGIC ---
        elif id_aksi == "PLAY_PAUSE": pyautogui.press('playpause')
        elif id_aksi == "TRACK_PREV": pyautogui.press('prevtrack')
        elif id_aksi == "TRACK_NEXT": pyautogui.press('nexttrack')
        elif id_aksi == "VOL_UP": pyautogui.press('volumeup')
        elif id_aksi == "VOL_DOWN": pyautogui.press('volumedown')
        elif id_aksi == "VOL_MUTE": pyautogui.press('volumemute')
        
        # --- APPS LOGIC ---
        elif id_aksi == "APP_GROOVE":
            os.startfile("mswindowsmusic:")
        elif id_aksi == "APP_NOTEPAD":
            os.startfile("notepad.exe")
        elif id_aksi == "APP_CALCULATOR":
            os.startfile("calc.exe")
        elif id_aksi == "APP_TASKMGR":
            os.startfile("taskmgr.exe")
        elif id_aksi == "APP_CHROME":
            try:
                os.startfile("chrome.exe")
            except Exception:
                os.system("start chrome")
        
        else:
            print(f"Action empty or file not found: {id_aksi}")
    except Exception as e:
        print(f"[ERROR] Failed to execute action {id_aksi}: {e}")

# =====================================================================
# 3. SERIAL CONNECTION & CONFIG JSON
# =====================================================================
CONFIG_FILE = "deck_config.json"
LIST_TOMBOL = ["KEY_4", "KEY_5", "KEY_6", "KEY_B", "KEY_7", "KEY_8", "KEY_9", "KEY_C", "KEY_*", "KEY_0", "KEY_#", "KEY_D"]

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as f:
        mapping_tombol = json.load(f)
else:
    mapping_tombol = {tombol: "Kosong" for tombol in LIST_TOMBOL}

# CHANGE 'COM5' TO MATCH YOUR OWN ESP32 PORT
try:
    ser = serial.Serial('COM5', 115200, timeout=0.1)
    print("Connected to ESP32 Successfully!")
except Exception as e:
    print("Warning: ESP32 Not Detected. UI opened for configuration mode.")
    ser = None

# =====================================================================
# 4. GUI IMPLEMENTATION (Tkinter Dark Mode)
# =====================================================================
root = tk.Tk()
root.title("Bootleg Stream Deck Controller")
root.geometry("980x640")
root.configure(bg="#181825")
root.resizable(False, False)  # Lock size so it won't break on full screen

style = ttk.Style()
style.theme_use('clam')

# Dark theme styling config
style.configure('TCombobox',
                fieldbackground='#313244',
                background='#45475a',
                foreground='#cdd6f4',
                arrowcolor='#cdd6f4')
style.map('TCombobox', fieldbackground=[('readonly', '#313244')])

root.option_add('*TCombobox*Listbox.background', '#313244')
root.option_add('*TCombobox*Listbox.foreground', '#cdd6f4')
root.option_add('*TCombobox*Listbox.selectBackground', '#89b4fa')
root.option_add('*TCombobox*Listbox.selectForeground', '#11111b')
root.option_add('*TCombobox*Listbox.font', ('Segoe UI', 10))

title_frame = tk.Frame(root, bg="#181825")
title_frame.pack(pady=(20, 10), fill=tk.X)

lbl_title = tk.Label(title_frame, text="🤖 BOOTLEG STREAM DECK CONTROLLER", 
                     bg="#181825", fg="#89b4fa", font=("Segoe UI", 16, "bold"))
lbl_title.pack()

status_text = "🟢 ESP32: Connected on COM5" if ser and ser.is_open else "🔴 ESP32: Disconnected (COM5)"
status_color = "#a6e3a1" if ser and ser.is_open else "#f38ba8"
lbl_status = tk.Label(title_frame, text=status_text, bg="#181825", fg=status_color, font=("Segoe UI", 10, "bold"))
lbl_status.pack(pady=(5, 0))

frame_grid = tk.Frame(root, bg="#181825")
frame_grid.pack(pady=10)

dropdown_objects = {}

for index, tombol in enumerate(LIST_TOMBOL):
    r = index // 4
    c = index % 4
    
    card_frame = tk.Frame(frame_grid, bg="#1e1e2e", bd=1, relief=tk.FLAT, padx=10, pady=10)
    card_frame.grid(row=r, column=c, padx=10, pady=10)
    
    lbl_key = tk.Label(card_frame, text=tombol, bg="#1e1e2e", fg="#cba6f7", font=("Segoe UI", 10, "bold"))
    lbl_key.pack(anchor="w", pady=(0, 5))
    
    cb = ttk.Combobox(card_frame, values=list(DAFTAR_AKSI.keys()), width=24, state="readonly", font=("Segoe UI", 10))
    cb.set(mapping_tombol.get(tombol, "Kosong"))
    cb.pack()
    
    dropdown_objects[tombol] = cb

lbl_save_status = tk.Label(root, text="", bg="#181825", fg="#a6e3a1", font=("Segoe UI", 11, "bold"))
lbl_save_status.pack(pady=(5, 5))

def simpan_konfigurasi():
    global mapping_tombol
    for tombol in LIST_TOMBOL:
        mapping_tombol[tombol] = dropdown_objects[tombol].get()
    with open(CONFIG_FILE, "w") as f:
        json.dump(mapping_tombol, f)
    print("Configuration saved to deck_config.json!")
    
    lbl_save_status.config(text="✓ Settings saved and applied successfully!")
    root.after(3000, lambda: lbl_save_status.config(text=""))

btn_save = tk.Button(root, text="APPLY & SAVE CHANGES", command=simpan_konfigurasi, 
                     bg="#a6e3a1", fg="#11111b", activebackground="#94e2d5", activeforeground="#11111b",
                     font=("Segoe UI", 12, "bold"), relief=tk.FLAT, bd=0, cursor="hand2", pady=10)
btn_save.pack(fill=tk.X, padx=30, pady=(5, 20))

def on_enter(e):
    btn_save.config(bg="#94e2d5")
def on_leave(e):
    btn_save.config(bg="#a6e3a1")

btn_save.bind("<Enter>", on_enter)
btn_save.bind("<Leave>", on_leave)

# =====================================================================
# 5. BACKGROUND SERIAL LISTENER
# =====================================================================
def baca_serial_usb():
    if ser and ser.is_open:
        try:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8', errors='ignore').strip()
                if data in mapping_tombol:
                    aksi_terpilih = mapping_tombol[data]
                    id_aksi = DAFTAR_AKSI.get(aksi_terpilih)
                    print(f"ESP32 Pressed: {data} -> Executing: {aksi_terpilih}")
                    eksekusi_aksi(id_aksi)
        except Exception as e:
            print(f"[ERROR] Serial read failed: {e}")
    root.after(50, baca_serial_usb)

root.after(50, baca_serial_usb)
root.mainloop()