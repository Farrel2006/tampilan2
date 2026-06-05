import streamlit as st

# =====================================
# CONFIG
# =====================================
st.set_page_config(
    page_title="Slide Presentasi Termodinamika",
    page_icon="📊",
    layout="wide"
)
# =====================================
# CSS STYLE: CLEAN ACADEMIC PRESENTATION (FIXED COMPATIBILITY)
# =====================================
st.markdown("""
<style>
/* Reset dasar ke gaya dokumen/slide formal */
html, body, [class*="css"] {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

.stApp {
    background-color: #f8fafc !important; /* Abu-abu sangat terang khas background slide */
}

/* Memperbaiki semua teks default Streamlit Markdown agar kontras dan tajam */
[data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {
    color: #334155 !important; /* Abu-abu gelap profesional, bukan samar-samar */
    font-size: 16px !important;
    line-height: 1.7 !important;
}

/* Gaya Judul Utama Slide */
.title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    color: #1e3a8a !important; /* Biru Royal Formal */
    margin-top: 20px;
    margin-bottom: 5px;
    letter-spacing: -0.5px;
}

.subtitle {
    text-align: center;
    color: #64748b !important;
    font-size: 18px;
    margin-bottom: 40px;
    font-weight: 400;
}

/* Kotak Konten Berbentuk Kartu Presentasi (Diberi border lebih tegas agar kelihatan) */
.intro-box {
    background-color: #ffffff !important;
    padding: 35px;
    border-radius: 12px;
    border: 2px solid #e2e8f0 !important; /* Dipertebal */
    margin-bottom: 30px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
}

/* Memastikan judul di dalam intro-box tetap berwarna biru */
.intro-box h3, .intro-box h4 {
    color: #1e3a8a !important;
    font-weight: 700 !important;
}

/* Kotak Hasil Perhitungan Akhir */
.result {
    background-color: #f1f5f9 !important;
    padding: 25px;
    border-radius: 10px;
    border-left: 5px solid #2563eb !important; 
    margin-top: 25px;
}

.result h3, .result h4, .result b {
    color: #0f172a !important;
}

/* Desain Tombol Formal & Seragam */
.stButton>button, div[data-testid="stButton"]>button {
    width: 100% !important;
    display: block !important;
    padding: 12px 20px !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    border: 1px solid #cbd5e1 !important;
    color: #334155 !important;
    background-color: #ffffff !important;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
    transition: all 0.2s ease !important;
}

/* Efek Hover Tombol Utama (Biru Presentasi) */
.stButton>button:hover, div[data-testid="stButton"]>button:hover {
    color: #ffffff !important;
    background-color: #2563eb !important;
    border-color: #2563eb !important;
    transform: translateY(-1px);
}

/* Input Form Bergaya Akademis */
.stNumberInput input, .stTextInput input {
    background-color: #ffffff !important;
    color: #1e293b !important;
    border-radius: 8px !important;
    border: 1px solid #cbd5e1 !important;
}

[data-testid="stWidgetLabel"] p {
    color: #1e3a8a !important; /* Label input jadi biru tua */
    font-weight: 700 !important;
    font-size: 15px !important;
}

/* Warna Math/LaTeX disesuaikan agar kontras di latar terang */
.katex {
    color: #1e3a8a !important;
    font-size: 22px !important;
}

.stAlert {
    border-radius: 10px;
    background-color: #eff6ff !important;
    border: 1px solid #bfdbfe !important;
}

.stAlert p { color: #1e40af !important; font-weight: 500; }
h1, h2, h3, h4 { color: #1e3a8a !important; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# =====================================
# UTILITIES
# =====================================
def fmt(angka):
    try:
        return f"{angka:g}"
    except:
        return str(angka)

# =====================================
# SESSION STATE NAVIGATION
# =====================================
if "current_page" not in st.session_state:
    st.session_state.current_page = "slide1"
if "menu" not in st.session_state:
    st.session_state.menu = None

menu_list = [
    "Hukum 1 Termodinamika", "Usaha", "Kalor", "Entalpi", "Hukum Hess",
    "ΔH Reaksi", "Energi Gibbs", "Entropi", "Gas Ideal", "Gas Nyata",
    "Proses Isobarik", "Proses Isokhorik", "Proses Isotermal", "Edukasi Isotop Gas"
]

# =====================================
# SLIDE 1: TITLE & OBJECTIVES
# =====================================
if st.session_state.current_page == "slide1":
    st.markdown("<div class='title'>Termodinamika & Komputasi Gas</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Modul Media Pembelajaran & Alat Bantu Analisis Data</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='intro-box'>
        <h3 style='margin-top:0; color:#1e3a8a;'>🎯 Pengantar Aplikasi</h3>
        <p>Aplikasi ini dirancang sebagai instrumen bantu perkuliahan dan praktikum laboratoriun untuk mempermudah 
        analisis parameter termodinamika, hukum-hukum gas ideal/nyata, serta fenomena kesetimbangan energi sistem.</p>
        <hr style='border: 0; border-top: 1px solid #e2e8f0; margin: 20px 0;'>
        <h4 style='color:#2563eb;'>🚀 Pokok Kemampuan Sistem:</h4>
        <ul style='margin-bottom:0; line-height: 1.8; color: #475569;'>
            <li><b>Akurasi Komputasi:</b> Meminimalkan galat perhitungan manual pada persamaan multivariabel.</li>
            <li><b>Penyelesaian Terstruktur:</b> Menampilkan penurunan rumus secara runut untuk kebutuhan pelaporan ilmiah.</li>
            <li><b>Analisis Molekular:</b> Menyediakan simulasi sifat makroskopis gas berdasarkan perbedaan massa isotopnya.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    _, col_btn, _ = st.columns([1, 1.5, 1])
    with col_btn:
        if st.button("Buka Daftar Modul Presentasi ➡️", key="next_to_slide2"):
            st.session_state.current_page = "slide2"
            st.rerun()

# =====================================
# SLIDE 2: INDEX / MODUL SELECTION
# =====================================
elif st.session_state.current_page == "slide2":
    st.markdown("<div class='title' style='font-size:36px;'>Daftar Materi & Modul Hitung</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Silakan pilih topik bahasan presentasi di bawah ini</div>", unsafe_allow_html=True)
    
    if st.button("⬅️ Kembali ke Halaman Pengantar", key="back_to_slide1"):
        st.session_state.current_page = "slide1"
        st.rerun()
        
    st.write("") 

    cols = st.columns(2)
    for i, m in enumerate(menu_list):
        with cols[i % 2]:
            if st.button(f"📄 {m}", key=f"menu_btn_{i}"):
                st.session_state.menu = m
                st.session_state.current_page = "calc_page"
                st.rerun()

# =====================================
# PAGES: LIVE CALCULATOR & DISCUSSIONS
# =====================================
elif st.session_state.current_page == "calc_page":
    menu = st.session_state.menu

    if st.button("⬅️ Kembali ke Daftar Modul"):
        st.session_state.current_page = "slide2"
        st.session_state.menu = None
        st.rerun()

    st.markdown(f"<h2>📌 Topik: {menu}</h2>", unsafe_allow_html=True)
    st.divider()

    # 1. HUKUM 1 TERMODINAMIKA
    if menu == "Hukum 1 Termodinamika":
        st.latex(r"\Delta U = Q - W")
        target = st.selectbox("Pilih komponen yang dicari:", ["ΔU (Perubahan Energi Dalam)", "Q (Kalor)", "W (Usaha)"])
        
        Q = st.number_input("Q (kJ)", value=0.0) if target != "Q (Kalor)" else 0.0
        W = st.number_input("W (kJ)", value=0.0) if target != "W (Usaha)" else 0.0
        dU = st.number_input("ΔU (kJ)", value=0.0) if target != "ΔU (Perubahan Energi Dalam)" else 0.0

        if st.button("Proses Perhitungan"):
            if "ΔU" in target:
                hasil = Q - W
                langkah = f"ΔU = Q - W <br> ΔU = {fmt(Q)} - {fmt(W)} <br> ΔU = <b>{fmt(hasil)} kJ</b>"
            elif "Q" in target:
                hasil = dU + W
                langkah = f"Q = ΔU + W <br> Q = {fmt(dU)} + {fmt(W)} <br> Q = <b>{fmt(hasil)} kJ</b>"
            else:
                hasil = Q - dU
                langkah = f"W = Q - ΔU <br> W = {fmt(Q)} - {fmt(dU)} <br> W = <b>{fmt(hasil)} kJ</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian:</h3>{langkah}</div>", unsafe_allow_html=True)

    # 2. USAHA
    elif menu == "Usaha":
        st.latex(r"W = P \cdot \Delta V")
        target = st.selectbox("Pilih komponen yang dicari:", ["W (Usaha)", "P (Tekanan)", "ΔV (Perubahan Volume)"])

        W = st.number_input("W (J)", value=0.0) if target != "W (Usaha)" else 0.0
        P = st.number_input("P (Pa)", value=0.0) if target != "P (Tekanan)" else 0.0
        dV = st.number_input("ΔV (m³)", value=0.0) if target != "ΔV (Perubahan Volume)" else 0.0

        if st.button("Proses Perhitungan"):
            if "W" in target:
                hasil = P * dV
                langkah = f"W = P × ΔV <br> W = {fmt(P)} × {fmt(dV)} <br> W = <b>{fmt(hasil)} J</b>"
            elif "P" in target:
                hasil = W / dV if dV != 0 else 0
                langkah = f"P = W / ΔV <br> P = {fmt(W)} / {fmt(dV)} <br> P = <b>{fmt(hasil)} Pa</b>"
            else:
                hasil = W / P if P != 0 else 0
                langkah = f"ΔV = W / P <br> ΔV = {fmt(W)} / {fmt(P)} <br> ΔV = <b>{fmt(hasil)} m³</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian:</h3>{langkah}</div>", unsafe_allow_html=True)

    # 3. KALOR
    elif menu == "Kalor":
        st.latex(r"Q = m \cdot c \cdot \Delta T")
        target = st.selectbox("Pilih komponen yang dicari:", ["Q (Kalor)", "m (Massa)", "c (Kalor Jenis)", "ΔT (Perubahan Suhu)"])

        Q = st.number_input("Q (J)", value=0.0) if target != "Q (Kalor)" else 0.0
        m = st.number_input("m (g)", value=0.0) if target != "m (Massa)" else 0.0
        c = st.number_input("c (J/g°C)", value=0.0) if target != "c (Kalor Jenis)" else 0.0
        dT = st.number_input("ΔT (°C)", value=0.0) if target != "ΔT (Perubahan Suhu)" else 0.0

        if st.button("Proses Perhitungan"):
            if "Q" in target:
                hasil = m * c * dT
                langkah = f"Q = m × c × ΔT <br> Q = {fmt(m)} × {fmt(c)} × {fmt(dT)} <br> Q = <b>{fmt(hasil)} J</b>"
            elif "m" in target:
                hasil = Q / (c * dT) if (c * dT) != 0 else 0
                langkah = f"m = Q / (c × ΔT) <br> m = {fmt(Q)} / ({fmt(c)} × {fmt(dT)}) <br> m = <b>{fmt(hasil)} g</b>"
            elif "c" in target:
                hasil = Q / (m * dT) if (m * dT) != 0 else 0
                langkah = f"c = Q / (m × ΔT) <br> c = {fmt(Q)} / ({fmt(m)} × {fmt(dT)}) <br> c = <b>{fmt(hasil)} J/g°C</b>"
            else:
                hasil = Q / (m * c) if (m * c) != 0 else 0
                langkah = f"ΔT = Q / (m × c) <br> ΔT = {fmt(Q)} / ({fmt(m)} × {fmt(c)}) <br> ΔT = <b>{fmt(hasil)} K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian:</h3>{langkah}</div>", unsafe_allow_html=True)

    # 4. ENTALPI
    elif menu == "Entalpi":
        st.latex(r"\Delta H = \Delta U + \Delta n \cdot R \cdot T")
        target = st.selectbox("Pilih komponen yang dicari:", ["ΔH (Entalpi)", "ΔU (Energi Dalam)", "Δn (Perubahan Mol)", "T (Suhu)"])
        R = 0.008314  

        dH = st.number_input("ΔH (kJ)", value=0.0) if target != "ΔH (Entalpi)" else 0.0
        dU = st.number_input("ΔU (kJ)", value=0.0) if target != "ΔU (Energi Dalam)" else 0.0
        dn = st.number_input("Δn (mol)", value=0.0) if target != "Δn (Perubahan Mol)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Proses Perhitungan"):
            if "ΔH" in target:
                hasil = dU + (dn * R * T)
                langkah = f"ΔH = ΔU + (Δn × R × T) <br> ΔH = {fmt(dU)} + ({fmt(dn)} × {R} × {fmt(T)}) <br> ΔH = <b>{fmt(hasil)} kJ</b>"
            elif "ΔU" in target:
                hasil = dH - (dn * R * T)
                langkah = f"ΔU = ΔH - (Δn × R × T) <br> ΔU = {fmt(dH)} - ({fmt(dn)} × {R} × {fmt(T)}) <br> ΔU = <b>{fmt(hasil)} kJ</b>"
            elif "Δn" in target:
                hasil = (dH - dU) / (R * T) if T != 0 else 0
                langkah = f"Δn = (ΔH - ΔU) / (R × T) <br> Δn = ({fmt(dH)} - {fmt(dU)}) / ({R} × {fmt(T)}) <br> Δn = <b>{fmt(hasil)} mol</b>"
            else:
                hasil = (dH - dU) / (dn * R) if dn != 0 else 0
                langkah = f"T = (ΔH - ΔU) / (Δn × R) <br> T = ({fmt(dH)} - {fmt(dU)}) / ({fmt(dn)} × {R}) <br> T = <b>{fmt(hasil)} K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian:</h3>{langkah}</div>", unsafe_allow_html=True)

    # 5. HUKUM HESS
    elif menu == "Hukum Hess":
        st.latex(r"\Delta H_{total} = \Delta H_1 + \Delta H_2 + ... + \Delta H_n")
        target = st.selectbox("Pilih operasi:", ["Hitung ΔH Total dari list", "Cari satu ΔH yang hilang"])

        if target == "Hitung ΔH Total dari list":
            data = st.text_input("Masukkan semua nilai ΔH (pisahkan dengan koma)", "10,-20,30")
            if st.button("Proses Perhitungan"):
                arr = [float(x) for x in data.split(",") if x.strip() != ""]
                st.markdown(f"<div class='result'><h3>Hasil Akhir Presentasi</h3>ΣΔH = <b>{fmt(sum(arr))} kJ</b></div>", unsafe_allow_html=True)
        else:
            total_h = st.number_input("Masukkan ΔH Total", value=0.0)
            data_parsial = st.text_input("Masukkan ΔH komponen lain yang diketahui (pisahkan dengan koma)", "10,-20")
            if st.button("Proses Perhitungan"):
                arr = [float(x) for x in data_parsial.split(",") if x.strip() != ""]
                hasil = total_h - sum(arr)
                st.markdown(f"<div class='result'><h3>Hasil Komputasi Variabel Hilang</h3>ΔH_x = {fmt(total_h)} - {fmt(sum(arr))} <br> ΔH_x = <b>{fmt(hasil)} kJ</b></div>", unsafe_allow_html=True)

    # 6. ΔH REAKSI
    elif menu == "ΔH Reaksi":
        st.latex(r"\Delta H = \sum Hf_{produk} - \sum Hf_{reaktan}")
        target = st.selectbox("Pilih komponen yang dicari:", ["ΔH Reaksi", "ΣHf Produk", "ΣHf Reaktan"])

        dH = st.number_input("ΔH Reaksi (kJ)", value=0.0) if target != "ΔH Reaksi" else 0.0
        prod = st.text_input("Masukkan nilai Produk (pisah koma)", "0") if target != "ΣHf Produk" else "0"
        reak = st.text_input("Masukkan nilai Reaktan (pisah koma)", "0") if target != "ΣHf Reaktan" else "0"

        if st.button("Proses Perhitungan"):
            p_sum = sum([float(x) for x in prod.split(",") if x.strip() != ""])
            r_sum = sum([float(x) for x in reak.split(",") if x.strip() != ""])

            if target == "ΔH Reaksi":
                hasil = p_sum - r_sum
                langkah = f"ΔH = {fmt(p_sum)} - {fmt(r_sum)} = <b>{fmt(hasil)} kJ/mol</b>"
            elif target == "ΣHf Produk":
                hasil = dH + r_sum
                langkah = f"ΣHf_produk = {fmt(dH)} + {fmt(r_sum)} = <b>{fmt(hasil)} kJ/mol</b>"
            else:
                hasil = p_sum - dH
                langkah = f"ΣHf_reaktan = {fmt(p_sum)} - {fmt(dH)} = <b>{fmt(hasil)} kJ/mol</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian:</h3>{langkah}</div>", unsafe_allow_html=True)

    # 7. ENERGI GIBBS
    elif menu == "Energi Gibbs":
        st.latex(r"\Delta G = \Delta H - T \cdot \Delta S")
        target = st.selectbox("Pilih komponen yang dicari:", ["ΔG (Energi Gibbs)", "ΔH (Entalpi)", "T (Suhu dalam K)", "ΔS (Entropi dalam kJ/K)"])

        dG = st.number_input("ΔG (kJ)", value=0.0) if target != "ΔG (Energi Gibbs)" else 0.0
        dH = st.number_input("ΔH (kJ)", value=0.0) if target != "ΔH (Entalpi)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu dalam K)" else 0.0
        dS = st.number_input("ΔS (kJ/K)", value=0.0) if target != "ΔS (Entropi dalam kJ/K)" else 0.0

        if st.button("Proses Perhitungan"):
            if "ΔG" in target:
                hasil = dH - (T * dS)
                langkah = f"ΔG = {fmt(dH)} - ({fmt(T)} × {fmt(dS)}) = <b>{fmt(hasil)} kJ</b>"
            elif "ΔH" in target:
                hasil = dG + (T * dS)
                langkah = f"ΔH = {fmt(dG)} + ({fmt(T)} × {fmt(dS)}) = <b>{fmt(hasil)} kJ</b>"
            elif "T" in target:
                hasil = (dH - dG) / dS if dS != 0 else 0
                langkah = f"T = ({fmt(dH)} - {fmt(dG)}) / {fmt(dS)} = <b>{fmt(hasil)} K</b>"
            else:
                hasil = (dH - dG) / T if T != 0 else 0
                langkah = f"ΔS = ({fmt(dH)} - {fmt(dG)}) / {fmt(T)} = <b>{fmt(hasil)} kJ/K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian:</h3>{langkah}</div>", unsafe_allow_html=True)

    # 8. ENTROPI
    elif menu == "Entropi":
        st.latex(r"\Delta S = \frac{Q}{T}")
        target = st.selectbox("Pilih komponen yang dicari:", ["ΔS (Entropi)", "Q (Kalor)", "T (Suhu)"])

        dS = st.number_input("ΔS (kJ/K)", value=0.0) if target != "ΔS (Entropi)" else 0.0
        Q = st.number_input("Q (kJ)", value=0.0) if target != "Q (Kalor)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Proses Perhitungan"):
            if "ΔS" in target:
                hasil = Q / T if T != 0 else 0
                langkah = f"ΔS = {fmt(Q)} / {fmt(T)} = <b>{fmt(hasil)} kJ/K</b>"
            elif "Q" in target:
                hasil = dS * T
                langkah = f"Q = {fmt(dS)} × {fmt(T)} = <b>{fmt(hasil)} kJ</b>"
            else:
                hasil = Q / dS if dS != 0 else 0
                langkah = f"T = {fmt(Q)} / {fmt(dS)} = <b>{fmt(hasil)} K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian:</h3>{langkah}</div>", unsafe_allow_html=True)

    # 9. GAS IDEAL
    elif menu == "Gas Ideal":
        st.latex(r"P \cdot V = n \cdot R \cdot T")
        target = st.selectbox("Pilih komponen yang dicari:", ["P (Tekanan)", "V (Volume)", "n (Jumlah Mol)", "T (Suhu)"])
        R = 0.0821

        P = st.number_input("P (atm)", value=0.0) if target != "P (Tekanan)" else 0.0
        V = st.number_input("V (L)", value=0.0) if target != "V (Volume)" else 0.0
        n = st.number_input("n (mol)", value=0.0) if target != "n (Jumlah Mol)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Proses Perhitungan"):
            if "P" in target:
                hasil = (n * R * T) / V if V != 0 else 0
                langkah = f"P = ({fmt(n)} × {R} × {fmt(T)}) / {fmt(V)} = <b>{fmt(hasil)} atm</b>"
            elif "V" in target:
                hasil = (n * R * T) / P if P != 0 else 0
                langkah = f"V = ({fmt(n)} × {R} × {fmt(T)}) / {fmt(P)} = <b>{fmt(hasil)} L</b>"
            elif "n" in target:
                hasil = (P * V) / (R * T) if T != 0 else 0
                langkah = f"n = ({fmt(P)} × {fmt(V)}) / ({R} × {fmt(T)}) = <b>{fmt(hasil)} mol</b>"
            else:
                hasil = (P * V) / (n * R) if n != 0 else 0
                langkah = f"T = ({fmt(P)} × {fmt(V)}) / ({fmt(n)} × {R}) = <b>{fmt(hasil)} K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian:</h3>{langkah}</div>", unsafe_allow_html=True)

     # 10. GAS NYATA
    elif menu == "Gas Nyata":
        st.latex(r"\left(P + \frac{an^2}{V^2}\right)(V - nb) = nRT")
        target = st.selectbox("Pilih komponen yang dicari:", ["P (Tekanan)", "T (Suhu)"])
        R = 0.0821

        n = st.number_input("n (mol)", value=0.0)
        V = st.number_input("V (L)", value=0.0)
        a = st.number_input("a (atm.L²/mol²)", value=0.0)
        b = st.number_input("b (L/mol)", value=0.0)
        
        P = st.number_input("P (atm)", value=0.0) if target != "P (Tekanan)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Proses Perhitungan"):
            if "P" in target:
                hasil = ((n * R * T) / (V - n * b)) - ((a * (n ** 2)) / (V ** 2)) if (V - n * b) != 0 and V != 0 else 0
                langkah = f"P = [({fmt(n)} × {R} × {fmt(T)}) / ({fmt(V)} - ({fmt(n)} × {b}))] - [({a} × {fmt(n)}²) / {fmt(V)}²] <br> P = <b>{fmt(hasil)} atm</b>"
            else:
                p_term = P + ((a * (n ** 2)) / (V ** 2)) if V != 0 else 0
                v_term = V - (n * b)
                hasil = (p_term * v_term) / (n * R) if (n * R) != 0 else 0
                langkah = f"T = [({fmt(P)} + {a}×{fmt(n)}²/{fmt(V)}²) × ({fmt(V)} - {fmt(n)}×{b})] / ({fmt(n)} × {R}) <br> T = <b>{fmt(hasil)} K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian:</h3>{langkah}</div>", unsafe_allow_html=True)

    # 11. PROSES ISOBARIK
    elif menu == "Proses Isobarik":
        st.latex(r"W = P \cdot (V_2 - V_1)")
        P = st.number_input("P (Pa atau atm)", value=0.0)
        V1 = st.number_input("V1 (m³ atau L)", value=0.0)
        V2 = st.number_input("V2 (m³ atau L)", value=0.0)
        if st.button("Hitung Usaha Isobarik"):
            hasil = P * (V2 - V1)
            st.markdown(f"<div class='result'>W = {fmt(P)} × ({fmt(V2)} - {fmt(V1)}) = <b>{fmt(hasil)} J / L·atm</b></div>", unsafe_allow_html=True)

    # 12. PROSES ISOKHORIK
    elif menu == "Proses Isokhorik":
        st.latex(r"W = 0, \quad \Delta U = Q = n \cdot C_v \cdot \Delta T")
        st.info("Catatan Slide: Pada proses Isokhorik volume konstan, Kerja (W) bernilai nol.")
        n = st.number_input("n (mol)", value=0.0)
        Cv = st.number_input("Cv (J/mol.K)", value=0.0)
        dT = st.number_input("ΔT (K)", value=0.0)
        if st.button("Hitung Energi"):
            hasil = n * Cv * dT
            st.markdown(f"<div class='result'>W = 0 <br> Q = ΔU = {fmt(n)} × {fmt(Cv)} × {fmt(dT)} = <b>{fmt(hasil)} Joule</b></div>", unsafe_allow_html=True)

    # 13. PROSES ISOTERMAL
    elif menu == "Proses Isotermal":
        st.latex(r"W = Q = n \cdot R \cdot T \cdot \ln\left(\frac{V_2}{V_1}\right)")
        R = 8.314  
        n = st.number_input("n (mol)", value=0.0)
        T = st.number_input("T (K)", value=0.0)
        V1 = st.number_input("V1", value=1.0)
        V2 = st.number_input("V2", value=1.0)
        if st.button("Hitung Kerja Isotermal"):
            import math
            if V1 != 0 and V2/V1 > 0:
                hasil = n * R * T * math.log(V2 / V1)
                st.markdown(f"<div class='result'>W = {fmt(n)} × {R} × {fmt(T)} × ln({fmt(V2)}/{fmt(V1)}) = <b>{fmt(hasil)} Joule</b></div>", unsafe_allow_html=True)
            else:
                st.error("Rasio ekspansi volume tidak memenuhi syarat logaritma.")

    # 14. EDUKASI ISOTOP GAS
    elif menu == "Edukasi Isotop Gas":
        st.markdown("""
        ### 🧪 Efek Isotop pada Sifat Termodinamika Gas
        Penggantian unsur dengan isotopnya yang lebih berat (misal $H_2 \rightarrow D_2$) akan mengubah sifat fisis makro zat tanpa mengganggu struktur konfigurasi elektron luarnya.
        
        #### Poin Teoretis Utama:
        1. **Kecepatan Efektif ($v_{rms}$):** Berbanding terbalik dengan akar massa molar ($M$). Partikel isotop berat bergerak lebih lambat pada kesetimbangan termal yang sama.
        $$v_{rms} = \sqrt{\frac{3RT}{M}}$$
        2. **Pergeseran Kapasitas Kalor:** Perubahan massa merubah momen inersia molekul serta tingkat energi vibrasi kuantumnya.
        """)
        
        st.write("")
        st.subheader("📊 Komputasi Nilai Efektif ($v_{rms}$) antar Isotop")
        
        pilihan_gas = st.selectbox(
            "Pilih Kelompok Gas / Isotop:",
            ["Hidrogen (H₂ vs D₂)", "Uranium Heksafluorida (²³⁵UF₆ vs ²³⁸UF₆)", "Uap Air (H₂O vs D₂O)"]
        )
        T_isotop = st.number_input("Suhu Sistem (K)", value=300.0, min_value=0.1)
        
        if pilihan_gas == "Hidrogen (H₂ vs D₂)":
            label_1, M1 = "Hidrogen Biasa ($H_2$)", 0.002016  
            label_2, M2 = "Deuterium ($D_2$)", 0.004028  
        elif pilihan_gas == "Uranium Heksafluorida (²³⁵UF₆ vs ²³⁸UF₆)":
            label_1, M1 = "²³⁵UF₆ Gas", 0.34903
            label_2, M2 = "²³⁸UF₆ Gas", 0.35204
        else:
            label_1, M1 = "Uap Air Biasa ($H_2O$)", 0.018015
            label_2, M2 = "Uap Air Berat ($D_2O$)", 0.020027

        if st.button("Hitung Rasio Kecepatan"):
            import math
            R = 8.314
            v1 = math.sqrt((3 * R * T_isotop) / M1)
            v2 = math.sqrt((3 * R * T_isotop) / M2)
            rasio = v1 / v2
            
            langkah = f"""
            <h4>Hasil Simulasi Presentasi ({fmt(T_isotop)} K):</h4>
            <ul>
                <li><b>{label_1}</b> ($M$ = {fmt(M1*1000)} g/mol) $\rightarrow$ $v_{{rms}}$ = <b>{fmt(v1)} m/s</b></li>
                <li><b>{label_2}</b> ($M$ = {fmt(M2*1000)} g/mol) $\rightarrow$ $v_{{rms}}$ = <b>{fmt(v2)} m/s</b></li>
            </ul>
            <hr style='border-top: 1px solid #e2e8f0;'>
            📌 <b>Kesimpulan Analisis:</b> Senyawa gas ringan ({label_1}) berdifusi <b>{fmt(rasio)} kali lebih cepat</b> dibanding isotop beratnya. Perbedaan properti kinetik gas akibat fraksionasi isotop termodinamika ini diaplikasikan langsung pada teknologi pemisahan membran nuklir.
            """
            st.markdown(f"<div class='result'>{langkah}</div>", unsafe_allow_html=True)
