import datetime
import enum

from models.cart import Cart
from utils.generate_ids import generate_ids

MIDDLE_NAME_DEFAULT_PLACEHOLDER = '_'

type ClientId = int

class Client:
    id: ClientId
    firstName: str
    lastName: str
    middleName: str
    dateOfBirth: datetime.datetime | None
    # paymentDetail: str | None
    # cart: list[Cart]
    
    def __init__(self, id: ClientId, firstName: str, lastName: str, middleName: str, dateOfBirth: datetime.datetime = None): #, cart = []):
        self.id = id # generate_ids()
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName or MIDDLE_NAME_DEFAULT_PLACEHOLDER
        self.dateOfBirth = dateOfBirth
        # self.paymentDetail = string
        # self.cart: list[Cart] = cart

    def __str__(self):
        return  f"{self.firstName} {self.lastName}"

    def id_name(self) -> str:
        return f"{self.firstName.upper()}_{self.lastName.upper()}_"


class PaymentDetail(enum):
    CREDITCARD = "CREDITCARD"
    CASH = "CASH"
    INTERAC =  "INTERAC"
    BITCOIN = "BITCOIN"


