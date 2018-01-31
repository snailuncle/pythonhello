import re
match = re.search(r"[1-9]\d{5}", "bit 100081")
if match:
    print(match.group(0))
else:
    print(0)
match = re.match(r"[1-9]\d{5}", "100032232")
if match:
    print(match.group(0))
else:
    print("000")
match = re.split(r"[1-9]\d{5}", "bit 100031 tsu102020")
print(match)
match = re.split(r"[1-9]\d{5}", "bit 111111 tsu 333333", maxsplit=1)
print(match)
print("finditer迭代开始")
s = "bit 123456 tsu123321 9"
matchR = r"[1-9]\d{5}"
for m in re.finditer(matchR, s):
    if m:
        print(m.group(0))
s = re.sub(matchR, "666中国人", s)
print(s)
