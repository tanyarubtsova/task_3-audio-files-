import os
import librosa
import numpy
import time
import multiprocessing
#import warnings
#warnings.filterwarnings('ignore')

def fun(*path):
    for i in path:
        y, sr = librosa.core.load(i)
        path_ans = i.replace("audio", "threads_answer")
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        numpy.save(path_ans, mfcc)
    return 0


start = time.time()
rep = os.walk('audio')
os.system("rm -r process_answer")
os.makedirs('process_answer')
work = []
for addr, dir, file in rep:
    for f in file:
        str = addr + '/' + f
        work.append(str)
    for d in dir:
        os.makedirs(addr.replace("audio", "process_answer") + '/' + d)
process_count = 4
th = [0] * process_count
c = 0
if len(work) % process_count:
    c = 1
for i in range(process_count):
    print(tuple(work[i * (len(work) // process_count + c): (i + 1) * (len(work) // process_count + c)]))
    th[i] = multiprocessing.Process(target=fun,
                                args=tuple(work[i * (len(work) // process_count + c): (i + 1) * (len(work) // process_count + c)]))
    th[i].start()
for i in range(len(th)):
    th[i].join()
print(time.time() - start)
