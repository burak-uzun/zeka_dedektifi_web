# 🧠 Yapay Zekâ Dedektifi Web

Bu proje, öğrencilerin metin ve ses girdileri üzerinden **zeka türünü tahmin eden** bir demo web uygulamasıdır.

## Özellikler

- Yazılı ve sesli giriş imkanı
- Metin analizi: duygu, kelime sayısı, okunabilirlik, anahtar kelimeler
- Zeka türü tahmini (Mantıksal, Sözel, Görsel, Müziksel, Sosyal)
- Öğrenci sonuç paneli ve dağılım grafiği
- Sonuçların CSV olarak indirilmesi

## Deploy ve Çalıştırma

### Local
1. Python ortamını oluştur:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Gerekli paketleri yükle:
```bash
pip install -r requirements.txt
```

3. Uygulamayı çalıştır:
```bash
streamlit run zeka_dedektifi_web.py
```

### Streamlit Cloud
1. GitHub'a yükle
2. Streamlit Cloud’da “New App” → GitHub repo → branch seç → Deploy
