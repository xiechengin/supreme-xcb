pygame 2.0.1 (SDL 2.0.14, Python 3.6.10)
Hello from the pygame community. https://www.pygame.org/contribute.html
__doc__ = 'pygame module to transform surfaces'
__file__ = '/Users/shuike/anaconda3/envs/py36QT/lib/python3.6/site-packages/pygame/transform.cpython-36m-darwin.so'
__name__ = 'pygame.transform'
__package__ = 'pygame'
def average_color(Surface, Rect=None):
    'average_color(Surface, Rect = None) -> Color\nfinds the average color of a surface'
    pass

def average_surfaces(Surfaces, DestSurface=None, palette_colors=1):
    'average_surfaces(Surfaces, DestSurface = None, palette_colors = 1) -> Surface\nfind the average surface from many surfaces.'
    pass

def chop(Surface, rect):
    'chop(Surface, rect) -> Surface\ngets a copy of an image with an interior area removed'
    pass

def flip(Surface, xbool, ybool):
    'flip(Surface, xbool, ybool) -> Surface\nflip vertically and horizontally'
    pass

def get_smoothscale_backend():
    "get_smoothscale_backend() -> String\nreturn smoothscale filter version in use: 'GENERIC', 'MMX', or 'SSE'"
    pass

def laplacian():
    "threshold(dest_surf, surf, search_color, threshold=(0,0,0,0), set_color=(0,0,0,0), set_behavior=1, search_surf=None, inverse_set=False) -> num_threshold_pixels\nfinds which, and how many pixels in a surface are within a threshold of a 'search_color' or a 'search_surf'."
    pass

def rotate(Surface, angle):
    'rotate(Surface, angle) -> Surface\nrotate an image'
    pass

def rotozoom(Surface, angle, scale):
    'rotozoom(Surface, angle, scale) -> Surface\nfiltered scale and rotation'
    pass

def scale(Surface, width, height):
    'scale(Surface, (width, height), DestSurface = None) -> Surface\nresize to new resolution'
    pass

def scale2x(Surface, DestSurface=None):
    'scale2x(Surface, DestSurface = None) -> Surface\nspecialized image doubler'
    pass

def set_smoothscale_backend(type):
    "set_smoothscale_backend(type) -> None\nset smoothscale filter version to one of: 'GENERIC', 'MMX', or 'SSE'"
    pass

def smoothscale(Surface, width, height):
    'smoothscale(Surface, (width, height), DestSurface = None) -> Surface\nscale a surface to an arbitrary size smoothly'
    pass

def threshold(dest_surf, surf, search_color, threshold=(0,0,0,0), set_color=(0,0,0,0), set_behavior=1, search_surf=None, inverse_set=False):
    "threshold(dest_surf, surf, search_color, threshold=(0,0,0,0), set_color=(0,0,0,0), set_behavior=1, search_surf=None, inverse_set=False) -> num_threshold_pixels\nfinds which, and how many pixels in a surface are within a threshold of a 'search_color' or a 'search_surf'."
    pass

