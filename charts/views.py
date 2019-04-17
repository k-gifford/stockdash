import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

import plotly.plotly as py
import plotly.graph_objs as go
from datetime import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html

from django_plotly_dash import DjangoDash

from django.views.decorators.clickjacking import xframe_options_exempt

class TickerChart(TemplateView):
    template_name = ""
    name = ""
    ticker = "STOR"
    plot = ""


    def get_context_data(self, *args, **kwargs):
        self.context = super().get_context_data(*args, **kwargs)

        dash_app = self.get_dash_layout()
        self.context['plot'] = dash_app
        print(self.context)
        return self.context


    @xframe_options_exempt
    def get_dash_layout(self):
        self.context['symbol'] = self.ticker
        ts = TimeSeries(key='7UUDZNRH3NEXO77C', output_format='pandas')
        self.context['data'], self.context['meta_data'] = ts.get_intraday(symbol=self.ticker, interval='60min', outputsize='compact')

        info = self.context['data']

        # data = [trace]

        # return py.plot(data, filename='simple_candlestick')
        app = DjangoDash('dash-chart-app')

        app.layout = html.Div([
            dcc.Graph(
                figure = go.Figure(
                    data=[
                        go.Ohlc(
                            x=info.index,
                            open=info['1. open'].values,
                            high=info['2. high'].values,
                            low=info['3. low'].values,
                            close=info['4. close'].values
                        )
                    ]
                ),
                style={'height':300},
                id='dash-chart'
            )
        ])
        return app
