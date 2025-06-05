import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Life Insurance Requirement Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="auto"
)

# ---- CUSTOM CSS FOR THEME AND INPUTS ----
st.markdown("""
    <style>
    .stApp {
        background-color: #e6f0fa !important;
    }
    /* Make all input fields white with blue text */
    input, textarea, .stNumberInput input, .stTextInput input {
        background-color: #ffffff !important;
        color: #003366 !important;
    }
    /* Style increment/decrement buttons: white bg, blue icon, NO border */
    .stNumberInput button {
        background-color: #ffffff !important;
        color: #1976d2 !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }
    .stNumberInput button:focus, .stNumberInput button:active {
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }
    .stNumberInput button svg {
        fill: #1976d2 !important;
        color: #1976d2 !important;
    }
    /* Make dropdowns white with blue border and text */
    .stSelectbox>div>div {
        background-color: #ffffff !important;
        color: #003366 !important;
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
    /* Make dropdown options light (remove dark mode) */
    div[data-baseweb="popover"] {
        background-color: #ffffff !important;
        color: #003366 !important;
    }
    div[data-baseweb="popover"] [role="option"] {
        background-color: #ffffff !important;
        color: #003366 !important;
    }
    /* Make all labels blue */
    label, .css-1cpxqw2 {
        color: #1976d2 !important;
        font-weight: 600 !important;
    }
    /* Headings */
    h1, h2, h3, h4, h5 {
        color: #1976d2 !important;
    }
    .stButton>button {
        background-color: #1976d2 !important;
        color: white !important;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- PAGE NAVIGATION ----
if "page" not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

st.title("Life Insurance Requirement Calculator")

# ---- PAGE 1: Basic Information ----
if st.session_state.page == 1:
    st.header("1. Basic Information")
    age = st.number_input("Enter your age:", value=None, placeholder="Type your age...")
    gender = st.selectbox("Select your gender:", ["Select", "Male", "Female", "Other"])
    occupation_type = st.selectbox(
        "Select your occupation type:",
        ["Select", "Salaried", "Self-Employed", "Business Owner", "Other"]
    )
    marital_status = st.selectbox("Select your marital status:", ["Select", "Single", "Married"])
    spouse_age = st.number_input("Enter your spouse’s age (if applicable):", value=None, placeholder="Type spouse's age...")
    children_age = st.text_input("Enter children's ages (comma separated, if any):")
    parents_age = st.text_input("Enter parents’ ages (comma separated, if any):")
    st.button("Next", on_click=next_page, type="primary")

# ---- PAGE 2: Expenses & Liabilities ----
elif st.session_state.page == 2:
    st.header("2. Monthly Expenses & Liabilities")
    monthly_expenses = st.number_input("Current monthly expenses (living costs):", value=None, placeholder="Type monthly expenses...")
    home_loan = st.number_input("Home Loan amount:", value=None, placeholder="Type home loan amount...")
    personal_loan = st.number_input("Personal/Car Loan amount:", value=None, placeholder="Type personal/car loan amount...")
    business_loan = st.number_input("Business Loan amount:", value=None, placeholder="Type business loan amount...")
    col1, col2 = st.columns([1,1])
    with col1:
        st.button("Previous", on_click=prev_page)
    with col2:
        st.button("Next", on_click=next_page, type="primary")

# ---- PAGE 3: Future Expenses ----
elif st.session_state.page == 3:
    st.header("3. Future Expenses")
    education_fund = st.number_input("Children's Education Fund:", value=None, placeholder="Type education fund amount...")
    marriage_fund = st.number_input("Children's Marriage Fund:", value=None, placeholder="Type marriage fund amount...")
    retirement_expenses = st.number_input("Monthly expenses during retirement:", value=None, placeholder="Type retirement expenses...")
    parents_expenses = st.number_input("Elderly parents’ medical & living expenses:", value=None, placeholder="Type parents' expenses...")
    col1, col2 = st.columns([1,1])
    with col1:
        st.button("Previous", on_click=prev_page)
    with col2:
        st.button("Next", on_click=next_page, type="primary")

# ---- PAGE 4: Existing Assets & Income ----
elif st.session_state.page == 4:
    st.header("4. Existing Assets & Income")
    fixed_deposits = st.number_input("Fixed Deposits:", value=None, placeholder="Type fixed deposits amount...")
    mutual_funds = st.number_input("Mutual Funds:", value=None, placeholder="Type mutual funds amount...")
    stocks_bonds = st.number_input("Stocks & Bonds:", value=None, placeholder="Type stocks & bonds amount...")
    real_estate = st.number_input("Real Estate:", value=None, placeholder="Type real estate amount...")
    epf_nps = st.number_input("EPF/NPS/PPF Savings:", value=None, placeholder="Type EPF/NPS/PPF savings...")
    existing_insurance = st.number_input("Existing Life Insurance Cover:", value=None, placeholder="Type existing insurance cover...")
    current_income = st.number_input("Current Annual Income:", value=None, placeholder="Type current annual income...")
    col1, col2 = st.columns([1,1])
    with col1:
        st.button("Previous", on_click=prev_page)
    with col2:
        st.button("Next", on_click=next_page, type="primary")

# ---- PAGE 5: Assumptions & Calculate ----
elif st.session_state.page == 5:
    st.header("5. Assumptions")
    life_expectancy = st.number_input("Your expected life expectancy:", value=None, placeholder="Type your life expectancy...")
    spouse_life_expectancy = st.number_input("Spouse’s expected life expectancy:", value=None, placeholder="Type spouse's life expectancy...")
    standard_of_living = st.selectbox("Standard of Living:", ["Select", "Basic", "Moderate", "High"])
    annual_raise_income = st.number_input("Annual raise rate in income (%):", value=None, placeholder="Type annual raise in income...")
    annual_raise_expenses = st.number_input("Annual raise rate in expenses (%):", value=None, placeholder="Type annual raise in expenses...")
    coverage_duration = st.number_input("Coverage duration (years):", value=None, placeholder="Type coverage duration...")
    passive_income = st.number_input("Annual passive income (rental, dividends):", value=None, placeholder="Type passive income...")
    inflation_rate = st.number_input("Inflation Rate (%):", value=None, placeholder="Type inflation rate...")
    investment_return_rate = st.number_input("Expected Investment Return Rate (%):", value=None, placeholder="Type expected investment return rate...")
    st.button("Previous", on_click=prev_page)

    # Show Calculate button and results
    if st.button("Calculate Insurance Requirement", type="primary"):
        # Convert None to 0 for calculation
        def nz(x):
            return x if x is not None else 0
        eligible_years = nz(life_expectancy) - nz(age)
        B = nz(monthly_expenses) * 12 * eligible_years
        C = nz(education_fund) + nz(marriage_fund)
        D = nz(home_loan) + nz(personal_loan) + nz(business_loan)
        E = B + C + D - nz(existing_insurance)
        F = nz(fixed_deposits) + nz(mutual_funds) + nz(stocks_bonds) + nz(real_estate) + nz(epf_nps)
        G = E - F

        # Income Based Calculation
        I = nz(current_income) * 16.65

        st.subheader("Results")
        st.write(f"**Estimated Insurance Required (Expense-Based, ₹):** {round(G, 2):,.2f}")
        st.write(f"**Estimated Insurance Required (Income-Based, ₹):** {round(I, 2):,.2f}")

        st.info(
            "The higher of the two values above is generally considered a prudent insurance requirement, "
            "but you may adjust based on your specific needs and financial goals."
        )
