import builtins as _mod_builtins
import importlib._bootstrap as _mod_importlib__bootstrap

__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = None
__file__ = '/Users/shuike/anaconda3/lib/python3.7/site-packages/numpy/random/_common.cpython-37m-darwin.so'
__name__ = 'numpy.random._common'
__package__ = 'numpy.random'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
interface = _mod_importlib__bootstrap.interface
def namedtuple(typename, field_names):
    "Returns a new subclass of tuple with named fields.\n\n    >>> Point = namedtuple('Point', ['x', 'y'])\n    >>> Point.__doc__                   # docstring for the new class\n    'Point(x, y)'\n    >>> p = Point(11, y=22)             # instantiate with positional args or keywords\n    >>> p[0] + p[1]                     # indexable like a plain tuple\n    33\n    >>> x, y = p                        # unpack like a regular tuple\n    >>> x, y\n    (11, 22)\n    >>> p.x + p.y                       # fields also accessible by name\n    33\n    >>> d = p._asdict()                 # convert to a dictionary\n    >>> d['x']\n    11\n    >>> Point(**d)                      # convert from a dictionary\n    Point(x=11, y=22)\n    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields\n    Point(x=100, y=22)\n\n    "
    pass

