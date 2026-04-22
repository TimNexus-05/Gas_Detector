# Methane Gas Detector 

## Overview

The Methane Gas Detector with Alarm Response monitors methane concentration levels and provides real-time feedback through a display and audible alarm system.

When methane is detected, the device displays:
- **"Gas Detector"**
- The current methane concentration (%)
- The corresponding safety status

## Operating Behavior

The system responds based on methane concentration levels as follows:

### 🟢 Safe Condition
- **Methane Level:** Less than 4%
- **Display Status:** `SAFE`
- **Alarm:** Off  
- **Description:** Normal conditions. No immediate action required.

### 🟡 Warning Condition
- **Methane Level:** 5% – 10%
- **Display Status:** `WARNING`
- **Alarm:** Intermittent (beeping)  
- **Description:** Elevated methane levels detected. Caution is advised.

### 🔴 Danger Condition
- **Methane Level:** Greater than 10%
- **Display Status:** `DANGER`
- **Alarm:** Continuous buzz  
- **Description:** Critical methane concentration. Immediate action required.

## Summary Table

| Methane Level (%) | Status   | Alarm Behavior       |
|------------------|----------|----------------------|
| < 4%            | SAFE     | Off                  |
| 4% – 10%        | WARNING  | Intermittent Beeping |
| > 10%            | DANGER   | Continuous Buzz      |

##  Author
# BRIAN MARUGA MUTHONI
