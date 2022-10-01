import ask
from exp import exp
from search import search
import imp

path = 'data.txt'
def req():
    req = ask.ask()
    if req == 'внести':
        imp.imp()
    else:
        search(exp(path))
    return req

