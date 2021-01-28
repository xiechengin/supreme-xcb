import builtins as _mod_builtins

class TrapezoidMapTriFinder(_mod_builtins.object):
    'Create a new C++ TrapezoidMapTriFinder object\nThis should not be called directly, instead use the python class\nmatplotlib.tri.TrapezoidMapTriFinder instead.\n'
    __class__ = TrapezoidMapTriFinder
    def __init__(self, *args, **kwargs):
        'Create a new C++ TrapezoidMapTriFinder object\nThis should not be called directly, instead use the python class\nmatplotlib.tri.TrapezoidMapTriFinder instead.\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def find_many(self, x, y):
        'find_many(x, y)\n\nFind indices of triangles containing the point coordinates (x, y)'
        pass
    
    def get_tree_stats(self):
        'get_tree_stats()\n\nReturn statistics about the tree used by the trapezoid map'
        pass
    
    def initialize(self):
        'initialize()\n\nInitialize this object, creating the trapezoid map from the triangulation'
        pass
    
    def print_tree(self):
        'print_tree()\n\nPrint the search tree as text to stdout; useful for debug purposes'
        pass
    

class TriContourGenerator(_mod_builtins.object):
    'Create a new C++ TriContourGenerator object\nThis should not be called directly, instead use the functions\nmatplotlib.axes.tricontour and tricontourf instead.\n'
    __class__ = TriContourGenerator
    def __init__(self, *args, **kwargs):
        'Create a new C++ TriContourGenerator object\nThis should not be called directly, instead use the functions\nmatplotlib.axes.tricontour and tricontourf instead.\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def create_contour(self, level):
        'create_contour(level)\n\nCreate and return a non-filled contour.'
        pass
    
    def create_filled_contour(self, lower_level, upper_level):
        'create_filled_contour(lower_level, upper_level)\n\nCreate and return a filled contour'
        pass
    

class Triangulation(_mod_builtins.object):
    'Create a new C++ Triangulation object\nThis should not be called directly, instead use the python class\nmatplotlib.tri.Triangulation instead.\n'
    __class__ = Triangulation
    def __init__(self, *args, **kwargs):
        'Create a new C++ Triangulation object\nThis should not be called directly, instead use the python class\nmatplotlib.tri.Triangulation instead.\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def calculate_plane_coefficients(self, z, plane_coefficients):
        'Calculate plane equation coefficients for all unmasked triangles'
        pass
    
    def get_edges(self):
        'Return edges array'
        pass
    
    def get_neighbors(self):
        'Return neighbors array'
        pass
    
    def set_mask(self, mask):
        'Set or clear the mask array.'
        pass
    

__doc__ = None
__file__ = '/Users/shuike/anaconda3/envs/py36QT/lib/python3.6/site-packages/matplotlib/_tri.cpython-36m-darwin.so'
__name__ = 'matplotlib._tri'
__package__ = 'matplotlib'
