from online import get_currencies


# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 7. Вывод результата
#TODO– сделать проверку при вводе сушествует ли данная валюта
#TODO– добавить возможность использования нецелых чисел
#TODO– реализовать подгрузку курсов валют по API

#online_response = get_currencies()['data'] : исправлено
#Небезопасное обращение к ключу data. Стоит делать через get с переданным стандартным значением, чтобы исключить поломку проекта
#amount = float(input("Введите количество валюты: "))
#Если введу слово, например, "Привет", то сломаю программу :(


def convert(amount, from_ticker, to_ticker, currencies):
    from_currency = currencies.get(from_ticker)
    to_currency = currencies.get(to_ticker)
    coefficient = to_currency / from_currency
    return round(amount * coefficient, 2)


def input_currency(input_message, currencies):
    ticker = input(f"{input_message}: ").strip().upper() #upper() для "борьбы" с неправильным регистром
    currency = currencies.get(ticker, None)
    if currency is None:
        print(f'Валюта {ticker} не найдена. Пожалуйста, повторите ввод')
        return input_currency(input_message, currencies)
    return ticker


def input_amount(input_message):
    try:
        amount = input(f"{input_message}: ")
        num = float(amount)
        return num
    except ValueError:
        print(f'Ошибка ввода количества валюты "{amount}". Пожалуйста, введите число')
    return input_amount(input_message)

#current_currencies = {'RUB': 97.4545572753, 'EUR': 0.9487101161, 'USD': 1,}
online_response = get_currencies().get('data', None)
if online_response is None:
    print("Ошибка подгрузки курсов валют!")
    exit()

print("Привет, это программа Конвертер Валют!")

print("""
Для работы с программой требуется:
- выбрать исходную валюту 
- выбрать в какую валюту следует перевести
- ввести количество исходной валюты

Доступные валюты:""")
print(*online_response)

from_ticker = input_currency("Введите исходную валюту", online_response)
to_ticker = input_currency("Введите в какую валюту следует перевести", online_response)
amount = input_amount("Введите количество валюты: ")

print(f"Подгружены курсы: \n1 {from_ticker} = {online_response[from_ticker]} USD "
      f"\n1 {to_ticker} = {online_response[to_ticker]} USD\n")

result = convert(amount, from_ticker, to_ticker, online_response)

print(f'Результат: {amount} {from_ticker} = {result} {to_ticker}')