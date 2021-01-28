class PyCapsule(object):
    'Capsule objects let you wrap a C "void *" pointer in a Python\nobject.  They\'re a way of passing data through the Python interpreter\nwithout creating your own custom type.\n\nCapsules are used for communication between extension modules.\nThey provide a way for an extension module to export a C interface\nto other extension modules, so that extension modules can use the\nPython import mechanism to link to one another.\n'
    __class__ = PyCapsule
    def __init__(self, *args, **kwargs):
        'Capsule objects let you wrap a C "void *" pointer in a Python\nobject.  They\'re a way of passing data through the Python interpreter\nwithout creating your own custom type.\n\nCapsules are used for communication between extension modules.\nThey provide a way for an extension module to export a C interface\nto other extension modules, so that extension modules can use the\nPython import mechanism to link to one another.\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

OSError = type
AF_APPLETALK = 16
AF_DECnet = 12
AF_INET = 2
AF_INET6 = 30
AF_IPX = 23
AF_LINK = 18
AF_ROUTE = 17
AF_SNA = 11
AF_SYSTEM = 32
AF_UNIX = 1
AF_UNSPEC = 0
AI_ADDRCONFIG = 1024
AI_ALL = 256
AI_CANONNAME = 2
AI_DEFAULT = 1536
AI_MASK = 5127
AI_NUMERICHOST = 4
AI_NUMERICSERV = 4096
AI_PASSIVE = 1
AI_V4MAPPED = 2048
AI_V4MAPPED_CFG = 512
CAPI = PyCapsule()
def CMSG_LEN(length):
    'CMSG_LEN(length) -> control message length\n\nReturn the total length, without trailing padding, of an ancillary\ndata item with associated data of the given length.  This value can\noften be used as the buffer size for recvmsg() to receive a single\nitem of ancillary data, but RFC 3542 requires portable applications to\nuse CMSG_SPACE() and thus include space for padding, even when the\nitem will be the last in the buffer.  Raises OverflowError if length\nis outside the permissible range of values.'
    pass

def CMSG_SPACE(length):
    'CMSG_SPACE(length) -> buffer size\n\nReturn the buffer size needed for recvmsg() to receive an ancillary\ndata item with associated data of the given length, along with any\ntrailing padding.  The buffer space needed to receive multiple items\nis the sum of the CMSG_SPACE() values for their associated data\nlengths.  Raises OverflowError if length is outside the permissible\nrange of values.'
    pass

