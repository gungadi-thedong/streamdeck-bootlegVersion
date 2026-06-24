#include <Keypad.h>
#include <EEPROM.h>

// Konfigurasi Matriks Keypad 4x4
const byte ROWS = 4; 
const byte COLS = 4; 

// Peta tombol fisik keypad (Skip Baris 1: 1, 2, 3, A karena mati)
char keys[ROWS][COLS] = {
  {'1','2','3','A'}, 
  {'4','5','6','B'}, 
  {'7','8','9','C'}, 
  {'*','0','#','D'}  
};

// Pinout GPIO ESP32 lu
byte rowPins[ROWS] = {19, 18, 5, 17}; 
byte colPins[COLS] = {16, 4, 2, 15};  

// Inisialisasi Library Keypad
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  // Buka baris komunikasi Serial via Kabel USB ke PC
  Serial.begin(115200); 
  
  // Inisialisasi EEPROM (Alokasi 16 byte memori lokal)
  EEPROM.begin(16);
  
  // Print status ke Serial Monitor buat mastiin hardware siap
  Serial.println("=================================");
  Serial.println("  BOOTLEG STREAMDECK v1.0 READY  ");
  Serial.println("     Mode: Full Wired (USB)      ");
  Serial.println("=================================");
}

void loop() {
  // Ambil data tombol yang sedang dipencet
  char key = keypad.getKey();
  
  // Jika ada tombol yang ditekan
  if (key) {
    // Kirim kode teks mentah lewat kabel USB ke Python
    // Format: KEY_4, KEY_5, KEY_D, dll.
    Serial.print("KEY_");
    Serial.println(key); 
    
    // Jeda 150ms agar tidak terjadi double-input saat tombol dipencet agak lama
    delay(150); 
  }
}