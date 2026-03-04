import psutil
import os


print("메모리 사용량 조회하기")

memory_dict = psutil.virtual_memory()._asdict() # 메모리 사용량 조회하기, 튜플 형태를 딕셔너리로 변환
print(memory_dict)

total = memory_dict['total']
available = memory_dict['available']
percent = memory_dict['percent']

print(f"총 메모리 : {total} bytes")
print(f"메모리 즉시 제공 가능량 : {available} bytes")
print(f"메모리 사용률 : {percent} ")

pid = os.getpid()
current_process = psutil.Process(pid) # 현재 프로세스의 메모리 사용량 조회하기

# 프로세스가 사용한 물리적인 메모리량
kb = current_process.memory_full_info()[0] / 2 ** 20 # bytes -> KB
print(f"메모리 사용량 : {kb:.2f} KB")