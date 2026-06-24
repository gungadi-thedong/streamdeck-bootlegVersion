# 🤖 Bootleg Stream Deck (Wired ESP32 Controller)

Project kustomisasi tombol macro makro menggunakan hardware **ESP32** dan matriks **Keypad 4x4** jalur kabel (wired USB). Dilengkapi dengan aplikasi controller desktop berbasis Python (Tkinter GUI) bertema gelap modern (*Catppuccin-inspired*).

User bisa melakukan kustomisasi fungsi setiap tombol secara *real-time* lewat UI tanpa perlu *hardcoding* ulang di mikrokontroler.

---

## 🛠️ Persiapan Hardware & Library

### 1. Sisi Mikrokontroler (Arduino IDE)
Sebelum melakukan *flashing* ke ESP32, pastikan software **Arduino IDE** Anda sudah menyiapkan dependensi berikut:
* **ESP32 Board Core:** Sudah ter-install via Board Manager.
* **Keypad Library:** Cari dan install library **Keypad** oleh *Mark Stanley & Alexander Brevig* melalui Library Manager.
* *Catatan:* Library `EEPROM.h` sudah termasuk sebagai library bawaan di dalam core ESP32, tidak perlu install manual.

#### Cara Flash ESP32:
1. Hubungkan ESP32 ke PC menggunakan kabel data USB.
2. Buka berkas kode Arduino (`.ino`) di Arduino IDE.
3. Pastikan pin GPIO pada kode sudah sesuai dengan jalur kabel keypad fisik Anda.
4. Pilih Board (misal: *DOIT ESP32 DEVKIT V1*) dan Port COM yang sesuai.
5. Lakukan **Upload**. Untuk kestabilan koneksi beberapa modul chip, turunkan *Upload Speed* ke `115200` atau `9600` jika terjadi kendala *timeout*.

---

## 💻 Sisi PC (Setup Python App)

### 2. Instalasi Dependensi Software
Pastikan PC Anda sudah memiliki **Python 3.10+**. Buka Terminal/CMD di dalam direktori project ini, lalu jalankan perintah otomatis berikut untuk mengunduh semua library yang diperlukan:

```bash
pip install -r requirements.txt

English : 
# 🤖 Bootleg Stream Deck (Wired ESP32 Controller)

A highly customizable, budget-friendly DIY macro pad project powered by an **ESP32** and a **4x4 Keypad Matrix** via a stable, wired USB connection. 

This project features a modern, Catppuccin-inspired dark mode desktop controller app built with Python (Tkinter GUI). It allows users to rebind and customize actions for all 12 active keys in **real-time** directly from the UI, completely eliminating the need to re-flash the microcontroller every time you want to change a shortcut.

---

## 🛠️ Hardware & Library Setup

### 1. Microcontroller Side (Arduino IDE)
Before flashing the firmware to your ESP32, ensure your **Arduino IDE** is configured with the following dependencies:
* **ESP32 Board Core:** Installed via the Additional Boards Manager.
* **Keypad Library:** Search for and install the **Keypad** library by *Mark Stanley & Alexander Brevig* via the Library Manager.
* *Note:* The `EEPROM.h` library comes pre-bundled with the ESP32 core, so no manual installation is required.

#### How to Flash the ESP32:
1. Connect your ESP32 to your PC using a high-quality USB data cable.
2. Open the provided firmware file (`.ino`) in Arduino IDE.
3. Double-check the GPIO pin definitions in the code to ensure they match your physical keypad wiring layout.
4. Select your specific ESP32 board type (e.g., *DOIT ESP32 DEVKIT V1*) and the correct COM Port.
5. Click **Upload**. *(If you experience connection timeouts during flashing, try lowering the Upload Speed to `115200`).*

---

## 💻 PC Side (Python Desktop App Setup)

### 2. Installing Software Dependencies
Make sure you have **Python 3.10+** installed on your system. Open your Terminal or Command Prompt (CMD) inside the project directory and run the following command to install all necessary packages automatically:

```bash
pip install -r requirements.txt