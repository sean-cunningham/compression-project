import pytest
import os
import sys
from fastapi.testclient import TestClient
from main import app

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
