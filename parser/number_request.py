import requests

URL_TEMPLATE = f"https://kuban.mts.ru/json/numberselection/getfreephones?inputMask=&msisdnCount=&lowPrice=0&topPrice=26000"
URL_TEMPLATE2 = 'https://kuban.mts.ru/api/sitesettings/numberselection_stringtemplates'

price = [
    0,
    250,
    1000,
    5500,
    16000,
    26000,
]


class NumberURL:

    def __init__(self,
                 input_mask,
                 number_list_count,
                 low_price,
                 top_price):
        self.input_mask = input_mask
        self.number_list_count = number_list_count
        self.low_price = low_price
        self.top_price = top_price

    def __str__(self):
        return f"https://kuban.mts.ru/json/numberselection/getfreephones?" \
               f"inputMask={self.input_mask}&msisdnCount={self.number_list_count}" \
               f"&lowPrice={self.low_price}&topPrice={self.top_price}"


def get_numbers(input_mask='', number_list_count=20, low_price=0, top_price=26000):
    number_list = NumberURL(input_mask, number_list_count, low_price, top_price)
    r = requests.get(number_list.__str__())
    return r.json()
