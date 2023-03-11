import streamlit as st
from loan_calculator import calculate_loan_data, plot_remaining_credit


def main():
    st.set_page_config(layout="wide", page_title='Loan Calculator', page_icon=':money_with_wings:')
    st.title('Loan Calculator')

    with st.sidebar:
        total_credit_amount = st.number_input('Total Credit Amount', min_value=50000, max_value=600000, step=10000)
        interest_rate = st.slider('Interest Rate in Percent', min_value=1.0, max_value=5.0, value=3.0, step=0.1)
        monthly_payment = st.number_input('Monthly Payment', min_value=500, max_value=5000, step=50)
        credit_duration = st.slider('Credit Duration (Years)', min_value=5, max_value=20, value=10, step=1)
        yearly_target_repayment_rate = \
            st.slider('Repayment Rate (per year) in Percent', min_value=1.0, max_value=8.0, value=3.0, step=0.5)

    df, fig1, fig2 = calculate_loan_data(total_credit_amount, interest_rate/100, monthly_payment, credit_duration)

    st.write('## Credit Amount Over Time and Repayment Sum')
    st.plotly_chart(fig1)
    st.write('## Yearly Interest Amount')
    st.plotly_chart(fig2)

    st.write('## Credit Amount Table')
    st.write(df)

    # not exactly what it should calculate -> does not neglect interest rate
    fig3 = plot_remaining_credit(total_credit_amount, interest_rate, yearly_target_repayment_rate, credit_duration)
    st.write('## Remaining Credit with fixed "Tilgungsrate"')
    st.plotly_chart(fig3)


   # col1, col2 = st.columns([2, 2])

    # col1.subheader("A wide column with a chart")
    # col1.plotly_chart(fig1)

    # col2.subheader("A narrow column with the data")
    # col2.plotly_chart(fig2)


if __name__ == '__main__':
    main()

# EOF
