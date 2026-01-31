# Show examples of encoding/decoding and handling UnicodeDecodeError.

def demo_encoding_errors() -> None:
    text = "Café – π = 3.14159 ✅"

    encodings = ["utf-8", "utf-16", "cp1252"]

    for enc in encodings:
        print(f"\n=== Encoding with {enc} ===")
        try:
            encoded = text.encode(enc)
            print(f"Encoded bytes: {encoded!r}")
        except UnicodeEncodeError as e:
            print(f"UnicodeEncodeError while encoding with {enc}: {e}")
            continue

        # Correct decode
        decoded_ok = encoded.decode(enc)
        print(f"Decoded correctly with {enc}: {decoded_ok!r}")

        # Intentionally decode with a *wrong* encoding to cause trouble
        wrong_enc = "latin-1" if enc == "utf-8" else "utf-8"
        print(f"\nDecoding {enc} bytes *as* {wrong_enc}:")

        # strict (default) – may raise UnicodeDecodeError
        try:
            decoded_strict = encoded.decode(wrong_enc, errors="strict")
            print(f"strict: {decoded_strict!r}")
        except UnicodeDecodeError as e:
            print(f"strict raised UnicodeDecodeError: {e}")

        # ignore – silently drops problematic bytes
        decoded_ignore = encoded.decode(wrong_enc, errors="ignore")
        print(f"ignore: {decoded_ignore!r}")

        # replace – substitutes � for problematic bytes
        decoded_replace = encoded.decode(wrong_enc, errors="replace")
        print(f"replace: {decoded_replace!r}")

        # backslashreplace – shows escape sequences
        decoded_backslash = encoded.decode(wrong_enc, errors="backslashreplace")
        print(f"backslashreplace: {decoded_backslash!r}")


if __name__ == "__main__":
    demo_encoding_errors()