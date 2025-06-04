import streamlit as st

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
parents_age = st.text_input("Enter parents’ ages (comma separated, if any):")

# 2. Monthly Expenses & Liabilities
st.header("2. Monthly Expenses & Liabilities")
monthly_expenses = st.number_input("Current monthly expenses (living costs):")
home_loan = st.number_input("Home Loan amount:")
personal_loan = st.number_input("Personal/Car Loan amount:")
business_loan = st.number_input("Business Loan amount:")

# 3. Future Expenses
st.header("3. Future Expenses")
education_fund = st.number_input("Children's Education Fund:")
marriage_fund = st.number_input("Children's Marriage Fund:")
retirement_expenses = st.number_input("Monthly expenses during retirement:")
parents_expenses = st.number_input("Elderly parents’ medical & living expenses:")

# 4. Existing Assets & Income
st.header("4. Existing Assets & Income")
fixed_deposits = st.number_input("Fixed Deposits:")
mutual_funds = st.number_input("Mutual Funds:")
stocks_bonds = st.number_input("Stocks & Bonds:")
real_estate = st.number_input("Real Estate:")
epf_nps = st.number_input("EPF/NPS/PPF Savings:")
existing_insurance = st.number_input("Existing Life Insurance Cover:")
current_income = st.number_input("Current Annual Income:")

# 5. Assumptions
st.header("5. Assumptions")
life_expectancy = st.number_input("Your expected life expectancy:")
spouse_life_expectancy = st.number_input("Spouse’s expected life expectancy:")
standard_of_living = st.selectbox("Standard of Living:", ["Select", "Basic", "Moderate", "High"])
annual_raise_income = st.number_input("Annual raise rate in income (%):")
annual_raise_expenses = st.number_input("Annual raise rate in expenses (%):")
coverage_duration = st.number_input("Coverage duration (years):")
passive_income = st.number_input("Annual passive income (rental, dividends):")
inflation_rate = st.number_input("Inflation Rate (%):")
investment_return_rate = st.number_input("Expected Investment Return Rate (%):")

if st.button("Calculate Insurance Requirement"):
    # Validation for dropdowns
    if (
        gender == "Select"
        or occupation_type == "Select"
        or marital_status == "Select"
        or standard_of_living == "Select"
    ):
        st.warning("Please select all required dropdown options.")
    else:
        # Expense Based Calculations
        eligible_years = life_expectancy - age
        B = monthly_expenses * 12 * eligible_years
        C = education_fund + marriage_fund
        D = home_loan + personal_loan + business_loan
        E = B + C + D - existing_insurance
        F = fixed_deposits + mutual_funds + stocks_bonds + real_estate + epf_nps
        G = E - F

        # Income Based Calculation
        I = current_income * 16.65

        st.subheader("Results")
        st.write(f"**Estimated Insurance Required (Expense-Based, ₹):** {round(G, 2):,.2f}")
        st.write(f"**Estimated Insurance Required (Income-Based, ₹):** {round(I, 2):,.2f}")

        st.info(
            "The higher of the two values above is generally considered a prudent insurance requirement, "
            "but you may adjust based on your specific needs and financial goals."
        )
