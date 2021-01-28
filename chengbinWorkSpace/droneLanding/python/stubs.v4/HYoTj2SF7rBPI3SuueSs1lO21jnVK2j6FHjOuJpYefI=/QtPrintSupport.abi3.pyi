import PySide2.QtGui as _mod_PySide2_QtGui
import PySide2.QtWidgets as _mod_PySide2_QtWidgets
import Shiboken as _mod_Shiboken

class QAbstractPrintDialog(_mod_PySide2_QtWidgets.QDialog):
    'QAbstractPrintDialog(self, printer:PySide2.QtPrintSupport.QPrinter, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None)'
    AllPages = PrintRange()
    CurrentPage = PrintRange()
    DontUseSheet = PrintDialogOption()
    None_ = PrintDialogOption()
    PageRange = PrintRange()
    PrintCollateCopies = PrintDialogOption()
    PrintCurrentPage = PrintDialogOption()
    PrintDialogOption = PrintDialogOption
    PrintDialogOptions = PrintDialogOptions
    PrintPageRange = PrintDialogOption()
    PrintRange = PrintRange
    PrintSelection = PrintDialogOption()
    PrintShowPageSize = PrintDialogOption()
    PrintToFile = PrintDialogOption()
    Selection = PrintRange()
    __class__ = QAbstractPrintDialog
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, printer: PySide2.QtPrintSupport.QPrinter, parent: typing.Union[PySide2.QtWidgets.QWidget,NoneType]=None):
        'QAbstractPrintDialog(self, printer:PySide2.QtPrintSupport.QPrinter, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtPrintSupport'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addEnabledOption(self, option):
        'addEnabledOption(self, option:PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption)'
        pass
    
    def enabledOptions(self):
        'enabledOptions(self) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions'
        return PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions
    
    def fromPage(self):
        'fromPage(self) -> int'
        return int
    
    def isOptionEnabled(self, option):
        'isOptionEnabled(self, option:PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption) -> bool'
        return bool
    
    def maxPage(self):
        'maxPage(self) -> int'
        return int
    
    def minPage(self):
        'minPage(self) -> int'
        return int
    
    def printRange(self):
        'printRange(self) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange'
        return PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange
    
    def printer(self):
        'printer(self) -> PySide2.QtPrintSupport.QPrinter'
        return PySide2.QtPrintSupport.QPrinter
    
    def setEnabledOptions(self, options):
        'setEnabledOptions(self, options:PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions)'
        pass
    
    def setFromTo(self, fromPage, toPage):
        'setFromTo(self, fromPage:int, toPage:int)'
        pass
    
    def setMinMax(self, min, max):
        'setMinMax(self, min:int, max:int)'
        pass
    
    def setOptionTabs(self, tabs):
        'setOptionTabs(self, tabs:typing.Sequence)'
        pass
    
    def setPrintRange(self, range):
        'setPrintRange(self, range:PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def toPage(self):
        'toPage(self) -> int'
        return int
    

class QPageSetupDialog(_mod_PySide2_QtWidgets.QDialog):
    'QPageSetupDialog(self, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None)\nQPageSetupDialog(self, printer:PySide2.QtPrintSupport.QPrinter, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None)'
    __class__ = QPageSetupDialog
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, printer: PySide2.QtPrintSupport.QPrinter, parent: typing.Union[PySide2.QtWidgets.QWidget,NoneType]=None):
        'QPageSetupDialog(self, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None)\nQPageSetupDialog(self, printer:PySide2.QtPrintSupport.QPrinter, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtPrintSupport'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def done(self, result):
        'done(self, result:int)'
        pass
    
    def exec_(self):
        'exec_(self) -> int'
        return int
    
    def open(self, receiver: PySide2.QtCore.QObject, member: bytes):
        'open(self)\nopen(self, receiver:PySide2.QtCore.QObject, member:bytes)'
        pass
    
    def printer(self):
        'printer(self) -> PySide2.QtPrintSupport.QPrinter'
        return PySide2.QtPrintSupport.QPrinter
    
    def setVisible(self, visible):
        'setVisible(self, visible:bool)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QPrintDialog(QAbstractPrintDialog):
    'QPrintDialog(self, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None)\nQPrintDialog(self, printer:PySide2.QtPrintSupport.QPrinter, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None)'
    __class__ = QPrintDialog
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, printer: PySide2.QtPrintSupport.QPrinter, parent: typing.Union[PySide2.QtWidgets.QWidget,NoneType]=None):
        'QPrintDialog(self, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None)\nQPrintDialog(self, printer:PySide2.QtPrintSupport.QPrinter, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtPrintSupport'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def accepted(self):
        pass
    
    def done(self, result):
        'done(self, result:int)'
        pass
    
    def exec_(self):
        'exec_(self) -> int'
        return int
    
    def open(self, receiver: PySide2.QtCore.QObject, member: bytes):
        'open(self)\nopen(self, receiver:PySide2.QtCore.QObject, member:bytes)'
        pass
    
    def options(self):
        'options(self) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions'
        return PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions
    
    def setOption(self, option, on):
        'setOption(self, option:PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption, on:bool=True)'
        pass
    
    def setOptions(self, options):
        'setOptions(self, options:PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions)'
        pass
    
    def setVisible(self, visible):
        'setVisible(self, visible:bool)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def testOption(self, option):
        'testOption(self, option:PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption) -> bool'
        return bool
    

