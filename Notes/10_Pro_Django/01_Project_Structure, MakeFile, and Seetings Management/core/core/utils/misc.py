import yaml


def yaml_coerce(value):
    # we will going to pass string dict into 'value' and it will going to convert into python dictionary
    if isinstance(value, str):
        return yaml.load(f'dummy: ${value}', Loader=yaml.SafeLoader)['dummy']

    return value
