# Lempel-Ziv-Welch (LZW)

def lzw_compress(data):
    if data == b"":
        return []

    b_string = b""
    result = []
    lookup_size = 256
    lookup = {bytes([i]): i for i in range(lookup_size)}

    for byte in data:
        b_string_plus = b_string + bytes([byte])
        if b_string_plus in lookup:
            b_string = b_string_plus
        else:
            print(lookup[b_string])
            result.append(lookup[b_string])
            lookup[b_string_plus] = lookup_size
            lookup_size += 1
            b_string = bytes([byte])

    if b_string:
        result.append(lookup[b_string])

    return result


def lzw_decompress(data):
    if data == []:
        return b""

    lookup_size = 256
    lookup = {i: bytes([i]) for i in range(lookup_size)}

    val = bytes([data.pop(0)])
    result = bytearray(val)

    for b in data:
        if b in lookup:
            res = lookup[b]
        elif b == lookup_size:
            res = val + val[:1]
        else:
            raise ValueError("invalid data")

        result.extend(res)

        lookup[lookup_size] = val + res[:1]
        lookup_size += 1

        val = res

    return bytes(result)
