if str == bytes:
    string_or_bytes = basestring
else:
    string_or_bytes = (str, bytes, bytearray)

def is_unicode_or_bytes(argument):
    return isinstance(argument, string_or_bytes)
