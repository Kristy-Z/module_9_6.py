def all_variants(text):
    if not text:
        yield ''
        return

    first = text[0]
    second = text[1:]

    for variant in all_variants(second):
        yield variant
        yield first + variant

a = all_variants("abc")
for i in a:
    print(i)
