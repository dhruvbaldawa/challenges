import sys
import logging
import re


def get_subsequence(sentence_words, words):
    result = float('inf')
    start = -1
    end = -1
    bin = { word: -1 for word in words }
    for i in xrange(len(sentence_words)):
        word = re.sub('[^A-Za-z0-9]','', sentence_words[i])
        word = word.lower()

        if word not in bin:
            continue

        # put the position for the word in the bin
        bin[word] = i

        # get the first occuring element
        head = min(bin.values())
        # get the last occuring element
        tail = max(bin.values())

        # there is atleast one element found yet
        if head == -1:
            continue
        else:
            # if minimum length is greater than tail-head+1
            if result > tail-head+1:
                # set the new minimum length
                start, end, result = head, tail, tail-head+1

        # if the result has all the elements from the bin
        if result == len(bin):
            break

    if start == -1:
        return 'NO SUBSEGMENT FOUND'
    else:
        match = " ".join(sentence_words[start:end+1] )
        return re.sub('[^A-Za-z ]', '', match)


def main():
    data = sys.stdin.read().splitlines()
    sentence = data[0]
    words = data[2:]

    sentence_words = sentence.split()
    logging.debug('sentence_words: %s' % sentence_words)

    match = get_subsequence(sentence_words, words)
    print match

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
