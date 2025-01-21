from multiprocessing import Process, Event
from multiprocessing import synchronize
import itertools
import time


def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        if done.wait(.1):
            break
    
    blanks = " " *  len(status)
    print(f"\r{blanks}\r", end="")

def slow():
    time.sleep(3)
    return 1212

def supervisor():
    event = Event()
    spinner = Process(target=spin, args=["Thinking", event])
    print(f"{spinner = }")
    spinner.start()
    ret = slow()
    event.set()
    spinner.join()

    return ret

def main():
    ret = supervisor()
    print(f"{ret = }")

if __name__ == "__main__":
    main()
