import threading
import os
import time

def something(word):
    while True:
        print(word)
        time.sleep(3)

if __name__ == '__main__':
    print('기준 프로세스 아이디 :', os.getpid())
    t = threading.Thread(target=something, args=('happy',))
    t.daemon = True # 메인이 끝나면 같이 끝내기
    t.start()

    print('메인 스레드에서 반복문 시작')
    while True:
        try:
            print('ㅇ먀ㅣㅛ...')
            time.sleep(1)
        except KeyboardInterrupt:
            print('good bye~')
            break