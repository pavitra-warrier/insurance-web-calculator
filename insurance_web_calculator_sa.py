import streamlit as st

# Set blue and white theme using Streamlit config
st.set_page_config(
    page_title="Life Insurance Requirement Calculator",
    page_icon="💡",
    layout="centered",
    initial_sidebar_state="auto"
)

# Custom CSS for blue and white theme
st.markdown("""
    <style>
        body, .stApp {
            background-color: #f6fbff;
        }
        .stButton>button {
            background-color: #1976d2;
            color: white;
            font-weight: bold;
        }
        .st-bb {
            color: #1976d2;
        }
        .st-cb {
            color: #1976d2;
        }
        .st-dc {
            color: #1976d2;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='color: #1976d2; text-align: center;'>💡 Life Insurance Requirement Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #1976d2;'>Estimate your ideal insurance cover in minutes</h4>", unsafe_allow_html=True)

# 1. Basic Information
st.header("1. Basic Information")
age = st.number_input("Your Age:")
gender = st.selectbox("Gender:", ["Select...", "Male", "Female", "Other"])
occupation_type = st.selectbox("Occupation Type:", ["Select...", "Salaried", "Self-Employed", "Business Owner", "Other"])
marital_status = st.selectbox("Marital Status:", ["Select...", "Single", "Married"])
spouse_age = st.number_input("Spouse’s Age:")
children_age = st.text_input("Children’s Age (comma separated if more than one):")
parents_age = st.text_input("Parent’s Age (comma separated if more than one):")

# 2. Monthly Expenses & Liabilities
st.header("2. Monthly Expenses & Liabilities")
monthly_expenses = st.number_input("Monthly Expenses (Living Costs):")
home_loan = st.number_input("Home Loan Amount:")
personal_loan = st.number_input("Personal/Car Loan Amount:")
business_loan = st.number_input("Business Loan Amount:")

# 3. Future Expenses
st.header("3. Future Expenses")
education_fund = st.number_input("Children’s Education Fund:")
marriage_fund = st.number_input("Children’s Marriage Fund:")
retirement_expenses = st.number_input("Monthly Expenses During Retirement:")
parents_expenses = st.number_input("Elderly Parents’ Medical & Living Expenses:")

# 4. Existing Assets
st.header("4. Existing Assets")
fixed_deposits = st.number_input("Fixed Deposits:")
mutual_funds = st.number_input("Mutual Funds:")
stocks_bonds = st.number_input("Stocks & Bonds:")
real_estate = st.number_input("Real Estate:")
epf_nps = st.number_input("EPF/NPS/PPF Savings:")
existing_insurance = st.number_input("Existing Life Insurance Cover:")
current_income = st.number_input("Current Annual Income:")

# 5. Assumptions
st.header("5. Assumptions")
life_expectancy = st.number_input("Your Life Expectancy:")
spouse_life_expectancy = st.number_input("Spouse’s Life Expectancy:")
standard_of_living = st.text_input("Standard of Living (e.g., Basic, Moderate, Luxurious):")
annual_raise_income = st.number_input("Annual Raise Rate in Income (%):")
annual_raise_expenses = st.number_input("Annual Raise Rate in Expenses (%):")
coverage_duration = st.number_input("Coverage Duration (years):")
passive_income = st.number_input("Passive Income (Rental, Dividends):")
inflation_rate = st.slider("Inflation Rate (%):", 0.0, 15.0, 6.0)
expected_return = st.slider("Expected Investment Return Rate (%):", 0.0, 20.0, 8.0)

# Calculation logic
if st.button("Calculate Insurance Requirement"):
    # Validate dropdowns
    if gender == "Select..." or occupation_type == "Select..." or marital_status == "Select...":
        st.warning("Please select your Gender, Occupation Type, and Marital Status.")
    else:
        # Expense Based Calculations
        eligible_years = life_expectancy - age
        B = monthly_expenses * 12 * eligible_years
        C = education_fund + marriage_fund
        D = home_loan + personal_loan + business_loan
        E = B + C + D - existing_insurance
        F = fixed_deposits + mutual_funds + stocks_bonds + real_estate + epf_nps
        G = E - F

        # Income Based Calculations
        I = current_income * 16.65

        st.markdown("---")
        st.markdown(f"<h3 style='color: #1976d2;'>Expense-Based Insurance Required: ₹ {round(G, 2):,.2f}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: #1976d2;'>Income-Based Insurance Required: ₹ {round(I, 2):,.2f}</h3>", unsafe_allow_html=True)
        st.info("You may choose the higher of the two values above as your ideal insurance cover.")

