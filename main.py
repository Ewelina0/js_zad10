import re

def find_words(text):
    print(re.findall(r"\b\w{4,}\b", text))


if __name__ == '__main__':
    text = 'raz dwa trzy cztery pięć sześć siedem osiem.'
    find_words(text)
