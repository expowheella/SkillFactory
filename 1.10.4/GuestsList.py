class GuestsList:
    def __init__(self, full_name, city):
        self.full_name = full_name
        self.city = city

class NewGuests(GuestsList):
    def __init__(self, full_name= '', city= '', status = ''):
        super().__init__(full_name, city)
        self.status = status

    def init_from_dict(self, collection):
        self.full_name = collection.get("full_name")
        self.city = collection.get("city")
        self.status = collection.get("status")