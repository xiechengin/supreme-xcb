import builtins as _mod_builtins

class Vector2(_mod_builtins.object):
    'Vector2() -> Vector2\nVector2(int) -> Vector2\nVector2(float) -> Vector2\nVector2(Vector2) -> Vector2\nVector2(x, y) -> Vector2\nVector2((x, y)) -> Vector2\na 2-Dimensional Vector'
    def __add__(self, value):
        'Return self+value.'
        return Vector2()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = Vector2
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __floordiv__(self, value):
        'Return self//value.'
        return 0
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __ifloordiv__(self, value):
        'Return self//=value.'
        pass
    
    def __imul__(self, value):
        'Return self*=value.'
        return None
    
    def __init__(self, Vector2):
        'Vector2() -> Vector2\nVector2(int) -> Vector2\nVector2(float) -> Vector2\nVector2(Vector2) -> Vector2\nVector2(x, y) -> Vector2\nVector2((x, y)) -> Vector2\na 2-Dimensional Vector'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return Vector2()
    
    def __itruediv__(self, value):
        'Return self/=value.'
        pass
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return Vector2()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return Vector2()
    
    def __pos__(self):
        '+self'
        return Vector2()
    
    def __radd__(self, value):
        'Return value+self.'
        return Vector2()
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rfloordiv__(self, value):
        'Return value//self.'
        return Vector2()
    
    def __rmul__(self, value):
        'Return value*self.'
        return Vector2()
    
    def __rsub__(self, value):
        'Return value-self.'
        return Vector2()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return Vector2()
    
    def __safe_for_unpickling__(self):
        pass
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    def __sub__(self, value):
        'Return self-value.'
        return Vector2()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def angle_to(self, Vector2):
        'angle_to(Vector2) -> float\ncalculates the angle to a given vector in degrees.'
        return 1.0
    
    def as_polar(self):
        'as_polar() -> (r, phi)\nreturns a tuple with radial distance and azimuthal angle.'
        return tuple()
    
    def cross(self, Vector2):
        'cross(Vector2) -> Vector2\ncalculates the cross- or vector-product'
        pass
    
    def distance_squared_to(self, Vector2):
        'distance_squared_to(Vector2) -> float\ncalculates the squared Euclidean distance to a given vector.'
        return 1.0
    
    def distance_to(self, Vector2):
        'distance_to(Vector2) -> float\ncalculates the Euclidean distance to a given vector.'
        return 1.0
    
    def dot(self, Vector2):
        'dot(Vector2) -> float\ncalculates the dot- or scalar-product with the other vector'
        return 1.0
    
    def elementwise(self):
        'elementwise() -> VectorElementwiseProxy\nThe next operation will be performed elementwise.'
        pass
    
    @property
    def epsilon(self):
        'small value used in comparisons'
        pass
    
    def from_polar(self, r, phi):
        'from_polar((r, phi)) -> None\nSets x and y from a polar coordinates tuple.'
        pass
    
    def is_normalized(self):
        'is_normalized() -> Bool\ntests if the vector is normalized i.e. has length == 1.'
        pass
    
    def length(self):
        'length() -> float\nreturns the Euclidean length of the vector.'
        return 1.0
    
    def length_squared(self):
        'length_squared() -> float\nreturns the squared Euclidean length of the vector.'
        return 1.0
    
    def lerp(self, Vector2, float):
        'lerp(Vector2, float) -> Vector2\nreturns a linear interpolation to the given vector.'
        pass
    
    def magnitude(self):
        'magnitude() -> float\nreturns the Euclidean magnitude of the vector.'
        return 1.0
    
    def magnitude_squared(self):
        'magnitude_squared() -> float\nreturns the squared magnitude of the vector.'
        return 1.0
    
    def normalize(self):
        'normalize() -> Vector2\nreturns a vector with the same direction but length 1.'
        pass
    
    def normalize_ip(self):
        'normalize_ip() -> None\nnormalizes the vector in place so that its length is 1.'
        pass
    
    def reflect(self, Vector2):
        'reflect(Vector2) -> Vector2\nreturns a vector reflected of a given normal.'
        pass
    
    def reflect_ip(self, Vector2):
        'reflect_ip(Vector2) -> None\nreflect the vector of a given normal in place.'
        pass
    
    def rotate(self, angle):
        'rotate(angle) -> Vector2\nrotates a vector by a given angle in degrees.'
        pass
    
    def rotate_ip(self, angle):
        'rotate_ip(angle) -> None\nrotates the vector by a given angle in degrees in place.'
        pass
    
    def rotate_ip_rad(self, angle):
        'rotate_ip_rad(angle) -> None\nrotates the vector by a given angle in radians in place.'
        pass
    
    def rotate_rad(self, angle):
        'rotate_rad(angle) -> Vector2\nrotates a vector by a given angle in radians.'
        pass
    
    def scale_to_length(self, float):
        'scale_to_length(float) -> None\nscales the vector to a given length.'
        pass
    
    def slerp(self, Vector2, float):
        'slerp(Vector2, float) -> Vector2\nreturns a spherical interpolation to the given vector.'
        pass
    
    def update(self, Vector2):
        'update() -> None\nupdate(int) -> None\nupdate(float) -> None\nupdate(Vector2) -> None\nupdate(x, y) -> None\nupdate((x, y)) -> None\nSets the coordinates of the vector.'
        pass
    
    @property
    def x(self):
        pass
    
    @property
    def y(self):
        pass
    

