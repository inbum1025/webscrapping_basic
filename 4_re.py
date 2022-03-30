import re  # 정규식  library

p = re.compile("ca.e")  # .은 문자 하나를 의미함

# ^ (^de): 문자열의 시작
# $ (se$) : 문자열의 끝


def print_match(m):
    if m:
        print("m.group():", m.group())  # 일치하는 문자열
        print("m.string", m.string)  # 입력받은 문자열
        print("m.start()", m.start())  # 일치하는 문자열의 시작indxex
        print("m.end()", m.end())  # 일치하는 문자열의 끝 index
        print("m.span()", m.span())  # 일치하는 문자열의 시작 / 끝 index

    else:
        print("매치되지않음")


m = p.match("case")  # 처음부터 일치하는지

print_match(m)


# m = p.search("good care")  # 일치하는 문자열이 있는지
# print_match(m)

# m = p.search("good care")   #주어진 문자열에 일치하는게 있는지 확인
# 1st = p.findall("good care cafe")  # 일치하는 모든것을 <리시트> 형태로 줌
