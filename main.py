import json
import random
import time

def generate_telemetry():
    """Uydu simülasyonu için rastgele veri üretir."""
    data = {
        "voltage": round(random.uniform(3.3, 5.0), 2),
        "temperature": round(random.uniform(-20, 50), 2),
        "power_output": round(random.uniform(150, 200), 2),
        "timestamp": time.strftime("%H:%M:%S") # Verinin ne zaman üretildiğini ekledik
    }
    return data

def receive_data(data):
    """Gelen veriyi JSON formatında ekrana yazdırır."""
    print("\n[Yeryüzü İstasyonu] Yeni veri paketi alındı:")
    # json.dumps kullanımı için en üste 'import json' ekledik
    print(json.dumps(data, indent=4))

# Ana döngü
if __name__ == "__main__":
    print("Sistem başlatıldı. Veriler aktarılıyor...\n")
    
    try:
        while True:
            # 1. Veriyi üret
            uydudan_gelen = generate_telemetry()
            
            # 2. Veriyi işle/yazdır
            receive_data(uydudan_gelen)
            
            # 3. 2 saniye bekle
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nSistem kullanıcı tarafından durduruldu.")
