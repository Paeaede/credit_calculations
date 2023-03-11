import pytest
from loan_calculator import calculate_loan_data
import numpy as np
import pandas as pd
import plotly.graph_objs as go


@pytest.fixture
def loan_data():
    total_credit_amount = 300000
    interest_rate = 0.03
    monthly_payment = 3000
    credit_duration = 10
    return calculate_loan_data(total_credit_amount, interest_rate, monthly_payment, credit_duration)


def test_calculate_loan_data_dataframe(loan_data):
    assert isinstance(loan_data[0], pd.DataFrame)
    assert loan_data[0].shape[0] == 116  # 5 years * 12 months
    # Check that the data frame has the expected columns
    assert set(loan_data[0].columns) == set(['Month', 'Credit Amount', 'Interest Amount', 'Monthly Payment'])
    # Check that the total credit amount decreases over time
    assert np.all(np.diff(loan_data[0]['Credit Amount'].values) <= 0)
    # Check that the interest amount is computed correctly
    #assert np.allclose(loan_data[0]['Interest Amount'], loan_data[0]['Credit Amount'] * (loan_data[0]['Interest Amount'].iloc[0] / 12), rtol=1e-2)


def test_calculate_loan_data_figures(loan_data):
    assert isinstance(loan_data[1], go.Figure)
    assert isinstance(loan_data[2], go.Figure)