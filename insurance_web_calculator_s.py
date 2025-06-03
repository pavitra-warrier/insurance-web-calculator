import streamlit as st

def calculate_insurance():
    st.title("Life Insurance Requirement Calculator")

    # Basic Information
    age = st.number_input("Enter your age:")
    gender = st.text_input("Enter your gender (Male/Female/Other):")
    occupation_type = st.text_input("Enter your occupation_type (Salaried/Self-Employed/Business Owner):")
    monthly_expenses = st.number_input("Enter your current monthly expenses:")
    life_expectancy  = st.number_input("Enter your life expectancy:")

    # Understanding Liabilities
    home_loan = st.number_input("Home Loan amount:")
    personal_loan = st.number_input("Personal/Car Loan amount:")
    business_loan = st.number_input("Business Loan amount:")

    # Future Expenses
    education_fund = st.number_input("Children's Education Fund:")
    marriage_fund = st.number_input("Children's Marriage Fund:")
    retirement_expenses = st.number_input("Monthly expenses during retirement:")
    parents_expenses = st.number_input("Parents’ Medical & Living Expenses:")

    # Existing Assets
    fixed_deposits = st.number_input("Fixed Deposits:")
    mutual_funds = st.number_input("Mutual Funds:")
    stocks_bonds = st.number_input("Stocks & Bonds:")
    real_estate = st.number_input("Real Estate:")
    epf_nps = st.number_input("EPF/NPS/PPF Savings:")
    existing_insurance = st.number_input("Existing Life Insurance Cover:")

    if st.button("Calculate Insurance Requirement"):
        # Calculations
        eligible_years = life_expectancy - age
        B = monthly_expenses * 12 * eligible_years
        C = education_fund + marriage_fund
        D = home_loan + personal_loan + business_loan
        E = B + C + D - existing_insurance
        F = fixed_deposits + mutual_funds + stocks_bonds + real_estate + epf_nps
        G = E - F

        st.write("\nEstimated Insurance Required (₹):", round(G, 2))

if __name__ == "__main__":
    calculate_insurance()
