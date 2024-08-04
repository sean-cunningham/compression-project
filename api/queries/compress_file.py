import time
import zlib


def compress(file: bytes):
    results = {}

    algos = {
        "zlib": zlib
    }

    for name, algo in algos.items():
        start = time.time()
        compressed_file = algo.compress(file)
        compress_time = time.time() - start

        start = time.time()
        algo.decompress(compressed_file)
        decompress_time = time.time() - start

        results[name] = {
            'original_size': len(file),
            'compressed_size': len(compressed_file),
            'compress_time': compress_time,
            'decompress_time': decompress_time
        }

    return results
