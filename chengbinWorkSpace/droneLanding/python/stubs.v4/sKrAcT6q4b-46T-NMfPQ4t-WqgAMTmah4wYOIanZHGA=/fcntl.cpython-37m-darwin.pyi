FASYNC = 64
FD_CLOEXEC = 1
F_DUPFD = 0
F_DUPFD_CLOEXEC = 67
F_FULLFSYNC = 51
F_GETFD = 1
F_GETFL = 3
F_GETLK = 7
F_GETOWN = 5
F_NOCACHE = 48
F_RDLCK = 1
F_SETFD = 2
F_SETFL = 4
F_SETLK = 8
F_SETLKW = 9
F_SETOWN = 6
F_UNLCK = 2
F_WRLCK = 3
LOCK_EX = 2
LOCK_NB = 4
LOCK_SH = 1
LOCK_UN = 8
__doc__ = 'This module performs file control and I/O control on file \ndescriptors.  It is an interface to the fcntl() and ioctl() Unix\nroutines.  File descriptors can be obtained with the fileno() method of\na file or socket object.'
__file__ = '/Users/shuike/anaconda3/lib/python3.7/lib-dynload/fcntl.cpython-37m-darwin.so'
__name__ = 'fcntl'
__package__ = ''
def fcntl(fd, cmd, arg):
    'Perform the operation `cmd` on file descriptor fd.\n\nThe values used for `cmd` are operating system dependent, and are available\nas constants in the fcntl module, using the same names as used in\nthe relevant C header files.  The argument arg is optional, and\ndefaults to 0; it may be an int or a string.  If arg is given as a string,\nthe return value of fcntl is a string of that length, containing the\nresulting value put in the arg buffer by the operating system.  The length\nof the arg string is not allowed to exceed 1024 bytes.  If the arg given\nis an integer or if none is specified, the result value is an integer\ncorresponding to the return value of the fcntl call in the C code.'
    pass

def flock(fd, operation):
    'Perform the lock operation `operation` on file descriptor `fd`.\n\nSee the Unix manual page for flock(2) for details (On some systems, this\nfunction is emulated using fcntl()).'
    pass

def ioctl(fd, request, arg, mutate_flag):
    'Perform the operation `request` on file descriptor `fd`.\n\nThe values used for `request` are operating system dependent, and are available\nas constants in the fcntl or termios library modules, using the same names as\nused in the relevant C header files.\n\nThe argument `arg` is optional, and defaults to 0; it may be an int or a\nbuffer containing character data (most likely a string or an array).\n\nIf the argument is a mutable buffer (such as an array) and if the\nmutate_flag argument (which is only allowed in this case) is true then the\nbuffer is (in effect) passed to the operating system and changes made by\nthe OS will be reflected in the contents of the buffer after the call has\nreturned.  The return value is the integer returned by the ioctl system\ncall.\n\nIf the argument is a mutable buffer and the mutable_flag argument is false,\nthe behavior is as if a string had been passed.\n\nIf the argument is an immutable buffer (most likely a string) then a copy\nof the buffer is passed to the operating system and the return value is a\nstring of the same length containing whatever the operating system put in\nthe buffer.  The length of the arg buffer in this case is not allowed to\nexceed 1024 bytes.\n\nIf the arg given is an integer or if none is specified, the result value is\nan integer corresponding to the return value of the ioctl call in the C\ncode.'
    pass

def lockf(fd, cmd, len, start, whence):
    'A wrapper around the fcntl() locking calls.\n\n`fd` is the file descriptor of the file to lock or unlock, and operation is one\nof the following values:\n\n    LOCK_UN - unlock\n    LOCK_SH - acquire a shared lock\n    LOCK_EX - acquire an exclusive lock\n\nWhen operation is LOCK_SH or LOCK_EX, it can also be bitwise ORed with\nLOCK_NB to avoid blocking on lock acquisition.  If LOCK_NB is used and the\nlock cannot be acquired, an OSError will be raised and the exception will\nhave an errno attribute set to EACCES or EAGAIN (depending on the operating\nsystem -- for portability, check for either value).\n\n`len` is the number of bytes to lock, with the default meaning to lock to\nEOF.  `start` is the byte offset, relative to `whence`, to that the lock\nstarts.  `whence` is as with fileobj.seek(), specifically:\n\n    0 - relative to the start of the file (SEEK_SET)\n    1 - relative to the current buffer position (SEEK_CUR)\n    2 - relative to the end of the file (SEEK_END)'
    pass

