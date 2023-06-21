import datetime

import requests


class ExchangeRatesService:
    def get_rates(self):
        url = 'https://api.privatbank.ua/p24api/exchange_rates'

        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2023, 1, 20)

        rates = []

        current_date = start_date
        while current_date <= end_date:
            params = {
                'date': current_date.strftime('%d.%m.%Y')
            }

            response = requests.get(url, params=params)
            data = response.json()

            rates.extend(data['exchangeRate'])

            current_date += datetime.timedelta(days=1)

        return rates
