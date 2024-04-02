# # # thread= a flow of execution. like a separate order of instructions
# # import threading
# # import time
# #
# # # GIL(global interpreter lock)
# #
# # # import tkinter
# #
# #
# # # cpu bound=program task spends most of it's time waiting for internal events
# # # (cpu intensive ) we use multiprocessing
# # # # io bound program/task spends most  of it's time waiting for external events (user input,web scraping)
# # # print(threading.active_count())
# # # print(threading.enumerate())
# # def eat_breakfast():
# #     time.sleep(3)
# #     print("you eat breakfast")
# #
# #
# # def drink_coffee():
# #     time.sleep(4)
# #     print("you drink coffee")
# #
# #
# # def study():
# #     time.sleep(5)
# #     print("you finish studying")
# #
# #
# # x = threading.Thread(target=eat_breakfast, args=())
# # x.start()
# # y = threading.Thread(target=drink_coffee, args=())
# # y.start()
# # z = threading.Thread(target=study, args=())
# # z.start()
# # x.join()
# # y.join()
# # z.join()
# # print("hello")
# # print(threading.active_count())
# # print(threading.enumerate())
# # # print(time.process_time())
# # print(time.perf_counter())
#
# # daemon threads
# # a thread that runs in the background not important for program to run
# # your program will not wait for daemon threads to complete before exiting
# #  non daemon threads cannot normally be killed, stay alive until task is complete
# # e.g. background task garbage collection,waiting for input,long-running processes
# import threading
# import time
#
#
# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for:", count, "seconds")
#         if count == 60:
#             break
#
#
# x = threading.Thread(target=timer,daemon=True)
# x.start()
# answer = input("Do you wish to exit? ")
# print()
import time
from multiprocessing import Process, cpu_count


def counter(num):
    count = 0
    while count < num:
        count += 1
        # print(count)


def main():
    print(cpu_count())
    a = Process(target=counter, args=(125000000,))
    b = Process(target=counter, args=(125000000,))
    c = Process(target=counter, args=(125000000,))
    d = Process(target=counter, args=(125000000,))
    e = Process(target=counter, args=(125000000,))
    f = Process(target=counter, args=(125000000,))
    g = Process(target=counter, args=(125000000,))
    h = Process(target=counter, args=(125000000,))
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    print(time.thread_time())


if __name__ == '__main__':
    #    main process
    main()

