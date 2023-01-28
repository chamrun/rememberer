import os
import pickle
import hashlib


def save_obj(obj, name=None, path='./pickles/'):
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


def load_obj(name, path='./pickles/'):
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

    :param func:
    :param args:
    :param kwargs:
    :return:
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

