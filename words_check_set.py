def word_check(words: str) -> None:
    f = open('words.txt', 'rt')
    correct_word_set: set = set(word.strip() for word in f.read().strip().splitlines() if word.strip)
    f.close()
    words: str = str(words).strip()
    words_set: set = set(word.strip() for word in words.lower().split(' ') if word.strip())

    words_count: int = len(words_set)
    mistakes_count: int = 0
    mistakes_words: set = {}

    mistakes_words: set = words_set - correct_word_set
    mistakes_count: int = len(mistakes_words)

    print(f"words count: {words_count}\nmistakes words: {mistakes_words}\nmistakes_count: {mistakes_count}")

if __name__ == "__main__":
    word_check(input('Enter Your Sentences: '))