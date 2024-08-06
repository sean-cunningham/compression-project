import pytest
import os
import sys
from fastapi.testclient import TestClient
from main import app
from queries.rle import rle_compress, rle_decompress

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

    assert 'zlib' in results
    assert results['zlib']['compressed_size'] < len(content)
    assert 'compress_time' in results['zlib']
    assert 'decompress_time' in results['zlib']


def test_rle_compress():
    assert rle_compress(b"") == ""
    assert rle_compress(b"aaabbbaaaaaabbbbbbb") == b"\x03a\x03b\x06a\x07b"


def test_rle_decompress():
    assert rle_decompress(b"") == ""
    assert rle_decompress(b"\x03a\x03b\x06a\x07b") == b"aaabbbaaaaaabbbbbbb"
