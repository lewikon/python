from time import sleep
from progress.bar import Bar

bar = Bar('Processing', max=20)
for i in range(20):
    sleep(1)
    bar.next()
bar.finish()