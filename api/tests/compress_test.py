import pytest
import os
import sys
from fastapi.testclient import TestClient
from main import app
from queries.rle import rle_compress, rle_decompress
from queries.lzw import lzw_compress, lzw_decompress
from queries.compress_file import algos

client = TestClient(app)


def test_compression():

    path = os.path.join(os.path.dirname(__file__), 'test_file.txt')

    with open(path, 'rb') as f:
        content = f.read()

    response = client.post(
        "/compress/",
        files={'file': ('test_file.txt', content, 'text/plain')}
    )

    assert response.status_code == 200

    results = response.json()

    for algo in algos.keys():
        assert algo in results
        assert 'compressed_size' in results[algo]
        assert 'compress_time' in results[algo]
        assert 'decompress_time' in results[algo]


def test_rle_compress():
    assert rle_compress(b"") == ""
    assert rle_compress(b"aaabbbaaaaaabbbbbbb") == b"\x03a\x03b\x06a\x07b"


def test_rle_decompress():
    assert rle_decompress(b"") == ""
    assert rle_decompress(b"\x03a\x03b\x06a\x07b") == b"aaabbbaaaaaabbbbbbb"


def test_lzw_compress():
    assert lzw_compress(b"") == []
    assert lzw_compress(b"aaabbbaaaaaabbbbbbb") == [97, 256, 98, 258, 256, 260, 97, 258, 263, 258]


def test_lzw_decompress():
    assert lzw_decompress([]) == b""
    assert lzw_decompress([97, 256, 98, 258, 256, 260, 97, 258, 263, 258]) == b"aaabbbaaaaaabbbbbbb"
