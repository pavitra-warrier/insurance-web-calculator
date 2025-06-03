import streamlit as st

st.title("Life Insurance Requirement Calculator")

# Basic Information Section
st.header("Basic Information")
age = st.number_input("Enter your age:")

# Dropdowns with 'Select...' as the first option
gender = st.selectbox("Select your gender:", ["Select...", "Male", "Female", "Other"])
occupation_type = st.selectbox(
    "Select your occupation type:",
    ["Select...", "Salaried", "Self-Employed", "Business Owner", "Other"]
)
monthly_expenses = st.number_input("Enter your current monthly expenses:")
life_expectancy = st.number_input("Enter your expected life expectancy:")

# Understanding Liabilities Section
st.header("Understanding Liabilities")
home_loan = st.number_input("Home Loan amount:")
personal_loan = st.number_input("Personal/Car Loan amount:")
business_loan = st.number_input("Business Loan amount:")

# Future Expenses Section
st.header("Future Expenses")
education_fund = st.number_input("Children's Education Fund:")
marriage_fund = st.number_input("Children's Marriage Fund:")
retirement_expenses = st.number_input("Monthly expenses during retirement:")
parents_expenses = st.number_input("Parents’ Medical & Living Expenses:")

# Existing Assets Section
st.header("Existing Assets")
fixed_deposits = st.number_input("Fixed Deposits:")
mutual_funds = st.number_input("Mutual Funds:")
stocks_bonds = st.number_input("Stocks & Bonds:")
real_estate = st.number_input("Real Estate:")
epf_nps = st.number_input("EPF/NPS/PPF Savings:")
existing_insurance = st.number_input("Existing Life Insurance Cover:")

if st.button("Calculate Insurance Requirement"):
    # Check if user has selected a valid option
    if gender == "Select..." or occupation_type == "Select...":
        st.warning("Please select your gender and occupation type.")
    else:
        eligible_years = life_expectancy - age
        B = monthly_expenses * 12 * eligible_years
        C = education_fund + marriage_fund
        D = home_loan + personal_loan + business_loan
        E = B + C + D - existing_insurance
        F = fixed_deposits + mutual_funds + stocks_bonds + real_estate + epf_nps
        G = E - F

        st.success(f"Estimated Insurance Required (₹): {round(G, 2):,.2f}")
