from attrs import define

@define
class ShellData:
    shell_type: str
    damage: int