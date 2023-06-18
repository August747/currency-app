from django.shortcuts import render

from currency.services import ExchangeRatesService


def index(request):
    service = ExchangeRatesService()
    rates = service.get_rates()
    print(rates)
    rates.save()
    return render(request, 'core/index.html')
