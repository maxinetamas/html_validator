#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    tags = _extract_tags(html)
    strings = []
    for i, symbol in enumerate(tags):
        if symbol[1] != '/':
            strings.append(symbol[1:-1])
        else:
            if len(strings) == 0:
                return False
            for j in range(len(strings)):
                if symbol[2:-1] == strings[j]:
                    strings.pop()
    if len(strings) == 0:
        return True
    else:
        return False

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the class/book
    # the main difference between your code and the code from class will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    arr = []
    for i in range(0, len(html) - 1):
        if html[i] == '<':
            for j in range(0, len(html) - i):
                if html[j] == '>':
                    arr.append(html[i:j + 1])
    return arr
