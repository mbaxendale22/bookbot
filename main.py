def read_in(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def get_word_count(passage):
    return len(passage.split())


def get_char_count(passage):
    char_count_dict = {}

    for c in passage:
        lowered = c.lower()
        if lowered in char_count_dict:
            char_count_dict[lowered] += 1
        else:
            char_count_dict[lowered] = 1

    return char_count_dict


def sorting_key(dict):
    return dict["num"]


def generate_report(word_count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    sorted_list = []

    for c in char_count:
        if c.isalpha():
            sorted_list.append({"char": c, "num": char_count[c]})

    sorted_list.sort(key=sorting_key, reverse=True)

    for c in sorted_list:
        print(f"the '{c['char']}' character was found {c['num']} times")


def main():
    words = read_in("./books/frankenstein.txt")
    word_count = get_word_count(words)
    a = get_char_count(words)
    generate_report(word_count, a)


main()