class Vector3(_mod_builtins.object):
    'Vector3() -> Vector3\nVector3(int) -> Vector3\nVector3(float) -> Vector3\nVector3(Vector3) -> Vector3\nVector3(x, y, z) -> Vector3\nVector3((x, y, z)) -> Vector3\na 3-Dimensional Vector'
    def __add__(self, value):
        'Return self+value.'
        return Vector3()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = Vector3
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __floordiv__(self, value):
        'Return self//value.'
        return 0
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __ifloordiv__(self, value):
        'Return self//=value.'
        pass
    
    def __imul__(self, value):
        'Return self*=value.'
        return None
    
    def __init__(self, x, y, z):
        'Vector3() -> Vector3\nVector3(int) -> Vector3\nVector3(float) -> Vector3\nVector3(Vector3) -> Vector3\nVector3(x, y, z) -> Vector3\nVector3((x, y, z)) -> Vector3\na 3-Dimensional Vector'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return Vector3()
    
    def __itruediv__(self, value):
        'Return self/=value.'
        pass
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return Vector3()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return Vector3()
    
    def __pos__(self):
        '+self'
        return Vector3()
    
    def __radd__(self, value):
        'Return value+self.'
        return Vector3()
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rfloordiv__(self, value):
        'Return value//self.'
        return Vector3()
    
    def __rmul__(self, value):
        'Return value*self.'
        return Vector3()
    
    def __rsub__(self, value):
        'Return value-self.'
        return Vector3()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return Vector3()
    
    def __safe_for_unpickling__(self):
        pass
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    def __sub__(self, value):
        'Return self-value.'
        return Vector3()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def angle_to(self, Vector3):
        'angle_to(Vector3) -> float\ncalculates the angle to a given vector in degrees.'
        return 1.0
    
    def as_spherical(self):
        'as_spherical() -> (r, theta, phi)\nreturns a tuple with radial distance, inclination and azimuthal angle.'
        return tuple()
    
    def cross(self, Vector3):
        'cross(Vector3) -> Vector3\ncalculates the cross- or vector-product'
        pass
    
    def distance_squared_to(self, Vector3):
        'distance_squared_to(Vector3) -> float\ncalculates the squared Euclidean distance to a given vector.'
        return 1.0
    
    def distance_to(self, Vector3):
        'distance_to(Vector3) -> float\ncalculates the Euclidean distance to a given vector.'
        return 1.0
    
    def dot(self, Vector3):
        'dot(Vector3) -> float\ncalculates the dot- or scalar-product with the other vector'
        return 1.0
    
    def elementwise(self):
        'elementwise() -> VectorElementwiseProxy\nThe next operation will be performed elementwise.'
        pass
    
    @property
    def epsilon(self):
        'small value used in comparisons'
        pass
    
    def from_spherical(self, r, theta, phi):
        'from_spherical((r, theta, phi)) -> None\nSets x, y and z from a spherical coordinates 3-tuple.'
        pass
    
    def is_normalized(self):
        'is_normalized() -> Bool\ntests if the vector is normalized i.e. has length == 1.'
        pass
    
    def length(self):
        'length() -> float\nreturns the Euclidean length of the vector.'
        return 1.0
    
    def length_squared(self):
        'length_squared() -> float\nreturns the squared Euclidean length of the vector.'
        return 1.0
    
    def lerp(self, Vector3, float):
        'lerp(Vector3, float) -> Vector3\nreturns a linear interpolation to the given vector.'
        pass
    
    def magnitude(self):
        'magnitude() -> float\nreturns the Euclidean magnitude of the vector.'
        return 1.0
    
    def magnitude_squared(self):
        'magnitude_squared() -> float\nreturns the squared Euclidean magnitude of the vector.'
        return 1.0
    
    def normalize(self):
        'normalize() -> Vector3\nreturns a vector with the same direction but length 1.'
        pass
    
    def normalize_ip(self):
        'normalize_ip() -> None\nnormalizes the vector in place so that its length is 1.'
        pass
    
    def reflect(self, Vector3):
        'reflect(Vector3) -> Vector3\nreturns a vector reflected of a given normal.'
        pass
    
    def reflect_ip(self, Vector3):
        'reflect_ip(Vector3) -> None\nreflect the vector of a given normal in place.'
        pass
    
    def rotate(self, angle, Vector3):
        'rotate(angle, Vector3) -> Vector3\nrotates a vector by a given angle in degrees.'
        pass
    
    def rotate_ip(self, angle, Vector3):
        'rotate_ip(angle, Vector3) -> None\nrotates the vector by a given angle in degrees in place.'
        pass
    
    def rotate_ip_rad(self, angle, Vector3):
        'rotate_ip_rad(angle, Vector3) -> None\nrotates the vector by a given angle in radians in place.'
        pass
    
    def rotate_rad(self, angle, Vector3):
        'rotate_rad(angle, Vector3) -> Vector3\nrotates a vector by a given angle in radians.'
        pass
    
    def rotate_x(self, angle):
        'rotate_x(angle) -> Vector3\nrotates a vector around the x-axis by the angle in degrees.'
        pass
    
    def rotate_x_ip(self, angle):
        'rotate_x_ip(angle) -> None\nrotates the vector around the x-axis by the angle in degrees in place.'
        pass
    
    def rotate_x_ip_rad(self, angle):
        'rotate_x_ip_rad(angle) -> None\nrotates the vector around the x-axis by the angle in radians in place.'
        pass
    
    def rotate_x_rad(self, angle):
        'rotate_x_rad(angle) -> Vector3\nrotates a vector around the x-axis by the angle in radians.'
        pass
    
    def rotate_y(self, angle):
        'rotate_y(angle) -> Vector3\nrotates a vector around the y-axis by the angle in degrees.'
        pass
    
    def rotate_y_ip(self, angle):
        'rotate_y_ip(angle) -> None\nrotates the vector around the y-axis by the angle in degrees in place.'
        pass
    
    def rotate_y_ip_rad(self, angle):
        'rotate_y_ip_rad(angle) -> None\nrotates the vector around the y-axis by the angle in radians in place.'
        pass
    
    def rotate_y_rad(self, angle):
        'rotate_y_rad(angle) -> Vector3\nrotates a vector around the y-axis by the angle in radians.'
        pass
    
    def rotate_z(self, angle):
        'rotate_z(angle) -> Vector3\nrotates a vector around the z-axis by the angle in degrees.'
        pass
    
    def rotate_z_ip(self, angle):
        'rotate_z_ip(angle) -> None\nrotates the vector around the z-axis by the angle in degrees in place.'
        pass
    
    def rotate_z_ip_rad(self, angle):
        'rotate_z_ip_rad(angle) -> None\nrotates the vector around the z-axis by the angle in radians in place.'
        pass
    
    def rotate_z_rad(self, angle):
        'rotate_z_rad(angle) -> Vector3\nrotates a vector around the z-axis by the angle in radians.'
        pass
    
    def scale_to_length(self, float):
        'scale_to_length(float) -> None\nscales the vector to a given length.'
        pass
    
    def slerp(self, Vector3, float):
        'slerp(Vector3, float) -> Vector3\nreturns a spherical interpolation to the given vector.'
        pass
    
    def update(self, x, y, z):
        'update() -> None\nupdate(int) -> None\nupdate(float) -> None\nupdate(Vector3) -> None\nupdate(x, y, z) -> None\nupdate((x, y, z)) -> None\nSets the coordinates of the vector.'
        pass
    
    @property
    def x(self):
        pass
    
    @property
    def y(self):
        pass
    
    @property
    def z(self):
        pass
    
