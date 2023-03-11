import pandas as pd
import plotly.graph_objs as go

def calculate_loan_data(total_credit_amount, interest_rate, monthly_payment, credit_duration):
    remaining_credit_amount = total_credit_amount
    table_data = []
    year_credit_data = []
    year_interest_data = []
    year_repayment_data = []
    month = 0

    while remaining_credit_amount > 0 and month <= credit_duration * 12:
        month += 1
        interest_amount = remaining_credit_amount * (interest_rate / 12)
        remaining_credit_amount += interest_amount - monthly_payment

        if month % 12 == 0:
            year_credit_data.append(remaining_credit_amount)
            year_interest_data.append(sum([remaining_credit_amount * (interest_rate / 12) for i in range(12)]))
            year_repayment_data.append(sum([monthly_payment - remaining_credit_amount * (interest_rate / 12) for i in range(12)]))

        table_data.append(
            [month, round(remaining_credit_amount, 2), round(interest_amount, 2), round(monthly_payment, 2)])

    df = pd.DataFrame(table_data, columns=['Month', 'Credit Amount', 'Interest Amount', 'Monthly Payment'])
    year_labels = [f'{i} year' for i in range(1, credit_duration + 1)]

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=year_labels, y=year_credit_data, name='Credit Amount'))
    fig1.add_trace(go.Bar(x=year_labels, y=year_repayment_data, name='Yearly Repayment'))
    fig1.update_layout(title='Credit Amount Over Time', xaxis_title='Year', yaxis_title='Credit Amount',
                       legend=dict(yanchor="top", y=1.0, xanchor="left", x=0.75))

    fig2 = go.Figure(data=go.Bar(x=year_labels, y=year_interest_data))
    fig2.update_layout(title='Yearly Interest Amount', xaxis_title='Year', yaxis_title='Interest Amount')

    return df, fig1, fig2


def plot_remaining_credit(total_credit_amount, interest_rate, yearly_target_repayment_rate, credit_duration):
    """
    :param total_credit_amount:
    :param interest_rate:
    :param yearly_target_repayment_rate:
    :param credit_duration:
    :return:
    """

    remaining_credit_amount = total_credit_amount
    table_data = []
    year_credit_data = []
    year_labels = []

    for i in range(credit_duration):
        print(i)
        year_labels.append(f'Year {len(year_labels) + 1}')
        year_credit_data.append(remaining_credit_amount)
        yearly_interest_amount = remaining_credit_amount * (interest_rate / 100)
        yearly_repayment = total_credit_amount * (yearly_target_repayment_rate / 100)
        remaining_credit_amount += yearly_interest_amount - yearly_repayment
        table_data.append([len(year_labels), round(remaining_credit_amount, 2)])

    df = pd.DataFrame(table_data, columns=['Year', 'Remaining Credit Amount'])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Remaining Credit Amount'], mode='lines+markers'))
    fig.update_layout(title='Remaining Credit Amount Over Time', xaxis_title='Year',
                      yaxis_title='Remaining Credit Amount')

    return fig

