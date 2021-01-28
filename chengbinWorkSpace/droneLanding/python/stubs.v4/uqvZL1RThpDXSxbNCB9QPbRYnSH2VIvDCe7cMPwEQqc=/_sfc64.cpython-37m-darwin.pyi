import builtins as _mod_builtins
import numpy.random._bit_generator as _mod_numpy_random__bit_generator

class SFC64(_mod_numpy_random__bit_generator.BitGenerator):
    '\n    SFC64(seed=None)\n\n    BitGenerator for Chris Doty-Humphrey\'s Small Fast Chaotic PRNG.\n\n    Parameters\n    ----------\n    seed : {None, int, array_like[ints], SeedSequence}, optional\n        A seed to initialize the `BitGenerator`. If None, then fresh,\n        unpredictable entropy will be pulled from the OS. If an ``int`` or\n        ``array_like[ints]`` is passed, then it will be passed to\n        `SeedSequence` to derive the initial `BitGenerator` state. One may also\n        pass in a `SeedSequence` instance.\n\n    Notes\n    -----\n    ``SFC64`` is a 256-bit implementation of Chris Doty-Humphrey\'s Small Fast\n    Chaotic PRNG ([1]_). ``SFC64`` has a few different cycles that one might be\n    on, depending on the seed; the expected period will be about\n    :math:`2^{255}` ([2]_). ``SFC64`` incorporates a 64-bit counter which means\n    that the absolute minimum cycle length is :math:`2^{64}` and that distinct\n    seeds will not run into each other for at least :math:`2^{64}` iterations.\n\n    ``SFC64`` provides a capsule containing function pointers that produce\n    doubles, and unsigned 32 and 64- bit integers. These are not\n    directly consumable in Python and must be consumed by a ``Generator``\n    or similar object that supports low-level access.\n\n    **State and Seeding**\n\n    The ``SFC64`` state vector consists of 4 unsigned 64-bit values. The last\n    is a 64-bit counter that increments by 1 each iteration.\n\n    The input seed is processed by `SeedSequence` to generate the first\n    3 values, then the ``SFC64`` algorithm is iterated a small number of times\n    to mix.\n\n    **Compatibility Guarantee**\n\n    ``SFC64`` makes a guarantee that a fixed seed will always produce the same\n    random integer stream.\n\n    References\n    ----------\n    .. [1] `"PractRand"\n            <http://pracrand.sourceforge.net/RNG_engines.txt>`_\n    .. [2] `"Random Invertible Mapping Statistics"\n            <http://www.pcg-random.org/posts/random-invertible-mapping-statistics.html>`_\n    '
    __class__ = SFC64
    def __init__(self, *args, **kwargs):
        '\n    SFC64(seed=None)\n\n    BitGenerator for Chris Doty-Humphrey\'s Small Fast Chaotic PRNG.\n\n    Parameters\n    ----------\n    seed : {None, int, array_like[ints], SeedSequence}, optional\n        A seed to initialize the `BitGenerator`. If None, then fresh,\n        unpredictable entropy will be pulled from the OS. If an ``int`` or\n        ``array_like[ints]`` is passed, then it will be passed to\n        `SeedSequence` to derive the initial `BitGenerator` state. One may also\n        pass in a `SeedSequence` instance.\n\n    Notes\n    -----\n    ``SFC64`` is a 256-bit implementation of Chris Doty-Humphrey\'s Small Fast\n    Chaotic PRNG ([1]_). ``SFC64`` has a few different cycles that one might be\n    on, depending on the seed; the expected period will be about\n    :math:`2^{255}` ([2]_). ``SFC64`` incorporates a 64-bit counter which means\n    that the absolute minimum cycle length is :math:`2^{64}` and that distinct\n    seeds will not run into each other for at least :math:`2^{64}` iterations.\n\n    ``SFC64`` provides a capsule containing function pointers that produce\n    doubles, and unsigned 32 and 64- bit integers. These are not\n    directly consumable in Python and must be consumed by a ``Generator``\n    or similar object that supports low-level access.\n\n    **State and Seeding**\n\n    The ``SFC64`` state vector consists of 4 unsigned 64-bit values. The last\n    is a 64-bit counter that increments by 1 each iteration.\n\n    The input seed is processed by `SeedSequence` to generate the first\n    3 values, then the ``SFC64`` algorithm is iterated a small number of times\n    to mix.\n\n    **Compatibility Guarantee**\n\n    ``SFC64`` makes a guarantee that a fixed seed will always produce the same\n    random integer stream.\n\n    References\n    ----------\n    .. [1] `"PractRand"\n            <http://pracrand.sourceforge.net/RNG_engines.txt>`_\n    .. [2] `"Random Invertible Mapping Statistics"\n            <http://www.pcg-random.org/posts/random-invertible-mapping-statistics.html>`_\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce_cython__(self):
        pass
    
    def __setstate_cython__(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def state(self):
        '\n        Get or set the PRNG state\n\n        Returns\n        -------\n        state : dict\n            Dictionary containing the information required to describe the\n            state of the PRNG\n        '
        pass
    

__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = None
__file__ = '/Users/shuike/anaconda3/lib/python3.7/site-packages/numpy/random/_sfc64.cpython-37m-darwin.so'
__name__ = 'numpy.random._sfc64'
__package__ = 'numpy.random'
__test__ = _mod_builtins.dict()
