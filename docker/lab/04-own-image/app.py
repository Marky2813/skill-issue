import os, socket 
print(f"hello from PID {os.getpid()} on host {socket.gethostname()}")
