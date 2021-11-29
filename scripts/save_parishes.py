from sscm.parishes.models import Deanship, Parish


def run():
    import csv

    with open('farnosti.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',')
        for row in spamreader:
            deanship = Deanship.objects.filter(short=row['dekanat_id']).first()
            Parish.objects.create(
                id=row['id'],
                deanship=deanship,
                name=row['name']
            )
