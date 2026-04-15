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
 Sensor.  
 Buzzer.  
 Leds (red and green).  
 Resistors.  
 Connecting wires.  
 display.  

## Pin layout

| Component        | ESP32 Pin | Description                  |
|------------------|----------|------------------------------|
| MQ-2 Sensor      | GPIO3   | Analog input (ADC)           |
| Buzzer           | GPIO2   | Alarm output                 |
| Red LED          | GPIO6    | Danger indicator             |
| GND              | GND      | Common ground for all parts  |
| VCC (Sensor)     | 5V       | Power supply for MQ-4        |

## How It Works
The MQ-2 sensor outputs an analog signal proportional to methane concentration.
The ESP32 reads this signal using its ADC pin.

The system compares the value to a threshold:

- If gas <40% shows SAFE
  - Green LED ON
  - Buzzer OFF
    
- If methane level is between 40%-70% Gives a WARNING    

- If gas ≥70% shows DANGER
  - Red LED ON
  - Buzzer ON

## Sample Output
Methane Level: 20%
Status: SAFE

Methane Level: 80%   
Status: DANGER

## Author {Kelvin Karong'e}
