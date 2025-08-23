from attrs import Attribute
from typing import Any, Union, NoReturn

def is_positive(instance: Any, attribute: Attribute, value: int) -> Union[None, NoReturn]:

    if value <= 0:
        raise ValueError(f"'{attribute.name}' must be positive.")