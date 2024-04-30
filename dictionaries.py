def dictionaries(lang):
    match lang:
        case "ru":
            dictionary = {
                ### приветствие
                'greeting': 'Привет, {name}, меня зовут Stay Fit Bot и вместе мы сможем узнать, сколько калорий тебе'
                            ' нужно потреблять ежедневно, и составить тебе рацион питания!',

                ### кнопки стартового меню
                'add_data': "Добавить данные о себе",
                'choose_language': 'Выбрать язык',
                'fill_data': 'Пожалуйста, заполните данные о себе',

                'required_field': 'Введите свой {param} :',
                'agree': 'Давайте заполним',
                'remeining_fields': 'Осталось заполнить ещё немного...',

                ### Меню выбора языка
                ## Текст сообщения
                'choosing_language_text': 'Выберите язык из предложенных вариантов:',
                'ru_language_selected': 'Вы выбрали русский язык. {param}',
                'en_language_selected': 'Вы выбрали английский язык. {param}',

                ## Кнопки
                'ru': "Русский",
                'en': 'Английский',

                ### кнопки редактирования данных пользователя
                'sex': 'пол',
                'age': 'возраст',
                'height': 'рост(см)',
                'weight': 'вес(кг)',
                'type_of_physical_activity': 'тип физической активности',
                'language': 'язык',

                ### текст для кнопок выбора пола
                'sex_choosing': 'Выберите ваш пол:',
                'male': 'Мужской',
                'female': 'Женский',

                ### текст для редактирования возраста
                'age_choosing': 'Введите ваш возраст:',
                'age_extinction': 'Для верных расчётов возраст должен быть числом от 8 до 84 лет.',

                ### текст для редактирования высоты
                'height_choosing': 'Введите ваш рост(в см):',
                'height_extinction': 'Для верных расчётов рост должен быть числом от 120 до 220 см.',

                ### текст для редактирования веса
                'weight_choosing': 'Введите ваш вес(в кг):',
                'weight_extinction': 'Для верных расчётов вес должен быть числом от 25 до 140 кг.',

                ### текст для выбора типа физической активности

                'type_of_physical_activity_text': 'Выберите тип физической активности:',
                'activity_level_1': 'Минимальные физические нагрузки',
                'activity_level_2': 'Небольшая дневная активность/легкие упражнения',
                'activity_level_3': 'Тренировки в фитнес-зале 4-5 раз в неделю',
                'activity_level_4': 'Интенсивные тренировки 4-5 раз в неделю',
                'activity_level_5': 'Ежедневные тренировки',
                'activity_level_6': 'Ежедневные интенсивные тренировки',
                'activity_level_7': 'Интенсивные тренировки 2 раза в день',

                'welcome_back': 'С возвращением, {name}!',
                ### текст для перехода в главное меню
                'greetings': 'Данные заполнены!',
                'to_menu_text': 'Перейти в главное меню',
                ### текст главного меню
                'menu_text': 'Теперь ты в главном меню',
                'view_profile': 'Посмотреть профиль',
                'calories': 'Дневная норма потребления',
                'recipes': 'Рецепты еды',

                'calories_text': 'Ваша дневная норма калорий: {calories} ккал',

                'profile_info_text': 'Пол: {sex}'
                                     '\nВозраст: {age}'
                                     '\nРост: {height}'
                                     '\nВес: {weight}'
                                     '\nТип физической активности: {type_of_physical_activity}',

                'edit_profile': 'Выберите, какие данные вы хотите изменить:',

                'recipes_text': 'Выберите предпочитаемый вид рецептов:',
                'back_to_recipes': 'Вернуться к выбору вида рецептов',

                'kosher': 'Кошер',
                'vegan': 'Веган',
                'halal': 'Халяль',
                'regular': 'Обычные',

                'kosher_recipes_text': 'Список кошерных рецептов:',
                'vegan_recipes_text': 'Список веганских рецептов:',
                'halal_recipes_text': 'Список халяльных рецептов:',
                'regular_recipes_text': 'Список обычных рецептов:',

                'servings_number': 'Порций: {servings}',
                'recipe_text': '{title} (на {servings} порций):\n\nИнгредиенты:\n{ingredients_text}\nИнструкции:\n{'
                               'instructions_text}"',

                'purpose_text': 'Выберите свою цель:',
                'lose_weight': 'Похудеть',
                'stay_in_shape': 'Сохранять вес',
                'gain_weight': 'Набрать вес',


                'successful_change_text': 'Данные успешно изменены.'
            }
            return dictionary

        case "en":
            dictionary = {
                ### Greeting
                'greeting': 'Hello, {name}, my name is Stay Fit Bot and together we can determine how many calories you need to consume daily and create a nutrition plan for you!',

                ### Start menu buttons
                'add_data': "Add your data",
                'choose_language': 'Choose language',
                'fill_data': 'Please, fill in your data',

                'required_field': 'Enter your {param}:',
                'agree': 'Let\'s fill it in',
                'remaining_fields': 'A few more fields to fill in...',

                ### Language selection menu
                ## Message text
                'choosing_language_text': 'Choose a language from the options below:',
                'ru_language_selected': 'You have chosen Russian language. {param}',
                'en_language_selected': 'You have chosen English language. {param}',

                ## Buttons
                'ru': "Russian",
                'en': 'English',

                ### User data editing buttons
                'sex': 'gender',
                'age': 'age',
                'height': 'height(ft,in)',
                'weight': 'weight(lb)',
                'type_of_physical_activity': 'type of physical activity',
                'language': 'language',

                ### Text for gender selection buttons
                'sex_choosing': 'Select your gender:',
                'male': 'Male',
                'female': 'Female',

                ### Text for editing age
                'age_choosing': 'Enter your age:',
                'age_extinction': 'For accurate calculations, age should be a number between 8 and 84 years.',

                ### Text for editing height
                'height_choosing': 'Enter your height(ft/in)',
                'height_extinction': 'For accurate calculations, height should be a number between 47 and 86 inches.',

                ### Text for editing weight
                'weight_choosing': 'Enter your weight(lbs)',
                'weight_extinction': 'For accurate calculations, weight should be a number between 55 and 308 lbs.',

                ### Text for selecting type of physical activity

                'type_of_physical_activity_text': 'Select your type of physical activity:',
                'activity_level_1': 'Minimal physical activity',
                'activity_level_2': 'Light daily activity/light exercises',
                'activity_level_3': 'Gym workouts 4-5 times per week',
                'activity_level_4': 'Intensive workouts 4-5 times per week',
                'activity_level_5': 'Daily workouts',
                'activity_level_6': 'Daily intensive workouts',
                'activity_level_7': 'Intensive workouts twice a day',

                'welcome_back': 'Welcome back, {name}!',
                ### Text to go back to main menu
                'greetings': 'Data filled in!',
                'to_menu_text': 'Go to main menu',
                ### Main menu text
                'menu_text': 'Now you are in the main menu',
                'view_profile': 'View profile',
                'calories': 'Daily calorie intake',
                'calories_text': 'Your daily calorie intake: {calories} kcal',
                'recipes': 'Food recipes',

                'profile_info_text': 'Gender: {sex}'
                                     '\nAge: {age}'
                                     '\nHeight: {height}'
                                     '\nWeight: {weight}'
                                     '\nType of Physical Activity: {type_of_physical_activity}',

                'edit_profile': 'Select which data you want to change:',

                'recipes_text': 'Select preferred type of recipes:',
                'back_to_recipes': 'Back to recipe type selection',

                'kosher': 'Kosher',
                'vegan': 'Vegan',
                'halal': 'Halal',
                'regular': 'Regular',

                'kosher_recipes_text': 'List of kosher recipes:',
                'vegan_recipes_text': 'List of vegan recipes:',
                'halal_recipes_text': 'List of halal recipes:',
                'regular_recipes_text': 'List of regular recipes:',

                'servings_number': 'Servings: {servings}',
                'recipe_text': '{title} (for {servings} servings):\n\nIngredients:\n{'
                               'ingredients_text}\nInstructions:\n{instructions_text}"',


                'purpose_text': 'Choose your purpose:',
                'lose_weight': 'Lose weight',
                'stay_in_shape': 'Stay in shape',
                'gain_weight': 'Gain weight',

                'successful_change_text': 'Data successfully changed.'
            }
            return dictionary
