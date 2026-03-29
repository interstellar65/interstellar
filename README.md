# interstellar
# 🚀 Uzay Tabanlı Hibrit Enerji Sistemi

## 📌 Proje Hakkında

Bu proje, uzay tabanlı güneş enerjisini kullanarak sürdürülebilir ve yüksek verimli bir enerji üretim sistemi geliştirmeyi amaçlamaktadır. Sistem, uzayda elde edilen güneş enerjisinin mikrodalga aracılığıyla Dünya’ya iletilmesi prensibine dayanır.

## 🎯 Amaç

* Sürekli ve kesintisiz enerji üretimi sağlamak
* Yenilenebilir enerji kaynaklarını daha verimli hale getirmek
* Enerji iletiminde kayıpları minimuma indirmek
* Geleceğin enerji ihtiyacına çözüm sunmak

## ⚙️ Sistem Nasıl Çalışır?

1. Uzayda bulunan güneş panelleri güneş ışığını toplar
2. Toplanan enerji elektrik enerjisine dönüştürülür
3. Elektrik enerjisi mikrodalga sinyallerine çevrilir
4. Bu sinyaller Dünya’ya gönderilir
5. Dünya’daki alıcı (rectenna) sistemi enerjiyi tekrar elektriğe çevirir

## 🔧 Kullanılan Teknolojiler

* Güneş panelleri
* Mikrodalga enerji iletimi
* Rectenna (alıcı sistem)
* Güç dönüşüm devreleri
* Arduino tabanlı kontrol sistemleri

## 💻 Kod Yapısı

Proje kapsamında enerji hesaplamaları ve sistem simülasyonları Python dili ile gerçekleştirilmiştir.

Örnek:

```python
def energy_system(area_m2):
    solar_irradiance = 1361
    panel_eff = 0.28
    microwave_eff = 0.70
    transmission_eff = 0.75
    rectenna_eff = 0.85

    input_energy = solar_irradiance * area_m2
    output = input_energy * panel_eff * microwave_eff * transmission_eff * rectenna_eff

    return output
```

## 📊 Avantajlar

* 24 saat kesintisiz enerji üretimi
* Hava koşullarından etkilenmeme
* Yüksek verimlilik
* Temiz ve çevre dostu enerji

## 🚀 Gelecek Çalışmalar

* Sistem verimliliğinin artırılması
* Daha düşük maliyetli çözümler geliştirilmesi
* Prototip üretimi ve test süreçleri

## 👨‍💻 Geliştirici

Bu proje, uzay teknolojileri ve enerji sistemlerine ilgi duyan öğrenciler tarafından geliştirilmiştir.

---

⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!

