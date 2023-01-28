import os
import pickle
import hashlib


def save_obj(obj, name=None, path='./rem/'):
    """
    Serialize and save the given object to disk.
    :param obj: The object to be serialized and saved.
    :param name: The name to be used for the saved file. If not provided, a SHA256 hash of the object will be used.
    :param path: The path to the directory where the file will be saved. Default is './rem/'.
    :return: The absolute path of the saved file.
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


def load_obj(name, path='./rem/'):
    """
    Load and deserialize the object saved at the given path.
    :param name: The name of the file to be loaded.
    :param path: The path to the directory where the file is saved. Default is './rem/'.
    :return: The deserialized object.
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


def rem(func, *args, **kwargs):
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
    hash_object = hashlib.sha256()
    hash_object.update(pickle.dumps(func))
    hash_object.update(pickle.dumps(args))
    hash_object.update(pickle.dumps(kwargs))
    name = hash_object.hexdigest()
    saved = load_obj(name)
    if saved:
        return saved
    result = func(*args, **kwargs)
    save_obj(result, name)
    return result
