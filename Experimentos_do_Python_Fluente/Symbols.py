'''
The ord() function returns the number representing the unicode code of a specified character.

'''
symbols = '$¢£¥€¤'
codes = []
codes2 = []
codes3 = []
for symbol in symbols:
    codes.append(ord(symbol))

print("CODES:", codes)

codes2 = [ord(symbol) for symbol in symbols]
print("CODES2:", codes2)

codes3 = [last := ord(c) for c in symbols]
print("CODES3:", codes3, last)


beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print("beyond_ascii", beyond_ascii)

beyond_ascii_map_filter = list(filter(lambda c: c > 127, map(ord, symbols)))
print("beyond_ascii_map_filter", beyond_ascii_map_filter)