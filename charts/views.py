import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

import plotly.plotly as py
import plotly.graph_objs as go
from datetime import datetime

class TickerChart(TemplateView):
    template_name = ""
    name = ""
    ticker = "STOR"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['symbol'] = self.ticker
        ts = TimeSeries(key='7UUDZNRH3NEXO77C', output_format='pandas')
        context['data'], context['meta_data'] = ts.get_intraday(symbol=self.ticker, interval='60min', outputsize='compact')
        return context

    def get_labels(self):

        return []

    def get_providers(self):
        """Return names of datasets."""

        return []

    def get_data(self):

        return [[]]
