class PropertySpace:
    def __init__(self, price: int):
        # effects: odds, outcome.
        # outcome - move, money
        self.price = price
        self.owner = None
        self.houses = 0
        self.hotels = 0
        self.rent_schedule = "idk"
