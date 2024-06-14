# Explanation: https://youtu.be/DaxcmbWcdTA?list=PL5sSYBuH9_fgeMXw7JJXVCRqN8d02__De&t=3338
def deep_update(base_dict, update_with):
    for key, value in update_with.items():
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)

            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            else:
                base_dict[key] = value

        else:
            base_dict[key] = value

    return base_dict
