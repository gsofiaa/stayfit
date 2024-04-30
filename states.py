from aiogram.fsm.state import StatesGroup, State


class Wait(StatesGroup):
    purpose = State()
    new = State()
    language_choose = State()
    add = State()
    sex = State()
    age = State()
    height = State()
    weight = State()
    type_of_physical_activity = State()

    calories = State()
    to_menu = State()
    menu = State()
    added = State()

    choosing_recipe = State()
    showing_recipes = State()
    showing_recipe = State()


class Edit(StatesGroup):
    edit = State()
    edit_sex = State()
    edit_age = State()
    edit_height = State()
    edit_weight = State()
    edit_type_of_physical_activity = State()
    edit_language = State()
