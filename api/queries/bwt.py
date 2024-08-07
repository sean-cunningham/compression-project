# Burrows-Wheeler Transformation

import os


def find_unique(b_str):
    count, length, max_try = 0, 1, 100
    while True:
        unique = os.urandom(length)
        if unique not in b_str:
            return unique
        count += 1
        if count >= max_try:
            length += 1
            count = 0


def bw_transform(b_str):
    mark = find_unique(b_str)
    b_str += mark
    arr = [b_str[i:] + b_str[:i] for i in range(len(b_str))]
    arr.sort()
    new_word = b"".join([word[-1:] for word in arr])

    idx = arr.index(b_str)

    return new_word, idx, mark


def bw_rebuild(word, idx, mark):
    arr = [b""] * len(word)
    for _ in range(len(word)):
        arr = sorted([word[i:i+1] + arr[i] for i in range(len(word))])

    result = arr[idx]
    return result.rstrip(mark)


def compress_bw_rle(data):
    bw_transform(data)
