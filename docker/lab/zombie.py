import os, time

pid = os.fork()          # split into two processes: parent and child
if pid == 0:
    print("child: exiting now")
    os._exit(0)          # child dies immediately
else:
    print(f"parent: child pid is {pid}, I'm calling wait()")
    os.wait()
    time.sleep(60)