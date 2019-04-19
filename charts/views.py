import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
import time
import pandas as pd

class TickerChart(TemplateView):
    template_name = ""
    name = ""
    ticker = "STOR"
    plot = ""


    def get_context_data(self, *args, **kwargs):
        self.context = super().get_context_data(*args, **kwargs)

        self.context['symbol'] = self.ticker
        ts = TimeSeries(key='7UUDZNRH3NEXO77C', output_format='pandas')
        data, meta_data = ts.get_intraday(symbol=self.ticker, interval='1min', outputsize='compact')

        self.context['index'] = []

        date_index = pd.to_datetime(data.index)
        date_index = date_index.to_pydatetime().tolist()
        for date in date_index:
            self.context['index'].append(int(time.mktime(date.timetuple())) * 1000)

        self.context['open'] = data['1. open'].tolist()
        self.context['high'] = data['2. high'].tolist()
        self.context['low'] = data['3. low'].tolist()
        self.context['close'] = data['4. close'].tolist()
        self.context['volume'] = data['5. volume'].tolist()

        return self.context