pygame 2.0.1 (SDL 2.0.14, Python 3.6.10)
Hello from the pygame community. https://www.pygame.org/contribute.html

class VectorElementwiseProxy(_mod_builtins.object):
    def __abs__(self):
        'abs(self)'
        return VectorElementwiseProxy()
    
    def __add__(self, value):
        'Return self+value.'
        return VectorElementwiseProxy()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = VectorElementwiseProxy
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __floordiv__(self, value):
        'Return self//value.'
        return 0
    
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
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mod__(self, value):
        'Return self%value.'
        return VectorElementwiseProxy()
    
    def __mul__(self, value):
        'Return self*value.'
        return VectorElementwiseProxy()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return VectorElementwiseProxy()
    
    def __pos__(self):
        '+self'
        return VectorElementwiseProxy()
    
    def __pow__(self, value, mod):
        'Return pow(self, value, mod).'
        return VectorElementwiseProxy()
    
    def __radd__(self, value):
        'Return value+self.'
        return VectorElementwiseProxy()
    
    def __rfloordiv__(self, value):
        'Return value//self.'
        return VectorElementwiseProxy()
    
    def __rmod__(self, value):
        'Return value%self.'
        return VectorElementwiseProxy()
    
    def __rmul__(self, value):
        'Return value*self.'
        return VectorElementwiseProxy()
    
    def __rpow__(self, value, mod):
        'Return pow(value, self, mod).'
        return VectorElementwiseProxy()
    
    def __rsub__(self, value):
        'Return value-self.'
        return VectorElementwiseProxy()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return VectorElementwiseProxy()
    
    def __sub__(self, value):
        'Return self-value.'
        return VectorElementwiseProxy()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    

class VectorIterator(_mod_builtins.object):
    __class__ = VectorIterator
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return VectorIterator()
    
    def __length_hint__(self):
        return 0
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

_PYGAME_C_API = _mod_builtins.PyCapsule()
__doc__ = 'pygame module for vector classes'
__file__ = '/Users/shuike/anaconda3/envs/py36QT/lib/python3.6/site-packages/pygame/math.cpython-36m-darwin.so'
__name__ = 'pygame.math'
__package__ = 'pygame'
def disable_swizzling():
    'disables swizzling.'
    pass

def enable_swizzling():
    'enables swizzling.'
    pass

