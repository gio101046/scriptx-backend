# subscription entity definition

class Subscription():
    def __init__(self):
        self.id = None
        self.user_id = None
        self.service_id = None
        self.amount = None
        self.subscription_date = None
        self.cycle = None
        self.notes = None
        # Bonus: Category
