from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardMarkup
from dictionaries import dictionaries
from recipes import recipes


def add_data_kb(lang):
    add_data = [
        [KeyboardButton(text=dictionaries(lang)['choose_language'])],
    ]
    return ReplyKeyboardMarkup(keyboard=add_data, resize_keyboard=True)


def add_user_profile_kb(lang):
    add_user_profile = [
        [InlineKeyboardButton(text=dictionaries(lang)['add_data'], callback_data="add")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=add_user_profile)


def create_choosing_language(lang):
    choosing_language = [
        [KeyboardButton(text=dictionaries(lang)['ru'])],
        [KeyboardButton(text=dictionaries(lang)['en'])],
    ]
    return ReplyKeyboardMarkup(keyboard=choosing_language, resize_keyboard=True, one_time_keyboard=True)


def agree_kb(lang):
    agree = [
        [KeyboardButton(text=dictionaries(lang)['agree'])]
    ]
    return ReplyKeyboardMarkup(keyboard=agree, resize_keyboard=True)


def create_add_user_sex(lang):
    add_user_sex = [
        [InlineKeyboardButton(text=dictionaries(lang)['male'], callback_data="male")],
        [InlineKeyboardButton(text=dictionaries(lang)['female'], callback_data="female")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=add_user_sex, resize_keyboard=True, one_time_keyboard=True)


def create_activity_level_keyboard(lang):
    add_activity_level = [
        [InlineKeyboardButton(text=dictionaries(lang)['activity_level_1'], callback_data="activity_level_1")],
        [InlineKeyboardButton(text=dictionaries(lang)['activity_level_2'], callback_data="activity_level_2")],
        [InlineKeyboardButton(text=dictionaries(lang)['activity_level_3'], callback_data="activity_level_3")],
        [InlineKeyboardButton(text=dictionaries(lang)['activity_level_4'], callback_data="activity_level_4")],
        [InlineKeyboardButton(text=dictionaries(lang)['activity_level_5'], callback_data="activity_level_5")],
        [InlineKeyboardButton(text=dictionaries(lang)['activity_level_6'], callback_data="activity_level_6")],
        [InlineKeyboardButton(text=dictionaries(lang)['activity_level_7'], callback_data="activity_level_7")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=add_activity_level, resize_keyboard=True, one_time_keyboard=True)


def purpose_kb(lang):
    purpose = [
        [InlineKeyboardButton(text=dictionaries(lang)['lose_weight'], callback_data='lose_weight')],
        [InlineKeyboardButton(text=dictionaries(lang)['stay_in_shape'], callback_data='stay_in_shape')],
        [InlineKeyboardButton(text=dictionaries(lang)['gain_weight'], callback_data='gain_weight')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=purpose)


def edit_user_characteristics_kb(lang):
    edit_user_characteristics = [
        [InlineKeyboardButton(text=(dictionaries(lang)['sex'][0].upper() + dictionaries(lang)['sex'][1:]),
                              callback_data="sex")],
        [InlineKeyboardButton(text=(dictionaries(lang)['age'][0].upper() + dictionaries(lang)['age'][1:]),
                              callback_data="age")],
        [InlineKeyboardButton(text=(dictionaries(lang)['height'][0].upper() + dictionaries(lang)['height'][1:]),
                              callback_data="height")],
        [InlineKeyboardButton(text=(dictionaries(lang)['weight'][0].upper() + dictionaries(lang)['weight'][1:]),
                              callback_data="weight")],
        [InlineKeyboardButton(text=(dictionaries(lang)['type_of_physical_activity'][0].upper() +
                                    dictionaries(lang)['type_of_physical_activity'][1:]),
                              callback_data="type_of_physical_activity")],
        [InlineKeyboardButton(text=(dictionaries(lang)['language'][0].upper() + dictionaries(lang)['language'][1:]),
                              callback_data="language")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=edit_user_characteristics)


def to_menu_kb(lang):
    to_menu = [
        [InlineKeyboardButton(text=dictionaries(lang)['to_menu_text'], callback_data="to_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=to_menu)


def menu_kb(lang):
    menu = [
        [InlineKeyboardButton(text=dictionaries(lang)['view_profile'], callback_data='view_profile')],
        [InlineKeyboardButton(text=dictionaries(lang)['calories'], callback_data='calories')],
        [InlineKeyboardButton(text=dictionaries(lang)['recipes'], callback_data='recipes')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=menu)


def profile_info_kb(lang):
    profile_info = [
        [InlineKeyboardButton(text=dictionaries(lang)['to_menu_text'], callback_data="to_menu")],
        [InlineKeyboardButton(text=dictionaries(lang)['edit_profile'], callback_data="edit_profile")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=profile_info)


def recipes_type_kb(lang):
    recipes_type = [
        [InlineKeyboardButton(text=dictionaries(lang)['kosher'], callback_data="kosher")],
        [InlineKeyboardButton(text=dictionaries(lang)['vegan'], callback_data="vegan")],
        [InlineKeyboardButton(text=dictionaries(lang)['halal'], callback_data="halal")],
        [InlineKeyboardButton(text=dictionaries(lang)['regular'], callback_data="regular")],
        [InlineKeyboardButton(text=dictionaries(lang)['to_menu_text'], callback_data="to_menu")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=recipes_type)


def vegan_recipes_kb(lang):
    vegan_recipes = [
        [InlineKeyboardButton(text=recipes(lang, food='vegan', servings=None)['pasta_with_mushrooms']['title'],
                              callback_data="pasta_with_mushrooms")],
        [InlineKeyboardButton(text=recipes(lang, food='vegan', servings=None)['lintil_cutlets']['title'],
                              callback_data="lintil_cutlets")],
        [InlineKeyboardButton(text=recipes(lang, food='vegan', servings=None)['ratatouille']['title'],
                              callback_data="ratatouille")],
        [InlineKeyboardButton(text=recipes(lang, food='vegan', servings=None)['pasta_with_fresh_tomatoes']['title'],
                              callback_data='pasta_with_fresh_tomatoes')],
        [InlineKeyboardButton(text=dictionaries(lang)['back_to_recipes'], callback_data="recipes")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=vegan_recipes)


def kosher_recipes_kb(lang):
    kosher_recipes = [
        [InlineKeyboardButton(text=recipes(lang, food='kosher', servings=None)['shakshuka']['title'],
                              callback_data="shakshuka")],
        [InlineKeyboardButton(
            text=recipes(lang, food='kosher', servings=None)['eggplant_salad_with_dill_and_garlic']['title'],
            callback_data="eggplant_salad_with_dill_and_garlic")],
        [InlineKeyboardButton(text=recipes(lang, food='kosher', servings=None)['broccoli_bake']['title'],
                              callback_data="broccoli_bake")],
        [InlineKeyboardButton(text=recipes(lang, food='kosher', servings=None)['chicken_cutlets_with_ptitim']['title'],
                              callback_data='chicken_cutlets_with_ptitim')],
        [InlineKeyboardButton(
            text=recipes(lang, food='kosher', servings=None)['chicken_soup_with_corn_and_paprika']['title'],
            callback_data="chicken_soup_with_corn_and_paprika")],
        [InlineKeyboardButton(text=dictionaries(lang)['back_to_recipes'], callback_data="recipes")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kosher_recipes)


def halal_recipes_kb(lang):
    halal_recipes = [
        [InlineKeyboardButton(
            text=recipes(lang, food='halal', servings=None)['chicken_skewers_with_vegetables']['title'],
            callback_data="chicken_skewers_with_vegetables")],
        [InlineKeyboardButton(text=recipes(lang, food='halal', servings=None)['fried_fish_with_vegetables']['title'],
                              callback_data="fried_fish_with_vegetables")],
        [InlineKeyboardButton(
            text=recipes(lang, food='halal', servings=None)['chicken_with_rice_and_vegetables']['title'],
            callback_data="chicken_with_rice_and_vegetables")],
        [InlineKeyboardButton(text=recipes(lang, food='halal', servings=None)['basbousa']['title'],
                              callback_data="basbousa")],
        [InlineKeyboardButton(text=recipes(lang, food='halal', servings=None)['maqlooba']['title'],
                              callback_data="maqlooba")],
        [InlineKeyboardButton(text=dictionaries(lang)['back_to_recipes'], callback_data="recipes")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=halal_recipes)


def regular_recipes_kb(lang):
    regular_recipes = [
        [InlineKeyboardButton(
            text=recipes(lang, food='regular', servings=None)['chicken_with_rice_and_vegetables']['title'],
            callback_data="chicken_with_rice_and_vegetables")],
        [InlineKeyboardButton(text=recipes(lang, food='regular', servings=None)['spaghetti_with_meatballs']['title'],
                              callback_data="spaghetti_with_meatballs")],
        [InlineKeyboardButton(text=recipes(lang, food='regular', servings=None)['lasagna']['title'],
                              callback_data="lasagna")],
        [InlineKeyboardButton(text=recipes(lang, food='regular', servings=None)['baked_fish_with_potatoes']['title'],
                              callback_data="baked_fish_with_potatoes")],
        [InlineKeyboardButton(text=recipes(lang, food='regular', servings=None)['chicken_noodle_soup']['title'],
                              callback_data="chicken_noodle_soup")],
        [InlineKeyboardButton(text=dictionaries(lang)['back_to_recipes'], callback_data="recipes")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=regular_recipes)


def servings_keyboard(lang, servings):
    servings_keyboard = [
        [
            InlineKeyboardButton(text="◀️", callback_data="decrease_servings", size="small"),
            InlineKeyboardButton(text=dictionaries(lang)['servings_number'].format(servings=servings),
                                 callback_data="oops"),
            InlineKeyboardButton(text="▶️", callback_data="increase_servings", size="small")
        ],
        [InlineKeyboardButton(text=dictionaries(lang)['to_menu_text'], callback_data="to_menu")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=servings_keyboard)
