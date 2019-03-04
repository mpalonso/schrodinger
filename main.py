'''
Created on 4 mar. 2019

@author: mparra
@git: https://github.com/mpalonso
@version: 0.1
@todo: 
    - Cron script
'''
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
def DrawEntropy(freqList):
    N = len(freqList)

    ind = np.arange(N)  # the x locations for the groups
    width = 1.00        # the width of the bars

    #fig = plt.figure()
    fig = plt.figure(figsize=(11,5),dpi=100)
    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind, freqList, width)
    ax.set_autoscalex_on(False)
    ax.set_xlim([0,255])

    ax.set_ylabel('Frequency')
    ax.set_xlabel('Byte')
    ax.set_title('Frequency of Bytes 0 to 255\nFILENAME: ' + sys.argv[1])

    plt.show()
def main():
    if len(sys.argv) != 2:
        print("Error: main.py [path]filename")
        sys.exit()
    
    f = open(sys.argv[1], "rb")
    byteArray = f.read()
    f.close()
    print(str(byteArray))
    fileSize = len(byteArray)
    print("File Size" + str(fileSize))
    print("Calculating Entropy...")
    freqList = []
    for b in range(256):
        ctr = 0
        for byte in byteArray:
            if byte == b:
                ctr += 1
        freqList.append(float(ctr) / fileSize)
    print("Frecuency of each byte-character: " + str(freqList))
    print("Calculating Shannon entropy")
    ent = 0.0
    for freq in freqList:
            if freq > 0:
                ent = ent + freq * math.log(freq, 2)
            ent = -ent
    print(ent)
    DrawEntropy(freqList)

if __name__ == '__main__':
    main()