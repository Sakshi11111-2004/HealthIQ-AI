# 🩺 DocuSense AI – Medical Report Explainer

DocuSense AI is an AI-powered Streamlit app that analyzes PDF medical reports (like blood tests) and provides:
- ✅ Auto-extracted health values
- 🧠 Simple, human-friendly health summaries
- 📊 Visual bar charts of markers (Hemoglobin, LDL, Vitamin B12, etc.)
- 💡 Personalized health tips

---

## 🛠️ Features
- Upload any blood test PDF report
- Extracts values like Hemoglobin, RBC, LDL, HDL, HbA1c, Vitamin B12, Platelet Count, etc.
- Matches against normal medical ranges
- Flags High / Low / Normal status with colored summaries
- Shows interactive bar chart with warning zones
- Clean, minimal UI powered by Streamlit

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/docusense-ai.git
cd docusense-ai

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
