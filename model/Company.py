# company entity definition
from pydantic import BaseModel


class Company():
    def __init__(self):
        self.service_id : int = None # This denotes to which user the subscription belongs
        self.name : str = None 
        self.logo_url : str = None
        self.ticker : str = None
        self.price : float = None