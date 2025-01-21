## Points to note
* `time.sleep()` blocks the calling thread but releases the GIL allowing other python threads to run.
* `threading.Event` class is Python's simplest signalling mechanism to coordinate threads.
* Every python process has its own `GIL`

### threading.event
* `threading.Event` class is Python's simplest signalling mechanism to coordinate threads.
* Event instance has an internal boolean flag which starts with False
* `Event.set()` sets the flag to True
* When flag=False, a thread that calls `Event.wait()` would wait for the flag to be set and is hence blocked.
* if there is a timeout specified like `Event.wait(s)`, then this call returns False when timeout elapses
* call returns True if the flag is set by another thread using `Event.set()`


### multiprocessing.Process
* Each instance runs a new python interpreter as a child process in the bg
* 1 Process -> 1 GIL
* multiprocess APIs work very similar to threading APIs