EAI_ADDRFAMILY = 1
EAI_AGAIN = 2
EAI_BADFLAGS = 3
EAI_BADHINTS = 12
EAI_FAIL = 4
EAI_FAMILY = 5
EAI_MAX = 15
EAI_MEMORY = 6
EAI_NODATA = 7
EAI_NONAME = 8
EAI_OVERFLOW = 14
EAI_PROTOCOL = 13
EAI_SERVICE = 9
EAI_SOCKTYPE = 10
EAI_SYSTEM = 11
INADDR_ALLHOSTS_GROUP = 3758096385
INADDR_ANY = 0
INADDR_BROADCAST = 4294967295
INADDR_LOOPBACK = 2130706433
INADDR_MAX_LOCAL_GROUP = 3758096639
INADDR_NONE = 4294967295
INADDR_UNSPEC_GROUP = 3758096384
IPPORT_RESERVED = 1024
IPPORT_USERRESERVED = 5000
IPPROTO_AH = 51
IPPROTO_DSTOPTS = 60
IPPROTO_EGP = 8
IPPROTO_EON = 80
IPPROTO_ESP = 50
IPPROTO_FRAGMENT = 44
IPPROTO_GGP = 3
IPPROTO_GRE = 47
IPPROTO_HELLO = 63
IPPROTO_HOPOPTS = 0
IPPROTO_ICMP = 1
IPPROTO_ICMPV6 = 58
IPPROTO_IDP = 22
IPPROTO_IGMP = 2
IPPROTO_IP = 0
IPPROTO_IPCOMP = 108
IPPROTO_IPIP = 4
IPPROTO_IPV4 = 4
IPPROTO_IPV6 = 41
IPPROTO_MAX = 256
IPPROTO_ND = 77
IPPROTO_NONE = 59
IPPROTO_PIM = 103
IPPROTO_PUP = 12
IPPROTO_RAW = 255
IPPROTO_ROUTING = 43
IPPROTO_RSVP = 46
IPPROTO_SCTP = 132
IPPROTO_TCP = 6
IPPROTO_TP = 29
IPPROTO_UDP = 17
IPPROTO_XTP = 36
IPV6_CHECKSUM = 26
IPV6_JOIN_GROUP = 12
IPV6_LEAVE_GROUP = 13
IPV6_MULTICAST_HOPS = 10
IPV6_MULTICAST_IF = 9
IPV6_MULTICAST_LOOP = 11
IPV6_RECVTCLASS = 35
IPV6_RTHDR_TYPE_0 = 0
IPV6_TCLASS = 36
IPV6_UNICAST_HOPS = 4
IPV6_V6ONLY = 27
IP_ADD_MEMBERSHIP = 12
IP_DEFAULT_MULTICAST_LOOP = 1
IP_DEFAULT_MULTICAST_TTL = 1
IP_DROP_MEMBERSHIP = 13
IP_HDRINCL = 2
IP_MAX_MEMBERSHIPS = 4095
IP_MULTICAST_IF = 9
IP_MULTICAST_LOOP = 11
IP_MULTICAST_TTL = 10
IP_OPTIONS = 1
IP_RECVDSTADDR = 7
IP_RECVOPTS = 5
IP_RECVRETOPTS = 6
IP_RETOPTS = 8
IP_TOS = 3
IP_TTL = 4
LOCAL_PEERCRED = 1
MSG_CTRUNC = 32
MSG_DONTROUTE = 4
MSG_DONTWAIT = 128
MSG_EOF = 256
MSG_EOR = 8
MSG_OOB = 1
MSG_PEEK = 2
MSG_TRUNC = 16
MSG_WAITALL = 64
NI_DGRAM = 16
NI_MAXHOST = 1025
NI_MAXSERV = 32
NI_NAMEREQD = 4
NI_NOFQDN = 1
NI_NUMERICHOST = 2
NI_NUMERICSERV = 8
PF_SYSTEM = 32
SCM_CREDS = 3
SCM_RIGHTS = 1
SHUT_RD = 0
SHUT_RDWR = 2
SHUT_WR = 1
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_RDM = 4
SOCK_SEQPACKET = 5
SOCK_STREAM = 1
SOL_IP = 0
SOL_SOCKET = 65535
SOL_TCP = 6
SOL_UDP = 17
SOMAXCONN = 128
SO_ACCEPTCONN = 2
SO_BROADCAST = 32
SO_DEBUG = 1
SO_DONTROUTE = 16
SO_ERROR = 4103
SO_KEEPALIVE = 8
SO_LINGER = 128
SO_OOBINLINE = 256
SO_RCVBUF = 4098
SO_RCVLOWAT = 4100
SO_RCVTIMEO = 4102
SO_REUSEADDR = 4
SO_REUSEPORT = 512
SO_SNDBUF = 4097
SO_SNDLOWAT = 4099
SO_SNDTIMEO = 4101
SO_TYPE = 4104
SO_USELOOPBACK = 64
SYSPROTO_CONTROL = 2
SocketType = socket
TCP_KEEPCNT = 258
TCP_KEEPINTVL = 257
TCP_MAXSEG = 2
TCP_NODELAY = 1
__doc__ = 'Implementation module for socket operations.\n\nSee the socket module for documentation.'
__file__ = '/Users/shuike/anaconda3/envs/py36QT/lib/python3.6/lib-dynload/_socket.cpython-36m-darwin.so'
__name__ = '_socket'
__package__ = ''
def dup(integer):
    "dup(integer) -> integer\n\nDuplicate an integer socket file descriptor.  This is like os.dup(), but for\nsockets; on some platforms os.dup() won't work for socket file descriptors."
    return 1

