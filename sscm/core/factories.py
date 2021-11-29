def many_to_many(attribute, create, extracted, related_factory):
    if not create:
        return
    if extracted:
        if type(extracted) is tuple:
            for customer in extracted:
                attribute.add(customer)
        else:
            attribute.add(extracted)
    else:
        attribute.add(related_factory())
