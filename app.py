import streamlit as st
from pdf_processor import extract_pdf_data
from ai_engine import generate_ddr

st.set_page_config(
    page_title="AI DDR Generator",
    layout="wide"
)

st.title("🏠 AI Detailed Diagnostic Report Generator")

st.write("Upload inspection and thermal reports to generate a professional DDR report.")

col1, col2 = st.columns(2)

with col1:
    inspection_file = st.file_uploader("Upload Inspection Report", type=["pdf"])

with col2:
    thermal_file = st.file_uploader("Upload Thermal Report", type=["pdf"])

if st.button("Generate DDR Report"):

    with st.spinner("Analyzing documents with AI..."):

        inspection_text, inspection_images = extract_pdf_data(inspection_file)
        thermal_text, thermal_images = extract_pdf_data(thermal_file)

        report = generate_ddr(inspection_text, thermal_text)

        st.success("Report Generated Successfully")

        st.subheader("Generated DDR Report")

        st.write(report)

        st.subheader("Extracted Images")

        for img in inspection_images + thermal_images:
            st.image(img)