import requests


def get_crypto_info(currency_code):
    url = f"https://api.coingecko.com/api/v3/coins/{currency_code}"
    try:
        response = requests.get(url)

        if response.status_code == 404:
            print("Помилка: криптовалюта не знайдена")
            return

        response.raise_for_status()
        crypto_data = response.json()

        name = crypto_data.get('name')
        if not name:
            print("Помилка: не вдалося отримати назву криптовалюти")
            return

        symbol = crypto_data.get('symbol', 'Немає даних').upper()

        description = crypto_data.get('description', {})
        if isinstance(description, dict):
            description = description.get('en', 'Немає опису англійською')
        else:
            description = str(description) if description else 'Немає опису'

        if len(description) > 500:
            description = description[:500] + "..."

        print(f"\nІм'я криптовалюти: {name}")
        print(f"Символ: {symbol}")
        print(f"Опис:\n{description}")

    except requests.exceptions.RequestException as e:
        print(f"Помилка при отриманні даних: {e}")
    except Exception as e:
        print(f"Неочікувана помилка: {e}")


def main():
    print("Отримання інформації про криптовалюту")
    print("Приклад валютного коду: bitcoin, ethereum, dogecoin")

    currency_code = input("Введіть валютний код криптовалюти: ").strip().lower()
    if not currency_code:
        print("Помилка: не введено код валюти")
        return

    get_crypto_info(currency_code)


if __name__ == "__main__":
    main()
