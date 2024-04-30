from aiogram import F, Router, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
import kb
from utils import *
from db import db
from dictionaries import dictionaries
from recipes import recipes
from states import Wait, Edit

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    user_id = msg.from_user.id
    user_lang = msg.from_user.language_code
    user_profile = db.get_user_profile(user_id)

    name = msg.from_user.full_name
    greeting_message = dictionaries(user_lang)['greeting']
    welcome_back_message = dictionaries(user_lang)['welcome_back']

    if not user_profile:
        db.create_user_profile(user_id=user_id, user_lang=user_lang, sex=None, age=None, height=None, weight=None,
                               type_of_physical_activity=None)
        await state.set_state(Wait.new)
        await msg.answer(greeting_message.format(name=name), reply_markup=kb.add_data_kb(user_lang))
    else:
        user_lang = user_profile.user_lang
        await state.set_state(Wait.to_menu)
        await msg.answer(welcome_back_message.format(name=name), reply_markup=kb.to_menu_kb(user_lang))


@router.message(Wait.new)
async def choose_language(query: CallbackQuery, bot: Bot, state: FSMContext):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    choosing_language_text = dictionaries(lang)['choosing_language_text']
    await bot.send_message(chat_id=user_id, text=choosing_language_text.format(),
                           reply_markup=kb.create_choosing_language(lang))
    await state.set_state(Wait.language_choose)


@router.message(Wait.language_choose, F.text.in_(['Русский', 'Russian']))
async def add_ru_language(query: CallbackQuery, bot: Bot, state: FSMContext):
    user_id = query.from_user.id

    db.update_user_profile(user_id, user_lang='ru')

    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    add_ru_language_text = dictionaries(lang)['ru_language_selected']
    fill_data = dictionaries(lang)['fill_data']

    if user_profile.sex or user_profile.age or user_profile.height or user_profile.weight or user_profile.type_of_physical_activity is None:
        await bot.send_message(chat_id=query.from_user.id, text=add_ru_language_text.format(param=fill_data),
                               reply_markup=kb.add_user_profile_kb(lang))
        await state.set_state(Wait.add)
    else:
        await bot.send_message(chat_id=query.from_user.id, text=add_ru_language_text.format(),
                               reply_markup=kb.to_menu_kb(lang))
        await state.set_state(Wait.to_menu)


@router.message(Wait.language_choose, F.text.in_(['Английский', 'English']))
async def add_en_language(query: CallbackQuery, bot: Bot, state: FSMContext):
    user_id = query.from_user.id

    db.update_user_profile(user_id, user_lang='en')

    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    add_en_language_text = dictionaries(lang)['en_language_selected']
    fill_data = dictionaries(lang)['fill_data']

    if user_profile.sex or user_profile.age or user_profile.height or user_profile.weight or user_profile.type_of_physical_activity is None:
        await bot.send_message(chat_id=query.from_user.id, text=add_en_language_text.format(param=fill_data),
                               reply_markup=kb.add_user_profile_kb(lang))
        await state.set_state(Wait.add)
    else:
        await bot.send_message(chat_id=query.from_user.id, text=add_en_language_text.format(),
                               reply_markup=kb.to_menu_kb(lang))
        await state.set_state(Wait.to_menu)


