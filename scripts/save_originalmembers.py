from sscm.originaldata.models import OriginalMember


def run():
    import csv
    original_members = []
    with open('members.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',')
        for row in spamreader:
            if row['datum_vstupu'] == "0000-00-00":
                row['datum_vstupu'] = None
            if row['datum_nar'] == "0000-00-00":
                row['datum_nar'] = None
            original_members.append(
                OriginalMember(
                    firstname=row['firstname'],
                    surname=row['surname'],
                    titul=row['titul'],
                    titul2=row['titul2'],
                    cl_cislo=row['cl_cislo'],
                    druh_clenstva=row['druh_clenstva'],
                    datum_nar=row['datum_nar'],
                    povolanie=row['povolanie'],
                    adresa=row['adresa'],
                    psc=row['psc'],
                    obec=row['obec'],
                    farnost_id_id=row['farnost_id'],
                    datum_vstupu=row['datum_vstupu'],
                    status=row['status'],
                    poznamka=row['poznamka'],
                )
            )
        try:
            OriginalMember.objects.bulk_create(original_members, ignore_conflicts=True)
        except ValueError as e:
            print(e)
