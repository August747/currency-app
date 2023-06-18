import requests


class ExchangeRatesService:

    def get_rates(self):
        url = 'https://api.privatbank.ua/p24api/exchange_rates'

        params = {
            'date': '11.01.2023'
        }

        response = requests.get(url, params=params)
        data = response.json()
        return data
