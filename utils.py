from db import db
from dictionaries import dictionaries


def calories_calc(user_id, purpose):
    user_profile = db.get_user_profile(user_id)

    activity_level = user_profile.type_of_physical_activity

    print(activity_level)
    print(purpose)
    match activity_level:
        case 'activity_level_1':
            activity_factor = 1.2
        case 'activity_level_2':
            activity_factor = 1.375
        case 'activity_level_3':
            activity_factor = 1.4625
        case 'activity_level_4':
            activity_factor = 1.55
        case 'activity_level_5':
            activity_factor = 1.6375
        case 'activity_level_6':
            activity_factor = 1.725
        case 'activity_level_7':
            activity_factor = 1.9
        case _:  # Add a default case to handle unexpected values
            raise ValueError("Invalid activity level")

    match purpose:
        case 'lose_weight':
            purpose_factor = 0.8
        case 'stay_in_shape':
            purpose_factor = 1.0
        case 'gain_weight':
            purpose_factor = 1.2
        case _:  # Add a default case for purpose
            raise ValueError("Invalid purpose")

    calories = calculus(user_id, activity_factor, purpose_factor)
    return calories


def calculus(user_id, activity_factor, purpose_factor):
    user_profile = db.get_user_profile(user_id)

    sex = user_profile.sex
    age = user_profile.age
    height = user_profile.height
    weight = user_profile.weight

    if sex == "male":
        calories = (10 * weight + 6.25 * height - 5 * age + 5) * activity_factor * purpose_factor
    else:
        calories = (10 * weight + 6.25 * height - 5 * age - 161) * activity_factor * purpose_factor
    return int(calories)
