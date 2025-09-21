from attrs import define

@define
class ShellData:
    """
    Data transfer object for shell information.
    """
    shell_type: str
    damage: int