from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import enum

MIDDLE_NAME_DEFAULT_PLACEHOLDER = '_'

type ClientId = int


class Client(BaseModel):
    id: ClientId
    firstName: str
    lastName: str
    dateOfBirth: datetime.datetime | None

    # middleName: str
    # paymentDetail: PaymentDetail | str | None
    # cart: list[Cart]


