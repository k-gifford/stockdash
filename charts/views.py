from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView


class TickerChart(TemplateView):
    template_name = ""
    name = ""
    ticker = ""
