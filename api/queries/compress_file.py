import time
from queries.lzw import lzw_compress, lzw_decompress
from queries.rle import rle_compress, rle_decompress
from queries.bwt import bw_transform, bw_rebuild

algos = {
        "Run Length Encoding": [rle_compress, rle_decompress, False],
        "Lempel-Ziv-Welch (LZW)": [lzw_compress, lzw_decompress, False],
        "Run Length Encoding w/ BWT": [rle_compress, rle_decompress, True],
        "Lempel-Ziv-Welch (LZW) w/ BWT": [lzw_compress, lzw_decompress, True]
    }


def compress(file: bytes):
    results = {}

    for name, algo in algos.items():
        bool = algo[2]

        if bool:
            file, idx, mark = bw_transform(file)

        start = time.time()
        compressed_file = algo[0](file)
        compress_time = time.time() - start

        if bool:
            print("fjsdlafjdksl;")
            # compressed_file = bw_rebuild(compressed_file, idx, mark)

        start = time.time()
        algo[1](compressed_file)
        decompress_time = time.time() - start

        percent_compressed = len(compressed_file)/len(file)

        results[name] = {
            'original_size': len(file),
            'compressed_size': len(compressed_file),
            'decompression %': percent_compressed,
            'compress_time': compress_time,
            'decompress_time': decompress_time
        }

    return results
