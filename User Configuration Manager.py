def add_setting(settings_dict, my_tuple):
    key, value = my_tuple
    key = key.lower()
    value = value.lower()

    if key in settings_dict:
         return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"
    
test_settings = {'NAME': 'John'}   

def update_setting(settings_dict, my_tuple):
    key, value = my_tuple
    key = key.lower()
    value = value.lower()

    if key not in settings_dict:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings_dict[key] = value
    if key in settings_dict:
        return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings_dict, key):
    key = key.lower()

    if key not in settings_dict:
        return f"Setting not found!"

    settings_dict.pop(key)
    return f"Setting '{key}' deleted successfully!"

def view_settings(settings_dict):
    if len(settings_dict) == 0:
        return 'No settings available.'
    
    new_string = 'Current User Settings:\n'

    for key, value in settings_dict.items():
        cap_key = key.capitalize()
        new_string += f"{cap_key}: {value}\n"

    return new_string


