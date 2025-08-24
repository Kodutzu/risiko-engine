from attrs import Attribute
from typing import Any, Union, NoReturn
from .exceptions import PlayerChargeAtleastOneException

def charge_checker(instance: Any, attribute: Attribute, value: int) -> Union[None, NoReturn]:

    if value < 0:
        raise PlayerChargeAtleastOneException(f"'{attribute.name}' shouldn't be negative")