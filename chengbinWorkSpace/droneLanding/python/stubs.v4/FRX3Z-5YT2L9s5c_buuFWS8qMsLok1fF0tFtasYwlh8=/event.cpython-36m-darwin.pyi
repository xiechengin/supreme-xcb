pygame 2.0.1 (SDL 2.0.14, Python 3.6.10)
Hello from the pygame community. https://www.pygame.org/contribute.html
import builtins as _mod_builtins

def Event(type, **attributes):
    'Event(type, dict) -> EventType instance\nEvent(type, **attributes) -> EventType instance\ncreate a new event object'
    pass

EventType = _mod_builtins.Event
_PYGAME_C_API = _mod_builtins.PyCapsule()
def __PYGAMEinit__():
    'auto initialize for event module'
    pass

__doc__ = 'pygame module for interacting with events and queues'
__file__ = '/Users/shuike/anaconda3/envs/py36QT/lib/python3.6/site-packages/pygame/event.cpython-36m-darwin.so'
__name__ = 'pygame.event'
__package__ = 'pygame'
_joy_instance_map = _mod_builtins.dict()
def clear(eventtype=None, pump=True):
    'clear(eventtype=None) -> None\nclear(eventtype=None, pump=True) -> None\nremove all events from the queue'
    pass

def custom_type():
    'custom_type() -> int\nmake custom user event type'
    return 1

def event_name(type):
    'event_name(type) -> string\nget the string name from an event id'
    return ''

def get(eventtype=None, pump=True):
    'get(eventtype=None) -> Eventlist\nget(eventtype=None, pump=True) -> Eventlist\nget events from the queue'
    pass

def get_blocked(typelist):
    'get_blocked(type) -> bool\nget_blocked(typelist) -> bool\ntest if a type of event is blocked from the queue'
    return True

def get_grab():
    'get_grab() -> bool\ntest if the program is sharing input devices'
    return True

def peek(eventtype=None, pump=True):
    'peek(eventtype=None) -> bool\npeek(eventtype=None, pump=True) -> bool\ntest if event types are waiting on the queue'
    return True

def poll():
    'poll() -> EventType instance\nget a single event from the queue'
    pass

def post(Event):
    'post(Event) -> bool\nplace a new event on the queue'
    return True

def pump():
    'pump() -> None\ninternally process pygame event handlers'
    pass

def set_allowed(typelist):
    'set_allowed(type) -> None\nset_allowed(typelist) -> None\nset_allowed(None) -> None\ncontrol which events are allowed on the queue'
    pass

def set_blocked(typelist):
    'set_blocked(type) -> None\nset_blocked(typelist) -> None\nset_blocked(None) -> None\ncontrol which events are allowed on the queue'
    pass

def set_grab(bool):
    'set_grab(bool) -> None\ncontrol the sharing of input devices with other applications'
    pass

def wait(timeout):
    'wait() -> EventType instance\nwait(timeout) -> EventType instance\nwait for a single event from the queue'
    pass

