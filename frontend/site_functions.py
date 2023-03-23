from .models import Selecting_fields


def get_field_button_states():
    last_states = Selecting_fields.objects.all().values().last()

    states_list = []

    for key, value in last_states.items():
        if key != 'id':
            states_list.append(value)
    
    return states_list


def select_field_state(field_name):
    table = Selecting_fields()
    last_states = Selecting_fields.objects.all().values().last()
    all_keys = []

    for key in last_states:
        if key != 'id':
            if field_name == key:
                setattr(table, key, True)
            else:
                setattr(table, key, False)

    table.save()