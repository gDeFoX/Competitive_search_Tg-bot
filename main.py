import re

def clear_input() -> dict[str] | None:
    raw_input: str = input()

    normalized_input: str = re.sub(r"[.,;|+]", " ", raw_input)
    raw_words = normalized_input.split()

    clean_words = [
        word.strip().lower() 
        for word in raw_words 
        if len(word.strip()) > 1
    ]

    return clean_words

def main():
    search_input = clear_input()
    if search_input == None:
        return "Неверный ввод"
    else:
        return "Начинаю следующий шаг"


if __name__ == "__main__":
    main()