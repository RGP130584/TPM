from typing import Dict, TypeVar, Generic, Optional

T = TypeVar("T")


class BaseRegistry(Generic[T]):
    """
    Base registry interface for runtime discovery.
    Provides mechanisms for registration and lookup, with basic version support.
    """

    def __init__(self):
        # mapping format: { "name": { "version": item } }
        self._items: Dict[str, Dict[str, T]] = {}

    def register(self, name: str, version: str, item: T) -> None:
        if name not in self._items:
            self._items[name] = {}
        self._items[name][version] = item

    def get(self, name: str, version: Optional[str] = None) -> Optional[T]:
        if name not in self._items:
            return None

        versions = self._items[name]

        if not versions:
            return None

        if version:
            return versions.get(version)

        # Return the latest version added generically (not sorting string semvers right now)
        # Using the last added key as a simple fallback when version is None
        latest_version_key = list(versions.keys())[-1]
        return versions[latest_version_key]

    def list_all(self) -> Dict[str, list[str]]:
        return {name: list(versions.keys()) for name, versions in self._items.items()}
