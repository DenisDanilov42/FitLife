WATER_PER_KG = 0.03  # в литрах

# 1. Знакомство
user_name = input('Как вас зовут: ')
message = 'Сколько вам лет? '
while True:
    try:
        user_age = int(input(message))
        break
    except ValueError:
        message = 'Укажите ваш возраст числом (полных лет): '

# 2. Сбор данных
message = 'Укажите ваш вес (в кг): '
while True:
    try:
        user_weight = float(input(message))
        break
    except ValueError:
        message = 'Укажите ваш вес числом (в кг): '

message = 'Укажите рост (в метрах): '
while True:
    try:
        user_height = float(input(message))
        break
    except ValueError:
        message = 'Укажите ваш рост числом  \n'\
                  '(в метрах, используя точку, например 1.75): '

# 3. Расчеты
# Расчет ИМТ
bmi = user_weight / (user_height**2)
# Расчет рекомендуемой нормы воды
water_needed = user_weight * WATER_PER_KG

# 4. Вывод результата
print(f"\nПривет, {user_name}!")
print("=" * 40)
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print("=" * 40)
print(f"Твой Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_needed:.1f} л. в день")
print("-" * 40)
print("Расчет окончен. Будьте здоровы!")
