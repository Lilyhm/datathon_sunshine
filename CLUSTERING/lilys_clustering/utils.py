import json


class Params:
    def __init__(self, **entries):
        """Convert a dictionary into attributes of this object
        :param entries: input dictionary
        """
        self.__dict__.update(entries)


def dict_to_object(dct: dict) -> Params:
    """Convert a dictionary to an Params object.
    :param dct: dictionary
    :return: Params object
    """
    return Params(**dct)


def read_params(config_path: str):
    """
    Reads in the model config.json file and returns the Params object
    this to allow for json objects to be used as parameters within the code
    :return:
    """
    with open(config_path, "r") as f:
        dct = json.load(f)

    return dict_to_object(dct)
