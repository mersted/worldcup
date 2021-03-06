from multiprocessing import Process
from pipes import RedisPipe, PrintPipe, MongoPipe, FilePipe
from streams import TwitterFilterStream
import sys
import time


if __name__ == '__main__':
    words = "usa,america,germany,worldcup,worldcup2014,dempsey,bradley,hazard,kompany"
    pipes = []
    for word in words.split(","):
        pipes.append(RedisPipe(word, period=15, db=1, ns="track:" + word))
    pipes.append(MongoPipe())
    pipes.append(FilePipe())
    t = TwitterFilterStream(words, pipes=pipes)
    t.start()
