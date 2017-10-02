#!/usr/bin/env python 3

from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of Words from URl.

    Args:
        url: The URL of a UTF-8 text document.
    Returns:
        A list of strings containing the words from the document
    """
    with urlopen(url) as story:
        story_word = []

        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_word.append(word)

    return story_word


def print_words(story_words):
    for word in story_words:
        print(word)


def main():
    words = fetch_words("http://google.com")
    print_words(words)


if __name__ == '__main__':
    main()
