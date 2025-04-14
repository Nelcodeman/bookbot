def word_count(text: str) -> int:
    return len(text.split())


def letter_count(text: str):

    letters = {}

    text = text.lower()
    for n in text:
        letters[n] = letters.get(n, 0) + 1

    return letters


def sort_dict(char_dict: dict):
    final_list = []
    for key, value in char_dict.items():
        final_list.append(
            {
                "character": key,
                "count": value,
            }
        )
    final_list.sort(key=count, reverse=True)

    return final_list


def count(dicionario):
    return dicionario["count"]
