import time
from queries.lzw import lzw_compress, lzw_decompress
from queries.rle import rle_compress, rle_decompress
from queries.bwt import bw_transform, bw_rebuild

algos = {
        "Run Length Encoding (RLE)": [rle_compress, rle_decompress, False],
        "Lempel-Ziv-Welch (LZW)": [lzw_compress, lzw_decompress, False],
        "RLE w/ BWT": [rle_compress, rle_decompress, True],
        "LZW w/ BWT": [lzw_compress, lzw_decompress, True]
    }


def compress(file: bytes):
    results = {}

    for name, algo in algos.items():
        use_bwt = algo[2]

        if use_bwt:
            compressable_file, idx, mark = bw_transform(file)
        else:
            compressable_file = file

        start = time.time()
        compressed_file = algo[0](compressable_file)
        compress_time = time.time() - start

        # start = time.time()
        # decompressed_file = algo[1](compressed_file)
        # decompress_time = time.time() - start

        # if use_bwt:
        #     rebuilt_file = bw_rebuild(decompressed_file, idx, mark)
        # else:
        #     rebuilt_file = decompressed_file

        compressed = len(compressed_file)/len(file)
        original_size = len(file)
        compressed_size = len(compressed_file)
        # decompressed_size = len(rebuilt_file)

        results[name] = {
            'original_size': original_size,
            'compressed_size': compressed_size,
            'compression': compressed,
            'compress_time': compress_time,
            # 'decompress_time': decompress_time,
            # 'decompress_size': decompressed_size
        }

    return results
