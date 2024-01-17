# MAIN THREAD :
# Working with mainthread :
# Getteing the information about current thread :
import threading
print(1)
print(2)
print(3)
print(threading.current_thread())

for i in range(5):
    print('surendra')
print(threading.current_thread())
print(threading.current_thread().getName())    # thread name 
print(threading.current_thread().name)         # thread name
print(threading.current_thread().ident)        # thread id 
print(threading.current_thread().is_alive())   # to know active or not


