import tracemalloc # 메모리 할당 추적 python 3.4 이상에서 사용 가능

tracemalloc.start() # 메모리 할당 추적 시작

# 메모리 할당이 진행되는 작업
data = [b'%d' % num for num in range(1, 10001)]

joined_data = b' '.join(data) # data 리스트의 각 요소를 공백으로 구분하여 하나의 bytes 객체로 결합

current, peak = tracemalloc.get_traced_memory() # 현재 메모리 사용량과 peak 메모리 사용량 조회
print(f"현재 메모리 사용량 : {current / 10 ** 6} MB")
print(f"최대 메모리 사용량: {peak / 10 ** 6} MB")

tracemalloc.stop() # 메모리 할당 추적 중지

traced = tracemalloc.get_tracemalloc_memory()
print(traced / 10 ** 6)