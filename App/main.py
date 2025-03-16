import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# Page Configuration
st.set_page_config(page_title="Lauki Finance: Credit Risk Modelling", page_icon="📊", layout='wide')

# Custom CSS for Styling
st.markdown("""
    <style>
    .stApp { 
        background-color: #f7f9fc;
        font-family: Arial, sans-serif;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #2E7D32;
        margin-bottom: 20px;
    }
    .result-section {
        background-color: #E3F2FD;
        border-left: 6px solid #2E7D32;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .result-section p {
        font-size: 18px;
        margin: 5px 0;
    }
    .highlight {
        font-weight: bold;
        color: #2E7D32;
        font-size: 20px;
    }
    .rating-excellent {color: #2E7D32; font-weight: bold; font-size: 20px;}
    .rating-good {color: #1976D2; font-weight: bold; font-size: 20px;}
    .rating-average {color: #FFA726; font-weight: bold; font-size: 20px;}
    .rating-poor {color: #D32F2F; font-weight: bold; font-size: 20px;}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">Lauki Finance: Credit Risk Modelling</div>', unsafe_allow_html=True)

# Input Section
with st.container():
    st.markdown("### Borrower Information")
    with st.form("credit_risk_form"):

        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
        with col2:
            income = st.number_input('Income', min_value=0, value=1200000)
        with col3:
            loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)

        col4, col5, col6 = st.columns(3)
        with col4:
            loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
        with col5:
            avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)
        with col6:
            delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)

        col7, col8, col9 = st.columns(3)
        with col7:
            credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1, value=30)
        with col8:
            num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)
        with col9:
            loan_to_income_ratio = loan_amount / income if income > 0 else 0
            st.text(f"Loan to Income Ratio:")
            st.text(f"{loan_to_income_ratio:.2f}")
        col10, col11, col12 = st.columns(3)
        with col10:
            residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
        with col11:
            loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
        with col12:
            loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

        submit_button = st.form_submit_button("Calculate Risk")

# Result Section
if submit_button:
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    with st.container():
        st.markdown("### Prediction Results")
        # Color-coded risk rating
        if rating == "Excellent":
            st.markdown(f"<p class='rating-excellent'>🏅 Rating: {rating}</p>", unsafe_allow_html=True)
        elif rating == "Good":
            st.markdown(f"<p class='rating-good'>👍 Rating: {rating}</p>", unsafe_allow_html=True)
        elif rating == "Average":
            st.markdown(f"<p class='rating-average'>⚠️ Rating: {rating}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='rating-poor'>❗ Rating: {rating}</p>", unsafe_allow_html=True)

        st.markdown(f"""
            <div class='result-section'>
                <p><b>✅ Risk Calculation Complete!</b></p>
                <p><b>Default Probability:</b> <span class='highlight'>{probability:.2%}</span></p>
                <p><b>Credit Score:</b> <span class='highlight'>{credit_score}</span></p>
        """, unsafe_allow_html=True)


        st.markdown("</div>", unsafe_allow_html=True)
