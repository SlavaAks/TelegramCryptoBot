from aiogram.utils.keyboard import InlineKeyboardBuilder



def get_inline_keyboard(data: list):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Кнопка1", callback_data='apple_m1_c1')

    return keyboard_builder.as_markup()
