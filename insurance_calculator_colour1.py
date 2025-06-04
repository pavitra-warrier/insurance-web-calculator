import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Life Insurance Requirement Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="auto"
)

# ---- CUSTOM CSS FOR SOLID BLUE AND WHITE THEME ----
st.markdown("""
    <style>
    .stApp {
        background-color: #e6f0fa !important;   /* Solid very light blue */
    }
    .stButton>button {
        background-color: #1976d2 !important;
        color: white !important;
        border-radius: 5px;
    }
    .stNumberInput>div>input, .stTextInput>div>input, .stSelectbox>div>div {
        background-color: #ffffff !important;
        color: #003366 !important;
    }
    .stSelectbox>div>div {
        border: 1.5px solid #1976d2 !important;
        border-radius: 5px !important;
        background-image: url("data:image/svg+xml;utf8,<svg fill='blue' height='20' viewBox='0 0 24 24' width='20' xmlns='http://www.w3.org/2000/svg'><path d='M7 10l5 5 5-5z'/></svg>");
        background-repeat: no-repeat;
        background-position: right 10px center;
        background-size: 20px;
    }
    .stSelectbox>div>div>div {
        color: #003366 !important;
    }
    h1, h2, h3, h4, h5 {
        color: #1976d2 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---- FORCE LIGHT THEME ----
st.markdown(
    """
    <script>
    if (window.parent !== window) {
        window.parent.document.body.setAttribute('data-theme', 'light');
    }
    </script>
    """,
    unsafe_allow_html=True
)

st.title("Life Insurance Requirement Calculator")

# 1. Basic Information Section
st.header("1. Basic Information")
age = st.number_input("Enter your age:")
gender = st.selectbox("Select your gender:", ["Select", "Male", "Female", "Other"])
occupation_type = st.selectbox(
    "Select your occupation type:",
    ["Select", "Salaried", "Self-Employed", "Business Owner", "Other"]
)
marital_status = st.selectbox("Select your marital status:", ["Select", "Single", "Married"])
spouse_age = st.number_input("Enter your spouse’s age (if applicable):")
children_age = st.text_input("Enter children's ages (comma separated, if any):")
parents_age =
