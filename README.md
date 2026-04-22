# The projects features
## Review
 This branch introduces an IoT-enabled methane safety system designed to provide proactive protection for homes and small workplaces.  
 It acts as a watchful guardian continuously monitoring air quality to detect invisible methane leaks before they pose a danger.  
 It integrates sensor reading, alarm response, and user display into one system.  

## Objectives
 Detecting high levels of methane in the air using the sensor.  
 Triggering an alarm once high methane levels are achieved.  
 Displaying the realtime status of the system and value of methane.  

## Components of the project
 ESP32 board.  
 MQ2 Sensor.  
 Buzzer.  
 Leds (red and green).  
 Resistors.  
 Connecting wires.  
 display. 
 capacitor - low pass filter

## Pin layout

| Component        | signal |ESP32 pin                 |
|------------------|----------|------------------------------|
| MQ-2 Sensor      | A1 pin   | GPIO3 (ADC)          |
| MQ-2 sensor      | B2 pin   | 5V                    |  
| MQ-2 sensor      | H1 pin   | 5V(heater)            |  
| MQ-2 sensor      | H2 pin   | GND                   |  
| OLED display            | SDA      | GPIO4                 |  
| OLED display            | SCL      | GPIO5                |  
| OLED display            | GND       | GND
| Buzzer           | Signal   | GPIO0                |
| Buzzer           | GND      | GND               |
| Red LED          | Anode    | GPIO6             |
| Blue LED         | Anode    | GPIO2             |
| Green LED        | Anode    | GPIO7             |

## How It Works
The MQ-2 sensor outputs an analog signal proportional to methane concentration.
The ESP32 reads this signal using its ADC pin.

The system compares the value to a threshold:

- If gas <4% shows SAFE
  - Green LED ON
  - Buzzer OFF
    
- If methane level is between 4%-10% Gives a WARNING
  -Blue led ON

- If gas ≥10% shows DANGER
  - Red and blue LED ON
  - Buzzer ON


## Author {Kelvin Karong'e}
