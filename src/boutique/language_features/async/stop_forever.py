import threading

def fun():
    print("Geeks For Geeks")

t = threading.Thread(target=fun)

print("GFG")
print(T.isDaemon())

# set thread as Daemon
T.setDaemon(True)

# check status
print(T.isDaemon())
T.start()

if __name__ == "__main__":
    cl_arguments = sys.argv[1:]
    if len(cl_arguments) == 0:
        print("args help goes here")
    if cl_arguments[0] not in ('start', 'stop'):
        print("more help")
    main(cl_arguments[0])
