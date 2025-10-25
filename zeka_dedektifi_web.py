import streamlit as st
from keybert import KeyBERT
import textstat
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="🧠 Zeka Dedektifi Web", layout="wide")
st.title("🧠 Zeka Dedektifi – Web (Lite Sürüm)")

if "sonuclar" not in st.session_state:
    st.session_state.sonuclar = []

isim = st.text_input("👤 Öğrencinin Adı")
user_text = st.text_area("✍️ Yazılı Giriş:", height=150)

if st.button("Zeka Türünü Analiz Et ve Kaydet"):
    if len(user_text.strip()) < 20 or isim.strip() == "":
        st.warning("Lütfen öğrenci adı ve en az 20 karakterlik bir metin gir.")
        st.stop()

    st.info("Analiz yapılıyor... ⏳")

    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(user_text, top_n=3)
    kelimeler = [k[0] for k in keywords]

    kelime_sayisi = len(user_text.split())
    okunabilirlik = textstat.flesch_reading_ease(user_text)

    if "gör" in user_text.lower() or okunabilirlik > 60:
        tahmin = "Görsel"
    elif "sayı" in user_text.lower() or kelime_sayisi < 40:
        tahmin = "Mantıksal"
    else:
        tahmin = "Sözel"

    yeni_sonuc = {
        "İsim": isim,
        "Zeka Türü": tahmin,
        "Kelime Sayısı": kelime_sayisi,
        "Okunabilirlik": round(okunabilirlik, 2),
        "Anahtar Kelimeler": ", ".join(kelimeler)
    }
    st.session_state.sonuclar.append(yeni_sonuc)

    st.success(f"🎯 {isim} için tahmin edilen zeka türü: **{tahmin}**")

st.markdown("---")
st.header("📊 Öğrenci Sonuç Paneli")

if len(st.session_state.sonuclar) > 0:
    df_panel = pd.DataFrame(st.session_state.sonuclar)
    st.dataframe(df_panel, use_container_width=True)

    fig, ax = plt.subplots()
    df_panel["Zeka Türü"].value_counts().plot(kind='bar', ax=ax, color='skyblue')
    plt.title("Zeka Türü Dağılımı")
    plt.xlabel("Zeka Türü")
    plt.ylabel("Öğrenci Sayısı")
    st.pyplot(fig)

    csv = df_panel.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Sonuçları CSV olarak indir", csv, "zeka_sonuclari.csv", "text/csv")
else:
    st.info("Henüz analiz yapılmadı. Öğrenciler eklendikçe tablo ve grafik oluşacak.")
