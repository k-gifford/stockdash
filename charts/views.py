import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from alpha_vantage.timeseries import TimeSeries

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
        data, meta_data = ts.get_intraday(symbol=self.ticker, interval='60min', outputsize='full')

        data = data.to_json()
        print(data)
        self.context['data'] = data
        # self.context['close'] = data['1. close']
        # self.context['high'] = data['
        # print(self.context['index'])


        return self.context
