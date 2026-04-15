from machine import Pin, ADC, I2C, PWM
import time
import ssd1306

# -------------------
# MQ2 SENSOR
# -------------------
mq2 = ADC(Pin(3))
mq2.atten(ADC.ATTN_11DB)
mq2.width(ADC.WIDTH_12BIT)  # 0 - 4095

# -------------------
# BUZZER
# -------------------
buzzer = PWM(Pin(2))
buzzer.duty(0)

# -------------------
# LED (DANGER INDICATOR)
# -------------------
led = Pin(6, Pin.OUT)   # change pin if needed

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

def get_status(percent):
    if percent < 40:
        return "SAFE"
    elif percent < 70:
        return "WARNING"
    else:
        return "DANGER"

def to_percent(value):
    return int((value / 4095) * 100)

# -------------------
# MAIN LOOP
# -------------------
while True:
    raw = mq2.read()
    percent = to_percent(raw)
    status = get_status(percent)

    print("Raw:", raw, "Percent:", percent, "%", "Status:", status)

    # ---------------- OLED ----------------
    oled.fill(0)
    oled.text("GAS MONITOR", 0, 0)
    oled.text("Value: {}%".format(percent), 0, 20)
    oled.text("Status: {}".format(status), 0, 40)
    oled.show()

    # ---------------- ALERT LOGIC ----------------
    if status == "SAFE":
        silent()
        led.value(0)

    elif status == "WARNING":
        led.value(0)
        beep(800)
        time.sleep(0.2)
        silent()

    else:  # DANGER 🔥
        beep(1500)

        # LED blinking
        led.value(1)
        time.sleep(0.1)
        led.value(0)
        time.sleep(0.1)

    time.sleep(0.3)