class QPrintEngine(_mod_Shiboken.Object):
    'QPrintEngine(self)'
    PPK_CollateCopies = PrintEnginePropertyKey()
    PPK_ColorMode = PrintEnginePropertyKey()
    PPK_CopyCount = PrintEnginePropertyKey()
    PPK_Creator = PrintEnginePropertyKey()
    PPK_CustomBase = PrintEnginePropertyKey()
    PPK_CustomPaperSize = PrintEnginePropertyKey()
    PPK_DocumentName = PrintEnginePropertyKey()
    PPK_Duplex = PrintEnginePropertyKey()
    PPK_FontEmbedding = PrintEnginePropertyKey()
    PPK_FullPage = PrintEnginePropertyKey()
    PPK_NumberOfCopies = PrintEnginePropertyKey()
    PPK_Orientation = PrintEnginePropertyKey()
    PPK_OutputFileName = PrintEnginePropertyKey()
    PPK_PageMargins = PrintEnginePropertyKey()
    PPK_PageOrder = PrintEnginePropertyKey()
    PPK_PageRect = PrintEnginePropertyKey()
    PPK_PageSize = PrintEnginePropertyKey()
    PPK_PaperName = PrintEnginePropertyKey()
    PPK_PaperRect = PrintEnginePropertyKey()
    PPK_PaperSize = PrintEnginePropertyKey()
    PPK_PaperSource = PrintEnginePropertyKey()
    PPK_PaperSources = PrintEnginePropertyKey()
    PPK_PrinterName = PrintEnginePropertyKey()
    PPK_PrinterProgram = PrintEnginePropertyKey()
    PPK_QPageLayout = PrintEnginePropertyKey()
    PPK_QPageMargins = PrintEnginePropertyKey()
    PPK_QPageSize = PrintEnginePropertyKey()
    PPK_Resolution = PrintEnginePropertyKey()
    PPK_SelectionOption = PrintEnginePropertyKey()
    PPK_SupportedResolutions = PrintEnginePropertyKey()
    PPK_SupportsMultipleCopies = PrintEnginePropertyKey()
    PPK_WindowsPageSize = PrintEnginePropertyKey()
    PrintEnginePropertyKey = PrintEnginePropertyKey
    __class__ = QPrintEngine
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QPrintEngine(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtPrintSupport'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def abort(self):
        'abort(self) -> bool'
        return bool
    
    def metric(self, arg__1):
        'metric(self, arg__1:PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int'
        return int
    
    def newPage(self):
        'newPage(self) -> bool'
        return bool
    
    def printerState(self):
        'printerState(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState'
        return PySide2.QtPrintSupport.QPrinter.PrinterState
    
    def property(self, key):
        'property(self, key:PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey) -> typing.Any'
        return typing.Any
    
    def setProperty(self, key, value):
        'setProperty(self, key:PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey, value:typing.Any)'
        pass
    

class QPrintPreviewDialog(_mod_PySide2_QtWidgets.QDialog):
    'QPrintPreviewDialog(self, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None, flags:PySide2.QtCore.Qt.WindowFlags=Default(Qt.WindowFlags))\nQPrintPreviewDialog(self, printer:PySide2.QtPrintSupport.QPrinter, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None, flags:PySide2.QtCore.Qt.WindowFlags=Default(Qt.WindowFlags))'
    __class__ = QPrintPreviewDialog
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, printer: PySide2.QtPrintSupport.QPrinter, parent: typing.Union[PySide2.QtWidgets.QWidget,NoneType]=None, flags: PySide2.QtCore.Qt.WindowFlags=Default(Qt.WindowFlags)):
        'QPrintPreviewDialog(self, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None, flags:PySide2.QtCore.Qt.WindowFlags=Default(Qt.WindowFlags))\nQPrintPreviewDialog(self, printer:PySide2.QtPrintSupport.QPrinter, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None, flags:PySide2.QtCore.Qt.WindowFlags=Default(Qt.WindowFlags))'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtPrintSupport'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def done(self, result):
        'done(self, result:int)'
        pass
    
    def open(self, receiver: PySide2.QtCore.QObject, member: bytes):
        'open(self)\nopen(self, receiver:PySide2.QtCore.QObject, member:bytes)'
        pass
    
    def paintRequested(self):
        pass
    
    def printer(self):
        'printer(self) -> PySide2.QtPrintSupport.QPrinter'
        return PySide2.QtPrintSupport.QPrinter
    
    def setVisible(self, visible):
        'setVisible(self, visible:bool)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QPrintPreviewWidget(_mod_PySide2_QtWidgets.QWidget):
    'QPrintPreviewWidget(self, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None, flags:PySide2.QtCore.Qt.WindowFlags=Default(Qt.WindowFlags))\nQPrintPreviewWidget(self, printer:PySide2.QtPrintSupport.QPrinter, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None, flags:PySide2.QtCore.Qt.WindowFlags=Default(Qt.WindowFlags))'
    AllPagesView = ViewMode()
    CustomZoom = ZoomMode()
    FacingPagesView = ViewMode()
    FitInView = ZoomMode()
    FitToWidth = ZoomMode()
    SinglePageView = ViewMode()
    ViewMode = ViewMode
    ZoomMode = ZoomMode
    __class__ = QPrintPreviewWidget
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, printer: PySide2.QtPrintSupport.QPrinter, parent: typing.Union[PySide2.QtWidgets.QWidget,NoneType]=None, flags: PySide2.QtCore.Qt.WindowFlags=Default(Qt.WindowFlags)):
        'QPrintPreviewWidget(self, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None, flags:PySide2.QtCore.Qt.WindowFlags=Default(Qt.WindowFlags))\nQPrintPreviewWidget(self, printer:PySide2.QtPrintSupport.QPrinter, parent:typing.Union[PySide2.QtWidgets.QWidget, NoneType]=None, flags:PySide2.QtCore.Qt.WindowFlags=Default(Qt.WindowFlags))'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtPrintSupport'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def currentPage(self):
        'currentPage(self) -> int'
        return int
    
    def fitInView(self):
        'fitInView(self)'
        pass
    
    def fitToWidth(self):
        'fitToWidth(self)'
        pass
    
    def orientation(self):
        'orientation(self) -> PySide2.QtPrintSupport.QPrinter.Orientation'
        return PySide2.QtPrintSupport.QPrinter.Orientation
    
    def pageCount(self):
        'pageCount(self) -> int'
        return int
    
    def paintRequested(self):
        pass
    
    def previewChanged(self):
        pass
    
    def print_(self):
        'print_(self)'
        pass
    
    def setAllPagesViewMode(self):
        'setAllPagesViewMode(self)'
        pass
    
    def setCurrentPage(self, pageNumber):
        'setCurrentPage(self, pageNumber:int)'
        pass
    
    def setFacingPagesViewMode(self):
        'setFacingPagesViewMode(self)'
        pass
    
    def setLandscapeOrientation(self):
        'setLandscapeOrientation(self)'
        pass
    
    def setOrientation(self, orientation):
        'setOrientation(self, orientation:PySide2.QtPrintSupport.QPrinter.Orientation)'
        pass
    
    def setPortraitOrientation(self):
        'setPortraitOrientation(self)'
        pass
    
    def setSinglePageViewMode(self):
        'setSinglePageViewMode(self)'
        pass
    
    def setViewMode(self, viewMode):
        'setViewMode(self, viewMode:PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode)'
        pass
    
    def setVisible(self, visible):
        'setVisible(self, visible:bool)'
        pass
    
    def setZoomFactor(self, zoomFactor):
        'setZoomFactor(self, zoomFactor:float)'
        pass
    
    def setZoomMode(self, zoomMode):
        'setZoomMode(self, zoomMode:PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def updatePreview(self):
        'updatePreview(self)'
        pass
    
    def viewMode(self):
        'viewMode(self) -> PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode'
        return PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode
    
    def zoomFactor(self):
        'zoomFactor(self) -> float'
        return float
    
    def zoomIn(self, zoom):
        'zoomIn(self, zoom:float=1.1)'
        pass
    
    def zoomMode(self):
        'zoomMode(self) -> PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode'
        return PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode
    
    def zoomOut(self, zoom):
        'zoomOut(self, zoom:float=1.1)'
        pass
    

