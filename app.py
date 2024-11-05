import streamlit as st

# Title
st.title("DOGE for Developers")

# Input Box
input_text = st.text_area(
    label="Input",
    placeholder="Input message here ..."
)

# Attach Files 
uploaded_file = st.file_uploader("Attached Files:", type=["jpg", "jpeg", "png", "pdf"])
if uploaded_file is not None:
    st.write("File uploaded successfully!")

# Outputs Range Slider
selected_range = st.slider("Number of Outputs", 1, 5, 3)
st.write(f"{selected_range} outputs")


# Output Dropdown
options = ["Output 1", "Output 2", "Output 3", "Output 4", "Output 5"]
selected_option = st.selectbox(
    "Select Output",       
    options,               
    index=0,                 
)

# Tool Creation Output
st.text_area(
    label="Model: GPT 3.5",
    value="To add a new tool to the terminal, please ..."
)

# Output Files
st.text_area(
    label="Output Files",
    value="Output files are downloaded here",
    height=100
)

# Run Button
st.markdown(
    """
    <style>
    .stButton > button {
        color: white;
        background-color: #007bff;
        font-size: 16px;
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        padding: 8px 16px;
        border-radius: 8px;
        line-height: 22.4px;
        cursor: pointer;
        border: none;
        text-align: center;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)
run_button = st.button("Run")
