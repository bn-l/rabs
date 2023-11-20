import typing

# Pydantic 

if typing.TYPE_CHECKING:
    from .main import *


__all__ = (
    'real_to_abs_filename',
)


_dynamic_imports: 'dict[str, tuple[str, str]]' = {
    'real_to_abs_filename': (__package__, '.main'),
}

# See: https://peps.python.org/pep-0562/ for more details

def __getattr__(attr_name: str) -> object:
    dynamic_attr = _dynamic_imports.get(attr_name)

    if dynamic_attr is None:
        raise AttributeError(f"I have no package '{attr_name}'")

    package, module_name = dynamic_attr

    from importlib import import_module

    if module_name == '__module__':
        return import_module(f'.{attr_name}', package=package)
    else:
        module = import_module(module_name, package=package)
        return getattr(module, attr_name)


def __dir__() -> 'list[str]':
    return list(__all__)