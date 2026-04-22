 🛠️ Hardware Branch – Gas Detection System (ESP32-C3)

This branch documents the physical and simulated hardware setup for the Gas Detection System using ESP32-C3, MQ2 gas sensor, OLED display, buzzer, and LED indicators.

It focuses on **wiring decisions, pin mapping, and power considerations (especially MQ2 5V operation in Wokwi simulation).**

---

## 📌 System Overview

The hardware system detects combustible gases (LPG, methane, smoke) using an MQ2 sensor and provides real-time alerts via:

- OLED display (gas levels + status)
- Buzzer (audio alarm)
- LED indicators (visual status)
- ESP32-C3 (central controller)
- Low pass filter (ceramic capacitor)

---

## 🔌 Pin Mapping (ESP32-C3)

| Component | Signal | ESP32-C3 Pin |
|----------|--------|--------------|
| MQ2 Sensor | AO (Analog Output) | GPIO 3 (ADC) |
| MQ2 Sensor | VCC | 5V |
| MQ2 Sensor | GND | GND |
| OLED Display | SDA | GPIO 4 |
| OLED Display | SCL | GPIO 5 |
| Buzzer | Signal | GPIO 0 |
| Red LED | Anode | GPIO 6 |
|Green LED| Anode |GPIO 7|
|Blue LED| Anode|GPIO2|


---

## ⚡ MQ2 Sensor Power Configuration (IMPORTANT)

### 🔥 In this project (Wokwi simulation):

- The MQ2 sensor is powered directly using **5V**
- **NO voltage divider is used on the analog output (AO)**
- The analog output is read directly by the ESP32-C3 ADC pin

### ⚠️ Why this is acceptable in Wokwi:

- Wokwi simulates MQ2 as a safe virtual component
- Output voltage is already scaled within safe ADC limits
- No risk of damaging ESP32 in simulation
- Simplifies circuit design for learning and testing


-in real hardware we used 2 10k resistors to scale down the 5v output .
This scales 5V → ~3.3V safe input

---

## 🧠 System Signal Flow

1. MQ2 sensor detects gas concentration
2. Analog voltage increases proportionally
3. ESP32-C3 reads ADC value (GPIO 3)
4. Firmware converts reading into gas level %
5. System reacts:
   - Safe → Green LED ON
   - Warning → Red LED + Buzzer ON
6. OLED displays real-time status

---

## 📊 MQ2 Behavior Notes

- Requires warm-up time before stable readings
- Outputs analog voltage proportional to gas density
- Higher gas concentration → higher ADC value
- Sensitive to LPG, methane, smoke, alcohol vapors

---

## 🔊 Alarm Hardware Response

| Condition | LED | Buzzer | OLED |
|----------|-----|--------|------|
| Safe | Green ON | OFF | “SAFE” |
| Warning | Blue  ON | ON (PWM beep  intermitent beep) | 
|“DANGER” |Red and Blue on ,alternating|buzzer on| Continous beep|

---

## 🧪 Wokwi Setup Notes

- MQ2 VCC connected directly to **5V rail**
- AO connected directly to ESP32 ADC pin (GPIO 3)
- No resistors or voltage divider used in simulation
- Power stability handled virtually by Wokwi engine

---

## 🚀 Design Philosophy

This hardware design prioritizes:

- Simplicity for simulation (Wokwi)
- Clear separation between simulation vs real-world deployment
- Easy migration path to physical ESP32 hardware


---

## 👥 Branch Role

This branch focuses ONLY on:

- Wiring diagrams
- Pin assignments
- Sensor power logic
- Hardware-level constraints

<img width="453" height="398" alt="Screenshot From 2026-04-15 16-50-05" src="https://github.com/user-attachments/assets/ff96b95e-7b15-4ef5-956d-a192d130a0b1" />

<img width="1057" height="1401" alt="image" src="https://github.com/user-attachments/assets/299d0c15-8b75-45b0-8901-38351e501e1d" />





## Author
-Tim Wekesa
  

