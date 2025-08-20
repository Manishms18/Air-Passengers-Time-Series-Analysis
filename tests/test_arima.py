import numpy as np
from statsmodels.tsa.arima.model import ARIMA

def test_arima_fit_and_forecast_length():
    # tiny synthetic seasonal-ish series
    y = np.array([112,118,132,129,121,135,148,148,136,119,104,118], dtype=float)
    model = ARIMA(y, order=(1,1,1))
    res = model.fit()
    fc = res.forecast(steps=6)
    assert len(fc) == 6 and np.isfinite(fc).all()
