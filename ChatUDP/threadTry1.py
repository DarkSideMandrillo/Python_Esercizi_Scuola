import threading
import time

def contatore(nome, ritardo):
    for i in range(1, 11):
        time.sleep(ritardo)
        print(f"{nome}: {i}")

# Crea i thread
thread1 = threading.Thread(target=contatore, args=("Thread-1", 1))
thread2 = threading.Thread(target=contatore, args=("Thread-2", 2))

# Avvia i thread
thread1.start()
thread2.start()

# Aspetta che i thread finiscano
thread1.join()
thread2.join()

print("Entrambi i thread hanno finito!")
