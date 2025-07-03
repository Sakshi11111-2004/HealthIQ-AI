import streamlit as st
from extractor import extract_pdf_text
from parser import parse_medical_values
from analyzer import analyze_values
from explainers import explain_value
from chart import generate_bar_chart

# Load styles
st.set_page_config(page_title="DocuSense AI", layout="wide")
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🩺 DocuSense AI – Medical Report Explainer")

file = st.file_uploader("📄 Upload your blood test PDF", type="pdf")
if file:
    text = extract_pdf_text(file)
    st.subheader("🧾 Raw Extracted Text")
    st.text_area("", text[:2000], height=200)

    values = parse_medical_values(text)
    st.subheader("✅ Auto-Detected Values")
    st.json(values)

    if values:
        analysis = analyze_values(values)
        st.subheader("📊 Health Summary")

        for k, info in analysis.items():
            block = "summary-good" if info["status"] == "Normal" else "summary-bad"
            st.markdown(f"<div class='{block} report-box'><strong>{k} – {info['status']}</strong><br>"
                        f"Value: {info['value']}<br>"
                        f"Range: {info['range'][0]} – {info['range'][1]}<br>"
                        f"Meaning: {info['meaning']}<br>"
                        f"Insight: {info['insight']}<br>"
                        f"💡 Tip: {info['tip']}</div>", unsafe_allow_html=True)

        st.subheader("📈 Visual Overview")
        chart_path = generate_bar_chart(values, analysis)
        st.image(chart_path, use_container_width=True)
    else:
        st.warning("⚠️ No recognized markers found.")
