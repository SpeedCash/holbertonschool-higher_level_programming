#!/usr/bin/python3

def multiple_returns(sentence):

    if sentence:
        return len(sentence), sentence[0]
    else:
        return len(sentence), None


if __name__ == "__main__":
    print(multiple_returns("Python"))
    print(multiple_returns(""))
