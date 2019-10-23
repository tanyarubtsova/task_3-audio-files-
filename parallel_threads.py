import os
import librosa
import numpy
import time
import threading
#import warnings
#warnings.filterwarnings('ignore')

def fun(path):
    y, sr = librosa.core.load(path)
    path_ans = path.replace("audio", "threads_answer")
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    numpy.save(path_ans, mfcc)
    return 0


start = time.time()
rep = os.walk('audio')
os.system("rm -r threads_answer")
os.makedirs('threads_answer')
work = []
for addr, dir, file in rep:
    for f in file:
        str = addr + '/' + f,
        work.append(tuple(str))
    for d in dir:
        os.makedirs(addr.replace("audio", "threads_answer") + '/' + d)
thread_count = 4
for i in range(0, len(work), thread_count):
    th = [*range(thread_count)]

    for j in range(thread_count):
        if i + j < len(work):
            th[j] = threading.Thread(target=fun, args=work[i + j])
            th[j].start()
        else:
            thread_count = j
            break
    for j in range(thread_count):
        th[j].join()
print(time.time() - start)
