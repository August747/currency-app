from django.shortcuts import render

from currency.services import ExchangeRatesService
from currency.models import ExchangeRate, ExchangeRateProvider


def index(request):
    service = ExchangeRatesService()
    rates = service.get_rates()

    provider = ExchangeRateProvider.objects.create(name='PrivatBank',
                                                   api_url='https://api.privatbank.ua/p24api/exchange_rates')

    for rate in rates:
        base_currency = rate['currency']
        currencies = rate.get('currencies', [])
        for currency in currencies:
            ExchangeRate.objects.create(
                base_currency=base_currency,
                currency=currency['currency'],
                sale_rate=currency['saleRate'],
                buy_rate=currency['purchaseRate'],
                provider=provider
            )

    return render(request, 'core/index.html')
