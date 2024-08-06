# Run Length Encoding


def rle_compress(data):

    if data == b"":
        return ""

    compressed_data = bytearray()
    count = 1
    prev = data[0]

    for byte in data[1:]:
        if byte == prev:
            count += 1
            if count == 255:
                compressed_data.extend([count, prev])
                count = 1

        else:
            compressed_data.extend([count, prev])
            prev = byte
            count = 1

    compressed_data.extend([count, prev])
    return bytes(compressed_data)


def rle_decompress(data):
    decompressed_data = bytearray()

    if data == b"":
        return ""

    for i in range(0, len(data), 2):
        decompressed_data.extend([data[i+1]] * data[i])

    return bytes(decompressed_data)
