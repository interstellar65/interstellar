
import random
import time

def generate_telemetry():
    data = {
        "voltage": round(random.uniform(3.3, 5.0), 2),
        "temperature": round(random.uniform(-20, 50), 2),
        "power_output": round(random.uniform(150, 200), 2)
    }
    return data

while True:
    print("Uydu Verisi:", generate_telemetry())
    time.sleep(2)