from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import enum

from domains.client import ClientId

MIDDLE_NAME_DEFAULT_PLACEHOLDER = '_'



class Client(BaseModel):
    id: ClientId
    firstName: str
    lastName: str
    dateOfBirth: str | datetime.datetime | None = datetime.datetime.now()

    # middleName: str
    # paymentDetail: PaymentDetail | str | None
    # cart: list[Cart]


