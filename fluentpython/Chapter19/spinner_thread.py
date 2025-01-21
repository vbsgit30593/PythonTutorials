from threading import Event, Thread
import itertools
import time

def spinner(msg: str, done: Event) -> None:
    for ch in itertools.cycle(r'\|/-'):
        status = f'\r{ch} {msg}'
        print(status, end="", flush=True)
        if done.wait(.1):
            break

    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end="")

def slow() -> int:
    time.sleep(3)
    return 231


def supervisor():
    event = Event()
    thread = Thread(target=spinner, args=['Thinking', event])
    print(f"{thread = }")
    thread.start()
    ret = slow()
    event.set()
    thread.join()
    return ret

def main():
    ret = supervisor()
    print(f"Answer: {ret}")


if __name__ == "__main__":
    main()