class QPrinter(_mod_PySide2_QtGui.QPagedPaintDevice):
    'QPrinter(self, mode:PySide2.QtPrintSupport.QPrinter.PrinterMode=PySide2.QtPrintSupport.QPrinter.PrinterMode.ScreenResolution)\nQPrinter(self, printer:PySide2.QtPrintSupport.QPrinterInfo, mode:PySide2.QtPrintSupport.QPrinter.PrinterMode=PySide2.QtPrintSupport.QPrinter.PrinterMode.ScreenResolution)'
    Aborted = PrinterState()
    Active = PrinterState()
    AllPages = PrintRange()
    Auto = PaperSource()
    Cassette = PaperSource()
    Cicero = Unit()
    Color = ColorMode()
    ColorMode = ColorMode
    CurrentPage = PrintRange()
    CustomSource = PaperSource()
    DevicePixel = Unit()
    Didot = Unit()
    DuplexAuto = DuplexMode()
    DuplexLongSide = DuplexMode()
    DuplexMode = DuplexMode
    DuplexNone = DuplexMode()
    DuplexShortSide = DuplexMode()
    Envelope = PaperSource()
    EnvelopeManual = PaperSource()
    Error = PrinterState()
    FirstPageFirst = PageOrder()
    FormSource = PaperSource()
    GrayScale = ColorMode()
    HighResolution = PrinterMode()
    Idle = PrinterState()
    Inch = Unit()
    Landscape = Orientation()
    LargeCapacity = PaperSource()
    LargeFormat = PaperSource()
    LastPageFirst = PageOrder()
    LastPaperSource = PaperSource()
    Lower = PaperSource()
    Manual = PaperSource()
    MaxPageSource = PaperSource()
    Middle = PaperSource()
    Millimeter = Unit()
    NativeFormat = OutputFormat()
    OnlyOne = PaperSource()
    Orientation = Orientation
    OutputFormat = OutputFormat
    PageOrder = PageOrder
    PageRange = PrintRange()
    PaperSource = PaperSource
    PdfFormat = OutputFormat()
    Pica = Unit()
    Point = Unit()
    Portrait = Orientation()
    PrintRange = PrintRange
    PrinterMode = PrinterMode
    PrinterResolution = PrinterMode()
    PrinterState = PrinterState
    ScreenResolution = PrinterMode()
    Selection = PrintRange()
    SmallFormat = PaperSource()
    Tractor = PaperSource()
    Unit = Unit
    Upper = PaperSource()
    __class__ = QPrinter
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, printer: PySide2.QtPrintSupport.QPrinterInfo, mode: PySide2.QtPrintSupport.QPrinter.PrinterMode=PySide2.QtPrintSupport.QPrinter.PrinterMode.ScreenResolution):
        'QPrinter(self, mode:PySide2.QtPrintSupport.QPrinter.PrinterMode=PySide2.QtPrintSupport.QPrinter.PrinterMode.ScreenResolution)\nQPrinter(self, printer:PySide2.QtPrintSupport.QPrinterInfo, mode:PySide2.QtPrintSupport.QPrinter.PrinterMode=PySide2.QtPrintSupport.QPrinter.PrinterMode.ScreenResolution)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtPrintSupport'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def abort(self):
        'abort(self) -> bool'
        return bool
    
    def actualNumCopies(self):
        'actualNumCopies(self) -> int'
        return int
    
    def collateCopies(self):
        'collateCopies(self) -> bool'
        return bool
    
    def colorMode(self):
        'colorMode(self) -> PySide2.QtPrintSupport.QPrinter.ColorMode'
        return PySide2.QtPrintSupport.QPrinter.ColorMode
    
    def copyCount(self):
        'copyCount(self) -> int'
        return int
    
    def creator(self):
        'creator(self) -> str'
        return str
    
    def devType(self):
        'devType(self) -> int'
        return int
    
    def docName(self):
        'docName(self) -> str'
        return str
    
    def doubleSidedPrinting(self):
        'doubleSidedPrinting(self) -> bool'
        return bool
    
    def duplex(self):
        'duplex(self) -> PySide2.QtPrintSupport.QPrinter.DuplexMode'
        return PySide2.QtPrintSupport.QPrinter.DuplexMode
    
    def fontEmbeddingEnabled(self):
        'fontEmbeddingEnabled(self) -> bool'
        return bool
    
    def fromPage(self):
        'fromPage(self) -> int'
        return int
    
    def fullPage(self):
        'fullPage(self) -> bool'
        return bool
    
    def getPageMargins(self, unit):
        'getPageMargins(self, unit:PySide2.QtPrintSupport.QPrinter.Unit) -> typing.Tuple'
        return typing.Tuple
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def metric(self, arg__1):
        'metric(self, arg__1:PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int'
        return int
    
    def newPage(self):
        'newPage(self) -> bool'
        return bool
    
    def numCopies(self):
        'numCopies(self) -> int'
        return int
    
    def orientation(self):
        'orientation(self) -> PySide2.QtPrintSupport.QPrinter.Orientation'
        return PySide2.QtPrintSupport.QPrinter.Orientation
    
    def outputFileName(self):
        'outputFileName(self) -> str'
        return str
    
    def outputFormat(self):
        'outputFormat(self) -> PySide2.QtPrintSupport.QPrinter.OutputFormat'
        return PySide2.QtPrintSupport.QPrinter.OutputFormat
    
    def pageOrder(self):
        'pageOrder(self) -> PySide2.QtPrintSupport.QPrinter.PageOrder'
        return PySide2.QtPrintSupport.QPrinter.PageOrder
    
    def pageRect(self, arg__1: PySide2.QtPrintSupport.QPrinter.Unit):
        'pageRect(self) -> PySide2.QtCore.QRect\npageRect(self, arg__1:PySide2.QtPrintSupport.QPrinter.Unit) -> PySide2.QtCore.QRectF'
        pass
    
    def pageSize(self):
        'pageSize(self) -> PySide2.QtGui.QPagedPaintDevice.PageSize'
        return PySide2.QtGui.QPagedPaintDevice.PageSize
    
    def paintEngine(self):
        'paintEngine(self) -> PySide2.QtGui.QPaintEngine'
        return PySide2.QtGui.QPaintEngine
    
    def paperName(self):
        'paperName(self) -> str'
        return str
    
    def paperRect(self, arg__1: PySide2.QtPrintSupport.QPrinter.Unit):
        'paperRect(self) -> PySide2.QtCore.QRect\npaperRect(self, arg__1:PySide2.QtPrintSupport.QPrinter.Unit) -> PySide2.QtCore.QRectF'
        pass
    
    def paperSize(self, unit: PySide2.QtPrintSupport.QPrinter.Unit):
        'paperSize(self) -> PySide2.QtGui.QPagedPaintDevice.PageSize\npaperSize(self, unit:PySide2.QtPrintSupport.QPrinter.Unit) -> PySide2.QtCore.QSizeF'
        pass
    
    def paperSource(self):
        'paperSource(self) -> PySide2.QtPrintSupport.QPrinter.PaperSource'
        return PySide2.QtPrintSupport.QPrinter.PaperSource
    
    def pdfVersion(self):
        'pdfVersion(self) -> PySide2.QtGui.QPagedPaintDevice.PdfVersion'
        return PySide2.QtGui.QPagedPaintDevice.PdfVersion
    
    def printEngine(self):
        'printEngine(self) -> PySide2.QtPrintSupport.QPrintEngine'
        return PySide2.QtPrintSupport.QPrintEngine
    
    def printProgram(self):
        'printProgram(self) -> str'
        return str
    
    def printRange(self):
        'printRange(self) -> PySide2.QtPrintSupport.QPrinter.PrintRange'
        return PySide2.QtPrintSupport.QPrinter.PrintRange
    
    def printerName(self):
        'printerName(self) -> str'
        return str
    
    def printerState(self):
        'printerState(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState'
        return PySide2.QtPrintSupport.QPrinter.PrinterState
    
    def resolution(self):
        'resolution(self) -> int'
        return int
    
    def setCollateCopies(self, collate):
        'setCollateCopies(self, collate:bool)'
        pass
    
    def setColorMode(self, arg__1):
        'setColorMode(self, arg__1:PySide2.QtPrintSupport.QPrinter.ColorMode)'
        pass
    
    def setCopyCount(self, arg__1):
        'setCopyCount(self, arg__1:int)'
        pass
    
    def setCreator(self, arg__1):
        'setCreator(self, arg__1:str)'
        pass
    
    def setDocName(self, arg__1):
        'setDocName(self, arg__1:str)'
        pass
    
    def setDoubleSidedPrinting(self, enable):
        'setDoubleSidedPrinting(self, enable:bool)'
        pass
    
    def setDuplex(self, duplex):
        'setDuplex(self, duplex:PySide2.QtPrintSupport.QPrinter.DuplexMode)'
        pass
    
    def setEngines(self, printEngine, paintEngine):
        'setEngines(self, printEngine:PySide2.QtPrintSupport.QPrintEngine, paintEngine:PySide2.QtGui.QPaintEngine)'
        pass
    
    def setFontEmbeddingEnabled(self, enable):
        'setFontEmbeddingEnabled(self, enable:bool)'
        pass
    
    def setFromTo(self, fromPage, toPage):
        'setFromTo(self, fromPage:int, toPage:int)'
        pass
    
    def setFullPage(self, arg__1):
        'setFullPage(self, arg__1:bool)'
        pass
    
    def setMargins(self, m):
        'setMargins(self, m:PySide2.QtGui.QPagedPaintDevice.Margins)'
        pass
    
    def setNumCopies(self, arg__1):
        'setNumCopies(self, arg__1:int)'
        pass
    
    def setOrientation(self, arg__1):
        'setOrientation(self, arg__1:PySide2.QtPrintSupport.QPrinter.Orientation)'
        pass
    
    def setOutputFileName(self, arg__1):
        'setOutputFileName(self, arg__1:str)'
        pass
    
    def setOutputFormat(self, format):
        'setOutputFormat(self, format:PySide2.QtPrintSupport.QPrinter.OutputFormat)'
        pass
    
    def setPageMargins(self, left: float, top: float, right: float, bottom: float, unit: PySide2.QtPrintSupport.QPrinter.Unit):
        'setPageMargins(self, left:float, top:float, right:float, bottom:float, unit:PySide2.QtPrintSupport.QPrinter.Unit)\nsetPageMargins(self, margins:PySide2.QtCore.QMarginsF) -> bool'
        pass
    
    def setPageOrder(self, arg__1):
        'setPageOrder(self, arg__1:PySide2.QtPrintSupport.QPrinter.PageOrder)'
        pass
    
    def setPageSize(self, arg__1: PySide2.QtGui.QPagedPaintDevice.PageSize):
        'setPageSize(self, arg__1:PySide2.QtGui.QPageSize) -> bool\nsetPageSize(self, arg__1:PySide2.QtGui.QPagedPaintDevice.PageSize)'
        return True
    
    def setPageSizeMM(self, size):
        'setPageSizeMM(self, size:PySide2.QtCore.QSizeF)'
        pass
    
    def setPaperName(self, paperName):
        'setPaperName(self, paperName:str)'
        pass
    
    def setPaperSize(self, paperSize: PySide2.QtCore.QSizeF, unit: PySide2.QtPrintSupport.QPrinter.Unit):
        'setPaperSize(self, arg__1:PySide2.QtGui.QPagedPaintDevice.PageSize)\nsetPaperSize(self, paperSize:PySide2.QtCore.QSizeF, unit:PySide2.QtPrintSupport.QPrinter.Unit)'
        pass
    
    def setPaperSource(self, arg__1):
        'setPaperSource(self, arg__1:PySide2.QtPrintSupport.QPrinter.PaperSource)'
        pass
    
    def setPdfVersion(self, version):
        'setPdfVersion(self, version:PySide2.QtGui.QPagedPaintDevice.PdfVersion)'
        pass
    
    def setPrintProgram(self, arg__1):
        'setPrintProgram(self, arg__1:str)'
        pass
    
    def setPrintRange(self, range):
        'setPrintRange(self, range:PySide2.QtPrintSupport.QPrinter.PrintRange)'
        pass
    
    def setPrinterName(self, arg__1):
        'setPrinterName(self, arg__1:str)'
        pass
    
    def setResolution(self, arg__1):
        'setResolution(self, arg__1:int)'
        pass
    
    def setWinPageSize(self, winPageSize):
        'setWinPageSize(self, winPageSize:int)'
        pass
    
    def supportedResolutions(self):
        'supportedResolutions(self) -> typing.List'
        return typing.List
    
    def supportsMultipleCopies(self):
        'supportsMultipleCopies(self) -> bool'
        return bool
    
    def toPage(self):
        'toPage(self) -> int'
        return int
    
    def winPageSize(self):
        'winPageSize(self) -> int'
        return int
    

