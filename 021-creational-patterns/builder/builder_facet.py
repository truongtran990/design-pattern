class Person(object):
    def __init__(self):
        # address properties
        self.street_address = ""
        self.postcode = ""
        self.city = ""

        # employment properties
        self.company_name= ""
        self.position= ""
        self.annual_income = 0 

    def __str__(self):
        return f"""
        Address: {self.street_address}, {self.postcode}, {self.city}, 
        Employed at: {self.company_name}, {self.position}, {self.annual_income}
    """

class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    """
    Inherritance builder
    """
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position 
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    """
    Inherritance builder
    """
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode 
        return self

    def in_city(self, city):
        self.person.city = city
        return self

if __name__ == "__main__":
    pb = PersonBuilder()
    person = pb\
            .lives\
            .at("123 London Road")\
            .in_city("London")\
            .works\
                    .at("Shopee")\
                    .as_a("SW")\
            .build()

    print(person)
