foods = ["햄버거", "피자", "치킨", "떡볶이"]

print(id(foods)) # 메모리 주소
print(hex(id(foods))) # 16진수

mv = memoryview(b"happy day") # bytes 객체를 메모리뷰로 변환
print(mv)

# bytes 형태로 넣어서 bytes 방식 출력
print(mv[0]) 
print(mv[1])
print(mv[2])
print(mv[3])

print(mv[20])