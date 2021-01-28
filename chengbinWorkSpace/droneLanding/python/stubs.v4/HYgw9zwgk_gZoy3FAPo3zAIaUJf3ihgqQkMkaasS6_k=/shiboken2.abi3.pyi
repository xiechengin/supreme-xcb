import builtins as _mod_builtins

class VoidPtr(_mod_builtins.object):
    __class__ = VoidPtr
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
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        'int(self)'
        return 0
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'shiboken2.shiboken2'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def toBytes(self):
        pass
    

__doc__ = None
__file__ = '/Users/shuike/anaconda3/envs/py36QT/lib/python3.6/site-packages/shiboken2/shiboken2.abi3.so'
__name__ = 'shiboken2.shiboken2'
__package__ = 'shiboken2'
__version__ = '5.15.1'
__version_info__ = _mod_builtins.tuple()
def _unpickle_enum(arg__1, arg__2):
    return object

def createdByPython(arg__1):
    return bool

def delete(arg__1):
    pass

def dump(arg__1):
    return object

def getAllValidWrappers():
    return object

def getCppPointer(arg__1):
    return object

def invalidate(arg__1):
    pass

def isValid(arg__1):
    return bool

def ownedByPython(arg__1):
    return bool

def wrapInstance(arg__1, arg__2):
    return object

