# subscription entity definition
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Subscription(BaseModel):
    def __init__(self):
        self.id : int = None # This is the ID of the specific subscription itself
        self.user_id : int = None # This denotes to which user the subscription belongs
        self.service_id : int = None # This denotes to which service the subscription is paying to
        self.amount : float = None # how much is charged each cycle
        self.subscription_date : Optional[date] = None # Date the subscription was first started
        self.cycle : int = None # The cycle of the subscription, measured in days
        self.notes : str = None # Any additional notes
        # Bonus: Category
