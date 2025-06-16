import datetime
import enum

# from utils.generate_ids import generate_ids

MIDDLE_NAME_DEFAULT_PLACEHOLDER = '_'

type ClientId = int

# class PaymentDetail(enum):
#     CREDITCARD = "CREDITCARD"
#     CASH = "CASH"
#     INTERAC =  "INTERAC"
#     BITCOIN = "BITCOIN"

class Client:
    id: ClientId
    firstName: str
    lastName: str
    dateOfBirth: str | datetime.datetime | None
    # middleName: str
    # paymentDetail: str | None
    # cart: list[Cart]
    
    def __init__(self, id: ClientId, firstName: str, lastName: str,  dateOfBirth: str | datetime.datetime = None): #, cart = []): #middleName: str = None,
        self.id = id # generate_ids()
        self.firstName = firstName
        self.lastName = lastName
        # self.middleName = middleName or MIDDLE_NAME_DEFAULT_PLACEHOLDER
        self.dateOfBirth = dateOfBirth
        # self.paymentDetail = string
        # self.cart: list[Cart] = cart

    def __str__(self):
        return  f"{self.firstName} {self.lastName}"

    def __repr__(self) -> str:
        return f"Client(id={self.id}, firstName='{self.firstName}', lastName={self.lastName}, dateOfBirth={self.dateOfBirth})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Client):
            return NotImplemented
        return self.id == other.id # and self.sku == other.sku

    def id_name(self) -> str:
        return f"{self.firstName.upper()}_{self.lastName.upper()}_"





