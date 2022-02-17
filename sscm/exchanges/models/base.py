from django_countries import Countries


class ExchangeCountries(Countries):
    only = [
        ('AU', "Rakúsko"),
        ('CA', "Kanada"),
        ('CZ', "Česko"),
        ('DE', "Nemecko"),
        ('SK', "Slovensko"),
        ('US', "USA"),
    ]
