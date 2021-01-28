import _psutil_osx as _mod__psutil_osx

PSUTIL_CONN_NONE = 128
SIDL = 1
SRUN = 2
SSLEEP = 3
SSTOP = 4
SZOMB = 5
TCPS_CLOSED = 0
TCPS_CLOSE_WAIT = 5
TCPS_CLOSING = 7
TCPS_ESTABLISHED = 4
TCPS_FIN_WAIT_1 = 6
TCPS_FIN_WAIT_2 = 9
TCPS_LAST_ACK = 8
TCPS_LISTEN = 1
TCPS_SYN_RECEIVED = 3
TCPS_SYN_SENT = 2
TCPS_TIME_WAIT = 10
ZombieProcessError = _mod__psutil_osx.ZombieProcessError
__doc__ = None
__file__ = '/Users/shuike/anaconda3/lib/python3.7/site-packages/psutil/_psutil_osx.cpython-37m-darwin.so'
__name__ = 'psutil_osx'
__package__ = 'psutil'
def boot_time():
    'Return the system boot time expressed in seconds since the epoch.'
    pass

def cpu_count_logical():
    'Return number of logical CPUs on the system'
    pass

def cpu_count_phys():
    'Return number of physical CPUs on the system'
    pass

def cpu_freq():
    'Return cpu current frequency'
    pass

def cpu_stats():
    'Return CPU statistics'
    pass

def cpu_times():
    'Return system cpu times as a tuple (user, system, nice, idle, irc)'
    pass

def disk_io_counters():
    'Return dict of tuples of disks I/O information.'
    pass

def disk_partitions():
    'Return a list of tuples including device, mount point and fs type for all partitions mounted on the system.'
    pass

def net_io_counters():
    'Return dict of tuples of networks I/O information.'
    pass

def per_cpu_times():
    'Return system per-cpu times as a list of tuples'
    pass

def pids():
    'Returns a list of PIDs currently running on the system'
    pass

def proc_cmdline():
    'Return process cmdline as a list of cmdline arguments'
    pass

def proc_connections():
    'Get process TCP and UDP connections as a list of tuples'
    pass

def proc_cwd():
    'Return process current working directory.'
    pass

def proc_environ():
    'Return process environment data'
    pass

def proc_exe():
    'Return path of the process executable'
    pass

def proc_kinfo_oneshot():
    'Return multiple process info.'
    pass

def proc_memory_maps():
    "Return a list of tuples for every process's memory map"
    pass

def proc_memory_uss():
    'Return process USS memory'
    pass

def proc_name():
    'Return process name'
    pass

def proc_num_fds():
    'Return the number of fds opened by process.'
    pass

def proc_open_files():
    'Return files opened by process as a list of tuples'
    pass

def proc_pidtaskinfo_oneshot():
    'Return multiple process info.'
    pass

def proc_threads():
    'Return process threads as a list of tuples'
    pass

def sensors_battery():
    'Return battery information.'
    pass

def set_testing():
    'Set psutil in testing mode'
    pass

def swap_mem():
    'Return stats about swap memory, in bytes'
    pass

def users():
    'Return currently connected users as a list of tuples'
    pass

version = 547
def virtual_mem():
    'Return system virtual memory stats'
    pass

