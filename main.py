from machine import Pin, ADC, I2C, PWM
import time
import ssd1306

# -------------------
# MQ2 SENSOR
# -------------------
mq2 = ADC(Pin(3))
mq2.atten(ADC.ATTN_11DB)  # allows full 0–3.3V range
mq2.width(ADC.WIDTH_12BIT)

# -------------------
# BUZZER
# -------------------
buzzer = PWM(Pin(2))
buzzer.duty(0)

# -------------------
# OLED DISPLAY
# -------------------
i2c = I2C(0, scl=Pin(4), sda=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# -------------------
# FUNCTIONS
# -------------------
def beep(freq=1000, duty=512):
    buzzer.freq(freq)
    buzzer.duty(duty)

def silent():
    buzzer.duty(0)

def get_status(value):
    if value < 1500:
        return "SAFE"
    elif value < 2500:
        return "WARNING"
    else:
        return "DANGER"

# -------------------
# MAIN LOOP
# -------------------
while True:
    gas_value = mq2.read()
    status = get_status(gas_value)

    print("Gas:", gas_value, "Status:", status)

    # ---------------- OLED ----------------
    oled.fill(0)
    oled.text("GAS MONITOR", 0, 0)
    oled.text("Value: {}".format(gas_value), 0, 20)
    oled.text("Status: {}".format(status), 0, 40)
    oled.show()

    # ---------------- ALERT LOGIC ----------------
    if status == "SAFE":
        silent()

    elif status == "WARNING":
        beep(800)
        time.sleep(0.2)
        silent()

    else:  # DANGER
        beep(1500)
        time.sleep(0.1)

    time.sleep(0.5)