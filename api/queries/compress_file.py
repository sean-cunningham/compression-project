import time
from queries.lzw import lzw_compress, lzw_decompress
from queries.rle import rle_compress, rle_decompress

algos = {
        "Run Length Encoding": [rle_compress, rle_decompress],
        "Lempel-Ziv-Welch (LZW)": [lzw_compress, lzw_decompress]
    }


def compress(file: bytes):
    results = {}

    for name, algo in algos.items():
        start = time.time()
        compressed_file = algo[0](file)
        compress_time = time.time() - start

        start = time.time()
        algo[1](compressed_file)
        decompress_time = time.time() - start

        results[name] = {
            'original_size': len(file),
            'compressed_size': len(compressed_file),
            'compress_time': compress_time,
            'decompress_time': decompress_time
        }

    return results
