from threading import Lock


class Singleton(type):
    """Metaclass to create Singleton."""

    _instances: dict = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in Singleton._instances:
            with Singleton._lock:
                Singleton._instances.setdefault(cls, super().__call__(*args, **kwargs))
        return Singleton._instances[cls]
