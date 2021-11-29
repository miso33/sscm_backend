from sscm.parishes.models import Deanship


def run():
    import csv

    with open('dekanaty.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',')
        for row in spamreader:
            Deanship.objects.create(
                short=row['short'],
                diocese=row['diocese'],
                name=row['name']
            )
