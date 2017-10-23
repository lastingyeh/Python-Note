import threading
import time


def t1_job():
    print('T1 start\n')

    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

    # print('This is an added Thread, number is %s' % threading.current_thread())


def t2_job():
    print('T2 start\n')
    print('T2 finish\n')


def main():
    thread1 = threading.Thread(target=t1_job, name='T1')
    thread2 = threading.Thread(target=t2_job, name='T2')
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    # await added_thread finish
    # added_thread.join()
    print('all done\n')


if __name__ == '__main__':
    main()
