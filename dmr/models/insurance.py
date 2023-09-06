from __future__ import annotations
from pydantic import BaseModel
from typing import Optional
import datetime


class Insurance(BaseModel):
    """
    The Insurance object holds the insurance information about the vehicle.

    Possible attributes:

        Insurance.company (str): The insurance provider.

        Insurance.is_active (bool): Whether the insurance is active.

        Insurance.number (str): The insurance number, typically returns None.

        Insurance.created (datetime): The date when the insurance was created.
    """
    company: str
    is_active: bool
    number: Optional[int]
    created: datetime.datetime