class QPrinterInfo(_mod_Shiboken.Object):
    'QPrinterInfo(self)\nQPrinterInfo(self, other:PySide2.QtPrintSupport.QPrinterInfo)\nQPrinterInfo(self, printer:PySide2.QtPrintSupport.QPrinter)'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QPrinterInfo
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, other: PySide2.QtPrintSupport.QPrinterInfo):
        'QPrinterInfo(self)\nQPrinterInfo(self, other:PySide2.QtPrintSupport.QPrinterInfo)\nQPrinterInfo(self, printer:PySide2.QtPrintSupport.QPrinter)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtPrintSupport'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def availablePrinterNames(cls):
        'availablePrinterNames() -> typing.List'
        return typing.List
    
    @classmethod
    def availablePrinters(cls):
        'availablePrinters() -> typing.List'
        return typing.List
    
    def defaultColorMode(self):
        'defaultColorMode(self) -> PySide2.QtPrintSupport.QPrinter.ColorMode'
        return PySide2.QtPrintSupport.QPrinter.ColorMode
    
    def defaultDuplexMode(self):
        'defaultDuplexMode(self) -> PySide2.QtPrintSupport.QPrinter.DuplexMode'
        return PySide2.QtPrintSupport.QPrinter.DuplexMode
    
    def defaultPageSize(self):
        'defaultPageSize(self) -> PySide2.QtGui.QPageSize'
        return PySide2.QtGui.QPageSize
    
    @classmethod
    def defaultPrinter(cls):
        'defaultPrinter() -> PySide2.QtPrintSupport.QPrinterInfo'
        return PySide2.QtPrintSupport.QPrinterInfo
    
    @classmethod
    def defaultPrinterName(cls):
        'defaultPrinterName() -> str'
        return str
    
    def description(self):
        'description(self) -> str'
        return str
    
    def isDefault(self):
        'isDefault(self) -> bool'
        return bool
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def isRemote(self):
        'isRemote(self) -> bool'
        return bool
    
    def location(self):
        'location(self) -> str'
        return str
    
    def makeAndModel(self):
        'makeAndModel(self) -> str'
        return str
    
    def maximumPhysicalPageSize(self):
        'maximumPhysicalPageSize(self) -> PySide2.QtGui.QPageSize'
        return PySide2.QtGui.QPageSize
    
    def minimumPhysicalPageSize(self):
        'minimumPhysicalPageSize(self) -> PySide2.QtGui.QPageSize'
        return PySide2.QtGui.QPageSize
    
    @classmethod
    def printerInfo(cls, printerName):
        'printerInfo(printerName:str) -> PySide2.QtPrintSupport.QPrinterInfo'
        return PySide2.QtPrintSupport.QPrinterInfo
    
    def printerName(self):
        'printerName(self) -> str'
        return str
    
    def state(self):
        'state(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState'
        return PySide2.QtPrintSupport.QPrinter.PrinterState
    
    def supportedColorModes(self):
        'supportedColorModes(self) -> typing.List'
        return typing.List
    
    def supportedDuplexModes(self):
        'supportedDuplexModes(self) -> typing.List'
        return typing.List
    
    def supportedPageSizes(self):
        'supportedPageSizes(self) -> typing.List'
        return typing.List
    
    def supportedPaperSizes(self):
        'supportedPaperSizes(self) -> typing.List'
        return typing.List
    
    def supportedResolutions(self):
        'supportedResolutions(self) -> typing.List'
        return typing.List
    
    def supportedSizesWithNames(self):
        'supportedSizesWithNames(self) -> typing.List'
        return typing.List
    
    def supportsCustomPageSizes(self):
        'supportsCustomPageSizes(self) -> bool'
        return bool
    

__doc__ = None
__file__ = '/Users/shuike/anaconda3/envs/py36QT/lib/python3.6/site-packages/PySide2/QtPrintSupport.abi3.so'
__name__ = 'PySide2.QtPrintSupport'
__package__ = 'PySide2'
