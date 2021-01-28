import builtins as _mod_builtins

KQ_EV_ADD = 1
KQ_EV_CLEAR = 32
KQ_EV_DELETE = 2
KQ_EV_DISABLE = 8
KQ_EV_ENABLE = 4
KQ_EV_EOF = 32768
KQ_EV_ERROR = 16384
KQ_EV_FLAG1 = 8192
KQ_EV_ONESHOT = 16
KQ_EV_SYSFLAGS = 61440
KQ_FILTER_AIO = -3
KQ_FILTER_PROC = -5
KQ_FILTER_READ = -1
KQ_FILTER_SIGNAL = -6
KQ_FILTER_TIMER = -7
KQ_FILTER_VNODE = -4
KQ_FILTER_WRITE = -2
KQ_NOTE_ATTRIB = 8
KQ_NOTE_CHILD = 4
KQ_NOTE_DELETE = 1
KQ_NOTE_EXEC = 536870912
KQ_NOTE_EXIT = 2147483648
KQ_NOTE_EXTEND = 4
KQ_NOTE_FORK = 1073741824
KQ_NOTE_LINK = 16
KQ_NOTE_LOWAT = 1
KQ_NOTE_PCTRLMASK = -1048576
KQ_NOTE_PDATAMASK = 1048575
KQ_NOTE_RENAME = 32
KQ_NOTE_REVOKE = 64
KQ_NOTE_TRACK = 1
KQ_NOTE_TRACKERR = 2
KQ_NOTE_WRITE = 2
PIPE_BUF = 512
POLLERR = 8
POLLHUP = 16
POLLIN = 1
POLLNVAL = 32
POLLOUT = 4
POLLPRI = 2
POLLRDBAND = 128
POLLRDNORM = 64
POLLWRBAND = 256
POLLWRNORM = 4
__doc__ = 'This module supports asynchronous I/O on multiple file descriptors.\n\n*** IMPORTANT NOTICE ***\nOn Windows, only sockets are supported; on Unix, all file descriptors.'
__file__ = '/Users/shuike/anaconda3/lib/python3.7/lib-dynload/select.cpython-37m-darwin.so'
__name__ = 'select'
__package__ = ''
error = _mod_builtins.OSError
class kevent(_mod_builtins.object):
    "kevent(ident, filter=KQ_FILTER_READ, flags=KQ_EV_ADD, fflags=0, data=0, udata=0)\n\nThis object is the equivalent of the struct kevent for the C API.\n\nSee the kqueue manpage for more detailed information about the meaning\nof the arguments.\n\nOne minor note: while you might hope that udata could store a\nreference to a python object, it cannot, because it is impossible to\nkeep a proper reference count of the object once it's passed into the\nkernel. Therefore, I have restricted it to only storing an integer.  I\nrecommend ignoring it and simply using the 'ident' field to key off\nof. You could also set up a dictionary on the python side to store a\nudata->object mapping."
    __class__ = kevent
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, ident, filter=KQ_FILTER_READ, flags=KQ_EV_ADD, fflags=0, data=0, udata=0):
        "kevent(ident, filter=KQ_FILTER_READ, flags=KQ_EV_ADD, fflags=0, data=0, udata=0)\n\nThis object is the equivalent of the struct kevent for the C API.\n\nSee the kqueue manpage for more detailed information about the meaning\nof the arguments.\n\nOne minor note: while you might hope that udata could store a\nreference to a python object, it cannot, because it is impossible to\nkeep a proper reference count of the object once it's passed into the\nkernel. Therefore, I have restricted it to only storing an integer.  I\nrecommend ignoring it and simply using the 'ident' field to key off\nof. You could also set up a dictionary on the python side to store a\nudata->object mapping."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def data(self):
        pass
    
    @property
    def fflags(self):
        pass
    
    @property
    def filter(self):
        pass
    
    @property
    def flags(self):
        pass
    
    @property
    def ident(self):
        pass
    
    @property
    def udata(self):
        pass
    

class kqueue(_mod_builtins.object):
    'Kqueue syscall wrapper.\n\nFor example, to start watching a socket for input:\n>>> kq = kqueue()\n>>> sock = socket()\n>>> sock.connect((host, port))\n>>> kq.control([kevent(sock, KQ_FILTER_WRITE, KQ_EV_ADD)], 0)\n\nTo wait one second for it to become writeable:\n>>> kq.control(None, 1, 1000)\n\nTo stop listening:\n>>> kq.control([kevent(sock, KQ_FILTER_WRITE, KQ_EV_DELETE)], 0)'
    __class__ = kqueue
    def __init__(self, *args, **kwargs):
        'Kqueue syscall wrapper.\n\nFor example, to start watching a socket for input:\n>>> kq = kqueue()\n>>> sock = socket()\n>>> sock.connect((host, port))\n>>> kq.control([kevent(sock, KQ_FILTER_WRITE, KQ_EV_ADD)], 0)\n\nTo wait one second for it to become writeable:\n>>> kq.control(None, 1, 1000)\n\nTo stop listening:\n>>> kq.control([kevent(sock, KQ_FILTER_WRITE, KQ_EV_DELETE)], 0)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        'close() -> None\n\nClose the kqueue control file descriptor. Further operations on the kqueue\nobject will raise an exception.'
        pass
    
    @property
    def closed(self):
        'True if the kqueue handler is closed'
        pass
    
    def control(self, changelist, max_events, timeout=None):
        "control(changelist, max_events[, timeout=None]) -> eventlist\n\nCalls the kernel kevent function.\n- changelist must be an iterable of kevent objects describing the changes\n  to be made to the kernel's watch list or None.\n- max_events lets you specify the maximum number of events that the\n  kernel will return.\n- timeout is the maximum time to wait in seconds, or else None,\n  to wait forever. timeout accepts floats for smaller timeouts, too."
        pass
    
    def fileno(self):
        'fileno() -> int\n\nReturn the kqueue control file descriptor.'
        return 1
    
    @classmethod
    def fromfd(cls, fd):
        'fromfd(fd) -> kqueue\n\nCreate a kqueue object from a given control fd.'
        pass
    

def poll():
    'Returns a polling object, which supports registering and\nunregistering file descriptors, and then polling them for I/O events.'
    pass

def select(rlist, wlist, xlist, timeout=None):
    "select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)\n\nWait until one or more file descriptors are ready for some kind of I/O.\nThe first three arguments are sequences of file descriptors to be waited for:\nrlist -- wait until ready for reading\nwlist -- wait until ready for writing\nxlist -- wait for an ``exceptional condition''\nIf only one kind of condition is required, pass [] for the other lists.\nA file descriptor is either a socket or file object, or a small integer\ngotten from a fileno() method call on one of those.\n\nThe optional 4th argument specifies a timeout in seconds; it may be\na floating point number to specify fractions of seconds.  If it is absent\nor None, the call will never time out.\n\nThe return value is a tuple of three lists corresponding to the first three\narguments; each contains the subset of the corresponding file descriptors\nthat are ready.\n\n*** IMPORTANT NOTICE ***\nOn Windows, only sockets are supported; on Unix, all file\ndescriptors can be used."
    return tuple()

