def all_variants(text):
    if not text:
        yield ''
        return

    for variant in all_variants(text[1:]):
        yield variant
        yield text[0] + variant

a = all_variants("abc")
for i in a:
    print(i)