error = OSError
class gaierror(OSError):
    __class__ = gaierror
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'socket'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def getaddrinfo(host, port, family=None, type=None, proto=None, flags=None):
    'getaddrinfo(host, port [, family, type, proto, flags])\n    -> list of (family, type, proto, canonname, sockaddr)\n\nResolve host and port into addrinfo struct.'
    pass

def getdefaulttimeout():
    'getdefaulttimeout() -> timeout\n\nReturns the default timeout in seconds (float) for new socket objects.\nA value of None indicates that new socket objects have no timeout.\nWhen the socket module is first imported, the default is None.'
    pass

def gethostbyaddr(host):
    'gethostbyaddr(host) -> (name, aliaslist, addresslist)\n\nReturn the true host name, a list of aliases, and a list of IP addresses,\nfor a host.  The host argument is a string giving a host name or IP number.'
    return tuple()

def gethostbyname(host):
    "gethostbyname(host) -> address\n\nReturn the IP address (a string of the form '255.255.255.255') for a host."
    pass

def gethostbyname_ex(host):
    'gethostbyname_ex(host) -> (name, aliaslist, addresslist)\n\nReturn the true host name, a list of aliases, and a list of IP addresses,\nfor a host.  The host argument is a string giving a host name or IP number.'
    return tuple()

def gethostname():
    'gethostname() -> string\n\nReturn the current host name.'
    return ''

def getnameinfo(sockaddr, flags):
    'getnameinfo(sockaddr, flags) --> (host, port)\n\nGet host and port for a sockaddr.'
    return tuple()

def getprotobyname(name):
    'getprotobyname(name) -> integer\n\nReturn the protocol number for the named protocol.  (Rarely used.)'
    return 1

def getservbyname(servicename, protocolname=None):
    "getservbyname(servicename[, protocolname]) -> integer\n\nReturn a port number from a service name and protocol name.\nThe optional protocol name, if given, should be 'tcp' or 'udp',\notherwise any protocol will match."
    return 1

def getservbyport(port, protocolname=None):
    "getservbyport(port[, protocolname]) -> string\n\nReturn the service name from a port number and protocol name.\nThe optional protocol name, if given, should be 'tcp' or 'udp',\notherwise any protocol will match."
    return ''

has_ipv6 = True
class herror(OSError):
    __class__ = herror
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'socket'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def htonl(integer):
    'htonl(integer) -> integer\n\nConvert a 32-bit integer from host to network byte order.'
    return 1

def htons(integer):
    'htons(integer) -> integer\n\nConvert a 16-bit integer from host to network byte order.'
    return 1

def if_indextoname(if_index):
    'if_indextoname(if_index)\n\nReturns the interface name corresponding to the interface index if_index.'
    pass

def if_nameindex():
    'if_nameindex()\n\nReturns a list of network interface information (index, name) tuples.'
    pass

def if_nametoindex(if_name):
    'if_nametoindex(if_name)\n\nReturns the interface index corresponding to the interface name if_name.'
    pass

def inet_aton(string):
    'inet_aton(string) -> bytes giving packed 32-bit IP representation\n\nConvert an IP address in string format (123.45.67.89) to the 32-bit packed\nbinary format used in low-level network functions.'
    pass

def inet_ntoa(packed_ip):
    'inet_ntoa(packed_ip) -> ip_address_string\n\nConvert an IP address from 32-bit packed binary format to string format'
    pass

def inet_ntop(af, packed_ip):
    'inet_ntop(af, packed_ip) -> string formatted IP address\n\nConvert a packed IP address of the given family to string format.'
    return ''

def inet_pton(af, ip):
    'inet_pton(af, ip) -> packed IP address string\n\nConvert an IP address from string format to a packed string suitable\nfor use with low-level network functions.'
    pass

