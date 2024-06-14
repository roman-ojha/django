import os
# Explanation: https://youtu.be/DaxcmbWcdTA?list=PL5sSYBuH9_fgeMXw7JJXVCRqN8d02__De&t=4012
from .misc import yaml_coerce


def get_settings_from_environment(prefix="CORESETTINGS_"):
    # Remove prefix variable name and return the new environment variable dictionary
    # EX: CORESETTINGS_DB_NAME -> DB_NAME
    prefix_len = len(prefix)
    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
    """
    return:
    {
        "DB_NAME": <value>
    }
    """
