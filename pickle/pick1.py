import pickle
import socket
import StringIO

PATH = 'storage.txt'
string = 'hello'
dic = {1: 'test'}
integer = 5

name = 'steve'
address = '111'
age = '24'

def prepickle(**kwargs):
  
    for val in kwargs.iteritems():
        print val

def persist(path, *objects):
    pickler = pickle.Pickler(open(path, 'w'))
    
    for object in objects:
        pickler.dump(object)

def access(path):
    upickler = pickle.Unpickler(open(path, 'r'))
    try:
        while True:
            yield upickler.load()
    except EOFError:
        pass
        


raw = prepickle(name=name, address=address, age=age)
#persist(PATH, string, dic, integer)
#data = access(PATH)
#for item in data:
#    print item
#print '---------------------------------------'

#
#def persist2(path, *objects):
#    file = open(path, 'w')
#    for object in objects:
#        file.write(pickle.dumps(object))
#
#def access2(path):
#    file = open(path, 'r')
#    print pickle.load(file)
#
#persist2(PATH, string, dic, integer)
#data = access2(PATH)