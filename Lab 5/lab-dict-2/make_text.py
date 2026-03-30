import sys


def word_count(texts: list[str]) -> dict:
    word_list: list[str] = []
    count: int = 0
    for text in texts:
        fh = open(text)
        for line in map(str.strip, fh):
            for word in line.lower().split():
                word = word.strip('"!“”#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ')
                word_list.append(word)
                if word == word:
                    pass
    print(word_list)

def word_pairs(texts: list[str]) -> dict:
    word_counts: dict[tuple[str, str], dict[str, int]] = {}
    word_list: list[str] = []
    for text in texts:
        fh = open(text)
        for line in map(str.strip, fh):
            for word in line.lower().split():
                word = word.strip('"!“”#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ')
                word_list.append(word)

        fh.close()


def main(texts: list[str]):
    words: dict = word_count(texts)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main(["pg1497.txt"])
