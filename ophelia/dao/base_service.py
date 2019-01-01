from .connection import get_session


class BaseService(object):
    """
    Base apara servicios de acceso a datos
    """
    def __init__(self):
        self._session = get_session()
