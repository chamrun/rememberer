import os
import pickle
import hashlib
from builtins import function
from typing import AnyStr


def save_obj(obj: object, name: str = None, path: str = './rem/') -> AnyStr:
    """
    Serialize and save the given object to disk.

    Parameters:
        obj (object):  The object to be serialized and saved.
        name (str): The name of the file to be saved. If not given, a SHA256 hash of the object will be used.
        path (str): The path to the directory where the file will be saved. Default is './rem/'.

    Returns:
        AnyStr: The absolute path of the saved file.
    """
    if path[-1] != '/':
        path += '/'

    if not name:
        hash_object = hashlib.sha256()
        hash_object.update(pickle.dumps(obj))
        name = hash_object.hexdigest()

    current_dir = os.getcwd()
    for folder_name in path.split('/'):
        if not folder_name:
            continue

        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        os.chdir(folder_name)

    with open(f'{name}.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        abspath = os.path.abspath(f.name)

    os.chdir(current_dir)
    return abspath


def load_obj(name: str, path: str = './rem/'):
    """
    Load and deserialize the object saved at the given path.

    Parameters:
        name (str): The name of the file to be loaded.
        path (str): The path to the directory where the file is saved. Default is './rem/'.

    Returns:
        object: The deserialized object.
    """
    if path[-1] != '/':
        path += '/'

    if not (name.endswith('.pkl') or name.endswith('.pickle')):
        name += '.pkl'

    try:
        with open(f'{path}{name}', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


def rem(func: function, *args, **kwargs) -> object:
    """
    This is a function that can be applied to another function, it will cache the result of the function
    based on the arguments passed to it, so that if the same arguments are passed again, the cached result will be
    returned instead of re-computing the result.

    Parameters:
        func (function): The function that this decorator will be applied to.
        *args: Positional arguments that will be passed to the function.
        **kwargs: Keyword arguments that will be passed to the function.

    Returns:
        The result of the function call.
    """

    def stringify(obj):
        return str(obj) if isinstance(obj, (int, float, str, bool)) else repr(obj)

    params = (func.__module__ + func.__name__).encode() + func.__code__.co_code + b"".join(
        stringify(arg).encode() for arg in args) + b"".join(
        f"{key}={stringify(value)}".encode() for key, value in kwargs.items())

    name = hashlib.sha256(params).hexdigest()
    saved = load_obj(name)
    if saved:
        return saved

    result = func(*args, **kwargs)
    save_obj(result, name)
    return result


def forget(func: function, *args, **kwargs):
    """
    This is a function that can be applied to another function, it will delete the cached result of the function
    based on the arguments passed to it.

    Parameters:
        func (function): The function that this decorator will be applied to.
        *args: Positional arguments that will be passed to the function.
        **kwargs: Keyword arguments that will be passed to the function.

    Returns:
        The result of the function call.
    """

    def stringify(obj: object) -> str:
        return str(obj) if isinstance(obj, (int, float, str, bool)) else repr(obj)

    params = (func.__module__ + func.__name__).encode() + func.__code__.co_code + b"".join(
        stringify(arg).encode() for arg in args) + b"".join(
        f"{key}={stringify(value)}".encode() for key, value in kwargs.items())

    name = hashlib.sha256(params).hexdigest()
    saved = load_obj(name)
    if saved:
        os.remove(f'./rem/{name}.pkl')
        return saved

    result = func(*args, **kwargs)
    return result


def _create_name(func, args, kwargs) -> str:
    """
    Create a name for the cached result of the function based on the arguments passed to it.

    Parameters:
        func (function): The function that this decorator will be applied to.
        *args: Positional arguments that will be passed to the function.
        **kwargs: Keyword arguments that will be passed to the function.

    Returns:
        The name of the cached result.
    """

    def stringify(obj: object) -> str:
        """
        Convert the given object to a string.

        Parameters:
            obj (object): The object to be converted to a string.

        Returns:
            The string representation of the given object.
        """
        return str(obj) if isinstance(obj, (int, float, str, bool)) else repr(obj)

    params = (func.__module__ + func.__name__).encode() + func.__code__.co_code + b"".join(
        stringify(arg).encode() for arg in args) + b"".join(
        f"{key}={stringify(value)}".encode() for key, value in kwargs.items())
    name = hashlib.sha256(params).hexdigest()
    return name