@router.callback_query(Wait.add, F.data == "add")
async def add_user_data(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang
    required_field = dictionaries(user_profile.user_lang)['required_field']

    if user_profile.sex is None:
        missing_field = dictionaries(user_profile.user_lang)['sex']
        missing_field.lower()
        await bot.send_message(chat_id=user_id,
                               text=required_field.format(param=missing_field),
                               reply_markup=kb.create_add_user_sex(lang))
        await state.set_state(Wait.sex)

    elif user_profile.age is None:
        missing_field = dictionaries(user_profile.user_lang)['age']
        missing_field.lower()
        await bot.send_message(chat_id=user_id,
                               text=required_field.format(param=missing_field),
                               reply_markup=kb.agree_kb(lang))
        await state.set_state(Wait.age)

    elif user_profile.height is None:
        missing_field = dictionaries(user_profile.user_lang)['height']
        missing_field.lower()
        await bot.send_message(chat_id=user_id,
                               text=required_field.format(param=missing_field),
                               reply_markup=kb.agree_kb(lang))
        await state.set_state(Wait.height)

    elif user_profile.weight is None:
        missing_field = dictionaries(user_profile.user_lang)['weight']
        missing_field.lower()
        await bot.send_message(chat_id=user_id,
                               text=required_field.format(param=missing_field),
                               reply_markup=kb.agree_kb(lang))
        await state.set_state(Wait.weight)

    elif user_profile.type_of_physical_activity is None:
        missing_field = dictionaries(user_profile.user_lang)['type_of_physical_activity']
        missing_field.lower()
        await bot.send_message(chat_id=user_id,
                               text=required_field.format(param=missing_field),
                               reply_markup=kb.agree_kb(lang))
        await state.set_state(Wait.type_of_physical_activity)

    else:
        await state.set_state(Wait.menu)


@router.callback_query(Wait.sex, F.data.in_(["male", "female"]))
async def add_sex(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    sex = query.data
    db.update_user_profile(user_id, sex=str(sex))

    required_field = dictionaries(lang)['required_field']
    param = dictionaries(lang)['age']

    await state.set_state(Wait.age)
    await bot.send_message(chat_id=user_id,
                           text=required_field.format(param=param))


@router.message(Wait.age, F.text)
async def process_age(msg: Message, state: FSMContext, bot: Bot):
    user_id = msg.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    add_age_text_error = dictionaries(lang)['age_extinction']
    required_field = dictionaries(lang)['required_field']
    param = dictionaries(lang)['height']

    age = msg.text
    if age.isdigit() and 8 <= int(age) <= 84:
        db.update_user_profile(user_id, age=int(age))
        await state.set_state(Wait.height)
        await bot.send_message(chat_id=user_id,
                               text=required_field.format(param=param))
    else:
        await msg.answer(add_age_text_error.format())
        return


@router.message(Wait.height, F.text)
async def process_height(msg: Message, state: FSMContext, bot: Bot):
    user_id = msg.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    add_height_text_error = dictionaries(lang)['height_extinction']
    required_field = dictionaries(lang)['required_field']
    param = dictionaries(lang)['weight']

    height_input = msg.text

    if lang == 'en':
        feet, inches = map(int, height_input.split(","))
        height_cm = feet * 30.48 + inches * 2.54
        if 120 <= height_cm <= 220:
            db.update_user_profile(user_id, height=int(height_cm))
            await state.set_state(Wait.weight)
            await bot.send_message(chat_id=user_id, text=required_field.format(param=param))
        else:
            await msg.answer(add_height_text_error.format())
            return

    else:
        if 120 <= int(height_input) <= 220:
            db.update_user_profile(user_id, height=int(height_input))
            await state.set_state(Wait.weight)
            await bot.send_message(chat_id=user_id, text=required_field.format(param=param))
        else:
            await msg.answer(add_height_text_error.format())
            return


@router.message(Wait.weight, F.text)
async def process_weight(msg: Message, state: FSMContext, bot: Bot):
    user_id = msg.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    add_weight_text_error = dictionaries(lang)['weight_extinction']
    required_field = dictionaries(lang)['required_field']
    param = dictionaries(lang)['type_of_physical_activity']

    weight_input = msg.text
    if weight_input.isdigit():
        if lang == 'en':
            weight_kg = int(weight_input) * 0.453592
            if 25 <= weight_kg <= 140:
                db.update_user_profile(user_id, weight=int(weight_kg))
                await state.set_state(Wait.type_of_physical_activity)
                await bot.send_message(chat_id=user_id, text=required_field.format(param=param),
                                       reply_markup=kb.create_activity_level_keyboard(lang))
            else:
                await msg.answer(add_weight_text_error.format())
                return
        else:
            if weight_input.isdigit() and 25 <= int(weight_input) <= 140:
                db.update_user_profile(user_id, weight=int(weight_input))
                await state.set_state(Wait.type_of_physical_activity)
                await bot.send_message(chat_id=user_id, text=required_field.format(param=param),
                                       reply_markup=kb.create_activity_level_keyboard(lang))
            else:
                await msg.answer(add_weight_text_error.format())
                return
    else:
        await msg.answer(add_weight_text_error.format())
        return


@router.callback_query(Wait.type_of_physical_activity, F.data)
async def process_type_of_physical_activity(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    type_of_physical_activity = query.data
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang
    greetings = dictionaries(lang)['greetings']

    db.update_user_profile(user_id, type_of_physical_activity=type_of_physical_activity)

    await bot.send_message(chat_id=user_id, text=greetings.format(),
                           reply_markup=kb.to_menu_kb(lang))
    await state.set_state(Wait.to_menu)


@router.callback_query(F.data == 'to_menu')
async def to_menu(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    menu_text = dictionaries(lang)['menu_text']

    await state.set_state(Wait.menu)
    await bot.send_message(chat_id=user_id, text=menu_text.format(),
                           reply_markup=kb.menu_kb(lang))


@router.message(Command("menu"))
async def to_menu(msg: Message, state: FSMContext, bot: Bot):
    user_id = msg.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    menu_text = dictionaries(lang)['menu_text']

    await state.set_state(Wait.menu)
    await bot.send_message(chat_id=user_id, text=menu_text.format(),
                           reply_markup=kb.menu_kb(lang))


@router.callback_query(Wait.menu, F.data == 'view_profile')
async def view_profile_query(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    sex = dictionaries(lang)[user_profile.sex]
    age = user_profile.age
    height = user_profile.height
    weight = user_profile.weight
    type_of_physical_activity = dictionaries(lang)[user_profile.type_of_physical_activity]

    profile_info_text = dictionaries(lang)['profile_info_text']

    await bot.send_message(chat_id=user_id,
                           text=profile_info_text.format(sex=sex, age=age, height=height, weight=weight,
                                                         type_of_physical_activity=type_of_physical_activity),
                           reply_markup=kb.profile_info_kb(lang))


@router.callback_query(Wait.menu, F.data == 'calories')
async def purpose(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang
    purpose_text = dictionaries(lang)['purpose_text']

    await bot.send_message(chat_id=user_id, text=purpose_text.format(),
                           reply_markup=kb.purpose_kb(lang))
    await state.set_state(Wait.purpose)


@router.callback_query(Wait.purpose, F.data.in_(['lose_weight', 'stay_in_shape', 'gain_weight']))
async def calories_query(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    purpose = query.data

    calories_text = dictionaries(lang)['calories_text']
    calories = calories_calc(user_id, purpose)

    await bot.send_message(chat_id=user_id, text=calories_text.format(calories=calories),
                           reply_markup=kb.to_menu_kb(lang))
    await state.set_state(Wait.menu)


@router.callback_query(Wait.menu, F.data == 'recipes')
async def recipes_query(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    recipes_text = dictionaries(lang)['recipes_text']

    await bot.send_message(chat_id=user_id, text=recipes_text.format(),
                           reply_markup=kb.recipes_type_kb(lang))
    await state.set_state(Wait.choosing_recipe)


@router.callback_query(Wait.choosing_recipe,
                       F.data.in_(['kosher', 'vegan', 'halal', 'regular']))
async def type_of_recipes_query(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang
    data = query.data

    match data:
        case 'kosher':
            recipes_text = dictionaries(lang)['kosher_recipes_text']
            markup = kb.kosher_recipes_kb(lang)
        case 'vegan':
            recipes_text = dictionaries(lang)['vegan_recipes_text']
            markup = kb.vegan_recipes_kb(lang)
        case 'halal':
            recipes_text = dictionaries(lang)['halal_recipes_text']
            markup = kb.halal_recipes_kb(lang)
        case 'regular':
            recipes_text = dictionaries(lang)['regular_recipes_text']
            markup = kb.regular_recipes_kb(lang)
        case _:
            return

    await bot.send_message(chat_id=user_id, text=recipes_text.format(),
                           reply_markup=markup)
    await state.update_data(food=data)

    await state.set_state(Wait.showing_recipes)


@router.callback_query(Wait.showing_recipes, F.data)
async def recipe_query(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    state_data = await state.get_data()
    food = state_data.get('food', None)
    servings = 1

    data = str(query.data)
    recipe_data = recipes(lang, food, servings)[data]
    title = recipe_data['title']

    ingredients_text = ""
    for ingredient, details in recipe_data['ingredients'].items():
        if isinstance(details, dict):
            quantity_per_serving = details['quantity'] * servings
            unit = details['unit']
            ingredients_text += f"{ingredient}: {quantity_per_serving} {unit}\n"
        else:
            ingredients_text += f"{ingredient}: {details}\n"

    instructions_text = recipe_data['instructions']
    msg_text = dictionaries(lang)['recipe_text']
    await bot.send_message(
        chat_id=user_id,
        text=msg_text.format(title=title, servings=servings, ingredients_text=ingredients_text,
                             instructions_text=instructions_text),
        reply_markup=kb.servings_keyboard(lang, servings)
    )

    array_info = {'food': food, 'servings': servings, 'data': data}
    await state.update_data(data=array_info)
    await state.set_state(Wait.showing_recipe)


@router.callback_query(Wait.showing_recipe, F.data.in_(["decrease_servings", "increase_servings"]))
async def manage_servings(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang
    state_data_getter = await state.get_data()
    food = state_data_getter.get('food')
    servings = state_data_getter.get('servings')
    data = state_data_getter.get('data')

    if query.data == "decrease_servings":
        servings = max(1, servings - 1)
    else:
        servings += 1

    array_info = {'food': food, 'servings': servings, 'data': data}
    await state.update_data(data=array_info)

    data = str(data)
    recipe_data = recipes(lang, food, servings)[data]
    title = recipe_data['title']

    ingredients_text = ""
    for ingredient, details in recipe_data['ingredients'].items():
        if isinstance(details, dict):
            quantity_per_serving = details['quantity'] * servings
            unit = details['unit']
            ingredients_text += f"{ingredient}: {quantity_per_serving} {unit}\n"
        else:
            ingredients_text += f"{ingredient}: {details}\n"

    instructions_text = recipe_data['instructions']
    msg_text = dictionaries(lang)['recipe_text']

    await bot.edit_message_text(
        chat_id=user_id,
        message_id=query.message.message_id,
        text=msg_text.format(title=title, servings=servings, ingredients_text=ingredients_text,
                             instructions_text=instructions_text),
        reply_markup=kb.servings_keyboard(lang, servings=servings)
    )


@router.callback_query(Wait.menu, F.data == "edit_profile")
async def edit_user_characteristics(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    edit_user_characteristics = dictionaries(lang)["edit_profile"]

    await bot.send_message(chat_id=user_id, text=edit_user_characteristics.format(),
                           reply_markup=kb.edit_user_characteristics_kb(lang))
    await state.set_state(Edit.edit)


@router.callback_query(Edit.edit, F.data == 'sex')
async def edit_sex(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    sex_choice_text = dictionaries(lang)['sex_choosing']

    await bot.send_message(chat_id=user_id, text=sex_choice_text, reply_markup=kb.create_add_user_sex(lang))
    await state.set_state(Edit.edit_sex)


@router.callback_query(Edit.edit_sex, F.data.in_(["male", "female"]))
async def process_edit_sex(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang
    new_sex = query.data
    db.update_user_profile(user_id, sex=new_sex)

    successful_change_text = dictionaries(lang)['successful_change_text']

    await state.set_state(Wait.menu)
    await bot.send_message(chat_id=user_id, text=successful_change_text, reply_markup=kb.to_menu_kb(lang))


@router.callback_query(Edit.edit, F.data == 'age')
async def edit_age(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    age_choice_text = dictionaries(lang)['age_choosing']

    await bot.send_message(chat_id=user_id, text=age_choice_text)
    await state.set_state(Edit.edit_age)


@router.message(Edit.edit_age, F.text)
async def process_edit_age(msg: Message, state: FSMContext, bot: Bot):
    user_id = msg.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    successful_change_text = dictionaries(lang)['successful_change_text']
    add_age_text_error = dictionaries(lang)['age_extinction']

    new_age = msg.text
    if new_age.isdigit() and 8 <= int(new_age) <= 84:
        db.update_user_profile(user_id, age=int(new_age))
        await state.set_state(Wait.menu)
        await bot.send_message(chat_id=user_id, text=successful_change_text, reply_markup=kb.to_menu_kb(lang))
    else:
        await msg.answer(add_age_text_error.format())
        return


@router.callback_query(Edit.edit, F.data == 'height')
async def edit_height(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    height_choice_text = dictionaries(lang)['height_choosing']

    await bot.send_message(chat_id=user_id, text=height_choice_text)
    await state.set_state(Edit.edit_height)


@router.message(Edit.edit_height, F.text)
async def process_edit_height(msg: Message, state: FSMContext, bot: Bot):
    user_id = msg.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    add_height_text_error = dictionaries(lang)['height_extinction']
    successful_change_text = dictionaries(lang)['successful_change_text']

    new_height = msg.text

    if lang == 'en':
        feet, inches = map(int, new_height.split(","))
        height_cm = feet * 30.48 + inches * 2.54
        if 120 <= height_cm <= 220:
            db.update_user_profile(user_id, height=int(height_cm))
            await state.set_state(Wait.menu)
            await bot.send_message(chat_id=user_id, text=successful_change_text, reply_markup=kb.to_menu_kb(lang))
        else:
            await msg.answer(add_height_text_error.format())
            return

    else:
        if 120 <= int(new_height) <= 220:
            db.update_user_profile(user_id, height=int(new_height))
            await state.set_state(Wait.menu)
            await bot.send_message(chat_id=user_id, text=successful_change_text, reply_markup=kb.to_menu_kb(lang))
        else:
            await msg.answer(add_height_text_error.format())
            return


@router.callback_query(Edit.edit, F.data == 'weight')
async def edit_weight(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    weight_choice_text = dictionaries(lang)['weight_choosing']

    await bot.send_message(chat_id=user_id, text=weight_choice_text)
    await state.set_state(Edit.edit_weight)


@router.message(Edit.edit_weight, F.text)
async def edit_weight(msg: Message, state: FSMContext, bot: Bot):
    user_id = msg.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    add_weight_text_error = dictionaries(lang)['weight_extinction']
    successful_change_text = dictionaries(lang)['successful_change_text']

    new_weight = msg.text
    if new_weight.isdigit():
        if lang == 'en':
            weight_kg = int(new_weight) * 0.453592
            if 25 <= weight_kg <= 140:
                db.update_user_profile(user_id, weight=int(weight_kg))
                await state.set_state(Wait.menu)
                await bot.send_message(chat_id=user_id, text=successful_change_text, reply_markup=kb.to_menu_kb(lang))
            else:
                await msg.answer(add_weight_text_error.format())
                return
        else:
            if new_weight.isdigit() and 25 <= int(new_weight) <= 140:
                db.update_user_profile(user_id, weight=int(new_weight))
                await state.set_state(Wait.menu)
                await bot.send_message(chat_id=user_id, text=successful_change_text, reply_markup=kb.to_menu_kb(lang))
            else:
                await msg.answer(add_weight_text_error.format())
                return
    else:
        await msg.answer(add_weight_text_error.format())
        return


@router.callback_query(Edit.edit, F.data == 'type_of_physical_activity')
async def edit_type_of_physical_activity(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    type_of_physical_activity_text = dictionaries(lang)['type_of_physical_activity_text']

    await bot.send_message(chat_id=user_id, text=type_of_physical_activity_text,
                           reply_markup=kb.create_activity_level_keyboard(lang))
    await state.set_state(Edit.edit_type_of_physical_activity)


@router.callback_query(Edit.edit_type_of_physical_activity, F.data)
async def process_edit_type_of_physical_activity(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang
    new_type_of_physical_activity = query.data
    db.update_user_profile(user_id, type_of_physical_activity=new_type_of_physical_activity)

    successful_change_text = dictionaries(lang)['successful_change_text']

    await state.set_state(Wait.menu)
    await bot.send_message(chat_id=user_id, text=successful_change_text, reply_markup=kb.to_menu_kb(lang))


@router.callback_query(Edit.edit, F.data)
async def edit_language(query: CallbackQuery, bot: Bot, state: FSMContext):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    choosing_language_text = dictionaries(lang)['choosing_language_text']
    await bot.send_message(chat_id=user_id, text=choosing_language_text.format(),
                           reply_markup=kb.create_choosing_language(lang))
    await state.set_state(Edit.edit_language)


@router.message(Edit.edit_language, F.text.in_(['Русский', 'Russian']))
async def edit_language_to_ru(query: CallbackQuery, bot: Bot, state: FSMContext):
    user_id = query.from_user.id
    db.update_user_profile(user_id, user_lang='ru')
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    add_ru_language_text = dictionaries(lang)['ru_language_selected']

    await state.set_state(Wait.menu)
    await bot.send_message(chat_id=user_id, text=add_ru_language_text.format(param=''),
                           reply_markup=kb.to_menu_kb(lang))


@router.message(Edit.edit_language, F.text.in_(['Английский', 'English']))
async def edit_language_to_en(query: CallbackQuery, bot: Bot, state: FSMContext):
    user_id = query.from_user.id
    db.update_user_profile(user_id, user_lang='en')
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang

    add_en_language_text = dictionaries(lang)['en_language_selected']

    await state.set_state(Wait.menu)
    await bot.send_message(chat_id=user_id, text=add_en_language_text.format(param=''),
                           reply_markup=kb.to_menu_kb(lang))


@router.callback_query(Command("help"))
async def to_menu(query: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = query.from_user.id
    user_profile = db.get_user_profile(user_id)
    lang = user_profile.user_lang
