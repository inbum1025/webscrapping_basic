import re

p = re.compile("ca.e")  # .은 문자 하나를 의미함


def print_match(m):
    if m:
        print(m.group())
    else:
        print("매치되지않음")


m = p.match("case")  # 처음부터 일치하는지
print_match(m)

m = p.search("good care")  # 일치하는 문자열이 있는지
print_match(m)
