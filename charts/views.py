from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from alpha_vantage.timeseries import TimeSeries
import pandas as pd

class TickerChart(TemplateView):
    template_name = ""
    name = ""
    ticker = "STOR"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['symbol'] = self.ticker
        ts = TimeSeries(key='7UUDZNRH3NEXO77C', output_format='pandas')
        context['data'], context['meta_data'] = ts.get_intraday(symbol=self.ticker, interval='1min', outputsize='full')
        # data['4. close'].plot()
        # plt.title('Intraday Times Series for the MSFT stock (1 min)')
        # plt.show()
        return context
