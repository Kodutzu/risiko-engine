class PlayerException(Exception): pass


class PlayerNotFoundException(PlayerException): pass


class PlayerAlreadyExistsException(PlayerException): pass


class PlayerNotAliveException(PlayerException): pass


class PlayerAlreadyAliveException(PlayerException): pass


class PlayerAlreadyDeadException(PlayerException): pass


class PlayerNotDeadException(PlayerException): pass


class PlayerNotEnoughChargeException(PlayerException): pass


class PlayerChargeAtleastOneException(PlayerException): pass