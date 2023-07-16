import datetime
import requests
from concurrent.futures import ThreadPoolExecutor


class ExchangeRatesService:
    def get_rate_for_date(self, date):
        url = 'https://api.privatbank.ua/p24api/exchange_rates'
        params = {
            'date': date.strftime('%d.%m.%Y')
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data['exchangeRate']

    def get_rates(self):
        url = 'https://api.privatbank.ua/p24api/exchange_rates'
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2023, 1, 20)

        dates_to_fetch = [(start_date + datetime.timedelta(days=i)) for i in range((end_date - start_date).days + 1)]

        with ThreadPoolExecutor(max_workers=5) as executor:
            rates = list(executor.map(self.get_rate_for_date, dates_to_fetch))

        return rates
