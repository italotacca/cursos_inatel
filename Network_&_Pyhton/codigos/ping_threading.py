import threading
import os
import time

def pinger(site):
    os.system(f'ping {site}')

urls = ["www.google.com","www.facebook.com","www.youtube.com"]
threads = []

start_time = time.time()

for url in urls:
    t = threading.Thread(target=pinger, args=(url,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print (f"\nTempo para rodar o código: {time.time() - start_time} segundos")
