import builtins as _mod_builtins

B0 = 0
B110 = 110
B115200 = 115200
B1200 = 1200
B134 = 134
B150 = 150
B1800 = 1800
B19200 = 19200
B200 = 200
B230400 = 230400
B2400 = 2400
B300 = 300
B38400 = 38400
B4800 = 4800
B50 = 50
B57600 = 57600
B600 = 600
B75 = 75
B9600 = 9600
BRKINT = 2
BS0 = 0
BS1 = 32768
BSDLY = 32768
CDSUSP = 25
CEOF = 4
CEOL = 255
CEOT = 4
CERASE = 127
CFLUSH = 15
CINTR = 3
CKILL = 21
CLNEXT = 22
CLOCAL = 32768
CQUIT = 28
CR0 = 0
CR1 = 4096
CR2 = 8192
CR3 = 12288
CRDLY = 12288
CREAD = 2048
CRPRNT = 18
CRTSCTS = 196608
CS5 = 0
CS6 = 256
CS7 = 512
CS8 = 768
CSIZE = 768
CSTART = 17
CSTOP = 19
CSTOPB = 1024
CSUSP = 26
CWERASE = 23
ECHO = 8
ECHOCTL = 64
ECHOE = 2
ECHOK = 4
ECHOKE = 1
ECHONL = 16
ECHOPRT = 32
EXTA = 19200
EXTB = 38400
FF0 = 0
FF1 = 16384
FFDLY = 16384
FIOASYNC = 2147772029
FIOCLEX = 536897025
FIONBIO = 2147772030
FIONCLEX = 536897026
FIONREAD = 1074030207
FLUSHO = 8388608
HUPCL = 16384
ICANON = 256
ICRNL = 256
IEXTEN = 1024
IGNBRK = 1
IGNCR = 128
IGNPAR = 4
IMAXBEL = 8192
INLCR = 64
INPCK = 16
ISIG = 128
ISTRIP = 32
IXANY = 2048
IXOFF = 1024
IXON = 512
NCCS = 20
NL0 = 0
NL1 = 256
NLDLY = 768
NOFLSH = 2147483648
OCRNL = 16
OFDEL = 131072
OFILL = 128
ONLCR = 2
ONLRET = 64
ONOCR = 32
OPOST = 1
PARENB = 4096
PARMRK = 8
PARODD = 8192
PENDIN = 536870912
TAB0 = 0
TAB1 = 1024
TAB2 = 2048
TAB3 = 4
TABDLY = 3076
TCIFLUSH = 1
TCIOFF = 3
TCIOFLUSH = 3
TCION = 4
TCOFLUSH = 2
TCOOFF = 1
TCOON = 2
TCSADRAIN = 1
TCSAFLUSH = 2
TCSANOW = 0
TCSASOFT = 16
TIOCCONS = 2147775586
TIOCEXCL = 536900621
TIOCGETD = 1074033690
TIOCGPGRP = 1074033783
TIOCGWINSZ = 1074295912
TIOCMBIC = 2147775595
TIOCMBIS = 2147775596
TIOCMGET = 1074033770
TIOCMSET = 2147775597
TIOCM_CAR = 64
TIOCM_CD = 64
TIOCM_CTS = 32
TIOCM_DSR = 256
TIOCM_DTR = 2
TIOCM_LE = 1
TIOCM_RI = 128
TIOCM_RNG = 128
TIOCM_RTS = 4
TIOCM_SR = 16
TIOCM_ST = 8
TIOCNOTTY = 536900721
TIOCNXCL = 536900622
TIOCOUTQ = 1074033779
TIOCPKT = 2147775600
TIOCPKT_DATA = 0
TIOCPKT_DOSTOP = 32
TIOCPKT_FLUSHREAD = 1
TIOCPKT_FLUSHWRITE = 2
TIOCPKT_NOSTOP = 16
TIOCPKT_START = 8
TIOCPKT_STOP = 4
TIOCSCTTY = 536900705
TIOCSETD = 2147775515
TIOCSPGRP = 2147775606
TIOCSTI = 2147578994
TIOCSWINSZ = 2148037735
TOSTOP = 4194304
VDISCARD = 15
VEOF = 0
VEOL = 1
VEOL2 = 2
VERASE = 3
VINTR = 8
VKILL = 5
VLNEXT = 14
VMIN = 16
VQUIT = 9
VREPRINT = 6
VSTART = 12
VSTOP = 13
VSUSP = 10
VT0 = 0
VT1 = 65536
VTDLY = 65536
VTIME = 17
VWERASE = 4
__doc__ = 'This module provides an interface to the Posix calls for tty I/O control.\nFor a complete description of these calls, see the Posix or Unix manual\npages. It is only available for those Unix versions that support Posix\ntermios style tty I/O control.\n\nAll functions in this module take a file descriptor fd as their first\nargument. This can be an integer file descriptor, such as returned by\nsys.stdin.fileno(), or a file object, such as sys.stdin itself.'
__file__ = '/Users/shuike/anaconda3/envs/py36QT/lib/python3.6/lib-dynload/termios.cpython-36m-darwin.so'
__name__ = 'termios'
__package__ = ''
class error(_mod_builtins.Exception):
    __class__ = error
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'termios'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def tcdrain(fd):
    'tcdrain(fd) -> None\n\nWait until all output written to file descriptor fd has been transmitted.'
    pass

def tcflow(fd, action):
    'tcflow(fd, action) -> None\n\nSuspend or resume input or output on file descriptor fd.\nThe action argument can be termios.TCOOFF to suspend output,\ntermios.TCOON to restart output, termios.TCIOFF to suspend input,\nor termios.TCION to restart input.'
    pass

def tcflush(fd, queue):
    'tcflush(fd, queue) -> None\n\nDiscard queued data on file descriptor fd.\nThe queue selector specifies which queue: termios.TCIFLUSH for the input\nqueue, termios.TCOFLUSH for the output queue, or termios.TCIOFLUSH for\nboth queues. '
    pass

def tcgetattr(fd):
    'tcgetattr(fd) -> list_of_attrs\n\nGet the tty attributes for file descriptor fd, as follows:\n[iflag, oflag, cflag, lflag, ispeed, ospeed, cc] where cc is a list\nof the tty special characters (each a string of length 1, except the items\nwith indices VMIN and VTIME, which are integers when these fields are\ndefined).  The interpretation of the flags and the speeds as well as the\nindexing in the cc array must be done using the symbolic constants defined\nin this module.'
    return list()

def tcsendbreak(fd, duration):
    'tcsendbreak(fd, duration) -> None\n\nSend a break on file descriptor fd.\nA zero duration sends a break for 0.25-0.5 seconds; a nonzero duration\nhas a system dependent meaning.'
    pass

def tcsetattr(fd, when, attributes):
    'tcsetattr(fd, when, attributes) -> None\n\nSet the tty attributes for file descriptor fd.\nThe attributes to be set are taken from the attributes argument, which\nis a list like the one returned by tcgetattr(). The when argument\ndetermines when the attributes are changed: termios.TCSANOW to\nchange immediately, termios.TCSADRAIN to change after transmitting all\nqueued output, or termios.TCSAFLUSH to change after transmitting all\nqueued output and discarding all queued input. '
    pass

