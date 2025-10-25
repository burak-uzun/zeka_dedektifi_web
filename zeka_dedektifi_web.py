import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="🧠 Zeka Dedektifi Mini", layout="wide")
st.title("🧠 Zeka Dedektifi – Mini Web Sürüm")

if "sonuclar" not in st.session_state:
    st.session_state.sonuclar = []

isim = st.text_input("👤 Öğrenci Adı")
cevap = st.text_area("✍️ Öğrencinin Yazılı Cevabı:", height=150)

if st.button("Zeka Türünü Analiz Et"):
    if len(cevap.strip()) < 20 or isim.strip() == "":
        st.warning("Lütfen öğrenci adı ve en az 20 karakterlik metin gir.")
    else:
        metin = cevap.lower()
        kelimeler = len(metin.split())

        # Basit kurallar
        if any(x in metin for x in ["renk", "gör", "şekil", "resim", "hayal"]):
            zeka = "Görsel"
        elif any(x in metin for x in ["sayı", "hesap", "mantık", "problem", "analiz"]):
            zeka = "Mantıksal"
        elif any(x in metin for x in ["hikaye", "anlat", "kelime", "şiir", "duygu"]):
            zeka = "Sözel"
        else:
            zeka = "Karma"

        st.session_state.sonuclar.append({
            "İsim": isim,
            "Zeka Türü": zeka,
            "Kelime Sayısı": kelimeler
        })

        st.success(f"🎯 {isim} adlı öğrencinin tahmini zeka türü: **{zeka}**")

st.divider()
st.header("📊 Sonuç Paneli")

if len(st.session_state.sonuclar) > 0:
    df = pd.DataFrame(st.session_state.sonuclar)
    st.dataframe(df, use_container_width=True)

    fig, ax = plt.subplots()
    df["Zeka Türü"].value_counts().plot(kind="bar", ax=ax, color="skyblue")
    plt.title("Zeka Türü Dağılımı")
    st.pyplot(fig)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Sonuçları İndir", csv, "zeka_sonuclari.csv", "text/csv")
else:
    st.info("Henüz analiz yapılmadı.")
