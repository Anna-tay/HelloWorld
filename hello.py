def main(words):
    print(words)
    expand(words)

def expand(words_expand):
    for x in words_expand:
        print(x)

words = "Hello World"
main(words)