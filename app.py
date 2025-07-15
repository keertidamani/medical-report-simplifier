import streamlit as st
from simplify import simplify_medical_text
from parser import extract_text_from_pdf, extract_text_from_image

st.set_page_config(
    page_title="Medical Report Simplifier",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "About": "Built by Keerti Damani"
    }
)

st.title("Medical Report Simplifier")
st.markdown("This tool helps you understand complex medical reports by converting them into simple language you can easily grasp. You can input the report in three different ways below.")

input_method = st.radio(
    label="Choose your input method:",
    options=["Text", "PDF", "Image"],
    horizontal=False,
    index=0,
    help="Select how you want to provide your medical report"
)

text_input = ""

if input_method == "Text":
    st.write("You have chosen to paste your report directly as plain text.")
    text_input = st.text_area(
        label="Paste your report content here:",
        placeholder="Enter the medical report text...",
        height=200,
        max_chars=None,
        key="text_input_area"
    )

elif input_method == "PDF":
    st.write("You have chosen to upload a PDF file.")
    pdf_file = st.file_uploader(
        label="Upload your PDF report",
        type=["pdf"],
        accept_multiple_files=False,
        key="pdf_uploader"
    )
    if pdf_file is not None:
        text_input = extract_text_from_pdf(pdf_file)

elif input_method == "Image":
    st.write("You have chosen to upload a scanned image or handwritten report.")
    image_file = st.file_uploader(
        label="Upload your image file",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False,
        key="image_uploader"
    )
    if image_file is not None:
        st.image(
            image=image_file,
            caption="Uploaded Medical Report",
            use_column_width=True
        )
        text_input = extract_text_from_image(image_file)
        if "❌" in text_input or not text_input.strip():
            st.warning("Could not extract text. Try using a clearer image or better handwriting.")
            text_input = ""

if text_input:
    st.subheader("Extracted Text From Report")
    st.code(body=text_input, language="markdown")

    simplify_button = st.button(
        label="Simplify Report",
        key="simplify_button"
    )

    if simplify_button:
        with st.spinner("Processing and simplifying your report..."):
            result = simplify_medical_text(text_input)
            st.success("Here is your simplified report:")
            st.write(result)

st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Developed by <strong>Keerti Damani</strong> | © 2025</p>",
    unsafe_allow_html=True
)
