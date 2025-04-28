import streamlit as st
import easyocr
import pandas as pd
import io

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Streamlit UI
st.title("OCR Extractor App")
st.write("Upload any image (meter reading, number plate, etc.) and extract text.")

uploaded_files = st.file_uploader(
    "Upload one or multiple images",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    results = []

    for uploaded_file in uploaded_files:
        # Read file as bytes
        bytes_data = uploaded_file.read()
        # Save temp file
        with open(uploaded_file.name, "wb") as f:
            f.write(bytes_data)

        # OCR extraction
        extracted_text = reader.readtext(uploaded_file.name, detail=0)

        # Show image + extracted text
        st.image(uploaded_file, caption=uploaded_file.name, width=350)
        st.write("**Extracted Text:**", extracted_text if extracted_text else "No text found")

        results.append({
            "Image Name": uploaded_file.name,
            "Extracted Text": " | ".join(extracted_text) if extracted_text else "No text detected"
        })

    # Save results to Excel in memory
    df = pd.DataFrame(results)
    excel_buffer = io.BytesIO()
    df.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)

    # Download button
    st.download_button(
        label="📥 Download Results as Excel",
        data=excel_buffer,
        file_name="OCR_results.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
