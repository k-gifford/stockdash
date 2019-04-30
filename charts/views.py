import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
import pandas as pd
import json

class TickerChart(TemplateView):
    template_name = ""
    name = ""
    ticker = "STOR"
    plot = ""


    def get_context_data(self, *args, **kwargs):
        self.context = super().get_context_data(*args, **kwargs)

        self.context['symbol'] = self.ticker
        ts = TimeSeries(key='7UUDZNRH3NEXO77C', output_format='pandas')
        data, meta_data = ts.get_intraday(symbol=self.ticker, interval='60min', outputsize='compact')

        open = data['1. open'].tolist()
        high = data['2. high'].tolist()
        low = data['3. low'].tolist()
        close = data['4. close'].tolist()
        volume = data['5. volume'].tolist()

        # date_index = (pd.to_datetime(data.index)).to_pydatetime().tolist()
        date_index = [d.__str__() for d in pd.to_datetime(data.index)]

        d = dict() # dates in JSON
        pos = 0
        while pos < len(date_index):
            new_date = date_index[pos]
            d[new_date] = {'open': open[pos],
                            'high': high[pos],
                            'low': low[pos],
                            'close': close[pos],
                            'volume': volume[pos]}
            pos+=1

        self.context['payload'] = json.dumps(d)

        return self.context



#
