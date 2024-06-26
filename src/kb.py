from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start1 = [
        [InlineKeyboardButton(text='Создать напоминалку', callback_data='make'),
        InlineKeyboardButton(text='Удалить напоминалку', callback_data='delete')]
    ]

years = [
    [
        InlineKeyboardButton(text='2024', callback_data='months'),
        InlineKeyboardButton(text='2025', callback_data='months'),
    ]
]

months = [
    [
        InlineKeyboardButton(text='Январь', callback_data='days'),
        InlineKeyboardButton(text='Февраль', callback_data='days'),
        InlineKeyboardButton(text='Март', callback_data='days'),
    ],
    [
        InlineKeyboardButton(text='Апрель', callback_data='days'),
        InlineKeyboardButton(text='Май', callback_data='days'),
        InlineKeyboardButton(text='Июнь', callback_data='days'),
    ],
    [
        InlineKeyboardButton(text='Июль', callback_data='days'),
        InlineKeyboardButton(text='Август', callback_data='days'),
        InlineKeyboardButton(text='Сентябрь', callback_data='days'),
    ],
    [
        InlineKeyboardButton(text='Октябрь', callback_data='days'),
        InlineKeyboardButton(text='Ноябрь', callback_data='days'),
        InlineKeyboardButton(text='Декабрь', callback_data='days'),
    ]
]

odd_days = [
    [
        InlineKeyboardButton(text='01', callback_data='hours'),
        InlineKeyboardButton(text='02', callback_data='hours'),
        InlineKeyboardButton(text='03', callback_data='hours'),
        InlineKeyboardButton(text='04', callback_data='hours'),
        InlineKeyboardButton(text='05', callback_data='hours'),
        InlineKeyboardButton(text='06', callback_data='hours'),
        InlineKeyboardButton(text='07', callback_data='hours'),
        InlineKeyboardButton(text='08', callback_data='hours')
    ],
    [
        InlineKeyboardButton(text='09', callback_data='hours'),
        InlineKeyboardButton(text='10', callback_data='hours'),
        InlineKeyboardButton(text='11', callback_data='hours'),
        InlineKeyboardButton(text='12', callback_data='hours'),
        InlineKeyboardButton(text='13', callback_data='hours'),
        InlineKeyboardButton(text='14', callback_data='hours'),
        InlineKeyboardButton(text='15', callback_data='hours'),
        InlineKeyboardButton(text='16', callback_data='hours')
    ],
    [
        InlineKeyboardButton(text='17', callback_data='hours'),
        InlineKeyboardButton(text='18', callback_data='hours'),
        InlineKeyboardButton(text='19', callback_data='hours'),
        InlineKeyboardButton(text='20', callback_data='hours'),
        InlineKeyboardButton(text='21', callback_data='hours'),
        InlineKeyboardButton(text='22', callback_data='hours'),
        InlineKeyboardButton(text='23', callback_data='hours'),
        InlineKeyboardButton(text='24', callback_data='hours')
    ],
    [
        InlineKeyboardButton(text='25', callback_data='hours'),
        InlineKeyboardButton(text='26', callback_data='hours'),
        InlineKeyboardButton(text='27', callback_data='hours'),
        InlineKeyboardButton(text='28', callback_data='hours'),
        InlineKeyboardButton(text='29', callback_data='hours'),
        InlineKeyboardButton(text='30', callback_data='hours')
    ]
]

even_days = [
    [
        InlineKeyboardButton(text='01', callback_data='hours'),
        InlineKeyboardButton(text='02', callback_data='hours'),
        InlineKeyboardButton(text='03', callback_data='hours'),
        InlineKeyboardButton(text='04', callback_data='hours'),
        InlineKeyboardButton(text='05', callback_data='hours'),
        InlineKeyboardButton(text='06', callback_data='hours'),
        InlineKeyboardButton(text='07', callback_data='hours'),
        InlineKeyboardButton(text='08', callback_data='hours')
    ],
    [
        InlineKeyboardButton(text='09', callback_data='hours'),
        InlineKeyboardButton(text='10', callback_data='hours'),
        InlineKeyboardButton(text='11', callback_data='hours'),
        InlineKeyboardButton(text='12', callback_data='hours'),
        InlineKeyboardButton(text='13', callback_data='hours'),
        InlineKeyboardButton(text='14', callback_data='hours'),
        InlineKeyboardButton(text='15', callback_data='hours'),
        InlineKeyboardButton(text='16', callback_data='hours')
    ],
    [
        InlineKeyboardButton(text='17', callback_data='hours'),
        InlineKeyboardButton(text='18', callback_data='hours'),
        InlineKeyboardButton(text='19', callback_data='hours'),
        InlineKeyboardButton(text='20', callback_data='hours'),
        InlineKeyboardButton(text='21', callback_data='hours'),
        InlineKeyboardButton(text='22', callback_data='hours'),
        InlineKeyboardButton(text='23', callback_data='hours'),
        InlineKeyboardButton(text='24', callback_data='hours')
    ],
    [
        InlineKeyboardButton(text='25', callback_data='hours'),
        InlineKeyboardButton(text='26', callback_data='hours'),
        InlineKeyboardButton(text='27', callback_data='hours'),
        InlineKeyboardButton(text='28', callback_data='hours'),
        InlineKeyboardButton(text='29', callback_data='hours'),
        InlineKeyboardButton(text='30', callback_data='hours'),
        InlineKeyboardButton(text='31', callback_data='hours')
    ]
]

f_days = [
    [
        InlineKeyboardButton(text='01', callback_data='hours'),
        InlineKeyboardButton(text='02', callback_data='hours'),
        InlineKeyboardButton(text='03', callback_data='hours'),
        InlineKeyboardButton(text='04', callback_data='hours'),
        InlineKeyboardButton(text='05', callback_data='hours'),
        InlineKeyboardButton(text='06', callback_data='hours'),
        InlineKeyboardButton(text='07', callback_data='hours'),
        InlineKeyboardButton(text='08', callback_data='hours')
    ],
    [
        InlineKeyboardButton(text='09', callback_data='hours'),
        InlineKeyboardButton(text='10', callback_data='hours'),
        InlineKeyboardButton(text='11', callback_data='hours'),
        InlineKeyboardButton(text='12', callback_data='hours'),
        InlineKeyboardButton(text='13', callback_data='hours'),
        InlineKeyboardButton(text='14', callback_data='hours'),
        InlineKeyboardButton(text='15', callback_data='hours'),
        InlineKeyboardButton(text='16', callback_data='hours')
    ],
    [
        InlineKeyboardButton(text='17', callback_data='hours'),
        InlineKeyboardButton(text='18', callback_data='hours'),
        InlineKeyboardButton(text='19', callback_data='hours'),
        InlineKeyboardButton(text='20', callback_data='hours'),
        InlineKeyboardButton(text='21', callback_data='hours'),
        InlineKeyboardButton(text='22', callback_data='hours'),
        InlineKeyboardButton(text='23', callback_data='hours'),
        InlineKeyboardButton(text='24', callback_data='hours')
    ],
    [
        InlineKeyboardButton(text='25', callback_data='hours'),
        InlineKeyboardButton(text='26', callback_data='hours'),
        InlineKeyboardButton(text='27', callback_data='hours'),
        InlineKeyboardButton(text='28', callback_data='hours')
    ]
]

