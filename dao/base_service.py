from dao.connection import get_session


class BaseService():
    """
    Base apara servicios de acceso a datos
    """
    def __init__(self):
        self._session = get_session()
