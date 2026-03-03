from multiprocessing import Process, Pipe
import os

def send(conn):
    print(f"{os.getpid()}가 {os.getppid()}에게 메시지를 보낸다!")
    conn.send("Hello parent!")
    conn.close()

if __name__ == '__main__':
    parent, child = Pipe()
    p = Process(target=send, args=(child,))
    p.start()
    print('기존 프로세스 아이디 :', os.getpid())
    print(parent.recv())
    p.join() # 프로세스 종료까지 기다린다