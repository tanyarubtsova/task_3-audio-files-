'''TASK 3 - sequential program'''

import os
import librosa
import numpy
import time
#import warnings
#warnings.filterwarnings('ignore')

start = time.time()
rep = os.walk('audio')
os.system("rm -r answer")
os.makedirs('answer')
for addr, dir, file in rep:
    path_ans =addr + "/"
    path_ans = path_ans.replace("audio", "answer")
    for f in file:
        path = addr + '/' + f
        #print(path)
        y, sr = librosa.core.load(path)
        mfcc = librosa.feature.mfcc(y = y, sr = sr)
        numpy.save(path_ans + f, mfcc)
    for d in dir:
        os.makedirs(path_ans + d)
print(time.time() - start)