def ntohl(integer):
    'ntohl(integer) -> integer\n\nConvert a 32-bit integer from network to host byte order.'
    return 1

def ntohs(integer):
    'ntohs(integer) -> integer\n\nConvert a 16-bit integer from network to host byte order.'
    return 1

def setdefaulttimeout(timeout):
    'setdefaulttimeout(timeout)\n\nSet the default timeout in seconds (float) for new socket objects.\nA value of None indicates that new socket objects have no timeout.\nWhen the socket module is first imported, the default is None.'
    pass

def sethostname(name):
    'sethostname(name)\n\nSets the hostname to name.'
    pass

class socket(object):
    "socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None) -> socket object\n\nOpen a socket of the given type.  The family argument specifies the\naddress family; it defaults to AF_INET.  The type argument specifies\nwhether this is a stream (SOCK_STREAM, this is the default)\nor datagram (SOCK_DGRAM) socket.  The protocol argument defaults to 0,\nspecifying the default protocol.  Keyword arguments are accepted.\nThe socket is created as non-inheritable.\n\nA socket object represents one endpoint of a network connection.\n\nMethods of socket objects (keyword arguments not allowed):\n\n_accept() -- accept connection, returning new socket fd and client address\nbind(addr) -- bind the socket to a local address\nclose() -- close the socket\nconnect(addr) -- connect the socket to a remote address\nconnect_ex(addr) -- connect, return an error code instead of an exception\ndup() -- return a new socket fd duplicated from fileno()\nfileno() -- return underlying file descriptor\ngetpeername() -- return remote address [*]\ngetsockname() -- return local address\ngetsockopt(level, optname[, buflen]) -- get socket options\ngettimeout() -- return timeout or None\nlisten([n]) -- start listening for incoming connections\nrecv(buflen[, flags]) -- receive data\nrecv_into(buffer[, nbytes[, flags]]) -- receive data (into a buffer)\nrecvfrom(buflen[, flags]) -- receive data and sender's address\nrecvfrom_into(buffer[, nbytes, [, flags])\n  -- receive data and sender's address (into a buffer)\nsendall(data[, flags]) -- send all data\nsend(data[, flags]) -- send data, may not send all of it\nsendto(data[, flags], addr) -- send data to a given address\nsetblocking(0 | 1) -- set or clear the blocking I/O flag\nsetsockopt(level, optname, value[, optlen]) -- set socket options\nsettimeout(None | float) -- set or clear the timeout\nshutdown(how) -- shut down traffic in one or both directions\nif_nameindex() -- return all network interface indices and names\nif_nametoindex(name) -- return the corresponding interface index\nif_indextoname(index) -- return the corresponding interface name\n\n [*] not available on all platforms!"
    __class__ = socket
    def __del__(self):
        return None
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None):
        "socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None) -> socket object\n\nOpen a socket of the given type.  The family argument specifies the\naddress family; it defaults to AF_INET.  The type argument specifies\nwhether this is a stream (SOCK_STREAM, this is the default)\nor datagram (SOCK_DGRAM) socket.  The protocol argument defaults to 0,\nspecifying the default protocol.  Keyword arguments are accepted.\nThe socket is created as non-inheritable.\n\nA socket object represents one endpoint of a network connection.\n\nMethods of socket objects (keyword arguments not allowed):\n\n_accept() -- accept connection, returning new socket fd and client address\nbind(addr) -- bind the socket to a local address\nclose() -- close the socket\nconnect(addr) -- connect the socket to a remote address\nconnect_ex(addr) -- connect, return an error code instead of an exception\ndup() -- return a new socket fd duplicated from fileno()\nfileno() -- return underlying file descriptor\ngetpeername() -- return remote address [*]\ngetsockname() -- return local address\ngetsockopt(level, optname[, buflen]) -- get socket options\ngettimeout() -- return timeout or None\nlisten([n]) -- start listening for incoming connections\nrecv(buflen[, flags]) -- receive data\nrecv_into(buffer[, nbytes[, flags]]) -- receive data (into a buffer)\nrecvfrom(buflen[, flags]) -- receive data and sender's address\nrecvfrom_into(buffer[, nbytes, [, flags])\n  -- receive data and sender's address (into a buffer)\nsendall(data[, flags]) -- send all data\nsend(data[, flags]) -- send data, may not send all of it\nsendto(data[, flags], addr) -- send data to a given address\nsetblocking(0 | 1) -- set or clear the blocking I/O flag\nsetsockopt(level, optname, value[, optlen]) -- set socket options\nsettimeout(None | float) -- set or clear the timeout\nshutdown(how) -- shut down traffic in one or both directions\nif_nameindex() -- return all network interface indices and names\nif_nametoindex(name) -- return the corresponding interface index\nif_indextoname(index) -- return the corresponding interface name\n\n [*] not available on all platforms!"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _accept(self):
        '_accept() -> (integer, address info)\n\nWait for an incoming connection.  Return a new socket file descriptor\nrepresenting the connection, and the address of the client.\nFor IP sockets, the address info is a pair (hostaddr, port).'
        return tuple()
    
    def bind(self, address):
        'bind(address)\n\nBind the socket to a local address.  For IP sockets, the address is a\npair (host, port); the host must refer to the local host. For raw packet\nsockets the address is a tuple (ifname, proto [,pkttype [,hatype [,addr]]])'
        pass
    
    def close(self):
        'close()\n\nClose the socket.  It cannot be used after this call.'
        pass
    
    def connect(self, address):
        'connect(address)\n\nConnect the socket to a remote address.  For IP sockets, the address\nis a pair (host, port).'
        pass
    
    def connect_ex(self, address):
        'connect_ex(address) -> errno\n\nThis is like connect(address), but returns an error code (the errno value)\ninstead of raising an exception when an error occurs.'
        pass
    
    def detach(self):
        'detach()\n\nClose the socket object without closing the underlying file descriptor.\nThe object cannot be used after this call, but the file descriptor\ncan be reused for other purposes.  The file descriptor is returned.'
        pass
    
    @property
    def family(self):
        'the socket family'
        pass
    
    def fileno(self):
        'fileno() -> integer\n\nReturn the integer file descriptor of the socket.'
        return 1
    
    def getpeername(self):
        'getpeername() -> address info\n\nReturn the address of the remote endpoint.  For IP sockets, the address\ninfo is a pair (hostaddr, port).'
        pass
    
    def getsockname(self):
        'getsockname() -> address info\n\nReturn the address of the local endpoint.  For IP sockets, the address\ninfo is a pair (hostaddr, port).'
        pass
    
    def getsockopt(self, level, option, buffersize=None):
        'getsockopt(level, option[, buffersize]) -> value\n\nGet a socket option.  See the Unix manual for level and option.\nIf a nonzero buffersize argument is given, the return value is a\nstring of that length; otherwise it is an integer.'
        pass
    
    def gettimeout(self):
        'gettimeout() -> timeout\n\nReturns the timeout in seconds (float) associated with socket \noperations. A timeout of None indicates that timeouts on socket \noperations are disabled.'
        pass
    
    def listen(self, backlog=None):
        'listen([backlog])\n\nEnable a server to accept connections.  If backlog is specified, it must be\nat least 0 (if it is lower, it is set to 0); it specifies the number of\nunaccepted connections that the system will allow before refusing new\nconnections. If not specified, a default reasonable value is chosen.'
        pass
    
    @property
    def proto(self):
        'the socket protocol'
        pass
    
    def recv(self, buffersize, flags=None):
        'recv(buffersize[, flags]) -> data\n\nReceive up to buffersize bytes from the socket.  For the optional flags\nargument, see the Unix manual.  When no data is available, block until\nat least one byte is available or until the remote end is closed.  When\nthe remote end is closed and all data is read, return the empty string.'
        pass
    
    def recv_into(self, buffer, nbytes=None, flags=None):
        'recv_into(buffer, [nbytes[, flags]]) -> nbytes_read\n\nA version of recv() that stores its data into a buffer rather than creating \na new string.  Receive up to buffersize bytes from the socket.  If buffersize \nis not specified (or 0), receive up to the size available in the given buffer.\n\nSee recv() for documentation about the flags.'
        pass
    
    def recvfrom(self, buffersize, flags=None):
        "recvfrom(buffersize[, flags]) -> (data, address info)\n\nLike recv(buffersize, flags) but also return the sender's address info."
        return tuple()
    
    def recvfrom_into(self, buffer, nbytes=None, flags=None):
        "recvfrom_into(buffer[, nbytes[, flags]]) -> (nbytes, address info)\n\nLike recv_into(buffer[, nbytes[, flags]]) but also return the sender's address info."
        return tuple()
    
    def recvmsg(self, bufsize, ancbufsize=None, flags=None):
        'recvmsg(bufsize[, ancbufsize[, flags]]) -> (data, ancdata, msg_flags, address)\n\nReceive normal data (up to bufsize bytes) and ancillary data from the\nsocket.  The ancbufsize argument sets the size in bytes of the\ninternal buffer used to receive the ancillary data; it defaults to 0,\nmeaning that no ancillary data will be received.  Appropriate buffer\nsizes for ancillary data can be calculated using CMSG_SPACE() or\nCMSG_LEN(), and items which do not fit into the buffer might be\ntruncated or discarded.  The flags argument defaults to 0 and has the\nsame meaning as for recv().\n\nThe return value is a 4-tuple: (data, ancdata, msg_flags, address).\nThe data item is a bytes object holding the non-ancillary data\nreceived.  The ancdata item is a list of zero or more tuples\n(cmsg_level, cmsg_type, cmsg_data) representing the ancillary data\n(control messages) received: cmsg_level and cmsg_type are integers\nspecifying the protocol level and protocol-specific type respectively,\nand cmsg_data is a bytes object holding the associated data.  The\nmsg_flags item is the bitwise OR of various flags indicating\nconditions on the received message; see your system documentation for\ndetails.  If the receiving socket is unconnected, address is the\naddress of the sending socket, if available; otherwise, its value is\nunspecified.\n\nIf recvmsg() raises an exception after the system call returns, it\nwill first attempt to close any file descriptors received via the\nSCM_RIGHTS mechanism.'
        return tuple()
    
    def recvmsg_into(self, buffers, ancbufsize=None, flags=None):
        'recvmsg_into(buffers[, ancbufsize[, flags]]) -> (nbytes, ancdata, msg_flags, address)\n\nReceive normal data and ancillary data from the socket, scattering the\nnon-ancillary data into a series of buffers.  The buffers argument\nmust be an iterable of objects that export writable buffers\n(e.g. bytearray objects); these will be filled with successive chunks\nof the non-ancillary data until it has all been written or there are\nno more buffers.  The ancbufsize argument sets the size in bytes of\nthe internal buffer used to receive the ancillary data; it defaults to\n0, meaning that no ancillary data will be received.  Appropriate\nbuffer sizes for ancillary data can be calculated using CMSG_SPACE()\nor CMSG_LEN(), and items which do not fit into the buffer might be\ntruncated or discarded.  The flags argument defaults to 0 and has the\nsame meaning as for recv().\n\nThe return value is a 4-tuple: (nbytes, ancdata, msg_flags, address).\nThe nbytes item is the total number of bytes of non-ancillary data\nwritten into the buffers.  The ancdata item is a list of zero or more\ntuples (cmsg_level, cmsg_type, cmsg_data) representing the ancillary\ndata (control messages) received: cmsg_level and cmsg_type are\nintegers specifying the protocol level and protocol-specific type\nrespectively, and cmsg_data is a bytes object holding the associated\ndata.  The msg_flags item is the bitwise OR of various flags\nindicating conditions on the received message; see your system\ndocumentation for details.  If the receiving socket is unconnected,\naddress is the address of the sending socket, if available; otherwise,\nits value is unspecified.\n\nIf recvmsg_into() raises an exception after the system call returns,\nit will first attempt to close any file descriptors received via the\nSCM_RIGHTS mechanism.'
        return tuple()
    
    def send(self, data, flags=None):
        'send(data[, flags]) -> count\n\nSend a data string to the socket.  For the optional flags\nargument, see the Unix manual.  Return the number of bytes\nsent; this may be less than len(data) if the network is busy.'
        pass
    
    def sendall(self, data, flags=None):
        "sendall(data[, flags])\n\nSend a data string to the socket.  For the optional flags\nargument, see the Unix manual.  This calls send() repeatedly\nuntil all data is sent.  If an error occurs, it's impossible\nto tell how much data has been sent."
        pass
    
    def sendmsg(self, buffers, ancdata=None, flags=None, address=None):
        'sendmsg(buffers[, ancdata[, flags[, address]]]) -> count\n\nSend normal and ancillary data to the socket, gathering the\nnon-ancillary data from a series of buffers and concatenating it into\na single message.  The buffers argument specifies the non-ancillary\ndata as an iterable of bytes-like objects (e.g. bytes objects).\nThe ancdata argument specifies the ancillary data (control messages)\nas an iterable of zero or more tuples (cmsg_level, cmsg_type,\ncmsg_data), where cmsg_level and cmsg_type are integers specifying the\nprotocol level and protocol-specific type respectively, and cmsg_data\nis a bytes-like object holding the associated data.  The flags\nargument defaults to 0 and has the same meaning as for send().  If\naddress is supplied and not None, it sets a destination address for\nthe message.  The return value is the number of bytes of non-ancillary\ndata sent.'
        pass
    
    def sendto(self, data, flags=None, address=None):
        'sendto(data[, flags], address) -> count\n\nLike send(data, flags) but allows specifying the destination address.\nFor IP sockets, the address is a pair (hostaddr, port).'
        pass
    
    def setblocking(self, flag):
        'setblocking(flag)\n\nSet the socket to blocking (flag is true) or non-blocking (false).\nsetblocking(True) is equivalent to settimeout(None);\nsetblocking(False) is equivalent to settimeout(0.0).'
        pass
    
    def setsockopt(self, level, option, None_, optlen: int):
        'setsockopt(level, option, value: int)\nsetsockopt(level, option, value: buffer)\nsetsockopt(level, option, None, optlen: int)\n\nSet a socket option.  See the Unix manual for level and option.\nThe value argument can either be an integer, a string buffer, or \nNone, optlen.'
        pass
    
    def settimeout(self, timeout):
        "settimeout(timeout)\n\nSet a timeout on socket operations.  'timeout' can be a float,\ngiving in seconds, or None.  Setting a timeout of None disables\nthe timeout feature and is equivalent to setblocking(1).\nSetting a timeout of zero is the same as setblocking(0)."
        pass
    
    def shutdown(self, flag):
        'shutdown(flag)\n\nShut down the reading side of the socket (flag == SHUT_RD), the writing side\nof the socket (flag == SHUT_WR), or both ends (flag == SHUT_RDWR).'
        pass
    
    @property
    def timeout(self):
        'the socket timeout'
        pass
    
    @property
    def type(self):
        'the socket type'
        pass
    

def socketpair(family=None, type=None, proto=None):
    'socketpair([family[, type [, proto]]]) -> (socket object, socket object)\n\nCreate a pair of socket objects from the sockets returned by the platform\nsocketpair() function.\nThe arguments are the same as for socket() except the default family is\nAF_UNIX if defined on the platform; otherwise, the default is AF_INET.'
    return tuple()

class timeout(OSError):
    __class__ = timeout
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'socket'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

