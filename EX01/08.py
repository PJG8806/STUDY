# 내 파이썬 프로그램의 이름을 알아보자.
import psutil
import os

pid = os.getpid()
print(f"현재 PID: {pid}")
current_proc = psutil.Process(pid)
print(f"현재 프로세스 이름: {current_proc.name()}")