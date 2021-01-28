import PySide2.QtCore as _mod_PySide2_QtCore
import Shiboken as _mod_Shiboken

class QAbstractOpenGLFunctions(_mod_Shiboken.Object):
    'QAbstractOpenGLFunctions(self)'
    __class__ = QAbstractOpenGLFunctions
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QAbstractOpenGLFunctions(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def initializeOpenGLFunctions(self):
        'initializeOpenGLFunctions(self) -> bool'
        return bool
    
    def isInitialized(self):
        'isInitialized(self) -> bool'
        return bool
    
    def owningContext(self):
        'owningContext(self) -> PySide2.QtGui.QOpenGLContext'
        return PySide2.QtGui.QOpenGLContext
    
    def setOwningContext(self, context):
        'setOwningContext(self, context:PySide2.QtGui.QOpenGLContext)'
        pass
    

class QAbstractTextDocumentLayout(_mod_PySide2_QtCore.QObject):
    'QAbstractTextDocumentLayout(self, doc:PySide2.QtGui.QTextDocument)'
    PaintContext = PaintContext
    Selection = Selection
    __class__ = QAbstractTextDocumentLayout
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, doc: PySide2.QtGui.QTextDocument):
        'QAbstractTextDocumentLayout(self, doc:PySide2.QtGui.QTextDocument)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def anchorAt(self, pos):
        'anchorAt(self, pos:PySide2.QtCore.QPointF) -> str'
        return str
    
    def blockBoundingRect(self, block):
        'blockBoundingRect(self, block:PySide2.QtGui.QTextBlock) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def blockWithMarkerAt(self, pos):
        'blockWithMarkerAt(self, pos:PySide2.QtCore.QPointF) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def document(self):
        'document(self) -> PySide2.QtGui.QTextDocument'
        return PySide2.QtGui.QTextDocument
    
    def documentChanged(self, from_, charsRemoved, charsAdded):
        'documentChanged(self, from_:int, charsRemoved:int, charsAdded:int)'
        pass
    
    def documentSize(self):
        'documentSize(self) -> PySide2.QtCore.QSizeF'
        return PySide2.QtCore.QSizeF
    
    def documentSizeChanged(self):
        pass
    
    def draw(self, painter, context):
        'draw(self, painter:PySide2.QtGui.QPainter, context:PySide2.QtGui.QAbstractTextDocumentLayout.PaintContext)'
        pass
    
    def drawInlineObject(self, painter, rect, object, posInDocument, format):
        'drawInlineObject(self, painter:PySide2.QtGui.QPainter, rect:PySide2.QtCore.QRectF, object:PySide2.QtGui.QTextInlineObject, posInDocument:int, format:PySide2.QtGui.QTextFormat)'
        pass
    
    def format(self, pos):
        'format(self, pos:int) -> PySide2.QtGui.QTextCharFormat'
        return PySide2.QtGui.QTextCharFormat
    
    def formatAt(self, pos):
        'formatAt(self, pos:PySide2.QtCore.QPointF) -> PySide2.QtGui.QTextFormat'
        return PySide2.QtGui.QTextFormat
    
    def formatIndex(self, pos):
        'formatIndex(self, pos:int) -> int'
        return int
    
    def frameBoundingRect(self, frame):
        'frameBoundingRect(self, frame:PySide2.QtGui.QTextFrame) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def handlerForObject(self, objectType):
        'handlerForObject(self, objectType:int) -> PySide2.QtGui.QTextObjectInterface'
        return PySide2.QtGui.QTextObjectInterface
    
    def hitTest(self, point, accuracy):
        'hitTest(self, point:PySide2.QtCore.QPointF, accuracy:PySide2.QtCore.Qt.HitTestAccuracy) -> int'
        return int
    
    def imageAt(self, pos):
        'imageAt(self, pos:PySide2.QtCore.QPointF) -> str'
        return str
    
    def pageCount(self):
        'pageCount(self) -> int'
        return int
    
    def pageCountChanged(self):
        pass
    
    def paintDevice(self):
        'paintDevice(self) -> PySide2.QtGui.QPaintDevice'
        return PySide2.QtGui.QPaintDevice
    
    def positionInlineObject(self, item, posInDocument, format):
        'positionInlineObject(self, item:PySide2.QtGui.QTextInlineObject, posInDocument:int, format:PySide2.QtGui.QTextFormat)'
        pass
    
    def registerHandler(self, objectType, component):
        'registerHandler(self, objectType:int, component:PySide2.QtCore.QObject)'
        pass
    
    def resizeInlineObject(self, item, posInDocument, format):
        'resizeInlineObject(self, item:PySide2.QtGui.QTextInlineObject, posInDocument:int, format:PySide2.QtGui.QTextFormat)'
        pass
    
    def setPaintDevice(self, device):
        'setPaintDevice(self, device:PySide2.QtGui.QPaintDevice)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def unregisterHandler(self, objectType, component):
        'unregisterHandler(self, objectType:int, component:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    def update(self):
        pass
    
    def updateBlock(self):
        pass
    

class QAccessible(_mod_Shiboken.Object):
    Accelerator = Text()
    AcceleratorChanged = Event()
    ActionChanged = Event()
    ActionInterface = InterfaceType()
    ActiveDescendantChanged = Event()
    Alert = Event()
    AlertMessage = Role()
    AllRelations = RelationFlag()
    Animation = Role()
    Application = Role()
    Assistant = Role()
    AttributeChanged = Event()
    Border = Role()
    Button = Role()
    ButtonDropDown = Role()
    ButtonDropGrid = Role()
    ButtonMenu = Role()
    Canvas = Role()
    Caret = Role()
    Cell = Role()
    CharBoundary = TextBoundaryType()
    Chart = Role()
    CheckBox = Role()
    Client = Role()
    Clock = Role()
    ColorChooser = Role()
    Column = Role()
    ColumnHeader = Role()
    ComboBox = Role()
    ComplementaryContent = Role()
    ContextHelpEnd = Event()
    ContextHelpStart = Event()
    Controlled = RelationFlag()
    Controller = RelationFlag()
    Cursor = Role()
    DebugDescription = Text()
    DefaultActionChanged = Event()
    Description = Text()
    DescriptionChanged = Event()
    Desktop = Role()
    Dial = Role()
    Dialog = Role()
    DialogEnd = Event()
    DialogStart = Event()
    Document = Role()
    DocumentContentChanged = Event()
    DocumentLoadComplete = Event()
    DocumentLoadStopped = Event()
    DocumentReload = Event()
    DragDropEnd = Event()
    DragDropStart = Event()
    EditableText = Role()
    EditableTextInterface = InterfaceType()
    Equation = Role()
    Event = Event
    Focus = Event()
    Footer = Role()
    ForegroundChanged = Event()
    Form = Role()
    Graphic = Role()
    Grip = Role()
    Grouping = Role()
    Heading = Role()
    Help = Text()
    HelpBalloon = Role()
    HelpChanged = Event()
    HotkeyField = Role()
    HyperlinkEndIndexChanged = Event()
    HyperlinkNumberOfAnchorsChanged = Event()
    HyperlinkSelectedLinkChanged = Event()
    HyperlinkStartIndexChanged = Event()
    HypertextChanged = Event()
    HypertextLinkActivated = Event()
    HypertextLinkSelected = Event()
    HypertextNLinksChanged = Event()
    ImageInterface = InterfaceType()
    Indicator = Role()
    InterfaceType = InterfaceType
    InvalidEvent = Event()
    Label = RelationFlag()
    Labelled = RelationFlag()
    LayeredPane = Role()
    LineBoundary = TextBoundaryType()
    Link = Role()
    List = Role()
    ListItem = Role()
    LocationChanged = Event()
    MenuBar = Role()
    MenuCommand = Event()
    MenuEnd = Event()
    MenuItem = Role()
    MenuStart = Event()
    Name = Text()
    NameChanged = Event()
    NoBoundary = TextBoundaryType()
    NoRole = Role()
    Note = Role()
    Notification = Role()
    ObjectAttributeChanged = Event()
    ObjectCreated = Event()
    ObjectDestroyed = Event()
    ObjectHide = Event()
    ObjectReorder = Event()
    ObjectShow = Event()
    PageChanged = Event()
    PageTab = Role()
    PageTabList = Role()
    Pane = Role()
    Paragraph = Role()
    ParagraphBoundary = TextBoundaryType()
    ParentChanged = Event()
    PopupMenu = Role()
    PopupMenuEnd = Event()
    PopupMenuStart = Event()
    ProgressBar = Role()
    PropertyPage = Role()
    PushButton = Role()
    RadioButton = Role()
    Relation = Relation
    RelationFlag = RelationFlag
    Role = Role
    Row = Role()
    RowHeader = Role()
    ScrollBar = Role()
    ScrollingEnd = Event()
    ScrollingStart = Event()
    Section = Role()
    SectionChanged = Event()
    Selection = Event()
    SelectionAdd = Event()
    SelectionRemove = Event()
    SelectionWithin = Event()
    SentenceBoundary = TextBoundaryType()
    Separator = Role()
    Slider = Role()
    Sound = Role()
    SoundPlayed = Event()
    SpinBox = Role()
    Splitter = Role()
    State = State
    StateChanged = Event()
    StaticText = Role()
    StatusBar = Role()
    Table = Role()
    TableCaptionChanged = Event()
    TableCellInterface = InterfaceType()
    TableColumnDescriptionChanged = Event()
    TableColumnHeaderChanged = Event()
    TableInterface = InterfaceType()
    TableModelChanged = Event()
    TableRowDescriptionChanged = Event()
    TableRowHeaderChanged = Event()
    TableSummaryChanged = Event()
    Terminal = Role()
    Text = Text
    TextAttributeChanged = Event()
    TextBoundaryType = TextBoundaryType
    TextCaretMoved = Event()
    TextColumnChanged = Event()
    TextInserted = Event()
    TextInterface = InterfaceType()
    TextRemoved = Event()
    TextSelectionChanged = Event()
    TextUpdated = Event()
    TitleBar = Role()
    ToolBar = Role()
    ToolTip = Role()
    Tree = Role()
    TreeItem = Role()
    UserRole = Role()
    UserText = Text()
    Value = Text()
    ValueChanged = Event()
    ValueInterface = InterfaceType()
    VisibleDataChanged = Event()
    WebDocument = Role()
    Whitespace = Role()
    Window = Role()
    WordBoundary = TextBoundaryType()
    __class__ = QAccessible
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def accessibleInterface(cls, uniqueId):
        'accessibleInterface(uniqueId:int) -> PySide2.QtGui.QAccessibleInterface'
        return PySide2.QtGui.QAccessibleInterface
    
    @classmethod
    def cleanup(cls):
        'cleanup()'
        pass
    
    @classmethod
    def deleteAccessibleInterface(cls, uniqueId):
        'deleteAccessibleInterface(uniqueId:int)'
        pass
    
    @classmethod
    def isActive(cls):
        'isActive() -> bool'
        return bool
    
    @classmethod
    def qAccessibleTextBoundaryHelper(cls, cursor, boundaryType):
        'qAccessibleTextBoundaryHelper(cursor:PySide2.QtGui.QTextCursor, boundaryType:PySide2.QtGui.QAccessible.TextBoundaryType) -> typing.Tuple'
        return typing.Tuple
    
    @classmethod
    def queryAccessibleInterface(cls, arg__1):
        'queryAccessibleInterface(arg__1:PySide2.QtCore.QObject) -> PySide2.QtGui.QAccessibleInterface'
        return PySide2.QtGui.QAccessibleInterface
    
    @classmethod
    def registerAccessibleInterface(cls, iface):
        'registerAccessibleInterface(iface:PySide2.QtGui.QAccessibleInterface) -> int'
        return int
    
    @classmethod
    def setActive(cls, active):
        'setActive(active:bool)'
        pass
    
    @classmethod
    def setRootObject(cls, object):
        'setRootObject(object:PySide2.QtCore.QObject)'
        pass
    
    @classmethod
    def uniqueId(cls, iface):
        'uniqueId(iface:PySide2.QtGui.QAccessibleInterface) -> int'
        return int
    
    @classmethod
    def updateAccessibility(cls, event):
        'updateAccessibility(event:PySide2.QtGui.QAccessibleEvent)'
        pass
    

class QAccessibleEditableTextInterface(_mod_Shiboken.Object):
    'QAccessibleEditableTextInterface(self)'
    __class__ = QAccessibleEditableTextInterface
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QAccessibleEditableTextInterface(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def deleteText(self, startOffset, endOffset):
        'deleteText(self, startOffset:int, endOffset:int)'
        pass
    
    def insertText(self, offset, text):
        'insertText(self, offset:int, text:str)'
        pass
    
    def replaceText(self, startOffset, endOffset, text):
        'replaceText(self, startOffset:int, endOffset:int, text:str)'
        pass
    

class QAccessibleEvent(_mod_Shiboken.Object):
    'QAccessibleEvent(self, iface:PySide2.QtGui.QAccessibleInterface, typ:PySide2.QtGui.QAccessible.Event)\nQAccessibleEvent(self, obj:PySide2.QtCore.QObject, typ:PySide2.QtGui.QAccessible.Event)'
    __class__ = QAccessibleEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, iface: PySide2.QtGui.QAccessibleInterface, typ: PySide2.QtGui.QAccessible.Event):
        'QAccessibleEvent(self, iface:PySide2.QtGui.QAccessibleInterface, typ:PySide2.QtGui.QAccessible.Event)\nQAccessibleEvent(self, obj:PySide2.QtCore.QObject, typ:PySide2.QtGui.QAccessible.Event)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def accessibleInterface(self):
        'accessibleInterface(self) -> PySide2.QtGui.QAccessibleInterface'
        return PySide2.QtGui.QAccessibleInterface
    
    def child(self):
        'child(self) -> int'
        return int
    
    def object(self):
        'object(self) -> PySide2.QtCore.QObject'
        return PySide2.QtCore.QObject
    
    def setChild(self, chld):
        'setChild(self, chld:int)'
        pass
    
    def type(self):
        'type(self) -> PySide2.QtGui.QAccessible.Event'
        return PySide2.QtGui.QAccessible.Event
    
    def uniqueId(self):
        'uniqueId(self) -> int'
        return int
    

class QAccessibleInterface(_mod_Shiboken.Object):
    'QAccessibleInterface(self)'
    __class__ = QAccessibleInterface
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QAccessibleInterface(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def backgroundColor(self):
        'backgroundColor(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def child(self, index):
        'child(self, index:int) -> PySide2.QtGui.QAccessibleInterface'
        return PySide2.QtGui.QAccessibleInterface
    
    def childAt(self, x, y):
        'childAt(self, x:int, y:int) -> PySide2.QtGui.QAccessibleInterface'
        return PySide2.QtGui.QAccessibleInterface
    
    def childCount(self):
        'childCount(self) -> int'
        return int
    
    def editableTextInterface(self):
        'editableTextInterface(self) -> PySide2.QtGui.QAccessibleEditableTextInterface'
        return PySide2.QtGui.QAccessibleEditableTextInterface
    
    def focusChild(self):
        'focusChild(self) -> PySide2.QtGui.QAccessibleInterface'
        return PySide2.QtGui.QAccessibleInterface
    
    def foregroundColor(self):
        'foregroundColor(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def indexOfChild(self, arg__1):
        'indexOfChild(self, arg__1:PySide2.QtGui.QAccessibleInterface) -> int'
        return int
    
    def interface_cast(self, arg__1):
        'interface_cast(self, arg__1:PySide2.QtGui.QAccessible.InterfaceType) -> int'
        return int
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def object(self):
        'object(self) -> PySide2.QtCore.QObject'
        return PySide2.QtCore.QObject
    
    def parent(self):
        'parent(self) -> PySide2.QtGui.QAccessibleInterface'
        return PySide2.QtGui.QAccessibleInterface
    
    def rect(self):
        'rect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def relations(self, match):
        'relations(self, match:PySide2.QtGui.QAccessible.Relation=PySide2.QtGui.QAccessible.RelationFlag.AllRelations) -> typing.List'
        return typing.List
    
    def role(self):
        'role(self) -> PySide2.QtGui.QAccessible.Role'
        return PySide2.QtGui.QAccessible.Role
    
    def setText(self, t, text):
        'setText(self, t:PySide2.QtGui.QAccessible.Text, text:str)'
        pass
    
    def state(self):
        'state(self) -> PySide2.QtGui.QAccessible.State'
        return PySide2.QtGui.QAccessible.State
    
    def tableCellInterface(self):
        'tableCellInterface(self) -> PySide2.QtGui.QAccessibleTableCellInterface'
        return PySide2.QtGui.QAccessibleTableCellInterface
    
    def text(self, t):
        'text(self, t:PySide2.QtGui.QAccessible.Text) -> str'
        return str
    
    def textInterface(self):
        'textInterface(self) -> PySide2.QtGui.QAccessibleTextInterface'
        return PySide2.QtGui.QAccessibleTextInterface
    
    def valueInterface(self):
        'valueInterface(self) -> PySide2.QtGui.QAccessibleValueInterface'
        return PySide2.QtGui.QAccessibleValueInterface
    
    def virtual_hook(self, id, data):
        'virtual_hook(self, id:int, data:int)'
        pass
    
    def window(self):
        'window(self) -> PySide2.QtGui.QWindow'
        return PySide2.QtGui.QWindow
    

class QAccessibleObject(QAccessibleInterface):
    'QAccessibleObject(self, object:PySide2.QtCore.QObject)'
    __class__ = QAccessibleObject
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, object: PySide2.QtCore.QObject):
        'QAccessibleObject(self, object:PySide2.QtCore.QObject)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def childAt(self, x, y):
        'childAt(self, x:int, y:int) -> PySide2.QtGui.QAccessibleInterface'
        return PySide2.QtGui.QAccessibleInterface
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def object(self):
        'object(self) -> PySide2.QtCore.QObject'
        return PySide2.QtCore.QObject
    
    def rect(self):
        'rect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def setText(self, t, text):
        'setText(self, t:PySide2.QtGui.QAccessible.Text, text:str)'
        pass
    

class QAccessibleStateChangeEvent(QAccessibleEvent):
    'QAccessibleStateChangeEvent(self, iface:PySide2.QtGui.QAccessibleInterface, state:PySide2.QtGui.QAccessible.State)\nQAccessibleStateChangeEvent(self, obj:PySide2.QtCore.QObject, state:PySide2.QtGui.QAccessible.State)'
    __class__ = QAccessibleStateChangeEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, iface: PySide2.QtGui.QAccessibleInterface, state: PySide2.QtGui.QAccessible.State):
        'QAccessibleStateChangeEvent(self, iface:PySide2.QtGui.QAccessibleInterface, state:PySide2.QtGui.QAccessible.State)\nQAccessibleStateChangeEvent(self, obj:PySide2.QtCore.QObject, state:PySide2.QtGui.QAccessible.State)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def changedStates(self):
        'changedStates(self) -> PySide2.QtGui.QAccessible.State'
        return PySide2.QtGui.QAccessible.State
    

class QAccessibleTableCellInterface(_mod_Shiboken.Object):
    'QAccessibleTableCellInterface(self)'
    __class__ = QAccessibleTableCellInterface
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QAccessibleTableCellInterface(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def columnExtent(self):
        'columnExtent(self) -> int'
        return int
    
    def columnHeaderCells(self):
        'columnHeaderCells(self) -> typing.List'
        return typing.List
    
    def columnIndex(self):
        'columnIndex(self) -> int'
        return int
    
    def isSelected(self):
        'isSelected(self) -> bool'
        return bool
    
    def rowExtent(self):
        'rowExtent(self) -> int'
        return int
    
    def rowHeaderCells(self):
        'rowHeaderCells(self) -> typing.List'
        return typing.List
    
    def rowIndex(self):
        'rowIndex(self) -> int'
        return int
    
    def table(self):
        'table(self) -> PySide2.QtGui.QAccessibleInterface'
        return PySide2.QtGui.QAccessibleInterface
    

class QAccessibleTableModelChangeEvent(QAccessibleEvent):
    'QAccessibleTableModelChangeEvent(self, iface:PySide2.QtGui.QAccessibleInterface, changeType:PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType)\nQAccessibleTableModelChangeEvent(self, obj:PySide2.QtCore.QObject, changeType:PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType)'
    ColumnsInserted = ModelChangeType()
    ColumnsRemoved = ModelChangeType()
    DataChanged = ModelChangeType()
    ModelChangeType = ModelChangeType
    ModelReset = ModelChangeType()
    RowsInserted = ModelChangeType()
    RowsRemoved = ModelChangeType()
    __class__ = QAccessibleTableModelChangeEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, iface: PySide2.QtGui.QAccessibleInterface, changeType: PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType):
        'QAccessibleTableModelChangeEvent(self, iface:PySide2.QtGui.QAccessibleInterface, changeType:PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType)\nQAccessibleTableModelChangeEvent(self, obj:PySide2.QtCore.QObject, changeType:PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def firstColumn(self):
        'firstColumn(self) -> int'
        return int
    
    def firstRow(self):
        'firstRow(self) -> int'
        return int
    
    def lastColumn(self):
        'lastColumn(self) -> int'
        return int
    
    def lastRow(self):
        'lastRow(self) -> int'
        return int
    
    def modelChangeType(self):
        'modelChangeType(self) -> PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType'
        return PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType
    
    def setFirstColumn(self, col):
        'setFirstColumn(self, col:int)'
        pass
    
    def setFirstRow(self, row):
        'setFirstRow(self, row:int)'
        pass
    
    def setLastColumn(self, col):
        'setLastColumn(self, col:int)'
        pass
    
    def setLastRow(self, row):
        'setLastRow(self, row:int)'
        pass
    
    def setModelChangeType(self, changeType):
        'setModelChangeType(self, changeType:PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType)'
        pass
    

class QAccessibleTextCursorEvent(QAccessibleEvent):
    'QAccessibleTextCursorEvent(self, iface:PySide2.QtGui.QAccessibleInterface, cursorPos:int)\nQAccessibleTextCursorEvent(self, obj:PySide2.QtCore.QObject, cursorPos:int)'
    __class__ = QAccessibleTextCursorEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, iface: PySide2.QtGui.QAccessibleInterface, cursorPos: int):
        'QAccessibleTextCursorEvent(self, iface:PySide2.QtGui.QAccessibleInterface, cursorPos:int)\nQAccessibleTextCursorEvent(self, obj:PySide2.QtCore.QObject, cursorPos:int)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def cursorPosition(self):
        'cursorPosition(self) -> int'
        return int
    
    def setCursorPosition(self, position):
        'setCursorPosition(self, position:int)'
        pass
    

class QAccessibleTextInsertEvent(QAccessibleTextCursorEvent):
    'QAccessibleTextInsertEvent(self, iface:PySide2.QtGui.QAccessibleInterface, position:int, text:str)\nQAccessibleTextInsertEvent(self, obj:PySide2.QtCore.QObject, position:int, text:str)'
    __class__ = QAccessibleTextInsertEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, iface: PySide2.QtGui.QAccessibleInterface, position: int, text: str):
        'QAccessibleTextInsertEvent(self, iface:PySide2.QtGui.QAccessibleInterface, position:int, text:str)\nQAccessibleTextInsertEvent(self, obj:PySide2.QtCore.QObject, position:int, text:str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def changePosition(self):
        'changePosition(self) -> int'
        return int
    
    def textInserted(self):
        'textInserted(self) -> str'
        return str
    

class QAccessibleTextInterface(_mod_Shiboken.Object):
    'QAccessibleTextInterface(self)'
    __class__ = QAccessibleTextInterface
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QAccessibleTextInterface(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addSelection(self, startOffset, endOffset):
        'addSelection(self, startOffset:int, endOffset:int)'
        pass
    
    def attributes(self, offset):
        'attributes(self, offset:int) -> typing.Tuple'
        return typing.Tuple
    
    def characterCount(self):
        'characterCount(self) -> int'
        return int
    
    def characterRect(self, offset):
        'characterRect(self, offset:int) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def cursorPosition(self):
        'cursorPosition(self) -> int'
        return int
    
    def offsetAtPoint(self, point):
        'offsetAtPoint(self, point:PySide2.QtCore.QPoint) -> int'
        return int
    
    def removeSelection(self, selectionIndex):
        'removeSelection(self, selectionIndex:int)'
        pass
    
    def scrollToSubstring(self, startIndex, endIndex):
        'scrollToSubstring(self, startIndex:int, endIndex:int)'
        pass
    
    def selection(self, selectionIndex):
        'selection(self, selectionIndex:int) -> typing.Tuple'
        return typing.Tuple
    
    def selectionCount(self):
        'selectionCount(self) -> int'
        return int
    
    def setCursorPosition(self, position):
        'setCursorPosition(self, position:int)'
        pass
    
    def setSelection(self, selectionIndex, startOffset, endOffset):
        'setSelection(self, selectionIndex:int, startOffset:int, endOffset:int)'
        pass
    
    def text(self, startOffset, endOffset):
        'text(self, startOffset:int, endOffset:int) -> str'
        return str
    
    def textAfterOffset(self, offset, boundaryType):
        'textAfterOffset(self, offset:int, boundaryType:PySide2.QtGui.QAccessible.TextBoundaryType) -> typing.Tuple'
        return typing.Tuple
    
    def textAtOffset(self, offset, boundaryType):
        'textAtOffset(self, offset:int, boundaryType:PySide2.QtGui.QAccessible.TextBoundaryType) -> typing.Tuple'
        return typing.Tuple
    
    def textBeforeOffset(self, offset, boundaryType):
        'textBeforeOffset(self, offset:int, boundaryType:PySide2.QtGui.QAccessible.TextBoundaryType) -> typing.Tuple'
        return typing.Tuple
    

class QAccessibleTextRemoveEvent(QAccessibleTextCursorEvent):
    'QAccessibleTextRemoveEvent(self, iface:PySide2.QtGui.QAccessibleInterface, position:int, text:str)\nQAccessibleTextRemoveEvent(self, obj:PySide2.QtCore.QObject, position:int, text:str)'
    __class__ = QAccessibleTextRemoveEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, iface: PySide2.QtGui.QAccessibleInterface, position: int, text: str):
        'QAccessibleTextRemoveEvent(self, iface:PySide2.QtGui.QAccessibleInterface, position:int, text:str)\nQAccessibleTextRemoveEvent(self, obj:PySide2.QtCore.QObject, position:int, text:str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def changePosition(self):
        'changePosition(self) -> int'
        return int
    
    def textRemoved(self):
        'textRemoved(self) -> str'
        return str
    

class QAccessibleTextSelectionEvent(QAccessibleTextCursorEvent):
    'QAccessibleTextSelectionEvent(self, iface:PySide2.QtGui.QAccessibleInterface, start:int, end:int)\nQAccessibleTextSelectionEvent(self, obj:PySide2.QtCore.QObject, start:int, end:int)'
    __class__ = QAccessibleTextSelectionEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, iface: PySide2.QtGui.QAccessibleInterface, start: int, end: int):
        'QAccessibleTextSelectionEvent(self, iface:PySide2.QtGui.QAccessibleInterface, start:int, end:int)\nQAccessibleTextSelectionEvent(self, obj:PySide2.QtCore.QObject, start:int, end:int)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def selectionEnd(self):
        'selectionEnd(self) -> int'
        return int
    
    def selectionStart(self):
        'selectionStart(self) -> int'
        return int
    
    def setSelection(self, start, end):
        'setSelection(self, start:int, end:int)'
        pass
    

class QAccessibleTextUpdateEvent(QAccessibleTextCursorEvent):
    'QAccessibleTextUpdateEvent(self, iface:PySide2.QtGui.QAccessibleInterface, position:int, oldText:str, text:str)\nQAccessibleTextUpdateEvent(self, obj:PySide2.QtCore.QObject, position:int, oldText:str, text:str)'
    __class__ = QAccessibleTextUpdateEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, iface: PySide2.QtGui.QAccessibleInterface, position: int, oldText: str, text: str):
        'QAccessibleTextUpdateEvent(self, iface:PySide2.QtGui.QAccessibleInterface, position:int, oldText:str, text:str)\nQAccessibleTextUpdateEvent(self, obj:PySide2.QtCore.QObject, position:int, oldText:str, text:str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def changePosition(self):
        'changePosition(self) -> int'
        return int
    
    def textInserted(self):
        'textInserted(self) -> str'
        return str
    
    def textRemoved(self):
        'textRemoved(self) -> str'
        return str
    

class QAccessibleValueChangeEvent(QAccessibleEvent):
    'QAccessibleValueChangeEvent(self, iface:PySide2.QtGui.QAccessibleInterface, val:typing.Any)\nQAccessibleValueChangeEvent(self, obj:PySide2.QtCore.QObject, val:typing.Any)'
    __class__ = QAccessibleValueChangeEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, iface: PySide2.QtGui.QAccessibleInterface, val: typing.Any):
        'QAccessibleValueChangeEvent(self, iface:PySide2.QtGui.QAccessibleInterface, val:typing.Any)\nQAccessibleValueChangeEvent(self, obj:PySide2.QtCore.QObject, val:typing.Any)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def setValue(self, val):
        'setValue(self, val:typing.Any)'
        pass
    
    def value(self):
        'value(self) -> typing.Any'
        return typing.Any
    

class QAccessibleValueInterface(_mod_Shiboken.Object):
    'QAccessibleValueInterface(self)'
    __class__ = QAccessibleValueInterface
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QAccessibleValueInterface(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def currentValue(self):
        'currentValue(self) -> typing.Any'
        return typing.Any
    
    def maximumValue(self):
        'maximumValue(self) -> typing.Any'
        return typing.Any
    
    def minimumStepSize(self):
        'minimumStepSize(self) -> typing.Any'
        return typing.Any
    
    def minimumValue(self):
        'minimumValue(self) -> typing.Any'
        return typing.Any
    
    def setCurrentValue(self, value):
        'setCurrentValue(self, value:typing.Any)'
        pass
    

class QActionEvent(_mod_PySide2_QtCore.QEvent):
    __class__ = QActionEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class QBackingStore(_mod_Shiboken.Object):
    'QBackingStore(self, window:PySide2.QtGui.QWindow)'
    __class__ = QBackingStore
    __dict__ = {}
    def __init__(self, window: PySide2.QtGui.QWindow):
        'QBackingStore(self, window:PySide2.QtGui.QWindow)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def beginPaint(self, arg__1):
        'beginPaint(self, arg__1:PySide2.QtGui.QRegion)'
        pass
    
    def endPaint(self):
        'endPaint(self)'
        pass
    
    def flush(self, region, window, offset):
        'flush(self, region:PySide2.QtGui.QRegion, window:typing.Union[PySide2.QtGui.QWindow, NoneType]=None, offset:PySide2.QtCore.QPoint=Default(QPoint))'
        pass
    
    def hasStaticContents(self):
        'hasStaticContents(self) -> bool'
        return bool
    
    def paintDevice(self):
        'paintDevice(self) -> PySide2.QtGui.QPaintDevice'
        return PySide2.QtGui.QPaintDevice
    
    def resize(self, size):
        'resize(self, size:PySide2.QtCore.QSize)'
        pass
    
    def scroll(self, area, dx, dy):
        'scroll(self, area:PySide2.QtGui.QRegion, dx:int, dy:int) -> bool'
        return bool
    
    def setStaticContents(self, region):
        'setStaticContents(self, region:PySide2.QtGui.QRegion)'
        pass
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def staticContents(self):
        'staticContents(self) -> PySide2.QtGui.QRegion'
        return PySide2.QtGui.QRegion
    
    def window(self):
        'window(self) -> PySide2.QtGui.QWindow'
        return PySide2.QtGui.QWindow
    

class QBitmap(QPixmap):
    'QBitmap(self)\nQBitmap(self, arg__1:PySide2.QtCore.QSize)\nQBitmap(self, arg__1:PySide2.QtGui.QPixmap)\nQBitmap(self, fileName:str, format:typing.Union[bytes, NoneType]=None)\nQBitmap(self, other:PySide2.QtGui.QBitmap)\nQBitmap(self, w:int, h:int)'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QBitmap
    def __copy__(self):
        '__copy__()'
        pass
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, fileName: str, format: typing.Union[bytes,NoneType]=None):
        'QBitmap(self)\nQBitmap(self, arg__1:PySide2.QtCore.QSize)\nQBitmap(self, arg__1:PySide2.QtGui.QPixmap)\nQBitmap(self, fileName:str, format:typing.Union[bytes, NoneType]=None)\nQBitmap(self, other:PySide2.QtGui.QBitmap)\nQBitmap(self, w:int, h:int)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def clear(self):
        'clear(self)'
        pass
    
    @classmethod
    def fromData(cls, size, bits, monoFormat):
        'fromData(size:PySide2.QtCore.QSize, bits:bytes, monoFormat:PySide2.QtGui.QImage.Format=PySide2.QtGui.QImage.Format.Format_MonoLSB) -> PySide2.QtGui.QBitmap'
        return PySide2.QtGui.QBitmap
    
    @classmethod
    def fromImage(cls, image: PySide2.QtGui.QImage, flags: PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor):
        'fromImage(image:PySide2.QtGui.QImage, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QBitmap\nfromImage(image:PySide2.QtGui.QImage, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QPixmap'
        pass
    
    def swap(self, other: PySide2.QtGui.QPixmap):
        'swap(self, other:PySide2.QtGui.QBitmap)\nswap(self, other:PySide2.QtGui.QPixmap)'
        pass
    
    def transformed(self, arg__1: PySide2.QtGui.QMatrix, mode: PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation):
        'transformed(self, arg__1:PySide2.QtGui.QMatrix) -> PySide2.QtGui.QBitmap\ntransformed(self, arg__1:PySide2.QtGui.QMatrix, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap\ntransformed(self, matrix:PySide2.QtGui.QTransform) -> PySide2.QtGui.QBitmap'
        pass
    

class QBrush(_mod_Shiboken.Object):
    'QBrush(self)\nQBrush(self, brush:PySide2.QtGui.QBrush)\nQBrush(self, bs:PySide2.QtCore.Qt.BrushStyle)\nQBrush(self, color:PySide2.QtCore.Qt.GlobalColor, bs:PySide2.QtCore.Qt.BrushStyle=PySide2.QtCore.Qt.BrushStyle.SolidPattern)\nQBrush(self, color:PySide2.QtCore.Qt.GlobalColor, pixmap:PySide2.QtGui.QPixmap)\nQBrush(self, color:PySide2.QtGui.QColor, bs:PySide2.QtCore.Qt.BrushStyle=PySide2.QtCore.Qt.BrushStyle.SolidPattern)\nQBrush(self, color:PySide2.QtGui.QColor, pixmap:PySide2.QtGui.QPixmap)\nQBrush(self, gradient:PySide2.QtGui.QGradient)\nQBrush(self, image:PySide2.QtGui.QImage)\nQBrush(self, pixmap:PySide2.QtGui.QPixmap)'
    __class__ = QBrush
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, color: PySide2.QtCore.Qt.GlobalColor, bs: PySide2.QtCore.Qt.BrushStyle=PySide2.QtCore.Qt.BrushStyle.SolidPattern):
        'QBrush(self)\nQBrush(self, brush:PySide2.QtGui.QBrush)\nQBrush(self, bs:PySide2.QtCore.Qt.BrushStyle)\nQBrush(self, color:PySide2.QtCore.Qt.GlobalColor, bs:PySide2.QtCore.Qt.BrushStyle=PySide2.QtCore.Qt.BrushStyle.SolidPattern)\nQBrush(self, color:PySide2.QtCore.Qt.GlobalColor, pixmap:PySide2.QtGui.QPixmap)\nQBrush(self, color:PySide2.QtGui.QColor, bs:PySide2.QtCore.Qt.BrushStyle=PySide2.QtCore.Qt.BrushStyle.SolidPattern)\nQBrush(self, color:PySide2.QtGui.QColor, pixmap:PySide2.QtGui.QPixmap)\nQBrush(self, gradient:PySide2.QtGui.QGradient)\nQBrush(self, image:PySide2.QtGui.QImage)\nQBrush(self, pixmap:PySide2.QtGui.QPixmap)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QBrush()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QBrush()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def color(self):
        'color(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def gradient(self):
        'gradient(self) -> PySide2.QtGui.QGradient'
        return PySide2.QtGui.QGradient
    
    def isOpaque(self):
        'isOpaque(self) -> bool'
        return bool
    
    def matrix(self):
        'matrix(self) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    
    def setColor(self, color: PySide2.QtCore.Qt.GlobalColor):
        'setColor(self, color:PySide2.QtCore.Qt.GlobalColor)\nsetColor(self, color:PySide2.QtGui.QColor)'
        pass
    
    def setMatrix(self, mat):
        'setMatrix(self, mat:PySide2.QtGui.QMatrix)'
        pass
    
    def setStyle(self, arg__1):
        'setStyle(self, arg__1:PySide2.QtCore.Qt.BrushStyle)'
        pass
    
    def setTexture(self, pixmap):
        'setTexture(self, pixmap:PySide2.QtGui.QPixmap)'
        pass
    
    def setTextureImage(self, image):
        'setTextureImage(self, image:PySide2.QtGui.QImage)'
        pass
    
    def setTransform(self, arg__1):
        'setTransform(self, arg__1:PySide2.QtGui.QTransform)'
        pass
    
    def style(self):
        'style(self) -> PySide2.QtCore.Qt.BrushStyle'
        return PySide2.QtCore.Qt.BrushStyle
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QBrush)'
        pass
    
    def texture(self):
        'texture(self) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    def textureImage(self):
        'textureImage(self) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def transform(self):
        'transform(self) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    

class QClipboard(_mod_PySide2_QtCore.QObject):
    Clipboard = Mode()
    FindBuffer = Mode()
    LastMode = Mode()
    Mode = Mode
    Selection = Mode()
    __class__ = QClipboard
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def changed(self):
        pass
    
    def clear(self, mode):
        'clear(self, mode:PySide2.QtGui.QClipboard.Mode=PySide2.QtGui.QClipboard.Mode.Clipboard)'
        pass
    
    def dataChanged(self):
        pass
    
    def findBufferChanged(self):
        pass
    
    def image(self, mode):
        'image(self, mode:PySide2.QtGui.QClipboard.Mode=PySide2.QtGui.QClipboard.Mode.Clipboard) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def mimeData(self, mode):
        'mimeData(self, mode:PySide2.QtGui.QClipboard.Mode=PySide2.QtGui.QClipboard.Mode.Clipboard) -> PySide2.QtCore.QMimeData'
        return PySide2.QtCore.QMimeData
    
    def ownsClipboard(self):
        'ownsClipboard(self) -> bool'
        return bool
    
    def ownsFindBuffer(self):
        'ownsFindBuffer(self) -> bool'
        return bool
    
    def ownsSelection(self):
        'ownsSelection(self) -> bool'
        return bool
    
    def pixmap(self, mode):
        'pixmap(self, mode:PySide2.QtGui.QClipboard.Mode=PySide2.QtGui.QClipboard.Mode.Clipboard) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    def selectionChanged(self):
        pass
    
    def setImage(self, arg__1, mode):
        'setImage(self, arg__1:PySide2.QtGui.QImage, mode:PySide2.QtGui.QClipboard.Mode=PySide2.QtGui.QClipboard.Mode.Clipboard)'
        pass
    
    def setMimeData(self, data, mode):
        'setMimeData(self, data:PySide2.QtCore.QMimeData, mode:PySide2.QtGui.QClipboard.Mode=PySide2.QtGui.QClipboard.Mode.Clipboard)'
        pass
    
    def setPixmap(self, arg__1, mode):
        'setPixmap(self, arg__1:PySide2.QtGui.QPixmap, mode:PySide2.QtGui.QClipboard.Mode=PySide2.QtGui.QClipboard.Mode.Clipboard)'
        pass
    
    def setText(self, arg__1, mode):
        'setText(self, arg__1:str, mode:PySide2.QtGui.QClipboard.Mode=PySide2.QtGui.QClipboard.Mode.Clipboard)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def supportsFindBuffer(self):
        'supportsFindBuffer(self) -> bool'
        return bool
    
    def supportsSelection(self):
        'supportsSelection(self) -> bool'
        return bool
    
    def text(self, subtype: str, mode: PySide2.QtGui.QClipboard.Mode=PySide2.QtGui.QClipboard.Mode.Clipboard):
        'text(self, mode:PySide2.QtGui.QClipboard.Mode=PySide2.QtGui.QClipboard.Mode.Clipboard) -> str\ntext(self, subtype:str, mode:PySide2.QtGui.QClipboard.Mode=PySide2.QtGui.QClipboard.Mode.Clipboard) -> str'
        return ''
    

class QCloseEvent(_mod_PySide2_QtCore.QEvent):
    'QCloseEvent(self)'
    __class__ = QCloseEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QCloseEvent(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class QColor(_mod_Shiboken.Object):
    'QColor(self)\nQColor(self, arg__1:typing.Any)\nQColor(self, color:PySide2.QtCore.Qt.GlobalColor)\nQColor(self, color:PySide2.QtGui.QColor)\nQColor(self, name:str)\nQColor(self, r:int, g:int, b:int, a:int=255)\nQColor(self, rgb:int)\nQColor(self, spec:PySide2.QtGui.QColor.Spec, a1:int, a2:int, a3:int, a4:int, a5:int=0)'
    Cmyk = Spec()
    ExtendedRgb = Spec()
    HexArgb = NameFormat()
    HexRgb = NameFormat()
    Hsl = Spec()
    Hsv = Spec()
    Invalid = Spec()
    NameFormat = NameFormat
    Rgb = Spec()
    Spec = Spec
    __class__ = QColor
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, spec: PySide2.QtGui.QColor.Spec, a1: int, a2: int, a3: int, a4: int, a5: int=0):
        'QColor(self)\nQColor(self, arg__1:typing.Any)\nQColor(self, color:PySide2.QtCore.Qt.GlobalColor)\nQColor(self, color:PySide2.QtGui.QColor)\nQColor(self, name:str)\nQColor(self, r:int, g:int, b:int, a:int=255)\nQColor(self, rgb:int)\nQColor(self, spec:PySide2.QtGui.QColor.Spec, a1:int, a2:int, a3:int, a4:int, a5:int=0)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QColor()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QColor()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __setstate__(self, arg__1):
        '__setstate__(self, arg__1:object) -> object'
        return object
    
    def __str__(self):
        '__str__(self) -> object\n\nReturn str(self).'
        return object
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def alpha(self):
        'alpha(self) -> int'
        return int
    
    def alphaF(self):
        'alphaF(self) -> float'
        return float
    
    def black(self):
        'black(self) -> int'
        return int
    
    def blackF(self):
        'blackF(self) -> float'
        return float
    
    def blue(self):
        'blue(self) -> int'
        return int
    
    def blueF(self):
        'blueF(self) -> float'
        return float
    
    @classmethod
    def colorNames(cls):
        'colorNames() -> typing.List'
        return typing.List
    
    def convertTo(self, colorSpec):
        'convertTo(self, colorSpec:PySide2.QtGui.QColor.Spec) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def cyan(self):
        'cyan(self) -> int'
        return int
    
    def cyanF(self):
        'cyanF(self) -> float'
        return float
    
    def dark(self, f):
        'dark(self, f:int=200) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def darker(self, f):
        'darker(self, f:int=200) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    @classmethod
    def fromCmyk(cls, c, m, y, k, a):
        'fromCmyk(c:int, m:int, y:int, k:int, a:int=255) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    @classmethod
    def fromCmykF(cls, c, m, y, k, a):
        'fromCmykF(c:float, m:float, y:float, k:float, a:float=1.0) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    @classmethod
    def fromHsl(cls, h, s, l, a):
        'fromHsl(h:int, s:int, l:int, a:int=255) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    @classmethod
    def fromHslF(cls, h, s, l, a):
        'fromHslF(h:float, s:float, l:float, a:float=1.0) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    @classmethod
    def fromHsv(cls, h, s, v, a):
        'fromHsv(h:int, s:int, v:int, a:int=255) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    @classmethod
    def fromHsvF(cls, h, s, v, a):
        'fromHsvF(h:float, s:float, v:float, a:float=1.0) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    @classmethod
    def fromRgb(cls, r: int, g: int, b: int, a: int=255):
        'fromRgb(r:int, g:int, b:int, a:int=255) -> PySide2.QtGui.QColor\nfromRgb(rgb:int) -> PySide2.QtGui.QColor'
        pass
    
    @classmethod
    def fromRgbF(cls, r, g, b, a):
        'fromRgbF(r:float, g:float, b:float, a:float=1.0) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    @classmethod
    def fromRgba(cls, rgba):
        'fromRgba(rgba:int) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    @classmethod
    def fromRgba64(cls, r, g, b, a):
        'fromRgba64(r:int, g:int, b:int, a:int=65535) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def getCmyk(self):
        'getCmyk(self) -> typing.Tuple\ngetCmyk(self) -> typing.Tuple'
        pass
    
    def getCmykF(self):
        'getCmykF(self) -> typing.Tuple\ngetCmykF(self) -> typing.Tuple'
        pass
    
    def getHsl(self):
        'getHsl(self) -> typing.Tuple'
        return typing.Tuple
    
    def getHslF(self):
        'getHslF(self) -> typing.Tuple'
        return typing.Tuple
    
    def getHsv(self):
        'getHsv(self) -> typing.Tuple'
        return typing.Tuple
    
    def getHsvF(self):
        'getHsvF(self) -> typing.Tuple'
        return typing.Tuple
    
    def getRgb(self):
        'getRgb(self) -> typing.Tuple'
        return typing.Tuple
    
    def getRgbF(self):
        'getRgbF(self) -> typing.Tuple'
        return typing.Tuple
    
    def green(self):
        'green(self) -> int'
        return int
    
    def greenF(self):
        'greenF(self) -> float'
        return float
    
    def hslHue(self):
        'hslHue(self) -> int'
        return int
    
    def hslHueF(self):
        'hslHueF(self) -> float'
        return float
    
    def hslSaturation(self):
        'hslSaturation(self) -> int'
        return int
    
    def hslSaturationF(self):
        'hslSaturationF(self) -> float'
        return float
    
    def hsvHue(self):
        'hsvHue(self) -> int'
        return int
    
    def hsvHueF(self):
        'hsvHueF(self) -> float'
        return float
    
    def hsvSaturation(self):
        'hsvSaturation(self) -> int'
        return int
    
    def hsvSaturationF(self):
        'hsvSaturationF(self) -> float'
        return float
    
    def hue(self):
        'hue(self) -> int'
        return int
    
    def hueF(self):
        'hueF(self) -> float'
        return float
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    @classmethod
    def isValidColor(cls, name):
        'isValidColor(name:str) -> bool'
        return bool
    
    def light(self, f):
        'light(self, f:int=150) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def lighter(self, f):
        'lighter(self, f:int=150) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def lightness(self):
        'lightness(self) -> int'
        return int
    
    def lightnessF(self):
        'lightnessF(self) -> float'
        return float
    
    def magenta(self):
        'magenta(self) -> int'
        return int
    
    def magentaF(self):
        'magentaF(self) -> float'
        return float
    
    def name(self, format: PySide2.QtGui.QColor.NameFormat):
        'name(self) -> str\nname(self, format:PySide2.QtGui.QColor.NameFormat) -> str'
        return ''
    
    def red(self):
        'red(self) -> int'
        return int
    
    def redF(self):
        'redF(self) -> float'
        return float
    
    def rgb(self):
        'rgb(self) -> int'
        return int
    
    def rgba(self):
        'rgba(self) -> int'
        return int
    
    def saturation(self):
        'saturation(self) -> int'
        return int
    
    def saturationF(self):
        'saturationF(self) -> float'
        return float
    
    def setAlpha(self, alpha):
        'setAlpha(self, alpha:int)'
        pass
    
    def setAlphaF(self, alpha):
        'setAlphaF(self, alpha:float)'
        pass
    
    def setBlue(self, blue):
        'setBlue(self, blue:int)'
        pass
    
    def setBlueF(self, blue):
        'setBlueF(self, blue:float)'
        pass
    
    def setCmyk(self, c, m, y, k, a):
        'setCmyk(self, c:int, m:int, y:int, k:int, a:int=255)'
        pass
    
    def setCmykF(self, c, m, y, k, a):
        'setCmykF(self, c:float, m:float, y:float, k:float, a:float=1.0)'
        pass
    
    def setGreen(self, green):
        'setGreen(self, green:int)'
        pass
    
    def setGreenF(self, green):
        'setGreenF(self, green:float)'
        pass
    
    def setHsl(self, h, s, l, a):
        'setHsl(self, h:int, s:int, l:int, a:int=255)'
        pass
    
    def setHslF(self, h, s, l, a):
        'setHslF(self, h:float, s:float, l:float, a:float=1.0)'
        pass
    
    def setHsv(self, h, s, v, a):
        'setHsv(self, h:int, s:int, v:int, a:int=255)'
        pass
    
    def setHsvF(self, h, s, v, a):
        'setHsvF(self, h:float, s:float, v:float, a:float=1.0)'
        pass
    
    def setNamedColor(self, name):
        'setNamedColor(self, name:str)'
        pass
    
    def setRed(self, red):
        'setRed(self, red:int)'
        pass
    
    def setRedF(self, red):
        'setRedF(self, red:float)'
        pass
    
    def setRgb(self, r: int, g: int, b: int, a: int=255):
        'setRgb(self, r:int, g:int, b:int, a:int=255)\nsetRgb(self, rgb:int)'
        pass
    
    def setRgbF(self, r, g, b, a):
        'setRgbF(self, r:float, g:float, b:float, a:float=1.0)'
        pass
    
    def setRgba(self, rgba):
        'setRgba(self, rgba:int)'
        pass
    
    def spec(self):
        'spec(self) -> PySide2.QtGui.QColor.Spec'
        return PySide2.QtGui.QColor.Spec
    
    def toCmyk(self):
        'toCmyk(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def toExtendedRgb(self):
        'toExtendedRgb(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def toHsl(self):
        'toHsl(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def toHsv(self):
        'toHsv(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def toRgb(self):
        'toRgb(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def toTuple(self):
        'toTuple(self) -> object'
        return object
    
    def value(self):
        'value(self) -> int'
        return int
    
    def valueF(self):
        'valueF(self) -> float'
        return float
    
    def yellow(self):
        'yellow(self) -> int'
        return int
    
    def yellowF(self):
        'yellowF(self) -> float'
        return float
    

class QColorSpace(_mod_Shiboken.Object):
    'QColorSpace(self)\nQColorSpace(self, colorSpace:PySide2.QtGui.QColorSpace)\nQColorSpace(self, namedColorSpace:PySide2.QtGui.QColorSpace.NamedColorSpace)\nQColorSpace(self, primaries:PySide2.QtGui.QColorSpace.Primaries, fun:PySide2.QtGui.QColorSpace.TransferFunction, gamma:float=0.0)\nQColorSpace(self, primaries:PySide2.QtGui.QColorSpace.Primaries, gamma:float)\nQColorSpace(self, whitePoint:PySide2.QtCore.QPointF, redPoint:PySide2.QtCore.QPointF, greenPoint:PySide2.QtCore.QPointF, bluePoint:PySide2.QtCore.QPointF, fun:PySide2.QtGui.QColorSpace.TransferFunction, gamma:float=0.0)'
    AdobeRgb = NamedColorSpace()
    DisplayP3 = NamedColorSpace()
    NamedColorSpace = NamedColorSpace
    Primaries = Primaries
    ProPhotoRgb = NamedColorSpace()
    SRgb = NamedColorSpace()
    SRgbLinear = NamedColorSpace()
    TransferFunction = TransferFunction
    __class__ = QColorSpace
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, whitePoint: PySide2.QtCore.QPointF, redPoint: PySide2.QtCore.QPointF, greenPoint: PySide2.QtCore.QPointF, bluePoint: PySide2.QtCore.QPointF, fun: PySide2.QtGui.QColorSpace.TransferFunction, gamma: float=0.0):
        'QColorSpace(self)\nQColorSpace(self, colorSpace:PySide2.QtGui.QColorSpace)\nQColorSpace(self, namedColorSpace:PySide2.QtGui.QColorSpace.NamedColorSpace)\nQColorSpace(self, primaries:PySide2.QtGui.QColorSpace.Primaries, fun:PySide2.QtGui.QColorSpace.TransferFunction, gamma:float=0.0)\nQColorSpace(self, primaries:PySide2.QtGui.QColorSpace.Primaries, gamma:float)\nQColorSpace(self, whitePoint:PySide2.QtCore.QPointF, redPoint:PySide2.QtCore.QPointF, greenPoint:PySide2.QtCore.QPointF, bluePoint:PySide2.QtCore.QPointF, fun:PySide2.QtGui.QColorSpace.TransferFunction, gamma:float=0.0)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QColorSpace()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QColorSpace()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def fromIccProfile(cls, iccProfile):
        'fromIccProfile(iccProfile:PySide2.QtCore.QByteArray) -> PySide2.QtGui.QColorSpace'
        return PySide2.QtGui.QColorSpace
    
    def gamma(self):
        'gamma(self) -> float'
        return float
    
    def iccProfile(self):
        'iccProfile(self) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def primaries(self):
        'primaries(self) -> PySide2.QtGui.QColorSpace.Primaries'
        return PySide2.QtGui.QColorSpace.Primaries
    
    def setPrimaries(self, whitePoint: PySide2.QtCore.QPointF, redPoint: PySide2.QtCore.QPointF, greenPoint: PySide2.QtCore.QPointF, bluePoint: PySide2.QtCore.QPointF):
        'setPrimaries(self, primariesId:PySide2.QtGui.QColorSpace.Primaries)\nsetPrimaries(self, whitePoint:PySide2.QtCore.QPointF, redPoint:PySide2.QtCore.QPointF, greenPoint:PySide2.QtCore.QPointF, bluePoint:PySide2.QtCore.QPointF)'
        pass
    
    def setTransferFunction(self, transferFunction, gamma):
        'setTransferFunction(self, transferFunction:PySide2.QtGui.QColorSpace.TransferFunction, gamma:float=0.0)'
        pass
    
    def swap(self, colorSpace):
        'swap(self, colorSpace:PySide2.QtGui.QColorSpace)'
        pass
    
    def transferFunction(self):
        'transferFunction(self) -> PySide2.QtGui.QColorSpace.TransferFunction'
        return PySide2.QtGui.QColorSpace.TransferFunction
    
    def withTransferFunction(self, transferFunction, gamma):
        'withTransferFunction(self, transferFunction:PySide2.QtGui.QColorSpace.TransferFunction, gamma:float=0.0) -> PySide2.QtGui.QColorSpace'
        return PySide2.QtGui.QColorSpace
    

class QConicalGradient(QGradient):
    'QConicalGradient(self)\nQConicalGradient(self, QConicalGradient:PySide2.QtGui.QConicalGradient)\nQConicalGradient(self, center:PySide2.QtCore.QPointF, startAngle:float)\nQConicalGradient(self, cx:float, cy:float, startAngle:float)'
    __class__ = QConicalGradient
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, center: PySide2.QtCore.QPointF, startAngle: float):
        'QConicalGradient(self)\nQConicalGradient(self, QConicalGradient:PySide2.QtGui.QConicalGradient)\nQConicalGradient(self, center:PySide2.QtCore.QPointF, startAngle:float)\nQConicalGradient(self, cx:float, cy:float, startAngle:float)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def angle(self):
        'angle(self) -> float'
        return float
    
    def center(self):
        'center(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def setAngle(self, angle):
        'setAngle(self, angle:float)'
        pass
    
    def setCenter(self, center: PySide2.QtCore.QPointF):
        'setCenter(self, center:PySide2.QtCore.QPointF)\nsetCenter(self, x:float, y:float)'
        pass
    

class QContextMenuEvent(QInputEvent):
    'QContextMenuEvent(self, reason:PySide2.QtGui.QContextMenuEvent.Reason, pos:PySide2.QtCore.QPoint)\nQContextMenuEvent(self, reason:PySide2.QtGui.QContextMenuEvent.Reason, pos:PySide2.QtCore.QPoint, globalPos:PySide2.QtCore.QPoint)\nQContextMenuEvent(self, reason:PySide2.QtGui.QContextMenuEvent.Reason, pos:PySide2.QtCore.QPoint, globalPos:PySide2.QtCore.QPoint, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)'
    Keyboard = Reason()
    Mouse = Reason()
    Other = Reason()
    Reason = Reason
    __class__ = QContextMenuEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, reason: PySide2.QtGui.QContextMenuEvent.Reason, pos: PySide2.QtCore.QPoint, globalPos: PySide2.QtCore.QPoint, modifiers: PySide2.QtCore.Qt.KeyboardModifiers):
        'QContextMenuEvent(self, reason:PySide2.QtGui.QContextMenuEvent.Reason, pos:PySide2.QtCore.QPoint)\nQContextMenuEvent(self, reason:PySide2.QtGui.QContextMenuEvent.Reason, pos:PySide2.QtCore.QPoint, globalPos:PySide2.QtCore.QPoint)\nQContextMenuEvent(self, reason:PySide2.QtGui.QContextMenuEvent.Reason, pos:PySide2.QtCore.QPoint, globalPos:PySide2.QtCore.QPoint, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def globalPos(self):
        'globalPos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def globalX(self):
        'globalX(self) -> int'
        return int
    
    def globalY(self):
        'globalY(self) -> int'
        return int
    
    def pos(self):
        'pos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def reason(self):
        'reason(self) -> PySide2.QtGui.QContextMenuEvent.Reason'
        return PySide2.QtGui.QContextMenuEvent.Reason
    
    def x(self):
        'x(self) -> int'
        return int
    
    def y(self):
        'y(self) -> int'
        return int
    

class QCursor(_mod_Shiboken.Object):
    'QCursor(self)\nQCursor(self, bitmap:PySide2.QtGui.QBitmap, mask:PySide2.QtGui.QBitmap, hotX:int=-1, hotY:int=-1)\nQCursor(self, cursor:PySide2.QtGui.QCursor)\nQCursor(self, pixmap:PySide2.QtGui.QPixmap, hotX:int=-1, hotY:int=-1)\nQCursor(self, shape:PySide2.QtCore.Qt.CursorShape)'
    __class__ = QCursor
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, bitmap: PySide2.QtGui.QBitmap, mask: PySide2.QtGui.QBitmap, hotX: int=-1, hotY: int=-1):
        'QCursor(self)\nQCursor(self, bitmap:PySide2.QtGui.QBitmap, mask:PySide2.QtGui.QBitmap, hotX:int=-1, hotY:int=-1)\nQCursor(self, cursor:PySide2.QtGui.QCursor)\nQCursor(self, pixmap:PySide2.QtGui.QPixmap, hotX:int=-1, hotY:int=-1)\nQCursor(self, shape:PySide2.QtCore.Qt.CursorShape)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, outS):
        '__lshift__(self, outS:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QCursor()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QCursor()
    
    def __rshift__(self, inS):
        '__rshift__(self, inS:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bitmap(self):
        'bitmap(self) -> PySide2.QtGui.QBitmap'
        return PySide2.QtGui.QBitmap
    
    def hotSpot(self):
        'hotSpot(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def mask(self):
        'mask(self) -> PySide2.QtGui.QBitmap'
        return PySide2.QtGui.QBitmap
    
    def pixmap(self):
        'pixmap(self) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    @classmethod
    def pos(cls, screen: PySide2.QtGui.QScreen):
        'pos() -> PySide2.QtCore.QPoint\npos(screen:PySide2.QtGui.QScreen) -> PySide2.QtCore.QPoint'
        pass
    
    @classmethod
    def setPos(cls, screen: PySide2.QtGui.QScreen, p: PySide2.QtCore.QPoint):
        'setPos(p:PySide2.QtCore.QPoint)\nsetPos(screen:PySide2.QtGui.QScreen, p:PySide2.QtCore.QPoint)\nsetPos(screen:PySide2.QtGui.QScreen, x:int, y:int)\nsetPos(x:int, y:int)'
        pass
    
    def setShape(self, newShape):
        'setShape(self, newShape:PySide2.QtCore.Qt.CursorShape)'
        pass
    
    def shape(self):
        'shape(self) -> PySide2.QtCore.Qt.CursorShape'
        return PySide2.QtCore.Qt.CursorShape
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QCursor)'
        pass
    

class QDesktopServices(_mod_Shiboken.Object):
    'QDesktopServices(self)'
    __class__ = QDesktopServices
    __dict__ = {}
    def __init__(self):
        'QDesktopServices(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def openUrl(cls, url):
        'openUrl(url:PySide2.QtCore.QUrl) -> bool'
        return bool
    
    @classmethod
    def setUrlHandler(cls, scheme, receiver, method):
        'setUrlHandler(scheme:str, receiver:PySide2.QtCore.QObject, method:bytes)'
        pass
    
    @classmethod
    def unsetUrlHandler(cls, scheme):
        'unsetUrlHandler(scheme:str)'
        pass
    

class QDoubleValidator(QValidator):
    'QDoubleValidator(self, bottom:float, top:float, decimals:int, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQDoubleValidator(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    Notation = Notation
    ScientificNotation = Notation()
    StandardNotation = Notation()
    __class__ = QDoubleValidator
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, bottom: float, top: float, decimals: int, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QDoubleValidator(self, bottom:float, top:float, decimals:int, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQDoubleValidator(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bottom(self):
        'bottom(self) -> float'
        return float
    
    def bottomChanged(self):
        pass
    
    def decimals(self):
        'decimals(self) -> int'
        return int
    
    def decimalsChanged(self):
        pass
    
    def notation(self):
        'notation(self) -> PySide2.QtGui.QDoubleValidator.Notation'
        return PySide2.QtGui.QDoubleValidator.Notation
    
    def notationChanged(self):
        pass
    
    def setBottom(self, arg__1):
        'setBottom(self, arg__1:float)'
        pass
    
    def setDecimals(self, arg__1):
        'setDecimals(self, arg__1:int)'
        pass
    
    def setNotation(self, arg__1):
        'setNotation(self, arg__1:PySide2.QtGui.QDoubleValidator.Notation)'
        pass
    
    def setRange(self, bottom, top, decimals):
        'setRange(self, bottom:float, top:float, decimals:int=0)'
        pass
    
    def setTop(self, arg__1):
        'setTop(self, arg__1:float)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def top(self):
        'top(self) -> float'
        return float
    
    def topChanged(self):
        pass
    
    def validate(self, arg__1, arg__2):
        'validate(self, arg__1:str, arg__2:int) -> PySide2.QtGui.QValidator.State'
        return PySide2.QtGui.QValidator.State
    

class QDrag(_mod_PySide2_QtCore.QObject):
    'QDrag(self, dragSource:PySide2.QtCore.QObject)'
    __class__ = QDrag
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, dragSource: PySide2.QtCore.QObject):
        'QDrag(self, dragSource:PySide2.QtCore.QObject)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def actionChanged(self):
        pass
    
    @classmethod
    def cancel(cls):
        'cancel()'
        pass
    
    def defaultAction(self):
        'defaultAction(self) -> PySide2.QtCore.Qt.DropAction'
        return PySide2.QtCore.Qt.DropAction
    
    def dragCursor(self, action):
        'dragCursor(self, action:PySide2.QtCore.Qt.DropAction) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    def exec_(self, supportedActions: PySide2.QtCore.Qt.DropActions, defaultAction: PySide2.QtCore.Qt.DropAction):
        'exec_(self, supportedActions:PySide2.QtCore.Qt.DropActions, defaultAction:PySide2.QtCore.Qt.DropAction) -> PySide2.QtCore.Qt.DropAction\nexec_(self, supportedActions:PySide2.QtCore.Qt.DropActions=PySide2.QtCore.Qt.DropAction.MoveAction) -> PySide2.QtCore.Qt.DropAction'
        pass
    
    def hotSpot(self):
        'hotSpot(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def mimeData(self):
        'mimeData(self) -> PySide2.QtCore.QMimeData'
        return PySide2.QtCore.QMimeData
    
    def pixmap(self):
        'pixmap(self) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    def setDragCursor(self, cursor, action):
        'setDragCursor(self, cursor:PySide2.QtGui.QPixmap, action:PySide2.QtCore.Qt.DropAction)'
        pass
    
    def setHotSpot(self, hotspot):
        'setHotSpot(self, hotspot:PySide2.QtCore.QPoint)'
        pass
    
    def setMimeData(self, data):
        'setMimeData(self, data:PySide2.QtCore.QMimeData)'
        pass
    
    def setPixmap(self, arg__1):
        'setPixmap(self, arg__1:PySide2.QtGui.QPixmap)'
        pass
    
    def source(self):
        'source(self) -> PySide2.QtCore.QObject'
        return PySide2.QtCore.QObject
    
    def start(self, supportedActions):
        'start(self, supportedActions:PySide2.QtCore.Qt.DropActions=PySide2.QtCore.Qt.DropAction.CopyAction) -> PySide2.QtCore.Qt.DropAction'
        return PySide2.QtCore.Qt.DropAction
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def supportedActions(self):
        'supportedActions(self) -> PySide2.QtCore.Qt.DropActions'
        return PySide2.QtCore.Qt.DropActions
    
    def target(self):
        'target(self) -> PySide2.QtCore.QObject'
        return PySide2.QtCore.QObject
    
    def targetChanged(self):
        pass
    

class QDragEnterEvent(QDragMoveEvent):
    'QDragEnterEvent(self, pos:PySide2.QtCore.QPoint, actions:PySide2.QtCore.Qt.DropActions, data:PySide2.QtCore.QMimeData, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)'
    __class__ = QDragEnterEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, pos: PySide2.QtCore.QPoint, actions: PySide2.QtCore.Qt.DropActions, data: PySide2.QtCore.QMimeData, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers):
        'QDragEnterEvent(self, pos:PySide2.QtCore.QPoint, actions:PySide2.QtCore.Qt.DropActions, data:PySide2.QtCore.QMimeData, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class QDragLeaveEvent(_mod_PySide2_QtCore.QEvent):
    'QDragLeaveEvent(self)'
    __class__ = QDragLeaveEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QDragLeaveEvent(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class QDragMoveEvent(QDropEvent):
    'QDragMoveEvent(self, pos:PySide2.QtCore.QPoint, actions:PySide2.QtCore.Qt.DropActions, data:PySide2.QtCore.QMimeData, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, type:PySide2.QtCore.QEvent.Type=PySide2.QtCore.QEvent.Type.DragMove)'
    __class__ = QDragMoveEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, pos: PySide2.QtCore.QPoint, actions: PySide2.QtCore.Qt.DropActions, data: PySide2.QtCore.QMimeData, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, type: PySide2.QtCore.QEvent.Type=PySide2.QtCore.QEvent.Type.DragMove):
        'QDragMoveEvent(self, pos:PySide2.QtCore.QPoint, actions:PySide2.QtCore.Qt.DropActions, data:PySide2.QtCore.QMimeData, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, type:PySide2.QtCore.QEvent.Type=PySide2.QtCore.QEvent.Type.DragMove)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def accept(self, r: PySide2.QtCore.QRect):
        'accept(self)\naccept(self, r:PySide2.QtCore.QRect)'
        pass
    
    def answerRect(self):
        'answerRect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def ignore(self, r: PySide2.QtCore.QRect):
        'ignore(self)\nignore(self, r:PySide2.QtCore.QRect)'
        pass
    

class QDropEvent(_mod_PySide2_QtCore.QEvent):
    'QDropEvent(self, pos:PySide2.QtCore.QPointF, actions:PySide2.QtCore.Qt.DropActions, data:PySide2.QtCore.QMimeData, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, type:PySide2.QtCore.QEvent.Type=PySide2.QtCore.QEvent.Type.Drop)'
    __class__ = QDropEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, pos: PySide2.QtCore.QPointF, actions: PySide2.QtCore.Qt.DropActions, data: PySide2.QtCore.QMimeData, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, type: PySide2.QtCore.QEvent.Type=PySide2.QtCore.QEvent.Type.Drop):
        'QDropEvent(self, pos:PySide2.QtCore.QPointF, actions:PySide2.QtCore.Qt.DropActions, data:PySide2.QtCore.QMimeData, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, type:PySide2.QtCore.QEvent.Type=PySide2.QtCore.QEvent.Type.Drop)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def acceptProposedAction(self):
        'acceptProposedAction(self)'
        pass
    
    def dropAction(self):
        'dropAction(self) -> PySide2.QtCore.Qt.DropAction'
        return PySide2.QtCore.Qt.DropAction
    
    def keyboardModifiers(self):
        'keyboardModifiers(self) -> PySide2.QtCore.Qt.KeyboardModifiers'
        return PySide2.QtCore.Qt.KeyboardModifiers
    
    def mimeData(self):
        'mimeData(self) -> PySide2.QtCore.QMimeData'
        return PySide2.QtCore.QMimeData
    
    def mouseButtons(self):
        'mouseButtons(self) -> PySide2.QtCore.Qt.MouseButtons'
        return PySide2.QtCore.Qt.MouseButtons
    
    def pos(self):
        'pos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def posF(self):
        'posF(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def possibleActions(self):
        'possibleActions(self) -> PySide2.QtCore.Qt.DropActions'
        return PySide2.QtCore.Qt.DropActions
    
    def proposedAction(self):
        'proposedAction(self) -> PySide2.QtCore.Qt.DropAction'
        return PySide2.QtCore.Qt.DropAction
    
    def setDropAction(self, action):
        'setDropAction(self, action:PySide2.QtCore.Qt.DropAction)'
        pass
    
    def source(self):
        'source(self) -> PySide2.QtCore.QObject'
        return PySide2.QtCore.QObject
    

class QEnterEvent(_mod_PySide2_QtCore.QEvent):
    'QEnterEvent(self, localPos:PySide2.QtCore.QPointF, windowPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF)'
    __class__ = QEnterEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, localPos: PySide2.QtCore.QPointF, windowPos: PySide2.QtCore.QPointF, screenPos: PySide2.QtCore.QPointF):
        'QEnterEvent(self, localPos:PySide2.QtCore.QPointF, windowPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def globalPos(self):
        'globalPos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def globalX(self):
        'globalX(self) -> int'
        return int
    
    def globalY(self):
        'globalY(self) -> int'
        return int
    
    def localPos(self):
        'localPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def pos(self):
        'pos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def screenPos(self):
        'screenPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def windowPos(self):
        'windowPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def x(self):
        'x(self) -> int'
        return int
    
    def y(self):
        'y(self) -> int'
        return int
    

class QExposeEvent(_mod_PySide2_QtCore.QEvent):
    'QExposeEvent(self, rgn:PySide2.QtGui.QRegion)'
    __class__ = QExposeEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, rgn: PySide2.QtGui.QRegion):
        'QExposeEvent(self, rgn:PySide2.QtGui.QRegion)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def region(self):
        'region(self) -> PySide2.QtGui.QRegion'
        return PySide2.QtGui.QRegion
    
    @property
    def rgn(self):
        pass
    

class QFileOpenEvent(_mod_PySide2_QtCore.QEvent):
    'QFileOpenEvent(self, file:str)\nQFileOpenEvent(self, url:PySide2.QtCore.QUrl)'
    __class__ = QFileOpenEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, url: PySide2.QtCore.QUrl):
        'QFileOpenEvent(self, file:str)\nQFileOpenEvent(self, url:PySide2.QtCore.QUrl)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def file(self):
        'file(self) -> str'
        return str
    
    def openFile(self, file, flags):
        'openFile(self, file:PySide2.QtCore.QFile, flags:PySide2.QtCore.QIODevice.OpenMode) -> bool'
        return bool
    
    def url(self):
        'url(self) -> PySide2.QtCore.QUrl'
        return PySide2.QtCore.QUrl
    

class QFocusEvent(_mod_PySide2_QtCore.QEvent):
    'QFocusEvent(self, type:PySide2.QtCore.QEvent.Type, reason:PySide2.QtCore.Qt.FocusReason=PySide2.QtCore.Qt.FocusReason.OtherFocusReason)'
    __class__ = QFocusEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, type: PySide2.QtCore.QEvent.Type, reason: PySide2.QtCore.Qt.FocusReason=PySide2.QtCore.Qt.FocusReason.OtherFocusReason):
        'QFocusEvent(self, type:PySide2.QtCore.QEvent.Type, reason:PySide2.QtCore.Qt.FocusReason=PySide2.QtCore.Qt.FocusReason.OtherFocusReason)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def gotFocus(self):
        'gotFocus(self) -> bool'
        return bool
    
    def lostFocus(self):
        'lostFocus(self) -> bool'
        return bool
    
    def reason(self):
        'reason(self) -> PySide2.QtCore.Qt.FocusReason'
        return PySide2.QtCore.Qt.FocusReason
    

class QFont(_mod_Shiboken.Object):
    'QFont(self)\nQFont(self, family:str, pointSize:int=-1, weight:int=-1, italic:bool=False)\nQFont(self, font:PySide2.QtGui.QFont)\nQFont(self, font:PySide2.QtGui.QFont, pd:PySide2.QtGui.QPaintDevice)'
    AbsoluteSpacing = SpacingType()
    AllLowercase = Capitalization()
    AllUppercase = Capitalization()
    AnyStretch = Stretch()
    AnyStyle = StyleHint()
    Black = Weight()
    Bold = Weight()
    Capitalization = Capitalization
    Capitalize = Capitalization()
    Condensed = Stretch()
    Courier = StyleHint()
    Cursive = StyleHint()
    Decorative = StyleHint()
    DemiBold = Weight()
    Expanded = Stretch()
    ExtraBold = Weight()
    ExtraCondensed = Stretch()
    ExtraExpanded = Stretch()
    ExtraLight = Weight()
    Fantasy = StyleHint()
    ForceIntegerMetrics = StyleStrategy()
    ForceOutline = StyleStrategy()
    Helvetica = StyleHint()
    HintingPreference = HintingPreference
    Light = Weight()
    Medium = Weight()
    MixedCase = Capitalization()
    Monospace = StyleHint()
    NoAntialias = StyleStrategy()
    NoFontMerging = StyleStrategy()
    NoSubpixelAntialias = StyleStrategy()
    Normal = Weight()
    OldEnglish = StyleHint()
    OpenGLCompatible = StyleStrategy()
    PercentageSpacing = SpacingType()
    PreferAntialias = StyleStrategy()
    PreferBitmap = StyleStrategy()
    PreferDefault = StyleStrategy()
    PreferDefaultHinting = HintingPreference()
    PreferDevice = StyleStrategy()
    PreferFullHinting = HintingPreference()
    PreferMatch = StyleStrategy()
    PreferNoHinting = HintingPreference()
    PreferNoShaping = StyleStrategy()
    PreferOutline = StyleStrategy()
    PreferQuality = StyleStrategy()
    PreferVerticalHinting = HintingPreference()
    SansSerif = StyleHint()
    SemiCondensed = Stretch()
    SemiExpanded = Stretch()
    Serif = StyleHint()
    SmallCaps = Capitalization()
    SpacingType = SpacingType
    Stretch = Stretch
    Style = Style
    StyleHint = StyleHint
    StyleItalic = Style()
    StyleNormal = Style()
    StyleOblique = Style()
    StyleStrategy = StyleStrategy
    System = StyleHint()
    Thin = Weight()
    Times = StyleHint()
    TypeWriter = StyleHint()
    UltraCondensed = Stretch()
    UltraExpanded = Stretch()
    Unstretched = Stretch()
    Weight = Weight
    __class__ = QFont
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, family: str, pointSize: int=-1, weight: int=-1, italic: bool=False):
        'QFont(self)\nQFont(self, family:str, pointSize:int=-1, weight:int=-1, italic:bool=False)\nQFont(self, font:PySide2.QtGui.QFont)\nQFont(self, font:PySide2.QtGui.QFont, pd:PySide2.QtGui.QPaintDevice)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QFont()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QFont()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bold(self):
        'bold(self) -> bool'
        return bool
    
    @classmethod
    def cacheStatistics(cls):
        'cacheStatistics()'
        pass
    
    def capitalization(self):
        'capitalization(self) -> PySide2.QtGui.QFont.Capitalization'
        return PySide2.QtGui.QFont.Capitalization
    
    @classmethod
    def cleanup(cls):
        'cleanup()'
        pass
    
    def defaultFamily(self):
        'defaultFamily(self) -> str'
        return str
    
    def exactMatch(self):
        'exactMatch(self) -> bool'
        return bool
    
    def families(self):
        'families(self) -> typing.List'
        return typing.List
    
    def family(self):
        'family(self) -> str'
        return str
    
    def fixedPitch(self):
        'fixedPitch(self) -> bool'
        return bool
    
    def fromString(self, arg__1):
        'fromString(self, arg__1:str) -> bool'
        return bool
    
    def hintingPreference(self):
        'hintingPreference(self) -> PySide2.QtGui.QFont.HintingPreference'
        return PySide2.QtGui.QFont.HintingPreference
    
    @classmethod
    def initialize(cls):
        'initialize()'
        pass
    
    @classmethod
    def insertSubstitution(cls, arg__1, arg__2):
        'insertSubstitution(arg__1:str, arg__2:str)'
        pass
    
    @classmethod
    def insertSubstitutions(cls, arg__1, arg__2):
        'insertSubstitutions(arg__1:str, arg__2:typing.Sequence)'
        pass
    
    def isCopyOf(self, arg__1):
        'isCopyOf(self, arg__1:PySide2.QtGui.QFont) -> bool'
        return bool
    
    def italic(self):
        'italic(self) -> bool'
        return bool
    
    def kerning(self):
        'kerning(self) -> bool'
        return bool
    
    def key(self):
        'key(self) -> str'
        return str
    
    def lastResortFamily(self):
        'lastResortFamily(self) -> str'
        return str
    
    def lastResortFont(self):
        'lastResortFont(self) -> str'
        return str
    
    def letterSpacing(self):
        'letterSpacing(self) -> float'
        return float
    
    def letterSpacingType(self):
        'letterSpacingType(self) -> PySide2.QtGui.QFont.SpacingType'
        return PySide2.QtGui.QFont.SpacingType
    
    def overline(self):
        'overline(self) -> bool'
        return bool
    
    def pixelSize(self):
        'pixelSize(self) -> int'
        return int
    
    def pointSize(self):
        'pointSize(self) -> int'
        return int
    
    def pointSizeF(self):
        'pointSizeF(self) -> float'
        return float
    
    def rawMode(self):
        'rawMode(self) -> bool'
        return bool
    
    def rawName(self):
        'rawName(self) -> str'
        return str
    
    @classmethod
    def removeSubstitutions(cls, arg__1):
        'removeSubstitutions(arg__1:str)'
        pass
    
    def resolve(self, arg__1: PySide2.QtGui.QFont):
        'resolve(self) -> int\nresolve(self, arg__1:PySide2.QtGui.QFont) -> PySide2.QtGui.QFont\nresolve(self, mask:int)'
        return 1
    
    def setBold(self, arg__1):
        'setBold(self, arg__1:bool)'
        pass
    
    def setCapitalization(self, arg__1):
        'setCapitalization(self, arg__1:PySide2.QtGui.QFont.Capitalization)'
        pass
    
    def setFamilies(self, arg__1):
        'setFamilies(self, arg__1:typing.Sequence)'
        pass
    
    def setFamily(self, arg__1):
        'setFamily(self, arg__1:str)'
        pass
    
    def setFixedPitch(self, arg__1):
        'setFixedPitch(self, arg__1:bool)'
        pass
    
    def setHintingPreference(self, hintingPreference):
        'setHintingPreference(self, hintingPreference:PySide2.QtGui.QFont.HintingPreference)'
        pass
    
    def setItalic(self, b):
        'setItalic(self, b:bool)'
        pass
    
    def setKerning(self, arg__1):
        'setKerning(self, arg__1:bool)'
        pass
    
    def setLetterSpacing(self, type, spacing):
        'setLetterSpacing(self, type:PySide2.QtGui.QFont.SpacingType, spacing:float)'
        pass
    
    def setOverline(self, arg__1):
        'setOverline(self, arg__1:bool)'
        pass
    
    def setPixelSize(self, arg__1):
        'setPixelSize(self, arg__1:int)'
        pass
    
    def setPointSize(self, arg__1):
        'setPointSize(self, arg__1:int)'
        pass
    
    def setPointSizeF(self, arg__1):
        'setPointSizeF(self, arg__1:float)'
        pass
    
    def setRawMode(self, arg__1):
        'setRawMode(self, arg__1:bool)'
        pass
    
    def setRawName(self, arg__1):
        'setRawName(self, arg__1:str)'
        pass
    
    def setStretch(self, arg__1):
        'setStretch(self, arg__1:int)'
        pass
    
    def setStrikeOut(self, arg__1):
        'setStrikeOut(self, arg__1:bool)'
        pass
    
    def setStyle(self, style):
        'setStyle(self, style:PySide2.QtGui.QFont.Style)'
        pass
    
    def setStyleHint(self, arg__1, strategy):
        'setStyleHint(self, arg__1:PySide2.QtGui.QFont.StyleHint, strategy:PySide2.QtGui.QFont.StyleStrategy=PySide2.QtGui.QFont.StyleStrategy.PreferDefault)'
        pass
    
    def setStyleName(self, arg__1):
        'setStyleName(self, arg__1:str)'
        pass
    
    def setStyleStrategy(self, s):
        'setStyleStrategy(self, s:PySide2.QtGui.QFont.StyleStrategy)'
        pass
    
    def setUnderline(self, arg__1):
        'setUnderline(self, arg__1:bool)'
        pass
    
    def setWeight(self, arg__1):
        'setWeight(self, arg__1:int)'
        pass
    
    def setWordSpacing(self, spacing):
        'setWordSpacing(self, spacing:float)'
        pass
    
    def stretch(self):
        'stretch(self) -> int'
        return int
    
    def strikeOut(self):
        'strikeOut(self) -> bool'
        return bool
    
    def style(self):
        'style(self) -> PySide2.QtGui.QFont.Style'
        return PySide2.QtGui.QFont.Style
    
    def styleHint(self):
        'styleHint(self) -> PySide2.QtGui.QFont.StyleHint'
        return PySide2.QtGui.QFont.StyleHint
    
    def styleName(self):
        'styleName(self) -> str'
        return str
    
    def styleStrategy(self):
        'styleStrategy(self) -> PySide2.QtGui.QFont.StyleStrategy'
        return PySide2.QtGui.QFont.StyleStrategy
    
    @classmethod
    def substitute(cls, arg__1):
        'substitute(arg__1:str) -> str'
        return str
    
    @classmethod
    def substitutes(cls, arg__1):
        'substitutes(arg__1:str) -> typing.List'
        return typing.List
    
    @classmethod
    def substitutions(cls):
        'substitutions() -> typing.List'
        return typing.List
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QFont)'
        pass
    
    def toString(self):
        'toString(self) -> str'
        return str
    
    def underline(self):
        'underline(self) -> bool'
        return bool
    
    def weight(self):
        'weight(self) -> int'
        return int
    
    def wordSpacing(self):
        'wordSpacing(self) -> float'
        return float
    

class QFontDatabase(_mod_Shiboken.Object):
    'QFontDatabase(self)\nQFontDatabase(self, QFontDatabase:PySide2.QtGui.QFontDatabase)'
    Any = WritingSystem()
    Arabic = WritingSystem()
    Armenian = WritingSystem()
    Bengali = WritingSystem()
    Cyrillic = WritingSystem()
    Devanagari = WritingSystem()
    FixedFont = SystemFont()
    GeneralFont = SystemFont()
    Georgian = WritingSystem()
    Greek = WritingSystem()
    Gujarati = WritingSystem()
    Gurmukhi = WritingSystem()
    Hebrew = WritingSystem()
    Japanese = WritingSystem()
    Kannada = WritingSystem()
    Khmer = WritingSystem()
    Korean = WritingSystem()
    Lao = WritingSystem()
    Latin = WritingSystem()
    Malayalam = WritingSystem()
    Myanmar = WritingSystem()
    Nko = WritingSystem()
    Ogham = WritingSystem()
    Oriya = WritingSystem()
    Other = WritingSystem()
    Runic = WritingSystem()
    SimplifiedChinese = WritingSystem()
    Sinhala = WritingSystem()
    SmallestReadableFont = SystemFont()
    Symbol = WritingSystem()
    Syriac = WritingSystem()
    SystemFont = SystemFont
    Tamil = WritingSystem()
    Telugu = WritingSystem()
    Thaana = WritingSystem()
    Thai = WritingSystem()
    Tibetan = WritingSystem()
    TitleFont = SystemFont()
    TraditionalChinese = WritingSystem()
    Vietnamese = WritingSystem()
    WritingSystem = WritingSystem
    WritingSystemsCount = WritingSystem()
    __class__ = QFontDatabase
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, QFontDatabase: PySide2.QtGui.QFontDatabase):
        'QFontDatabase(self)\nQFontDatabase(self, QFontDatabase:PySide2.QtGui.QFontDatabase)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def addApplicationFont(cls, fileName):
        'addApplicationFont(fileName:str) -> int'
        return int
    
    @classmethod
    def addApplicationFontFromData(cls, fontData):
        'addApplicationFontFromData(fontData:PySide2.QtCore.QByteArray) -> int'
        return int
    
    @classmethod
    def applicationFontFamilies(cls, id):
        'applicationFontFamilies(id:int) -> typing.List'
        return typing.List
    
    def bold(self, family, style):
        'bold(self, family:str, style:str) -> bool'
        return bool
    
    def families(self, writingSystem):
        'families(self, writingSystem:PySide2.QtGui.QFontDatabase.WritingSystem=PySide2.QtGui.QFontDatabase.WritingSystem.Any) -> typing.List'
        return typing.List
    
    def font(self, family, style, pointSize):
        'font(self, family:str, style:str, pointSize:int) -> PySide2.QtGui.QFont'
        return PySide2.QtGui.QFont
    
    def hasFamily(self, family):
        'hasFamily(self, family:str) -> bool'
        return bool
    
    def isBitmapScalable(self, family, style):
        "isBitmapScalable(self, family:str, style:str='') -> bool"
        return bool
    
    def isFixedPitch(self, family, style):
        "isFixedPitch(self, family:str, style:str='') -> bool"
        return bool
    
    def isPrivateFamily(self, family):
        'isPrivateFamily(self, family:str) -> bool'
        return bool
    
    def isScalable(self, family, style):
        "isScalable(self, family:str, style:str='') -> bool"
        return bool
    
    def isSmoothlyScalable(self, family, style):
        "isSmoothlyScalable(self, family:str, style:str='') -> bool"
        return bool
    
    def italic(self, family, style):
        'italic(self, family:str, style:str) -> bool'
        return bool
    
    def pointSizes(self, family, style):
        "pointSizes(self, family:str, style:str='') -> typing.List"
        return typing.List
    
    @classmethod
    def removeAllApplicationFonts(cls):
        'removeAllApplicationFonts() -> bool'
        return bool
    
    @classmethod
    def removeApplicationFont(cls, id):
        'removeApplicationFont(id:int) -> bool'
        return bool
    
    def smoothSizes(self, family, style):
        'smoothSizes(self, family:str, style:str) -> typing.List'
        return typing.List
    
    @classmethod
    def standardSizes(cls):
        'standardSizes() -> typing.List'
        return typing.List
    
    def styleString(self, fontInfo: PySide2.QtGui.QFontInfo):
        'styleString(self, font:PySide2.QtGui.QFont) -> str\nstyleString(self, fontInfo:PySide2.QtGui.QFontInfo) -> str'
        return ''
    
    def styles(self, family):
        'styles(self, family:str) -> typing.List'
        return typing.List
    
    @classmethod
    def supportsThreadedFontRendering(cls):
        'supportsThreadedFontRendering() -> bool'
        return bool
    
    @classmethod
    def systemFont(cls, type):
        'systemFont(type:PySide2.QtGui.QFontDatabase.SystemFont) -> PySide2.QtGui.QFont'
        return PySide2.QtGui.QFont
    
    def weight(self, family, style):
        'weight(self, family:str, style:str) -> int'
        return int
    
    @classmethod
    def writingSystemName(cls, writingSystem):
        'writingSystemName(writingSystem:PySide2.QtGui.QFontDatabase.WritingSystem) -> str'
        return str
    
    @classmethod
    def writingSystemSample(cls, writingSystem):
        'writingSystemSample(writingSystem:PySide2.QtGui.QFontDatabase.WritingSystem) -> str'
        return str
    
    def writingSystems(self, family: str):
        'writingSystems(self) -> typing.List\nwritingSystems(self, family:str) -> typing.List'
        pass
    

class QFontInfo(_mod_Shiboken.Object):
    'QFontInfo(self, arg__1:PySide2.QtGui.QFont)\nQFontInfo(self, arg__1:PySide2.QtGui.QFontInfo)'
    __class__ = QFontInfo
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, arg__1: PySide2.QtGui.QFontInfo):
        'QFontInfo(self, arg__1:PySide2.QtGui.QFont)\nQFontInfo(self, arg__1:PySide2.QtGui.QFontInfo)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bold(self):
        'bold(self) -> bool'
        return bool
    
    def exactMatch(self):
        'exactMatch(self) -> bool'
        return bool
    
    def family(self):
        'family(self) -> str'
        return str
    
    def fixedPitch(self):
        'fixedPitch(self) -> bool'
        return bool
    
    def italic(self):
        'italic(self) -> bool'
        return bool
    
    def overline(self):
        'overline(self) -> bool'
        return bool
    
    def pixelSize(self):
        'pixelSize(self) -> int'
        return int
    
    def pointSize(self):
        'pointSize(self) -> int'
        return int
    
    def pointSizeF(self):
        'pointSizeF(self) -> float'
        return float
    
    def rawMode(self):
        'rawMode(self) -> bool'
        return bool
    
    def strikeOut(self):
        'strikeOut(self) -> bool'
        return bool
    
    def style(self):
        'style(self) -> PySide2.QtGui.QFont.Style'
        return PySide2.QtGui.QFont.Style
    
    def styleHint(self):
        'styleHint(self) -> PySide2.QtGui.QFont.StyleHint'
        return PySide2.QtGui.QFont.StyleHint
    
    def styleName(self):
        'styleName(self) -> str'
        return str
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QFontInfo)'
        pass
    
    def underline(self):
        'underline(self) -> bool'
        return bool
    
    def weight(self):
        'weight(self) -> int'
        return int
    

class QFontMetrics(_mod_Shiboken.Object):
    'QFontMetrics(self, arg__1:PySide2.QtGui.QFont)\nQFontMetrics(self, arg__1:PySide2.QtGui.QFontMetrics)\nQFontMetrics(self, font:PySide2.QtGui.QFont, pd:PySide2.QtGui.QPaintDevice)'
    __class__ = QFontMetrics
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, font: PySide2.QtGui.QFont, pd: PySide2.QtGui.QPaintDevice):
        'QFontMetrics(self, arg__1:PySide2.QtGui.QFont)\nQFontMetrics(self, arg__1:PySide2.QtGui.QFontMetrics)\nQFontMetrics(self, font:PySide2.QtGui.QFont, pd:PySide2.QtGui.QPaintDevice)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def ascent(self):
        'ascent(self) -> int'
        return int
    
    def averageCharWidth(self):
        'averageCharWidth(self) -> int'
        return int
    
    def boundingRect(self, x: int, y: int, w: int, h: int, flags: int, text: str, tabstops: int=0, tabarray: typing.Union[typing.Sequence[int],NoneType]=None):
        'boundingRect(self, r:PySide2.QtCore.QRect, flags:int, text:str, tabstops:int=0, tabarray:typing.Union[typing.Sequence[int], NoneType]=None) -> PySide2.QtCore.QRect\nboundingRect(self, text:str) -> PySide2.QtCore.QRect\nboundingRect(self, x:int, y:int, w:int, h:int, flags:int, text:str, tabstops:int=0, tabarray:typing.Union[typing.Sequence[int], NoneType]=None) -> PySide2.QtCore.QRect'
        pass
    
    def boundingRectChar(self, arg__1):
        'boundingRectChar(self, arg__1:str) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def capHeight(self):
        'capHeight(self) -> int'
        return int
    
    def charWidth(self, str, pos):
        'charWidth(self, str:str, pos:int) -> int'
        return int
    
    def descent(self):
        'descent(self) -> int'
        return int
    
    def elidedText(self, text, mode, width, flags):
        'elidedText(self, text:str, mode:PySide2.QtCore.Qt.TextElideMode, width:int, flags:int=0) -> str'
        return str
    
    def fontDpi(self):
        'fontDpi(self) -> float'
        return float
    
    def height(self):
        'height(self) -> int'
        return int
    
    def horizontalAdvance(self, arg__1: str, len: int=-1):
        'horizontalAdvance(self, arg__1:str) -> int\nhorizontalAdvance(self, arg__1:str, len:int=-1) -> int'
        return 1
    
    def inFont(self, arg__1):
        'inFont(self, arg__1:str) -> bool'
        return bool
    
    def inFontUcs4(self, ucs4):
        'inFontUcs4(self, ucs4:int) -> bool'
        return bool
    
    def leading(self):
        'leading(self) -> int'
        return int
    
    def leftBearing(self, arg__1):
        'leftBearing(self, arg__1:str) -> int'
        return int
    
    def lineSpacing(self):
        'lineSpacing(self) -> int'
        return int
    
    def lineWidth(self):
        'lineWidth(self) -> int'
        return int
    
    def maxWidth(self):
        'maxWidth(self) -> int'
        return int
    
    def minLeftBearing(self):
        'minLeftBearing(self) -> int'
        return int
    
    def minRightBearing(self):
        'minRightBearing(self) -> int'
        return int
    
    def overlinePos(self):
        'overlinePos(self) -> int'
        return int
    
    def rightBearing(self, arg__1):
        'rightBearing(self, arg__1:str) -> int'
        return int
    
    def size(self, flags, str, tabstops, tabarray):
        'size(self, flags:int, str:str, tabstops:int=0, tabarray:typing.Union[typing.Sequence[int], NoneType]=None) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def strikeOutPos(self):
        'strikeOutPos(self) -> int'
        return int
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QFontMetrics)'
        pass
    
    def tightBoundingRect(self, text):
        'tightBoundingRect(self, text:str) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def underlinePos(self):
        'underlinePos(self) -> int'
        return int
    
    def width(self, arg__1: str, len: int, flags: int):
        'width(self, arg__1:str, len:int, flags:int) -> int\nwidth(self, arg__1:str, len:int=-1) -> int'
        return 1
    
    def widthChar(self, arg__1):
        'widthChar(self, arg__1:str) -> int'
        return int
    
    def xHeight(self):
        'xHeight(self) -> int'
        return int
    

class QFontMetricsF(_mod_Shiboken.Object):
    'QFontMetricsF(self, arg__1:PySide2.QtGui.QFontMetrics)\nQFontMetricsF(self, arg__1:PySide2.QtGui.QFontMetricsF)\nQFontMetricsF(self, font:PySide2.QtGui.QFont)\nQFontMetricsF(self, font:PySide2.QtGui.QFont, pd:PySide2.QtGui.QPaintDevice)'
    __class__ = QFontMetricsF
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, font: PySide2.QtGui.QFont, pd: PySide2.QtGui.QPaintDevice):
        'QFontMetricsF(self, arg__1:PySide2.QtGui.QFontMetrics)\nQFontMetricsF(self, arg__1:PySide2.QtGui.QFontMetricsF)\nQFontMetricsF(self, font:PySide2.QtGui.QFont)\nQFontMetricsF(self, font:PySide2.QtGui.QFont, pd:PySide2.QtGui.QPaintDevice)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def ascent(self):
        'ascent(self) -> float'
        return float
    
    def averageCharWidth(self):
        'averageCharWidth(self) -> float'
        return float
    
    def boundingRect(self, r: PySide2.QtCore.QRectF, flags: int, string: str, tabstops: int=0, tabarray: typing.Union[typing.Sequence[int],NoneType]=None):
        'boundingRect(self, r:PySide2.QtCore.QRectF, flags:int, string:str, tabstops:int=0, tabarray:typing.Union[typing.Sequence[int], NoneType]=None) -> PySide2.QtCore.QRectF\nboundingRect(self, string:str) -> PySide2.QtCore.QRectF'
        pass
    
    def boundingRectChar(self, arg__1):
        'boundingRectChar(self, arg__1:str) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def capHeight(self):
        'capHeight(self) -> float'
        return float
    
    def descent(self):
        'descent(self) -> float'
        return float
    
    def elidedText(self, text, mode, width, flags):
        'elidedText(self, text:str, mode:PySide2.QtCore.Qt.TextElideMode, width:float, flags:int=0) -> str'
        return str
    
    def fontDpi(self):
        'fontDpi(self) -> float'
        return float
    
    def height(self):
        'height(self) -> float'
        return float
    
    def horizontalAdvance(self, string: str, length: int=-1):
        'horizontalAdvance(self, arg__1:str) -> float\nhorizontalAdvance(self, string:str, length:int=-1) -> float'
        return 1.0
    
    def inFont(self, arg__1):
        'inFont(self, arg__1:str) -> bool'
        return bool
    
    def inFontUcs4(self, ucs4):
        'inFontUcs4(self, ucs4:int) -> bool'
        return bool
    
    def leading(self):
        'leading(self) -> float'
        return float
    
    def leftBearing(self, arg__1):
        'leftBearing(self, arg__1:str) -> float'
        return float
    
    def lineSpacing(self):
        'lineSpacing(self) -> float'
        return float
    
    def lineWidth(self):
        'lineWidth(self) -> float'
        return float
    
    def maxWidth(self):
        'maxWidth(self) -> float'
        return float
    
    def minLeftBearing(self):
        'minLeftBearing(self) -> float'
        return float
    
    def minRightBearing(self):
        'minRightBearing(self) -> float'
        return float
    
    def overlinePos(self):
        'overlinePos(self) -> float'
        return float
    
    def rightBearing(self, arg__1):
        'rightBearing(self, arg__1:str) -> float'
        return float
    
    def size(self, flags, str, tabstops, tabarray):
        'size(self, flags:int, str:str, tabstops:int=0, tabarray:typing.Union[typing.Sequence[int], NoneType]=None) -> PySide2.QtCore.QSizeF'
        return PySide2.QtCore.QSizeF
    
    def strikeOutPos(self):
        'strikeOutPos(self) -> float'
        return float
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QFontMetricsF)'
        pass
    
    def tightBoundingRect(self, text):
        'tightBoundingRect(self, text:str) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def underlinePos(self):
        'underlinePos(self) -> float'
        return float
    
    def width(self, string):
        'width(self, string:str) -> float'
        return float
    
    def widthChar(self, arg__1):
        'widthChar(self, arg__1:str) -> float'
        return float
    
    def xHeight(self):
        'xHeight(self) -> float'
        return float
    

class QGradient(_mod_Shiboken.Object):
    'QGradient(self)\nQGradient(self, QGradient:PySide2.QtGui.QGradient)\nQGradient(self, arg__1:PySide2.QtGui.QGradient.Preset)'
    AboveTheSky = Preset()
    AfricanField = Preset()
    AlchemistLab = Preset()
    AmourAmour = Preset()
    AmyCrisp = Preset()
    AngelCare = Preset()
    AquaGuidance = Preset()
    AquaSplash = Preset()
    AwesomePine = Preset()
    BigMango = Preset()
    BlackSea = Preset()
    Blessing = Preset()
    BurningSpring = Preset()
    CheerfulCaramel = Preset()
    ChildCare = Preset()
    CleanMirror = Preset()
    CloudyApple = Preset()
    CloudyKnoxville = Preset()
    CochitiLake = Preset()
    ColdEvening = Preset()
    ColorInterpolation = InterpolationMode()
    ColorfulPeach = Preset()
    ComponentInterpolation = InterpolationMode()
    ConfidentCloud = Preset()
    ConicalGradient = Type()
    CoordinateMode = CoordinateMode
    CrystalRiver = Preset()
    Crystalline = Preset()
    DeepBlue = Preset()
    DeepRelief = Preset()
    DenseWater = Preset()
    DesertHump = Preset()
    DirtyBeauty = Preset()
    DustyGrass = Preset()
    EternalConstance = Preset()
    EverlastingSky = Preset()
    FabledSunset = Preset()
    FarawayRiver = Preset()
    FebruaryInk = Preset()
    FlyHigh = Preset()
    FlyingLemon = Preset()
    ForestInei = Preset()
    FreshMilk = Preset()
    FreshOasis = Preset()
    FrozenBerry = Preset()
    FrozenDreams = Preset()
    FrozenHeat = Preset()
    FruitBlend = Preset()
    GagarinView = Preset()
    GentleCare = Preset()
    GlassWater = Preset()
    GrassShampoo = Preset()
    GreatWhale = Preset()
    GrownEarly = Preset()
    HappyAcid = Preset()
    HappyFisher = Preset()
    HappyMemories = Preset()
    HappyUnicorn = Preset()
    HealthyWater = Preset()
    HeavenPeach = Preset()
    HeavyRain = Preset()
    HiddenJaguar = Preset()
    HighFlight = Preset()
    InterpolationMode = InterpolationMode
    ItmeoBranding = Preset()
    JapanBlush = Preset()
    JuicyCake = Preset()
    JuicyPeach = Preset()
    JungleDay = Preset()
    KindSteel = Preset()
    LadogaBottom = Preset()
    LadyLips = Preset()
    LandingAircraft = Preset()
    LeCocktail = Preset()
    LemonGate = Preset()
    LightBlue = Preset()
    LilyMeadow = Preset()
    LinearGradient = Type()
    LogicalMode = CoordinateMode()
    LoveKiss = Preset()
    MagicLake = Preset()
    MagicRay = Preset()
    MalibuBeach = Preset()
    MarbleWall = Preset()
    MarsParty = Preset()
    MeanFruit = Preset()
    MidnightBloom = Preset()
    MillenniumPine = Preset()
    MindCrawl = Preset()
    MixedHopes = Preset()
    MoleHall = Preset()
    MorningSalad = Preset()
    MorpheusDen = Preset()
    MountainRock = Preset()
    NearMoon = Preset()
    Nega = Preset()
    NewLife = Preset()
    NewRetrowave = Preset()
    NewYork = Preset()
    NightCall = Preset()
    NightFade = Preset()
    NightParty = Preset()
    NightSky = Preset()
    NoGradient = Type()
    NorseBeauty = Preset()
    NorthMiracle = Preset()
    NumPresets = Preset()
    ObjectBoundingMode = CoordinateMode()
    ObjectMode = CoordinateMode()
    OctoberSilence = Preset()
    OldHat = Preset()
    OrangeJuice = Preset()
    OverSun = Preset()
    PadSpread = Spread()
    PaloAlto = Preset()
    PartyBliss = Preset()
    PassionateBed = Preset()
    PerfectBlue = Preset()
    PerfectWhite = Preset()
    PhoenixStart = Preset()
    PlumBath = Preset()
    PlumPlate = Preset()
    PoliteRumors = Preset()
    PremiumDark = Preset()
    PremiumWhite = Preset()
    Preset = Preset
    PurpleDivision = Preset()
    RadialGradient = Type()
    RainyAshville = Preset()
    RareWind = Preset()
    RedSalvation = Preset()
    ReflectSpread = Spread()
    RepeatSpread = Spread()
    RichMetal = Preset()
    RipeMalinka = Preset()
    RiskyConcrete = Preset()
    RiverCity = Preset()
    RoyalGarden = Preset()
    SaintPetersburg = Preset()
    SaltMountain = Preset()
    SandStrike = Preset()
    SeaLord = Preset()
    SeaStrike = Preset()
    Seashore = Preset()
    ShadyWater = Preset()
    SharpBlues = Preset()
    SharpeyeEagle = Preset()
    ShyRainbow = Preset()
    SkyGlider = Preset()
    SleeplessNight = Preset()
    SmartIndigo = Preset()
    SmilingRain = Preset()
    SnowAgain = Preset()
    SoftCherish = Preset()
    SoftGrass = Preset()
    SoftLipstick = Preset()
    SolidStone = Preset()
    SpaceShift = Preset()
    SpikyNaga = Preset()
    Spread = Spread
    SpringWarmth = Preset()
    StarWine = Preset()
    StretchToDeviceMode = CoordinateMode()
    StrictNovember = Preset()
    StrongBliss = Preset()
    StrongStick = Preset()
    SugarLollipop = Preset()
    SummerGames = Preset()
    SunVeggie = Preset()
    SunnyMorning = Preset()
    SupremeSky = Preset()
    SweetDessert = Preset()
    SweetPeriod = Preset()
    TeenNotebook = Preset()
    TeenParty = Preset()
    TemptingAzure = Preset()
    TrueSunset = Preset()
    Type = Type
    ViciousStance = Preset()
    WarmFlame = Preset()
    WideMatrix = Preset()
    WildApple = Preset()
    WinterNeva = Preset()
    WitchDance = Preset()
    YoungGrass = Preset()
    YoungPassion = Preset()
    ZeusMiracle = Preset()
    __class__ = QGradient
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, arg__1: PySide2.QtGui.QGradient.Preset):
        'QGradient(self)\nQGradient(self, QGradient:PySide2.QtGui.QGradient)\nQGradient(self, arg__1:PySide2.QtGui.QGradient.Preset)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def coordinateMode(self):
        'coordinateMode(self) -> PySide2.QtGui.QGradient.CoordinateMode'
        return PySide2.QtGui.QGradient.CoordinateMode
    
    def interpolationMode(self):
        'interpolationMode(self) -> PySide2.QtGui.QGradient.InterpolationMode'
        return PySide2.QtGui.QGradient.InterpolationMode
    
    def setColorAt(self, pos, color):
        'setColorAt(self, pos:float, color:PySide2.QtGui.QColor)'
        pass
    
    def setCoordinateMode(self, mode):
        'setCoordinateMode(self, mode:PySide2.QtGui.QGradient.CoordinateMode)'
        pass
    
    def setInterpolationMode(self, mode):
        'setInterpolationMode(self, mode:PySide2.QtGui.QGradient.InterpolationMode)'
        pass
    
    def setSpread(self, spread):
        'setSpread(self, spread:PySide2.QtGui.QGradient.Spread)'
        pass
    
    def setStops(self, stops):
        'setStops(self, stops:typing.List)'
        pass
    
    def spread(self):
        'spread(self) -> PySide2.QtGui.QGradient.Spread'
        return PySide2.QtGui.QGradient.Spread
    
    def stops(self):
        'stops(self) -> typing.List'
        return typing.List
    
    def type(self):
        'type(self) -> PySide2.QtGui.QGradient.Type'
        return PySide2.QtGui.QGradient.Type
    

class QGuiApplication(_mod_PySide2_QtCore.QCoreApplication):
    'QGuiApplication(self)\nQGuiApplication(self, arg__1:typing.Sequence)'
    __class__ = QGuiApplication
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, arg__1: typing.Sequence):
        'QGuiApplication(self)\nQGuiApplication(self, arg__1:typing.Sequence)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def allWindows(cls):
        'allWindows() -> typing.List'
        return typing.List
    
    @classmethod
    def applicationDisplayName(cls):
        'applicationDisplayName() -> str'
        return str
    
    def applicationDisplayNameChanged(self):
        pass
    
    @classmethod
    def applicationState(cls):
        'applicationState() -> PySide2.QtCore.Qt.ApplicationState'
        return PySide2.QtCore.Qt.ApplicationState
    
    def applicationStateChanged(self):
        pass
    
    @classmethod
    def changeOverrideCursor(cls, arg__1):
        'changeOverrideCursor(arg__1:PySide2.QtGui.QCursor)'
        pass
    
    @classmethod
    def clipboard(cls):
        'clipboard() -> PySide2.QtGui.QClipboard'
        return PySide2.QtGui.QClipboard
    
    def commitDataRequest(self):
        pass
    
    @classmethod
    def desktopFileName(cls):
        'desktopFileName() -> str'
        return str
    
    @classmethod
    def desktopSettingsAware(cls):
        'desktopSettingsAware() -> bool'
        return bool
    
    def devicePixelRatio(self):
        'devicePixelRatio(self) -> float'
        return float
    
    def event(self, arg__1):
        'event(self, arg__1:PySide2.QtCore.QEvent) -> bool'
        return bool
    
    @classmethod
    def exec_(cls):
        'exec_() -> int'
        return int
    
    @classmethod
    def focusObject(cls):
        'focusObject() -> PySide2.QtCore.QObject'
        return PySide2.QtCore.QObject
    
    def focusObjectChanged(self):
        pass
    
    @classmethod
    def focusWindow(cls):
        'focusWindow() -> PySide2.QtGui.QWindow'
        return PySide2.QtGui.QWindow
    
    def focusWindowChanged(self):
        pass
    
    @classmethod
    def font(cls):
        'font() -> PySide2.QtGui.QFont'
        return PySide2.QtGui.QFont
    
    def fontChanged(self):
        pass
    
    def fontDatabaseChanged(self):
        pass
    
    @classmethod
    def highDpiScaleFactorRoundingPolicy(cls):
        'highDpiScaleFactorRoundingPolicy() -> PySide2.QtCore.Qt.HighDpiScaleFactorRoundingPolicy'
        return PySide2.QtCore.Qt.HighDpiScaleFactorRoundingPolicy
    
    @classmethod
    def inputMethod(cls):
        'inputMethod() -> PySide2.QtGui.QInputMethod'
        return PySide2.QtGui.QInputMethod
    
    @classmethod
    def isFallbackSessionManagementEnabled(cls):
        'isFallbackSessionManagementEnabled() -> bool'
        return bool
    
    @classmethod
    def isLeftToRight(cls):
        'isLeftToRight() -> bool'
        return bool
    
    @classmethod
    def isRightToLeft(cls):
        'isRightToLeft() -> bool'
        return bool
    
    def isSavingSession(self):
        'isSavingSession(self) -> bool'
        return bool
    
    def isSessionRestored(self):
        'isSessionRestored(self) -> bool'
        return bool
    
    @classmethod
    def keyboardModifiers(cls):
        'keyboardModifiers() -> PySide2.QtCore.Qt.KeyboardModifiers'
        return PySide2.QtCore.Qt.KeyboardModifiers
    
    def lastWindowClosed(self):
        pass
    
    @classmethod
    def layoutDirection(cls):
        'layoutDirection() -> PySide2.QtCore.Qt.LayoutDirection'
        return PySide2.QtCore.Qt.LayoutDirection
    
    def layoutDirectionChanged(self):
        pass
    
    @classmethod
    def modalWindow(cls):
        'modalWindow() -> PySide2.QtGui.QWindow'
        return PySide2.QtGui.QWindow
    
    @classmethod
    def mouseButtons(cls):
        'mouseButtons() -> PySide2.QtCore.Qt.MouseButtons'
        return PySide2.QtCore.Qt.MouseButtons
    
    def notify(self, arg__1, arg__2):
        'notify(self, arg__1:PySide2.QtCore.QObject, arg__2:PySide2.QtCore.QEvent) -> bool'
        return bool
    
    @classmethod
    def overrideCursor(cls):
        'overrideCursor() -> PySide2.QtGui.QCursor'
        return PySide2.QtGui.QCursor
    
    @classmethod
    def palette(cls):
        'palette() -> PySide2.QtGui.QPalette'
        return PySide2.QtGui.QPalette
    
    def paletteChanged(self):
        pass
    
    @classmethod
    def platformName(cls):
        'platformName() -> str'
        return str
    
    @classmethod
    def primaryScreen(cls):
        'primaryScreen() -> PySide2.QtGui.QScreen'
        return PySide2.QtGui.QScreen
    
    def primaryScreenChanged(self):
        pass
    
    @classmethod
    def queryKeyboardModifiers(cls):
        'queryKeyboardModifiers() -> PySide2.QtCore.Qt.KeyboardModifiers'
        return PySide2.QtCore.Qt.KeyboardModifiers
    
    @classmethod
    def quitOnLastWindowClosed(cls):
        'quitOnLastWindowClosed() -> bool'
        return bool
    
    @classmethod
    def restoreOverrideCursor(cls):
        'restoreOverrideCursor()'
        pass
    
    def saveStateRequest(self):
        pass
    
    def screenAdded(self):
        pass
    
    @classmethod
    def screenAt(cls, point):
        'screenAt(point:PySide2.QtCore.QPoint) -> PySide2.QtGui.QScreen'
        return PySide2.QtGui.QScreen
    
    def screenRemoved(self):
        pass
    
    @classmethod
    def screens(cls):
        'screens() -> typing.List'
        return typing.List
    
    def sessionId(self):
        'sessionId(self) -> str'
        return str
    
    def sessionKey(self):
        'sessionKey(self) -> str'
        return str
    
    @classmethod
    def setApplicationDisplayName(cls, name):
        'setApplicationDisplayName(name:str)'
        pass
    
    @classmethod
    def setDesktopFileName(cls, name):
        'setDesktopFileName(name:str)'
        pass
    
    @classmethod
    def setDesktopSettingsAware(cls, on):
        'setDesktopSettingsAware(on:bool)'
        pass
    
    @classmethod
    def setFallbackSessionManagementEnabled(cls, arg__1):
        'setFallbackSessionManagementEnabled(arg__1:bool)'
        pass
    
    @classmethod
    def setFont(cls, arg__1):
        'setFont(arg__1:PySide2.QtGui.QFont)'
        pass
    
    @classmethod
    def setHighDpiScaleFactorRoundingPolicy(cls, policy):
        'setHighDpiScaleFactorRoundingPolicy(policy:PySide2.QtCore.Qt.HighDpiScaleFactorRoundingPolicy)'
        pass
    
    @classmethod
    def setLayoutDirection(cls, direction):
        'setLayoutDirection(direction:PySide2.QtCore.Qt.LayoutDirection)'
        pass
    
    @classmethod
    def setOverrideCursor(cls, arg__1):
        'setOverrideCursor(arg__1:PySide2.QtGui.QCursor)'
        pass
    
    @classmethod
    def setPalette(cls, pal):
        'setPalette(pal:PySide2.QtGui.QPalette)'
        pass
    
    @classmethod
    def setQuitOnLastWindowClosed(cls, quit):
        'setQuitOnLastWindowClosed(quit:bool)'
        pass
    
    @classmethod
    def setWindowIcon(cls, icon):
        'setWindowIcon(icon:PySide2.QtGui.QIcon)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    @classmethod
    def styleHints(cls):
        'styleHints() -> PySide2.QtGui.QStyleHints'
        return PySide2.QtGui.QStyleHints
    
    @classmethod
    def sync(cls):
        'sync()'
        pass
    
    @classmethod
    def topLevelAt(cls, pos):
        'topLevelAt(pos:PySide2.QtCore.QPoint) -> PySide2.QtGui.QWindow'
        return PySide2.QtGui.QWindow
    
    @classmethod
    def topLevelWindows(cls):
        'topLevelWindows() -> typing.List'
        return typing.List
    
    @classmethod
    def windowIcon(cls):
        'windowIcon() -> PySide2.QtGui.QIcon'
        return PySide2.QtGui.QIcon
    

class QHelpEvent(_mod_PySide2_QtCore.QEvent):
    'QHelpEvent(self, type:PySide2.QtCore.QEvent.Type, pos:PySide2.QtCore.QPoint, globalPos:PySide2.QtCore.QPoint)'
    __class__ = QHelpEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, type: PySide2.QtCore.QEvent.Type, pos: PySide2.QtCore.QPoint, globalPos: PySide2.QtCore.QPoint):
        'QHelpEvent(self, type:PySide2.QtCore.QEvent.Type, pos:PySide2.QtCore.QPoint, globalPos:PySide2.QtCore.QPoint)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def globalPos(self):
        'globalPos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def globalX(self):
        'globalX(self) -> int'
        return int
    
    def globalY(self):
        'globalY(self) -> int'
        return int
    
    def pos(self):
        'pos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def x(self):
        'x(self) -> int'
        return int
    
    def y(self):
        'y(self) -> int'
        return int
    

class QHideEvent(_mod_PySide2_QtCore.QEvent):
    'QHideEvent(self)'
    __class__ = QHideEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QHideEvent(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class QHoverEvent(QInputEvent):
    'QHoverEvent(self, type:PySide2.QtCore.QEvent.Type, pos:PySide2.QtCore.QPointF, oldPos:PySide2.QtCore.QPointF, modifiers:PySide2.QtCore.Qt.KeyboardModifiers=PySide2.QtCore.Qt.KeyboardModifier.NoModifier)'
    __class__ = QHoverEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, type: PySide2.QtCore.QEvent.Type, pos: PySide2.QtCore.QPointF, oldPos: PySide2.QtCore.QPointF, modifiers: PySide2.QtCore.Qt.KeyboardModifiers=PySide2.QtCore.Qt.KeyboardModifier.NoModifier):
        'QHoverEvent(self, type:PySide2.QtCore.QEvent.Type, pos:PySide2.QtCore.QPointF, oldPos:PySide2.QtCore.QPointF, modifiers:PySide2.QtCore.Qt.KeyboardModifiers=PySide2.QtCore.Qt.KeyboardModifier.NoModifier)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def oldPos(self):
        'oldPos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def oldPosF(self):
        'oldPosF(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def pos(self):
        'pos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def posF(self):
        'posF(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    

class QIcon(_mod_Shiboken.Object):
    'QIcon(self)\nQIcon(self, engine:PySide2.QtGui.QIconEngine)\nQIcon(self, fileName:str)\nQIcon(self, other:PySide2.QtGui.QIcon)\nQIcon(self, pixmap:PySide2.QtGui.QPixmap)'
    Active = Mode()
    Disabled = Mode()
    Mode = Mode
    Normal = Mode()
    Off = State()
    On = State()
    Selected = Mode()
    State = State
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QIcon
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, engine: PySide2.QtGui.QIconEngine):
        'QIcon(self)\nQIcon(self, engine:PySide2.QtGui.QIconEngine)\nQIcon(self, fileName:str)\nQIcon(self, other:PySide2.QtGui.QIcon)\nQIcon(self, pixmap:PySide2.QtGui.QPixmap)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    __module__ = 'PySide2.QtGui'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QIcon()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QIcon()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def actualSize(self, window: PySide2.QtGui.QWindow, size: PySide2.QtCore.QSize, mode: PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off):
        'actualSize(self, size:PySide2.QtCore.QSize, mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off) -> PySide2.QtCore.QSize\nactualSize(self, window:PySide2.QtGui.QWindow, size:PySide2.QtCore.QSize, mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off) -> PySide2.QtCore.QSize'
        pass
    
    def addFile(self, fileName, size, mode, state):
        'addFile(self, fileName:str, size:PySide2.QtCore.QSize=Default(QSize), mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off)'
        pass
    
    def addPixmap(self, pixmap, mode, state):
        'addPixmap(self, pixmap:PySide2.QtGui.QPixmap, mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off)'
        pass
    
    def availableSizes(self, mode, state):
        'availableSizes(self, mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off) -> typing.List'
        return typing.List
    
    def cacheKey(self):
        'cacheKey(self) -> int'
        return int
    
    @classmethod
    def fallbackSearchPaths(cls):
        'fallbackSearchPaths() -> typing.List'
        return typing.List
    
    @classmethod
    def fallbackThemeName(cls):
        'fallbackThemeName() -> str'
        return str
    
    @classmethod
    def fromTheme(cls, name: str, fallback: PySide2.QtGui.QIcon):
        'fromTheme(name:str) -> PySide2.QtGui.QIcon\nfromTheme(name:str, fallback:PySide2.QtGui.QIcon) -> PySide2.QtGui.QIcon'
        pass
    
    @classmethod
    def hasThemeIcon(cls, name):
        'hasThemeIcon(name:str) -> bool'
        return bool
    
    def isMask(self):
        'isMask(self) -> bool'
        return bool
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def name(self):
        'name(self) -> str'
        return str
    
    def paint(self, painter: PySide2.QtGui.QPainter, x: int, y: int, w: int, h: int, alignment: PySide2.QtCore.Qt.Alignment=PySide2.QtCore.Qt.AlignmentFlag.AlignCenter, mode: PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off):
        'paint(self, painter:PySide2.QtGui.QPainter, rect:PySide2.QtCore.QRect, alignment:PySide2.QtCore.Qt.Alignment=PySide2.QtCore.Qt.AlignmentFlag.AlignCenter, mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off)\npaint(self, painter:PySide2.QtGui.QPainter, x:int, y:int, w:int, h:int, alignment:PySide2.QtCore.Qt.Alignment=PySide2.QtCore.Qt.AlignmentFlag.AlignCenter, mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off)'
        pass
    
    def pixmap(self, window: PySide2.QtGui.QWindow, size: PySide2.QtCore.QSize, mode: PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off):
        'pixmap(self, extent:int, mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off) -> PySide2.QtGui.QPixmap\npixmap(self, size:PySide2.QtCore.QSize, mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off) -> PySide2.QtGui.QPixmap\npixmap(self, w:int, h:int, mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off) -> PySide2.QtGui.QPixmap\npixmap(self, window:PySide2.QtGui.QWindow, size:PySide2.QtCore.QSize, mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off) -> PySide2.QtGui.QPixmap'
        pass
    
    @classmethod
    def setFallbackSearchPaths(cls, paths):
        'setFallbackSearchPaths(paths:typing.Sequence)'
        pass
    
    @classmethod
    def setFallbackThemeName(cls, name):
        'setFallbackThemeName(name:str)'
        pass
    
    def setIsMask(self, isMask):
        'setIsMask(self, isMask:bool)'
        pass
    
    @classmethod
    def setThemeName(cls, path):
        'setThemeName(path:str)'
        pass
    
    @classmethod
    def setThemeSearchPaths(cls, searchpath):
        'setThemeSearchPaths(searchpath:typing.Sequence)'
        pass
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QIcon)'
        pass
    
    @classmethod
    def themeName(cls):
        'themeName() -> str'
        return str
    
    @classmethod
    def themeSearchPaths(cls):
        'themeSearchPaths() -> typing.List'
        return typing.List
    

class QIconDragEvent(_mod_PySide2_QtCore.QEvent):
    'QIconDragEvent(self)'
    __class__ = QIconDragEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QIconDragEvent(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class QIconEngine(_mod_Shiboken.Object):
    'QIconEngine(self)\nQIconEngine(self, other:PySide2.QtGui.QIconEngine)'
    AvailableSizesArgument = AvailableSizesArgument
    AvailableSizesHook = IconEngineHook()
    IconEngineHook = IconEngineHook
    IconNameHook = IconEngineHook()
    IsNullHook = IconEngineHook()
    ScaledPixmapHook = IconEngineHook()
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QIconEngine
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, other: PySide2.QtGui.QIconEngine):
        'QIconEngine(self)\nQIconEngine(self, other:PySide2.QtGui.QIconEngine)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def actualSize(self, size, mode, state):
        'actualSize(self, size:PySide2.QtCore.QSize, mode:PySide2.QtGui.QIcon.Mode, state:PySide2.QtGui.QIcon.State) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def addFile(self, fileName, size, mode, state):
        'addFile(self, fileName:str, size:PySide2.QtCore.QSize, mode:PySide2.QtGui.QIcon.Mode, state:PySide2.QtGui.QIcon.State)'
        pass
    
    def addPixmap(self, pixmap, mode, state):
        'addPixmap(self, pixmap:PySide2.QtGui.QPixmap, mode:PySide2.QtGui.QIcon.Mode, state:PySide2.QtGui.QIcon.State)'
        pass
    
    def availableSizes(self, mode, state):
        'availableSizes(self, mode:PySide2.QtGui.QIcon.Mode=PySide2.QtGui.QIcon.Mode.Normal, state:PySide2.QtGui.QIcon.State=PySide2.QtGui.QIcon.State.Off) -> typing.List'
        return typing.List
    
    def clone(self):
        'clone(self) -> PySide2.QtGui.QIconEngine'
        return PySide2.QtGui.QIconEngine
    
    def iconName(self):
        'iconName(self) -> str'
        return str
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def key(self):
        'key(self) -> str'
        return str
    
    def paint(self, painter, rect, mode, state):
        'paint(self, painter:PySide2.QtGui.QPainter, rect:PySide2.QtCore.QRect, mode:PySide2.QtGui.QIcon.Mode, state:PySide2.QtGui.QIcon.State)'
        pass
    
    def pixmap(self, size, mode, state):
        'pixmap(self, size:PySide2.QtCore.QSize, mode:PySide2.QtGui.QIcon.Mode, state:PySide2.QtGui.QIcon.State) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    def read(self, in_):
        'read(self, in_:PySide2.QtCore.QDataStream) -> bool'
        return bool
    
    def scaledPixmap(self, size, mode, state, scale):
        'scaledPixmap(self, size:PySide2.QtCore.QSize, mode:PySide2.QtGui.QIcon.Mode, state:PySide2.QtGui.QIcon.State, scale:float) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    def write(self, out):
        'write(self, out:PySide2.QtCore.QDataStream) -> bool'
        return bool
    

class QImage(QPaintDevice):
    'QImage(self)\nQImage(self, arg__1:PySide2.QtGui.QImage)\nQImage(self, arg__1:str, arg__2:int, arg__3:int, arg__4:PySide2.QtGui.QImage.Format)\nQImage(self, arg__1:str, arg__2:int, arg__3:int, arg__4:int, arg__5:PySide2.QtGui.QImage.Format)\nQImage(self, data:bytes, width:int, height:int, bytesPerLine:int, format:PySide2.QtGui.QImage.Format, cleanupFunction:typing.Union[typing.Callable, NoneType]=None, cleanupInfo:typing.Union[int, NoneType]=None)\nQImage(self, data:bytes, width:int, height:int, format:PySide2.QtGui.QImage.Format, cleanupFunction:typing.Union[typing.Callable, NoneType]=None, cleanupInfo:typing.Union[int, NoneType]=None)\nQImage(self, fileName:str, format:typing.Union[bytes, NoneType]=None)\nQImage(self, size:PySide2.QtCore.QSize, format:PySide2.QtGui.QImage.Format)\nQImage(self, width:int, height:int, format:PySide2.QtGui.QImage.Format)\nQImage(self, xpm:typing.Sequence)'
    Format = Format
    Format_A2BGR30_Premultiplied = Format()
    Format_A2RGB30_Premultiplied = Format()
    Format_ARGB32 = Format()
    Format_ARGB32_Premultiplied = Format()
    Format_ARGB4444_Premultiplied = Format()
    Format_ARGB6666_Premultiplied = Format()
    Format_ARGB8555_Premultiplied = Format()
    Format_ARGB8565_Premultiplied = Format()
    Format_Alpha8 = Format()
    Format_BGR30 = Format()
    Format_BGR888 = Format()
    Format_Grayscale16 = Format()
    Format_Grayscale8 = Format()
    Format_Indexed8 = Format()
    Format_Invalid = Format()
    Format_Mono = Format()
    Format_MonoLSB = Format()
    Format_RGB16 = Format()
    Format_RGB30 = Format()
    Format_RGB32 = Format()
    Format_RGB444 = Format()
    Format_RGB555 = Format()
    Format_RGB666 = Format()
    Format_RGB888 = Format()
    Format_RGBA64 = Format()
    Format_RGBA64_Premultiplied = Format()
    Format_RGBA8888 = Format()
    Format_RGBA8888_Premultiplied = Format()
    Format_RGBX64 = Format()
    Format_RGBX8888 = Format()
    InvertMode = InvertMode
    InvertRgb = InvertMode()
    InvertRgba = InvertMode()
    NImageFormats = Format()
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QImage
    def __copy__(self):
        '__copy__()'
        pass
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
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
    def __init__(self, data: bytes, width: int, height: int, bytesPerLine: int, format: PySide2.QtGui.QImage.Format, cleanupFunction: typing.Union[typing.Callable,NoneType]=None, cleanupInfo: typing.Union[int,NoneType]=None):
        'QImage(self)\nQImage(self, arg__1:PySide2.QtGui.QImage)\nQImage(self, arg__1:str, arg__2:int, arg__3:int, arg__4:PySide2.QtGui.QImage.Format)\nQImage(self, arg__1:str, arg__2:int, arg__3:int, arg__4:int, arg__5:PySide2.QtGui.QImage.Format)\nQImage(self, data:bytes, width:int, height:int, bytesPerLine:int, format:PySide2.QtGui.QImage.Format, cleanupFunction:typing.Union[typing.Callable, NoneType]=None, cleanupInfo:typing.Union[int, NoneType]=None)\nQImage(self, data:bytes, width:int, height:int, format:PySide2.QtGui.QImage.Format, cleanupFunction:typing.Union[typing.Callable, NoneType]=None, cleanupInfo:typing.Union[int, NoneType]=None)\nQImage(self, fileName:str, format:typing.Union[bytes, NoneType]=None)\nQImage(self, size:PySide2.QtCore.QSize, format:PySide2.QtGui.QImage.Format)\nQImage(self, width:int, height:int, format:PySide2.QtGui.QImage.Format)\nQImage(self, xpm:typing.Sequence)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QImage()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QImage()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def allGray(self):
        'allGray(self) -> bool'
        return bool
    
    def alphaChannel(self):
        'alphaChannel(self) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def bitPlaneCount(self):
        'bitPlaneCount(self) -> int'
        return int
    
    def bits(self):
        'bits(self) -> bytes'
        return bytes
    
    def byteCount(self):
        'byteCount(self) -> int'
        return int
    
    def bytesPerLine(self):
        'bytesPerLine(self) -> int'
        return int
    
    def cacheKey(self):
        'cacheKey(self) -> int'
        return int
    
    def color(self, i):
        'color(self, i:int) -> int'
        return int
    
    def colorCount(self):
        'colorCount(self) -> int'
        return int
    
    def colorSpace(self):
        'colorSpace(self) -> PySide2.QtGui.QColorSpace'
        return PySide2.QtGui.QColorSpace
    
    def colorTable(self):
        'colorTable(self) -> typing.List'
        return typing.List
    
    def constBits(self):
        'constBits(self) -> bytes'
        return bytes
    
    def constScanLine(self, arg__1):
        'constScanLine(self, arg__1:int) -> bytes'
        return bytes
    
    def convertTo(self, f, flags):
        'convertTo(self, f:PySide2.QtGui.QImage.Format, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor)'
        pass
    
    def convertToColorSpace(self, arg__1):
        'convertToColorSpace(self, arg__1:PySide2.QtGui.QColorSpace)'
        pass
    
    def convertToFormat(self, f: PySide2.QtGui.QImage.Format, colorTable: typing.List, flags: PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor):
        'convertToFormat(self, f:PySide2.QtGui.QImage.Format, colorTable:typing.List, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QImage\nconvertToFormat(self, f:PySide2.QtGui.QImage.Format, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QImage'
        pass
    
    def convertToFormat_helper(self, format, flags):
        'convertToFormat_helper(self, format:PySide2.QtGui.QImage.Format, flags:PySide2.QtCore.Qt.ImageConversionFlags) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def convertToFormat_inplace(self, format, flags):
        'convertToFormat_inplace(self, format:PySide2.QtGui.QImage.Format, flags:PySide2.QtCore.Qt.ImageConversionFlags) -> bool'
        return bool
    
    def convertedToColorSpace(self, arg__1):
        'convertedToColorSpace(self, arg__1:PySide2.QtGui.QColorSpace) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def copy(self, rect: PySide2.QtCore.QRect=Default(QRect)):
        'copy(self, rect:PySide2.QtCore.QRect=Default(QRect)) -> PySide2.QtGui.QImage\ncopy(self, x:int, y:int, w:int, h:int) -> PySide2.QtGui.QImage'
        pass
    
    def createAlphaMask(self, flags):
        'createAlphaMask(self, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def createHeuristicMask(self, clipTight):
        'createHeuristicMask(self, clipTight:bool=True) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def createMaskFromColor(self, color, mode):
        'createMaskFromColor(self, color:int, mode:PySide2.QtCore.Qt.MaskMode=PySide2.QtCore.Qt.MaskMode.MaskInColor) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def depth(self):
        'depth(self) -> int'
        return int
    
    def devType(self):
        'devType(self) -> int'
        return int
    
    def devicePixelRatio(self):
        'devicePixelRatio(self) -> float'
        return float
    
    def dotsPerMeterX(self):
        'dotsPerMeterX(self) -> int'
        return int
    
    def dotsPerMeterY(self):
        'dotsPerMeterY(self) -> int'
        return int
    
    def fill(self, color: PySide2.QtCore.Qt.GlobalColor):
        'fill(self, color:PySide2.QtCore.Qt.GlobalColor)\nfill(self, color:PySide2.QtGui.QColor)\nfill(self, pixel:int)'
        pass
    
    def format(self):
        'format(self) -> PySide2.QtGui.QImage.Format'
        return PySide2.QtGui.QImage.Format
    
    @classmethod
    def fromData(cls, data, format):
        'fromData(data:PySide2.QtCore.QByteArray, format:typing.Union[bytes, NoneType]=None) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def hasAlphaChannel(self):
        'hasAlphaChannel(self) -> bool'
        return bool
    
    def height(self):
        'height(self) -> int'
        return int
    
    def invertPixels(self, mode):
        'invertPixels(self, mode:PySide2.QtGui.QImage.InvertMode=PySide2.QtGui.QImage.InvertMode.InvertRgb)'
        pass
    
    def isGrayscale(self):
        'isGrayscale(self) -> bool'
        return bool
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def load(self, fileName: str, format: typing.Union[bytes,NoneType]=None):
        'load(self, device:PySide2.QtCore.QIODevice, format:bytes) -> bool\nload(self, fileName:str, format:typing.Union[bytes, NoneType]=None) -> bool'
        return True
    
    def loadFromData(self, data, aformat):
        'loadFromData(self, data:PySide2.QtCore.QByteArray, aformat:typing.Union[bytes, NoneType]=None) -> bool'
        return bool
    
    def metric(self, metric):
        'metric(self, metric:PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int'
        return int
    
    def mirrored(self, horizontally, vertically):
        'mirrored(self, horizontally:bool=False, vertically:bool=True) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def mirrored_helper(self, horizontal, vertical):
        'mirrored_helper(self, horizontal:bool, vertical:bool) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def mirrored_inplace(self, horizontal, vertical):
        'mirrored_inplace(self, horizontal:bool, vertical:bool)'
        pass
    
    def offset(self):
        'offset(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def paintEngine(self):
        'paintEngine(self) -> PySide2.QtGui.QPaintEngine'
        return PySide2.QtGui.QPaintEngine
    
    def pixel(self, pt: PySide2.QtCore.QPoint):
        'pixel(self, pt:PySide2.QtCore.QPoint) -> int\npixel(self, x:int, y:int) -> int'
        return 1
    
    def pixelColor(self, pt: PySide2.QtCore.QPoint):
        'pixelColor(self, pt:PySide2.QtCore.QPoint) -> PySide2.QtGui.QColor\npixelColor(self, x:int, y:int) -> PySide2.QtGui.QColor'
        pass
    
    def pixelFormat(self):
        'pixelFormat(self) -> PySide2.QtGui.QPixelFormat'
        return PySide2.QtGui.QPixelFormat
    
    def pixelIndex(self, pt: PySide2.QtCore.QPoint):
        'pixelIndex(self, pt:PySide2.QtCore.QPoint) -> int\npixelIndex(self, x:int, y:int) -> int'
        return 1
    
    def rect(self):
        'rect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def reinterpretAsFormat(self, f):
        'reinterpretAsFormat(self, f:PySide2.QtGui.QImage.Format) -> bool'
        return bool
    
    def rgbSwapped(self):
        'rgbSwapped(self) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def rgbSwapped_helper(self):
        'rgbSwapped_helper(self) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def rgbSwapped_inplace(self):
        'rgbSwapped_inplace(self)'
        pass
    
    def save(self, device: PySide2.QtCore.QIODevice, format: typing.Union[bytes,NoneType]=None, quality: int=-1):
        'save(self, device:PySide2.QtCore.QIODevice, format:typing.Union[bytes, NoneType]=None, quality:int=-1) -> bool\nsave(self, fileName:str, format:typing.Union[bytes, NoneType]=None, quality:int=-1) -> bool'
        return True
    
    def scaled(self, s: PySide2.QtCore.QSize, aspectMode: PySide2.QtCore.Qt.AspectRatioMode=PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, mode: PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation):
        'scaled(self, s:PySide2.QtCore.QSize, aspectMode:PySide2.QtCore.Qt.AspectRatioMode=PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage\nscaled(self, w:int, h:int, aspectMode:PySide2.QtCore.Qt.AspectRatioMode=PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage'
        pass
    
    def scaledToHeight(self, h, mode):
        'scaledToHeight(self, h:int, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def scaledToWidth(self, w, mode):
        'scaledToWidth(self, w:int, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def scanLine(self, arg__1):
        'scanLine(self, arg__1:int) -> bytes'
        return bytes
    
    def setAlphaChannel(self, alphaChannel):
        'setAlphaChannel(self, alphaChannel:PySide2.QtGui.QImage)'
        pass
    
    def setColor(self, i, c):
        'setColor(self, i:int, c:int)'
        pass
    
    def setColorCount(self, arg__1):
        'setColorCount(self, arg__1:int)'
        pass
    
    def setColorSpace(self, arg__1):
        'setColorSpace(self, arg__1:PySide2.QtGui.QColorSpace)'
        pass
    
    def setColorTable(self, colors):
        'setColorTable(self, colors:typing.List)'
        pass
    
    def setDevicePixelRatio(self, scaleFactor):
        'setDevicePixelRatio(self, scaleFactor:float)'
        pass
    
    def setDotsPerMeterX(self, arg__1):
        'setDotsPerMeterX(self, arg__1:int)'
        pass
    
    def setDotsPerMeterY(self, arg__1):
        'setDotsPerMeterY(self, arg__1:int)'
        pass
    
    def setOffset(self, arg__1):
        'setOffset(self, arg__1:PySide2.QtCore.QPoint)'
        pass
    
    def setPixel(self, pt: PySide2.QtCore.QPoint, index_or_rgb: int):
        'setPixel(self, pt:PySide2.QtCore.QPoint, index_or_rgb:int)\nsetPixel(self, x:int, y:int, index_or_rgb:int)'
        pass
    
    def setPixelColor(self, pt: PySide2.QtCore.QPoint, c: PySide2.QtGui.QColor):
        'setPixelColor(self, pt:PySide2.QtCore.QPoint, c:PySide2.QtGui.QColor)\nsetPixelColor(self, x:int, y:int, c:PySide2.QtGui.QColor)'
        pass
    
    def setText(self, key, value):
        'setText(self, key:str, value:str)'
        pass
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def sizeInBytes(self):
        'sizeInBytes(self) -> int'
        return int
    
    def smoothScaled(self, w, h):
        'smoothScaled(self, w:int, h:int) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QImage)'
        pass
    
    def text(self, key):
        "text(self, key:str='') -> str"
        return str
    
    def textKeys(self):
        'textKeys(self) -> typing.List'
        return typing.List
    
    @classmethod
    def toImageFormat(cls, format):
        'toImageFormat(format:PySide2.QtGui.QPixelFormat) -> PySide2.QtGui.QImage.Format'
        return PySide2.QtGui.QImage.Format
    
    @classmethod
    def toPixelFormat(cls, format):
        'toPixelFormat(format:PySide2.QtGui.QImage.Format) -> PySide2.QtGui.QPixelFormat'
        return PySide2.QtGui.QPixelFormat
    
    def transformed(self, matrix: PySide2.QtGui.QTransform, mode: PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation):
        'transformed(self, matrix:PySide2.QtGui.QMatrix, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage\ntransformed(self, matrix:PySide2.QtGui.QTransform, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage'
        pass
    
    @classmethod
    def trueMatrix(cls, arg__1: PySide2.QtGui.QTransform, w: int, h: int):
        'trueMatrix(arg__1:PySide2.QtGui.QMatrix, w:int, h:int) -> PySide2.QtGui.QMatrix\ntrueMatrix(arg__1:PySide2.QtGui.QTransform, w:int, h:int) -> PySide2.QtGui.QTransform'
        pass
    
    def valid(self, pt: PySide2.QtCore.QPoint):
        'valid(self, pt:PySide2.QtCore.QPoint) -> bool\nvalid(self, x:int, y:int) -> bool'
        return True
    
    def width(self):
        'width(self) -> int'
        return int
    

class QImageIOHandler(_mod_Shiboken.Object):
    'QImageIOHandler(self)'
    Animation = ImageOption()
    BackgroundColor = ImageOption()
    ClipRect = ImageOption()
    CompressionRatio = ImageOption()
    Description = ImageOption()
    Endianness = ImageOption()
    Gamma = ImageOption()
    ImageFormat = ImageOption()
    ImageOption = ImageOption
    ImageTransformation = ImageOption()
    IncrementalReading = ImageOption()
    Name = ImageOption()
    OptimizedWrite = ImageOption()
    ProgressiveScanWrite = ImageOption()
    Quality = ImageOption()
    ScaledClipRect = ImageOption()
    ScaledSize = ImageOption()
    Size = ImageOption()
    SubType = ImageOption()
    SupportedSubTypes = ImageOption()
    Transformation = Transformation
    TransformationFlip = Transformation()
    TransformationFlipAndRotate90 = Transformation()
    TransformationMirror = Transformation()
    TransformationMirrorAndRotate90 = Transformation()
    TransformationNone = Transformation()
    TransformationRotate180 = Transformation()
    TransformationRotate270 = Transformation()
    TransformationRotate90 = Transformation()
    Transformations = Transformations
    TransformedByDefault = ImageOption()
    __class__ = QImageIOHandler
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QImageIOHandler(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def canRead(self):
        'canRead(self) -> bool'
        return bool
    
    def currentImageNumber(self):
        'currentImageNumber(self) -> int'
        return int
    
    def currentImageRect(self):
        'currentImageRect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def device(self):
        'device(self) -> PySide2.QtCore.QIODevice'
        return PySide2.QtCore.QIODevice
    
    def format(self):
        'format(self) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    def imageCount(self):
        'imageCount(self) -> int'
        return int
    
    def jumpToImage(self, imageNumber):
        'jumpToImage(self, imageNumber:int) -> bool'
        return bool
    
    def jumpToNextImage(self):
        'jumpToNextImage(self) -> bool'
        return bool
    
    def loopCount(self):
        'loopCount(self) -> int'
        return int
    
    def name(self):
        'name(self) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    def nextImageDelay(self):
        'nextImageDelay(self) -> int'
        return int
    
    def option(self, option):
        'option(self, option:PySide2.QtGui.QImageIOHandler.ImageOption) -> typing.Any'
        return typing.Any
    
    def read(self, image):
        'read(self, image:PySide2.QtGui.QImage) -> bool'
        return bool
    
    def setDevice(self, device):
        'setDevice(self, device:PySide2.QtCore.QIODevice)'
        pass
    
    def setFormat(self, format):
        'setFormat(self, format:PySide2.QtCore.QByteArray)'
        pass
    
    def setOption(self, option, value):
        'setOption(self, option:PySide2.QtGui.QImageIOHandler.ImageOption, value:typing.Any)'
        pass
    
    def supportsOption(self, option):
        'supportsOption(self, option:PySide2.QtGui.QImageIOHandler.ImageOption) -> bool'
        return bool
    
    def write(self, image):
        'write(self, image:PySide2.QtGui.QImage) -> bool'
        return bool
    

class QImageReader(_mod_Shiboken.Object):
    'QImageReader(self)\nQImageReader(self, device:PySide2.QtCore.QIODevice, format:PySide2.QtCore.QByteArray=Default(QByteArray))\nQImageReader(self, fileName:str, format:PySide2.QtCore.QByteArray=Default(QByteArray))'
    DeviceError = ImageReaderError()
    FileNotFoundError = ImageReaderError()
    ImageReaderError = ImageReaderError
    InvalidDataError = ImageReaderError()
    UnknownError = ImageReaderError()
    UnsupportedFormatError = ImageReaderError()
    __class__ = QImageReader
    __dict__ = {}
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, device: PySide2.QtCore.QIODevice, format: PySide2.QtCore.QByteArray=Default(QByteArray)):
        'QImageReader(self)\nQImageReader(self, device:PySide2.QtCore.QIODevice, format:PySide2.QtCore.QByteArray=Default(QByteArray))\nQImageReader(self, fileName:str, format:PySide2.QtCore.QByteArray=Default(QByteArray))'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def autoDetectImageFormat(self):
        'autoDetectImageFormat(self) -> bool'
        return bool
    
    def autoTransform(self):
        'autoTransform(self) -> bool'
        return bool
    
    def backgroundColor(self):
        'backgroundColor(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def canRead(self):
        'canRead(self) -> bool'
        return bool
    
    def clipRect(self):
        'clipRect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def currentImageNumber(self):
        'currentImageNumber(self) -> int'
        return int
    
    def currentImageRect(self):
        'currentImageRect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def decideFormatFromContent(self):
        'decideFormatFromContent(self) -> bool'
        return bool
    
    def device(self):
        'device(self) -> PySide2.QtCore.QIODevice'
        return PySide2.QtCore.QIODevice
    
    def error(self):
        'error(self) -> PySide2.QtGui.QImageReader.ImageReaderError'
        return PySide2.QtGui.QImageReader.ImageReaderError
    
    def errorString(self):
        'errorString(self) -> str'
        return str
    
    def fileName(self):
        'fileName(self) -> str'
        return str
    
    def format(self):
        'format(self) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    def gamma(self):
        'gamma(self) -> float'
        return float
    
    def imageCount(self):
        'imageCount(self) -> int'
        return int
    
    @classmethod
    def imageFormat(cls, device: PySide2.QtCore.QIODevice):
        'imageFormat(device:PySide2.QtCore.QIODevice) -> PySide2.QtCore.QByteArray\nimageFormat(fileName:str) -> PySide2.QtCore.QByteArray\nimageFormat(self) -> PySide2.QtGui.QImage.Format'
        pass
    
    @classmethod
    def imageFormatsForMimeType(cls, mimeType):
        'imageFormatsForMimeType(mimeType:PySide2.QtCore.QByteArray) -> typing.List'
        return typing.List
    
    def jumpToImage(self, imageNumber):
        'jumpToImage(self, imageNumber:int) -> bool'
        return bool
    
    def jumpToNextImage(self):
        'jumpToNextImage(self) -> bool'
        return bool
    
    def loopCount(self):
        'loopCount(self) -> int'
        return int
    
    def nextImageDelay(self):
        'nextImageDelay(self) -> int'
        return int
    
    def quality(self):
        'quality(self) -> int'
        return int
    
    def read(self):
        'read(self) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def scaledClipRect(self):
        'scaledClipRect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def scaledSize(self):
        'scaledSize(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def setAutoDetectImageFormat(self, enabled):
        'setAutoDetectImageFormat(self, enabled:bool)'
        pass
    
    def setAutoTransform(self, enabled):
        'setAutoTransform(self, enabled:bool)'
        pass
    
    def setBackgroundColor(self, color):
        'setBackgroundColor(self, color:PySide2.QtGui.QColor)'
        pass
    
    def setClipRect(self, rect):
        'setClipRect(self, rect:PySide2.QtCore.QRect)'
        pass
    
    def setDecideFormatFromContent(self, ignored):
        'setDecideFormatFromContent(self, ignored:bool)'
        pass
    
    def setDevice(self, device):
        'setDevice(self, device:PySide2.QtCore.QIODevice)'
        pass
    
    def setFileName(self, fileName):
        'setFileName(self, fileName:str)'
        pass
    
    def setFormat(self, format):
        'setFormat(self, format:PySide2.QtCore.QByteArray)'
        pass
    
    def setGamma(self, gamma):
        'setGamma(self, gamma:float)'
        pass
    
    def setQuality(self, quality):
        'setQuality(self, quality:int)'
        pass
    
    def setScaledClipRect(self, rect):
        'setScaledClipRect(self, rect:PySide2.QtCore.QRect)'
        pass
    
    def setScaledSize(self, size):
        'setScaledSize(self, size:PySide2.QtCore.QSize)'
        pass
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def subType(self):
        'subType(self) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    @classmethod
    def supportedImageFormats(cls):
        'supportedImageFormats() -> typing.List'
        return typing.List
    
    @classmethod
    def supportedMimeTypes(cls):
        'supportedMimeTypes() -> typing.List'
        return typing.List
    
    def supportedSubTypes(self):
        'supportedSubTypes(self) -> typing.List'
        return typing.List
    
    def supportsAnimation(self):
        'supportsAnimation(self) -> bool'
        return bool
    
    def supportsOption(self, option):
        'supportsOption(self, option:PySide2.QtGui.QImageIOHandler.ImageOption) -> bool'
        return bool
    
    def text(self, key):
        'text(self, key:str) -> str'
        return str
    
    def textKeys(self):
        'textKeys(self) -> typing.List'
        return typing.List
    
    def transformation(self):
        'transformation(self) -> PySide2.QtGui.QImageIOHandler.Transformations'
        return PySide2.QtGui.QImageIOHandler.Transformations
    

class QImageWriter(_mod_Shiboken.Object):
    'QImageWriter(self)\nQImageWriter(self, device:PySide2.QtCore.QIODevice, format:PySide2.QtCore.QByteArray)\nQImageWriter(self, fileName:str, format:PySide2.QtCore.QByteArray=Default(QByteArray))'
    DeviceError = ImageWriterError()
    ImageWriterError = ImageWriterError
    InvalidImageError = ImageWriterError()
    UnknownError = ImageWriterError()
    UnsupportedFormatError = ImageWriterError()
    __class__ = QImageWriter
    __dict__ = {}
    def __init__(self, fileName: str, format: PySide2.QtCore.QByteArray=Default(QByteArray)):
        'QImageWriter(self)\nQImageWriter(self, device:PySide2.QtCore.QIODevice, format:PySide2.QtCore.QByteArray)\nQImageWriter(self, fileName:str, format:PySide2.QtCore.QByteArray=Default(QByteArray))'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def canWrite(self):
        'canWrite(self) -> bool'
        return bool
    
    def compression(self):
        'compression(self) -> int'
        return int
    
    def description(self):
        'description(self) -> str'
        return str
    
    def device(self):
        'device(self) -> PySide2.QtCore.QIODevice'
        return PySide2.QtCore.QIODevice
    
    def error(self):
        'error(self) -> PySide2.QtGui.QImageWriter.ImageWriterError'
        return PySide2.QtGui.QImageWriter.ImageWriterError
    
    def errorString(self):
        'errorString(self) -> str'
        return str
    
    def fileName(self):
        'fileName(self) -> str'
        return str
    
    def format(self):
        'format(self) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    def gamma(self):
        'gamma(self) -> float'
        return float
    
    @classmethod
    def imageFormatsForMimeType(cls, mimeType):
        'imageFormatsForMimeType(mimeType:PySide2.QtCore.QByteArray) -> typing.List'
        return typing.List
    
    def optimizedWrite(self):
        'optimizedWrite(self) -> bool'
        return bool
    
    def progressiveScanWrite(self):
        'progressiveScanWrite(self) -> bool'
        return bool
    
    def quality(self):
        'quality(self) -> int'
        return int
    
    def setCompression(self, compression):
        'setCompression(self, compression:int)'
        pass
    
    def setDescription(self, description):
        'setDescription(self, description:str)'
        pass
    
    def setDevice(self, device):
        'setDevice(self, device:PySide2.QtCore.QIODevice)'
        pass
    
    def setFileName(self, fileName):
        'setFileName(self, fileName:str)'
        pass
    
    def setFormat(self, format):
        'setFormat(self, format:PySide2.QtCore.QByteArray)'
        pass
    
    def setGamma(self, gamma):
        'setGamma(self, gamma:float)'
        pass
    
    def setOptimizedWrite(self, optimize):
        'setOptimizedWrite(self, optimize:bool)'
        pass
    
    def setProgressiveScanWrite(self, progressive):
        'setProgressiveScanWrite(self, progressive:bool)'
        pass
    
    def setQuality(self, quality):
        'setQuality(self, quality:int)'
        pass
    
    def setSubType(self, type):
        'setSubType(self, type:PySide2.QtCore.QByteArray)'
        pass
    
    def setText(self, key, text):
        'setText(self, key:str, text:str)'
        pass
    
    def setTransformation(self, orientation):
        'setTransformation(self, orientation:PySide2.QtGui.QImageIOHandler.Transformations)'
        pass
    
    def subType(self):
        'subType(self) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    @classmethod
    def supportedImageFormats(cls):
        'supportedImageFormats() -> typing.List'
        return typing.List
    
    @classmethod
    def supportedMimeTypes(cls):
        'supportedMimeTypes() -> typing.List'
        return typing.List
    
    def supportedSubTypes(self):
        'supportedSubTypes(self) -> typing.List'
        return typing.List
    
    def supportsOption(self, option):
        'supportsOption(self, option:PySide2.QtGui.QImageIOHandler.ImageOption) -> bool'
        return bool
    
    def transformation(self):
        'transformation(self) -> PySide2.QtGui.QImageIOHandler.Transformations'
        return PySide2.QtGui.QImageIOHandler.Transformations
    
    def write(self, image):
        'write(self, image:PySide2.QtGui.QImage) -> bool'
        return bool
    

class QInputEvent(_mod_PySide2_QtCore.QEvent):
    'QInputEvent(self, type:PySide2.QtCore.QEvent.Type, modifiers:PySide2.QtCore.Qt.KeyboardModifiers=PySide2.QtCore.Qt.KeyboardModifier.NoModifier)'
    __class__ = QInputEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, type: PySide2.QtCore.QEvent.Type, modifiers: PySide2.QtCore.Qt.KeyboardModifiers=PySide2.QtCore.Qt.KeyboardModifier.NoModifier):
        'QInputEvent(self, type:PySide2.QtCore.QEvent.Type, modifiers:PySide2.QtCore.Qt.KeyboardModifiers=PySide2.QtCore.Qt.KeyboardModifier.NoModifier)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def modifiers(self):
        'modifiers(self) -> PySide2.QtCore.Qt.KeyboardModifiers'
        return PySide2.QtCore.Qt.KeyboardModifiers
    
    def setModifiers(self, amodifiers):
        'setModifiers(self, amodifiers:PySide2.QtCore.Qt.KeyboardModifiers)'
        pass
    
    def setTimestamp(self, atimestamp):
        'setTimestamp(self, atimestamp:int)'
        pass
    
    def timestamp(self):
        'timestamp(self) -> int'
        return int
    
    @property
    def ts(self):
        pass
    

class QInputMethod(_mod_PySide2_QtCore.QObject):
    Action = Action
    Click = Action()
    ContextMenu = Action()
    __class__ = QInputMethod
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def anchorRectangle(self):
        'anchorRectangle(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def anchorRectangleChanged(self):
        pass
    
    def animatingChanged(self):
        pass
    
    def commit(self):
        'commit(self)'
        pass
    
    def cursorRectangle(self):
        'cursorRectangle(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def cursorRectangleChanged(self):
        pass
    
    def hide(self):
        'hide(self)'
        pass
    
    def inputDirection(self):
        'inputDirection(self) -> PySide2.QtCore.Qt.LayoutDirection'
        return PySide2.QtCore.Qt.LayoutDirection
    
    def inputDirectionChanged(self):
        pass
    
    def inputItemClipRectangle(self):
        'inputItemClipRectangle(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def inputItemClipRectangleChanged(self):
        pass
    
    def inputItemRectangle(self):
        'inputItemRectangle(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def inputItemTransform(self):
        'inputItemTransform(self) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def invokeAction(self, a, cursorPosition):
        'invokeAction(self, a:PySide2.QtGui.QInputMethod.Action, cursorPosition:int)'
        pass
    
    def isAnimating(self):
        'isAnimating(self) -> bool'
        return bool
    
    def isVisible(self):
        'isVisible(self) -> bool'
        return bool
    
    def keyboardRectangle(self):
        'keyboardRectangle(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def keyboardRectangleChanged(self):
        pass
    
    def locale(self):
        'locale(self) -> PySide2.QtCore.QLocale'
        return PySide2.QtCore.QLocale
    
    def localeChanged(self):
        pass
    
    @classmethod
    def queryFocusObject(cls, query, argument):
        'queryFocusObject(query:PySide2.QtCore.Qt.InputMethodQuery, argument:typing.Any) -> typing.Any'
        return typing.Any
    
    def reset(self):
        'reset(self)'
        pass
    
    def setInputItemRectangle(self, rect):
        'setInputItemRectangle(self, rect:PySide2.QtCore.QRectF)'
        pass
    
    def setInputItemTransform(self, transform):
        'setInputItemTransform(self, transform:PySide2.QtGui.QTransform)'
        pass
    
    def setVisible(self, visible):
        'setVisible(self, visible:bool)'
        pass
    
    def show(self):
        'show(self)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def update(self, queries):
        'update(self, queries:PySide2.QtCore.Qt.InputMethodQueries)'
        pass
    
    def visibleChanged(self):
        pass
    

class QInputMethodEvent(_mod_PySide2_QtCore.QEvent):
    'QInputMethodEvent(self)\nQInputMethodEvent(self, other:PySide2.QtGui.QInputMethodEvent)\nQInputMethodEvent(self, preeditText:str, attributes:typing.Sequence)'
    Attribute = Attribute
    AttributeType = AttributeType
    Cursor = AttributeType()
    Language = AttributeType()
    Ruby = AttributeType()
    Selection = AttributeType()
    TextFormat = AttributeType()
    __class__ = QInputMethodEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, preeditText: str, attributes: typing.Sequence):
        'QInputMethodEvent(self)\nQInputMethodEvent(self, other:PySide2.QtGui.QInputMethodEvent)\nQInputMethodEvent(self, preeditText:str, attributes:typing.Sequence)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def attributes(self):
        'attributes(self) -> typing.List'
        return typing.List
    
    def commitString(self):
        'commitString(self) -> str'
        return str
    
    def preeditString(self):
        'preeditString(self) -> str'
        return str
    
    def replacementLength(self):
        'replacementLength(self) -> int'
        return int
    
    def replacementStart(self):
        'replacementStart(self) -> int'
        return int
    
    def setCommitString(self, commitString, replaceFrom, replaceLength):
        'setCommitString(self, commitString:str, replaceFrom:int=0, replaceLength:int=0)'
        pass
    

class QInputMethodQueryEvent(_mod_PySide2_QtCore.QEvent):
    'QInputMethodQueryEvent(self, queries:PySide2.QtCore.Qt.InputMethodQueries)'
    __class__ = QInputMethodQueryEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, queries: PySide2.QtCore.Qt.InputMethodQueries):
        'QInputMethodQueryEvent(self, queries:PySide2.QtCore.Qt.InputMethodQueries)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def queries(self):
        'queries(self) -> PySide2.QtCore.Qt.InputMethodQueries'
        return PySide2.QtCore.Qt.InputMethodQueries
    
    def setValue(self, query, value):
        'setValue(self, query:PySide2.QtCore.Qt.InputMethodQuery, value:typing.Any)'
        pass
    
    def value(self, query):
        'value(self, query:PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any'
        return typing.Any
    

class QIntValidator(QValidator):
    'QIntValidator(self, bottom:int, top:int, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQIntValidator(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    __class__ = QIntValidator
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, bottom: int, top: int, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QIntValidator(self, bottom:int, top:int, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQIntValidator(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bottom(self):
        'bottom(self) -> int'
        return int
    
    def bottomChanged(self):
        pass
    
    def fixup(self, input):
        'fixup(self, input:str)'
        pass
    
    def setBottom(self, arg__1):
        'setBottom(self, arg__1:int)'
        pass
    
    def setRange(self, bottom, top):
        'setRange(self, bottom:int, top:int)'
        pass
    
    def setTop(self, arg__1):
        'setTop(self, arg__1:int)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def top(self):
        'top(self) -> int'
        return int
    
    def topChanged(self):
        pass
    
    def validate(self, arg__1, arg__2):
        'validate(self, arg__1:str, arg__2:int) -> PySide2.QtGui.QValidator.State'
        return PySide2.QtGui.QValidator.State
    

class QKeyEvent(QInputEvent):
    "QKeyEvent(self, type:PySide2.QtCore.QEvent.Type, key:int, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, nativeScanCode:int, nativeVirtualKey:int, nativeModifiers:int, text:str='', autorep:bool=False, count:int=1)\nQKeyEvent(self, type:PySide2.QtCore.QEvent.Type, key:int, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, text:str='', autorep:bool=False, count:int=1)"
    __class__ = QKeyEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
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
    def __init__(self, type: PySide2.QtCore.QEvent.Type, key: int, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, nativeScanCode: int, nativeVirtualKey: int, nativeModifiers: int, text: str='', autorep: bool=False, count: int=1):
        "QKeyEvent(self, type:PySide2.QtCore.QEvent.Type, key:int, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, nativeScanCode:int, nativeVirtualKey:int, nativeModifiers:int, text:str='', autorep:bool=False, count:int=1)\nQKeyEvent(self, type:PySide2.QtCore.QEvent.Type, key:int, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, text:str='', autorep:bool=False, count:int=1)"
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def autor(self):
        pass
    
    def count(self):
        'count(self) -> int'
        return int
    
    def isAutoRepeat(self):
        'isAutoRepeat(self) -> bool'
        return bool
    
    def key(self):
        'key(self) -> int'
        return int
    
    def matches(self, key):
        'matches(self, key:PySide2.QtGui.QKeySequence.StandardKey) -> bool'
        return bool
    
    def modifiers(self):
        'modifiers(self) -> PySide2.QtCore.Qt.KeyboardModifiers'
        return PySide2.QtCore.Qt.KeyboardModifiers
    
    @property
    def nModifiers(self):
        pass
    
    @property
    def nScanCode(self):
        pass
    
    @property
    def nVirtualKey(self):
        pass
    
    def nativeModifiers(self):
        'nativeModifiers(self) -> int'
        return int
    
    def nativeScanCode(self):
        'nativeScanCode(self) -> int'
        return int
    
    def nativeVirtualKey(self):
        'nativeVirtualKey(self) -> int'
        return int
    
    def text(self):
        'text(self) -> str'
        return str
    

class QKeySequence(_mod_Shiboken.Object):
    'QKeySequence(self)\nQKeySequence(self, k1:int, k2:int=0, k3:int=0, k4:int=0)\nQKeySequence(self, key:PySide2.QtGui.QKeySequence.StandardKey)\nQKeySequence(self, key:str, format:PySide2.QtGui.QKeySequence.SequenceFormat=PySide2.QtGui.QKeySequence.SequenceFormat.NativeText)\nQKeySequence(self, ks:PySide2.QtGui.QKeySequence)'
    AddTab = StandardKey()
    Back = StandardKey()
    Backspace = StandardKey()
    Bold = StandardKey()
    Cancel = StandardKey()
    Close = StandardKey()
    Copy = StandardKey()
    Cut = StandardKey()
    Delete = StandardKey()
    DeleteCompleteLine = StandardKey()
    DeleteEndOfLine = StandardKey()
    DeleteEndOfWord = StandardKey()
    DeleteStartOfWord = StandardKey()
    Deselect = StandardKey()
    ExactMatch = SequenceMatch()
    Find = StandardKey()
    FindNext = StandardKey()
    FindPrevious = StandardKey()
    Forward = StandardKey()
    FullScreen = StandardKey()
    HelpContents = StandardKey()
    InsertLineSeparator = StandardKey()
    InsertParagraphSeparator = StandardKey()
    Italic = StandardKey()
    MoveToEndOfBlock = StandardKey()
    MoveToEndOfDocument = StandardKey()
    MoveToEndOfLine = StandardKey()
    MoveToNextChar = StandardKey()
    MoveToNextLine = StandardKey()
    MoveToNextPage = StandardKey()
    MoveToNextWord = StandardKey()
    MoveToPreviousChar = StandardKey()
    MoveToPreviousLine = StandardKey()
    MoveToPreviousPage = StandardKey()
    MoveToPreviousWord = StandardKey()
    MoveToStartOfBlock = StandardKey()
    MoveToStartOfDocument = StandardKey()
    MoveToStartOfLine = StandardKey()
    NativeText = SequenceFormat()
    New = StandardKey()
    NextChild = StandardKey()
    NoMatch = SequenceMatch()
    Open = StandardKey()
    PartialMatch = SequenceMatch()
    Paste = StandardKey()
    PortableText = SequenceFormat()
    Preferences = StandardKey()
    PreviousChild = StandardKey()
    Print = StandardKey()
    Quit = StandardKey()
    Redo = StandardKey()
    Refresh = StandardKey()
    Replace = StandardKey()
    Save = StandardKey()
    SaveAs = StandardKey()
    SelectAll = StandardKey()
    SelectEndOfBlock = StandardKey()
    SelectEndOfDocument = StandardKey()
    SelectEndOfLine = StandardKey()
    SelectNextChar = StandardKey()
    SelectNextLine = StandardKey()
    SelectNextPage = StandardKey()
    SelectNextWord = StandardKey()
    SelectPreviousChar = StandardKey()
    SelectPreviousLine = StandardKey()
    SelectPreviousPage = StandardKey()
    SelectPreviousWord = StandardKey()
    SelectStartOfBlock = StandardKey()
    SelectStartOfDocument = StandardKey()
    SelectStartOfLine = StandardKey()
    SequenceFormat = SequenceFormat
    SequenceMatch = SequenceMatch
    StandardKey = StandardKey
    Underline = StandardKey()
    Undo = StandardKey()
    UnknownKey = StandardKey()
    WhatsThis = StandardKey()
    ZoomIn = StandardKey()
    ZoomOut = StandardKey()
    __class__ = QKeySequence
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, key: str, format: PySide2.QtGui.QKeySequence.SequenceFormat=PySide2.QtGui.QKeySequence.SequenceFormat.NativeText):
        'QKeySequence(self)\nQKeySequence(self, k1:int, k2:int=0, k3:int=0, k4:int=0)\nQKeySequence(self, key:PySide2.QtGui.QKeySequence.StandardKey)\nQKeySequence(self, key:str, format:PySide2.QtGui.QKeySequence.SequenceFormat=PySide2.QtGui.QKeySequence.SequenceFormat.NativeText)\nQKeySequence(self, ks:PySide2.QtGui.QKeySequence)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, in_):
        '__lshift__(self, in_:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QKeySequence()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QKeySequence()
    
    def __rshift__(self, out):
        '__rshift__(self, out:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def count(self):
        'count(self) -> int'
        return int
    
    @classmethod
    def fromString(cls, str, format):
        'fromString(str:str, format:PySide2.QtGui.QKeySequence.SequenceFormat=PySide2.QtGui.QKeySequence.SequenceFormat.PortableText) -> PySide2.QtGui.QKeySequence'
        return PySide2.QtGui.QKeySequence
    
    def isEmpty(self):
        'isEmpty(self) -> bool'
        return bool
    
    @classmethod
    def keyBindings(cls, key):
        'keyBindings(key:PySide2.QtGui.QKeySequence.StandardKey) -> typing.List'
        return typing.List
    
    @classmethod
    def listFromString(cls, str, format):
        'listFromString(str:str, format:PySide2.QtGui.QKeySequence.SequenceFormat=PySide2.QtGui.QKeySequence.SequenceFormat.PortableText) -> typing.List'
        return typing.List
    
    @classmethod
    def listToString(cls, list, format):
        'listToString(list:typing.Sequence, format:PySide2.QtGui.QKeySequence.SequenceFormat=PySide2.QtGui.QKeySequence.SequenceFormat.PortableText) -> str'
        return str
    
    def matches(self, seq):
        'matches(self, seq:PySide2.QtGui.QKeySequence) -> PySide2.QtGui.QKeySequence.SequenceMatch'
        return PySide2.QtGui.QKeySequence.SequenceMatch
    
    @classmethod
    def mnemonic(cls, text):
        'mnemonic(text:str) -> PySide2.QtGui.QKeySequence'
        return PySide2.QtGui.QKeySequence
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QKeySequence)'
        pass
    
    def toString(self, format):
        'toString(self, format:PySide2.QtGui.QKeySequence.SequenceFormat=PySide2.QtGui.QKeySequence.SequenceFormat.PortableText) -> str'
        return str
    

class QLinearGradient(QGradient):
    'QLinearGradient(self)\nQLinearGradient(self, QLinearGradient:PySide2.QtGui.QLinearGradient)\nQLinearGradient(self, start:PySide2.QtCore.QPointF, finalStop:PySide2.QtCore.QPointF)\nQLinearGradient(self, xStart:float, yStart:float, xFinalStop:float, yFinalStop:float)'
    __class__ = QLinearGradient
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, xStart: float, yStart: float, xFinalStop: float, yFinalStop: float):
        'QLinearGradient(self)\nQLinearGradient(self, QLinearGradient:PySide2.QtGui.QLinearGradient)\nQLinearGradient(self, start:PySide2.QtCore.QPointF, finalStop:PySide2.QtCore.QPointF)\nQLinearGradient(self, xStart:float, yStart:float, xFinalStop:float, yFinalStop:float)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def finalStop(self):
        'finalStop(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def setFinalStop(self, stop: PySide2.QtCore.QPointF):
        'setFinalStop(self, stop:PySide2.QtCore.QPointF)\nsetFinalStop(self, x:float, y:float)'
        pass
    
    def setStart(self, start: PySide2.QtCore.QPointF):
        'setStart(self, start:PySide2.QtCore.QPointF)\nsetStart(self, x:float, y:float)'
        pass
    
    def start(self):
        'start(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    

class QMatrix(_mod_Shiboken.Object):
    'QMatrix(self)\nQMatrix(self, m11:float, m12:float, m21:float, m22:float, dx:float, dy:float)\nQMatrix(self, other:PySide2.QtGui.QMatrix)'
    __class__ = QMatrix
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __imul__(self, arg__1):
        '__imul__(self, arg__1:PySide2.QtGui.QMatrix) -> PySide2.QtGui.QMatrix\n\nReturn self*=value.'
        return PySide2.QtGui.QMatrix
    
    def __init__(self, m11: float, m12: float, m21: float, m22: float, dx: float, dy: float):
        'QMatrix(self)\nQMatrix(self, m11:float, m12:float, m21:float, m22:float, dx:float, dy:float)\nQMatrix(self, other:PySide2.QtGui.QMatrix)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __mul__(self, p: PySide2.QtCore.QPointF):
        '__mul__(self, l:PySide2.QtCore.QLine) -> PySide2.QtCore.QLine\n__mul__(self, l:PySide2.QtCore.QLineF) -> PySide2.QtCore.QLineF\n__mul__(self, o:PySide2.QtGui.QMatrix) -> PySide2.QtGui.QMatrix\n__mul__(self, p:PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint\n__mul__(self, p:PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF\n\nReturn self*value.'
        return QMatrix()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QMatrix()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QMatrix()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QMatrix()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def determinant(self):
        'determinant(self) -> float'
        return float
    
    def dx(self):
        'dx(self) -> float'
        return float
    
    def dy(self):
        'dy(self) -> float'
        return float
    
    def inverted(self):
        'inverted(self) -> typing.Tuple'
        return typing.Tuple
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def isInvertible(self):
        'isInvertible(self) -> bool'
        return bool
    
    def m11(self):
        'm11(self) -> float'
        return float
    
    def m12(self):
        'm12(self) -> float'
        return float
    
    def m21(self):
        'm21(self) -> float'
        return float
    
    def m22(self):
        'm22(self) -> float'
        return float
    
    def map(self, p: PySide2.QtGui.QPainterPath):
        'map(self, a:PySide2.QtGui.QPolygon) -> PySide2.QtGui.QPolygon\nmap(self, a:PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF\nmap(self, l:PySide2.QtCore.QLine) -> PySide2.QtCore.QLine\nmap(self, l:PySide2.QtCore.QLineF) -> PySide2.QtCore.QLineF\nmap(self, p:PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint\nmap(self, p:PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF\nmap(self, p:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath\nmap(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion\nmap(self, x:int, y:int) -> typing.Tuple\nmap(self, x:float, y:float) -> typing.Tuple'
        pass
    
    def mapRect(self, arg__1: PySide2.QtCore.QRectF):
        'mapRect(self, arg__1:PySide2.QtCore.QRect) -> PySide2.QtCore.QRect\nmapRect(self, arg__1:PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF'
        pass
    
    def mapToPolygon(self, r):
        'mapToPolygon(self, r:PySide2.QtCore.QRect) -> PySide2.QtGui.QPolygon'
        return PySide2.QtGui.QPolygon
    
    def reset(self):
        'reset(self)'
        pass
    
    def rotate(self, a):
        'rotate(self, a:float) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    
    def scale(self, sx, sy):
        'scale(self, sx:float, sy:float) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    
    def setMatrix(self, m11, m12, m21, m22, dx, dy):
        'setMatrix(self, m11:float, m12:float, m21:float, m22:float, dx:float, dy:float)'
        pass
    
    def shear(self, sh, sv):
        'shear(self, sh:float, sv:float) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    
    def translate(self, dx, dy):
        'translate(self, dx:float, dy:float) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    

class QMatrix2x2(_mod_Shiboken.Object):
    'QMatrix2x2(self)\nQMatrix2x2(self, QMatrix2x2:PySide2.QtGui.QMatrix2x2)\nQMatrix2x2(self, arg__1:typing.Iterable)'
    def __call__(self, row, column):
        '__call__(self, row:int, column:int) -> float\n\nCall self as a function.'
        return float
    
    __class__ = QMatrix2x2
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, other):
        '__iadd__(self, other:PySide2.QtGui.QMatrix2x2) -> PySide2.QtGui.QMatrix2x2\n\nReturn self+=value.'
        return PySide2.QtGui.QMatrix2x2
    
    def __imul__(self, factor):
        '__imul__(self, factor:float) -> PySide2.QtGui.QMatrix2x2\n\nReturn self*=value.'
        return PySide2.QtGui.QMatrix2x2
    
    def __init__(self, QMatrix2x2: PySide2.QtGui.QMatrix2x2):
        'QMatrix2x2(self)\nQMatrix2x2(self, QMatrix2x2:PySide2.QtGui.QMatrix2x2)\nQMatrix2x2(self, arg__1:typing.Iterable)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, other):
        '__isub__(self, other:PySide2.QtGui.QMatrix2x2) -> PySide2.QtGui.QMatrix2x2\n\nReturn self-=value.'
        return PySide2.QtGui.QMatrix2x2
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def constData(self):
        pass
    
    def data(self):
        'data(self) -> float'
        return float
    
    def fill(self, value):
        'fill(self, value:float)'
        pass
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def setToIdentity(self):
        'setToIdentity(self)'
        pass
    
    def transposed(self):
        'transposed(self) -> PySide2.QtGui.QMatrix2x2'
        return PySide2.QtGui.QMatrix2x2
    

class QMatrix2x3(_mod_Shiboken.Object):
    'QMatrix2x3(self)\nQMatrix2x3(self, QMatrix2x3:PySide2.QtGui.QMatrix2x3)\nQMatrix2x3(self, arg__1:typing.Iterable)'
    def __call__(self, row, column):
        '__call__(self, row:int, column:int) -> float\n\nCall self as a function.'
        return float
    
    __class__ = QMatrix2x3
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, other):
        '__iadd__(self, other:PySide2.QtGui.QMatrix2x3) -> PySide2.QtGui.QMatrix2x3\n\nReturn self+=value.'
        return PySide2.QtGui.QMatrix2x3
    
    def __imul__(self, factor):
        '__imul__(self, factor:float) -> PySide2.QtGui.QMatrix2x3\n\nReturn self*=value.'
        return PySide2.QtGui.QMatrix2x3
    
    def __init__(self, QMatrix2x3: PySide2.QtGui.QMatrix2x3):
        'QMatrix2x3(self)\nQMatrix2x3(self, QMatrix2x3:PySide2.QtGui.QMatrix2x3)\nQMatrix2x3(self, arg__1:typing.Iterable)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, other):
        '__isub__(self, other:PySide2.QtGui.QMatrix2x3) -> PySide2.QtGui.QMatrix2x3\n\nReturn self-=value.'
        return PySide2.QtGui.QMatrix2x3
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def constData(self):
        pass
    
    def data(self):
        'data(self) -> float'
        return float
    
    def fill(self, value):
        'fill(self, value:float)'
        pass
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def setToIdentity(self):
        'setToIdentity(self)'
        pass
    
    def transposed(self):
        'transposed(self) -> PySide2.QtGui.QMatrix3x2'
        return PySide2.QtGui.QMatrix3x2
    

class QMatrix2x4(_mod_Shiboken.Object):
    'QMatrix2x4(self)\nQMatrix2x4(self, QMatrix2x4:PySide2.QtGui.QMatrix2x4)\nQMatrix2x4(self, arg__1:typing.Iterable)'
    def __call__(self, row, column):
        '__call__(self, row:int, column:int) -> float\n\nCall self as a function.'
        return float
    
    __class__ = QMatrix2x4
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, other):
        '__iadd__(self, other:PySide2.QtGui.QMatrix2x4) -> PySide2.QtGui.QMatrix2x4\n\nReturn self+=value.'
        return PySide2.QtGui.QMatrix2x4
    
    def __imul__(self, factor):
        '__imul__(self, factor:float) -> PySide2.QtGui.QMatrix2x4\n\nReturn self*=value.'
        return PySide2.QtGui.QMatrix2x4
    
    def __init__(self, QMatrix2x4: PySide2.QtGui.QMatrix2x4):
        'QMatrix2x4(self)\nQMatrix2x4(self, QMatrix2x4:PySide2.QtGui.QMatrix2x4)\nQMatrix2x4(self, arg__1:typing.Iterable)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, other):
        '__isub__(self, other:PySide2.QtGui.QMatrix2x4) -> PySide2.QtGui.QMatrix2x4\n\nReturn self-=value.'
        return PySide2.QtGui.QMatrix2x4
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def constData(self):
        pass
    
    def data(self):
        'data(self) -> float'
        return float
    
    def fill(self, value):
        'fill(self, value:float)'
        pass
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def setToIdentity(self):
        'setToIdentity(self)'
        pass
    
    def transposed(self):
        'transposed(self) -> PySide2.QtGui.QMatrix4x2'
        return PySide2.QtGui.QMatrix4x2
    

class QMatrix3x2(_mod_Shiboken.Object):
    'QMatrix3x2(self)\nQMatrix3x2(self, QMatrix3x2:PySide2.QtGui.QMatrix3x2)\nQMatrix3x2(self, arg__1:typing.Iterable)'
    def __call__(self, row, column):
        '__call__(self, row:int, column:int) -> float\n\nCall self as a function.'
        return float
    
    __class__ = QMatrix3x2
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, other):
        '__iadd__(self, other:PySide2.QtGui.QMatrix3x2) -> PySide2.QtGui.QMatrix3x2\n\nReturn self+=value.'
        return PySide2.QtGui.QMatrix3x2
    
    def __imul__(self, factor):
        '__imul__(self, factor:float) -> PySide2.QtGui.QMatrix3x2\n\nReturn self*=value.'
        return PySide2.QtGui.QMatrix3x2
    
    def __init__(self, QMatrix3x2: PySide2.QtGui.QMatrix3x2):
        'QMatrix3x2(self)\nQMatrix3x2(self, QMatrix3x2:PySide2.QtGui.QMatrix3x2)\nQMatrix3x2(self, arg__1:typing.Iterable)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, other):
        '__isub__(self, other:PySide2.QtGui.QMatrix3x2) -> PySide2.QtGui.QMatrix3x2\n\nReturn self-=value.'
        return PySide2.QtGui.QMatrix3x2
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def constData(self):
        pass
    
    def data(self):
        'data(self) -> float'
        return float
    
    def fill(self, value):
        'fill(self, value:float)'
        pass
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def setToIdentity(self):
        'setToIdentity(self)'
        pass
    
    def transposed(self):
        'transposed(self) -> PySide2.QtGui.QMatrix2x3'
        return PySide2.QtGui.QMatrix2x3
    

class QMatrix3x3(_mod_Shiboken.Object):
    'QMatrix3x3(self)\nQMatrix3x3(self, QMatrix3x3:PySide2.QtGui.QMatrix3x3)\nQMatrix3x3(self, arg__1:typing.Iterable)'
    def __call__(self, row, column):
        '__call__(self, row:int, column:int) -> float\n\nCall self as a function.'
        return float
    
    __class__ = QMatrix3x3
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, other):
        '__iadd__(self, other:PySide2.QtGui.QMatrix3x3) -> PySide2.QtGui.QMatrix3x3\n\nReturn self+=value.'
        return PySide2.QtGui.QMatrix3x3
    
    def __imul__(self, factor):
        '__imul__(self, factor:float) -> PySide2.QtGui.QMatrix3x3\n\nReturn self*=value.'
        return PySide2.QtGui.QMatrix3x3
    
    def __init__(self, QMatrix3x3: PySide2.QtGui.QMatrix3x3):
        'QMatrix3x3(self)\nQMatrix3x3(self, QMatrix3x3:PySide2.QtGui.QMatrix3x3)\nQMatrix3x3(self, arg__1:typing.Iterable)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, other):
        '__isub__(self, other:PySide2.QtGui.QMatrix3x3) -> PySide2.QtGui.QMatrix3x3\n\nReturn self-=value.'
        return PySide2.QtGui.QMatrix3x3
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def constData(self):
        pass
    
    def data(self):
        'data(self) -> float'
        return float
    
    def fill(self, value):
        'fill(self, value:float)'
        pass
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def setToIdentity(self):
        'setToIdentity(self)'
        pass
    
    def transposed(self):
        'transposed(self) -> PySide2.QtGui.QMatrix3x3'
        return PySide2.QtGui.QMatrix3x3
    

class QMatrix3x4(_mod_Shiboken.Object):
    'QMatrix3x4(self)\nQMatrix3x4(self, QMatrix3x4:PySide2.QtGui.QMatrix3x4)\nQMatrix3x4(self, arg__1:typing.Iterable)'
    def __call__(self, row, column):
        '__call__(self, row:int, column:int) -> float\n\nCall self as a function.'
        return float
    
    __class__ = QMatrix3x4
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, other):
        '__iadd__(self, other:PySide2.QtGui.QMatrix3x4) -> PySide2.QtGui.QMatrix3x4\n\nReturn self+=value.'
        return PySide2.QtGui.QMatrix3x4
    
    def __imul__(self, factor):
        '__imul__(self, factor:float) -> PySide2.QtGui.QMatrix3x4\n\nReturn self*=value.'
        return PySide2.QtGui.QMatrix3x4
    
    def __init__(self, QMatrix3x4: PySide2.QtGui.QMatrix3x4):
        'QMatrix3x4(self)\nQMatrix3x4(self, QMatrix3x4:PySide2.QtGui.QMatrix3x4)\nQMatrix3x4(self, arg__1:typing.Iterable)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, other):
        '__isub__(self, other:PySide2.QtGui.QMatrix3x4) -> PySide2.QtGui.QMatrix3x4\n\nReturn self-=value.'
        return PySide2.QtGui.QMatrix3x4
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def constData(self):
        pass
    
    def data(self):
        'data(self) -> float'
        return float
    
    def fill(self, value):
        'fill(self, value:float)'
        pass
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def setToIdentity(self):
        'setToIdentity(self)'
        pass
    
    def transposed(self):
        'transposed(self) -> PySide2.QtGui.QMatrix4x3'
        return PySide2.QtGui.QMatrix4x3
    

class QMatrix4x2(_mod_Shiboken.Object):
    'QMatrix4x2(self)\nQMatrix4x2(self, QMatrix4x2:PySide2.QtGui.QMatrix4x2)\nQMatrix4x2(self, arg__1:typing.Iterable)'
    def __call__(self, row, column):
        '__call__(self, row:int, column:int) -> float\n\nCall self as a function.'
        return float
    
    __class__ = QMatrix4x2
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, other):
        '__iadd__(self, other:PySide2.QtGui.QMatrix4x2) -> PySide2.QtGui.QMatrix4x2\n\nReturn self+=value.'
        return PySide2.QtGui.QMatrix4x2
    
    def __imul__(self, factor):
        '__imul__(self, factor:float) -> PySide2.QtGui.QMatrix4x2\n\nReturn self*=value.'
        return PySide2.QtGui.QMatrix4x2
    
    def __init__(self, QMatrix4x2: PySide2.QtGui.QMatrix4x2):
        'QMatrix4x2(self)\nQMatrix4x2(self, QMatrix4x2:PySide2.QtGui.QMatrix4x2)\nQMatrix4x2(self, arg__1:typing.Iterable)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, other):
        '__isub__(self, other:PySide2.QtGui.QMatrix4x2) -> PySide2.QtGui.QMatrix4x2\n\nReturn self-=value.'
        return PySide2.QtGui.QMatrix4x2
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def constData(self):
        pass
    
    def data(self):
        'data(self) -> float'
        return float
    
    def fill(self, value):
        'fill(self, value:float)'
        pass
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def setToIdentity(self):
        'setToIdentity(self)'
        pass
    
    def transposed(self):
        'transposed(self) -> PySide2.QtGui.QMatrix2x4'
        return PySide2.QtGui.QMatrix2x4
    

class QMatrix4x3(_mod_Shiboken.Object):
    'QMatrix4x3(self)\nQMatrix4x3(self, QMatrix4x3:PySide2.QtGui.QMatrix4x3)\nQMatrix4x3(self, arg__1:typing.Iterable)'
    def __call__(self, row, column):
        '__call__(self, row:int, column:int) -> float\n\nCall self as a function.'
        return float
    
    __class__ = QMatrix4x3
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, other):
        '__iadd__(self, other:PySide2.QtGui.QMatrix4x3) -> PySide2.QtGui.QMatrix4x3\n\nReturn self+=value.'
        return PySide2.QtGui.QMatrix4x3
    
    def __imul__(self, factor):
        '__imul__(self, factor:float) -> PySide2.QtGui.QMatrix4x3\n\nReturn self*=value.'
        return PySide2.QtGui.QMatrix4x3
    
    def __init__(self, QMatrix4x3: PySide2.QtGui.QMatrix4x3):
        'QMatrix4x3(self)\nQMatrix4x3(self, QMatrix4x3:PySide2.QtGui.QMatrix4x3)\nQMatrix4x3(self, arg__1:typing.Iterable)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, other):
        '__isub__(self, other:PySide2.QtGui.QMatrix4x3) -> PySide2.QtGui.QMatrix4x3\n\nReturn self-=value.'
        return PySide2.QtGui.QMatrix4x3
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def constData(self):
        pass
    
    def data(self):
        'data(self) -> float'
        return float
    
    def fill(self, value):
        'fill(self, value:float)'
        pass
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def setToIdentity(self):
        'setToIdentity(self)'
        pass
    
    def transposed(self):
        'transposed(self) -> PySide2.QtGui.QMatrix3x4'
        return PySide2.QtGui.QMatrix3x4
    

class QMatrix4x4(_mod_Shiboken.Object):
    'QMatrix4x4(self)\nQMatrix4x4(self, m11:float, m12:float, m13:float, m14:float, m21:float, m22:float, m23:float, m24:float, m31:float, m32:float, m33:float, m34:float, m41:float, m42:float, m43:float, m44:float)\nQMatrix4x4(self, matrix:PySide2.QtGui.QMatrix)\nQMatrix4x4(self, transform:PySide2.QtGui.QTransform)\nQMatrix4x4(self, values:typing.Sequence)'
    def __add__(self, m2):
        '__add__(self, m2:PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4\n\nReturn self+value.'
        return PySide2.QtGui.QMatrix4x4
    
    __class__ = QMatrix4x4
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __dummy(self, arg__1):
        '__dummy(self, arg__1:typing.Sequence)'
        pass
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, other):
        '__iadd__(self, other:PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4\n\nReturn self+=value.'
        return PySide2.QtGui.QMatrix4x4
    
    def __imul__(self, other: PySide2.QtGui.QMatrix4x4):
        '__imul__(self, factor:float) -> PySide2.QtGui.QMatrix4x4\n__imul__(self, other:PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4\n\nReturn self*=value.'
        return None
    
    def __init__(self, m11: float, m12: float, m13: float, m14: float, m21: float, m22: float, m23: float, m24: float, m31: float, m32: float, m33: float, m34: float, m41: float, m42: float, m43: float, m44: float):
        'QMatrix4x4(self)\nQMatrix4x4(self, m11:float, m12:float, m13:float, m14:float, m21:float, m22:float, m23:float, m24:float, m31:float, m32:float, m33:float, m34:float, m41:float, m42:float, m43:float, m44:float)\nQMatrix4x4(self, matrix:PySide2.QtGui.QMatrix)\nQMatrix4x4(self, transform:PySide2.QtGui.QTransform)\nQMatrix4x4(self, values:typing.Sequence)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, other):
        '__isub__(self, other:PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4\n\nReturn self-=value.'
        return PySide2.QtGui.QMatrix4x4
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __mul__(self, point: PySide2.QtCore.QPointF):
        '__mul__(self, factor:float) -> PySide2.QtGui.QMatrix4x4\n__mul__(self, m2:PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4\n__mul__(self, point:PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint\n__mul__(self, point:PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF\n\nReturn self*value.'
        return QMatrix4x4()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '__neg__(self) -> PySide2.QtGui.QMatrix4x4\n\n-self'
        return PySide2.QtGui.QMatrix4x4
    
    def __radd__(self, value):
        'Return value+self.'
        return QMatrix4x4()
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QMatrix4x4()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QMatrix4x4()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QMatrix4x4()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __rsub__(self, value):
        'Return value-self.'
        return QMatrix4x4()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QMatrix4x4()
    
    def __sub__(self, m2):
        '__sub__(self, m2:PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4\n\nReturn self-value.'
        return PySide2.QtGui.QMatrix4x4
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def column(self, index):
        'column(self, index:int) -> PySide2.QtGui.QVector4D'
        return PySide2.QtGui.QVector4D
    
    def constData(self):
        pass
    
    def copyDataTo(self):
        'copyDataTo(self) -> float'
        return float
    
    def data(self):
        'data(self) -> typing.List'
        return typing.List
    
    def determinant(self):
        'determinant(self) -> float'
        return float
    
    def fill(self, value):
        'fill(self, value:float)'
        pass
    
    def flipCoordinates(self):
        'flipCoordinates(self)'
        pass
    
    def frustum(self, left, right, bottom, top, nearPlane, farPlane):
        'frustum(self, left:float, right:float, bottom:float, top:float, nearPlane:float, farPlane:float)'
        pass
    
    def inverted(self):
        'inverted(self) -> typing.Tuple'
        return typing.Tuple
    
    def isAffine(self):
        'isAffine(self) -> bool'
        return bool
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def lookAt(self, eye, center, up):
        'lookAt(self, eye:PySide2.QtGui.QVector3D, center:PySide2.QtGui.QVector3D, up:PySide2.QtGui.QVector3D)'
        pass
    
    def map(self, point: PySide2.QtGui.QVector4D):
        'map(self, point:PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint\nmap(self, point:PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF\nmap(self, point:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D\nmap(self, point:PySide2.QtGui.QVector4D) -> PySide2.QtGui.QVector4D'
        pass
    
    def mapRect(self, rect: PySide2.QtCore.QRectF):
        'mapRect(self, rect:PySide2.QtCore.QRect) -> PySide2.QtCore.QRect\nmapRect(self, rect:PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF'
        pass
    
    def mapVector(self, vector):
        'mapVector(self, vector:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D'
        return PySide2.QtGui.QVector3D
    
    def normalMatrix(self):
        'normalMatrix(self) -> PySide2.QtGui.QMatrix3x3'
        return PySide2.QtGui.QMatrix3x3
    
    def optimize(self):
        'optimize(self)'
        pass
    
    def ortho(self, left: float, right: float, bottom: float, top: float, nearPlane: float, farPlane: float):
        'ortho(self, left:float, right:float, bottom:float, top:float, nearPlane:float, farPlane:float)\northo(self, rect:PySide2.QtCore.QRect)\northo(self, rect:PySide2.QtCore.QRectF)'
        pass
    
    def perspective(self, verticalAngle, aspectRatio, nearPlane, farPlane):
        'perspective(self, verticalAngle:float, aspectRatio:float, nearPlane:float, farPlane:float)'
        pass
    
    def rotate(self, angle: float, vector: PySide2.QtGui.QVector3D):
        'rotate(self, angle:float, vector:PySide2.QtGui.QVector3D)\nrotate(self, angle:float, x:float, y:float, z:float=0.0)\nrotate(self, quaternion:PySide2.QtGui.QQuaternion)'
        pass
    
    def row(self, index):
        'row(self, index:int) -> PySide2.QtGui.QVector4D'
        return PySide2.QtGui.QVector4D
    
    def scale(self, vector: PySide2.QtGui.QVector3D):
        'scale(self, factor:float)\nscale(self, vector:PySide2.QtGui.QVector3D)\nscale(self, x:float, y:float)\nscale(self, x:float, y:float, z:float)'
        pass
    
    def setColumn(self, index, value):
        'setColumn(self, index:int, value:PySide2.QtGui.QVector4D)'
        pass
    
    def setRow(self, index, value):
        'setRow(self, index:int, value:PySide2.QtGui.QVector4D)'
        pass
    
    def setToIdentity(self):
        'setToIdentity(self)'
        pass
    
    def toAffine(self):
        'toAffine(self) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    
    def toTransform(self, distanceToPlane: float):
        'toTransform(self) -> PySide2.QtGui.QTransform\ntoTransform(self, distanceToPlane:float) -> PySide2.QtGui.QTransform'
        pass
    
    def translate(self, vector: PySide2.QtGui.QVector3D):
        'translate(self, vector:PySide2.QtGui.QVector3D)\ntranslate(self, x:float, y:float)\ntranslate(self, x:float, y:float, z:float)'
        pass
    
    def transposed(self):
        'transposed(self) -> PySide2.QtGui.QMatrix4x4'
        return PySide2.QtGui.QMatrix4x4
    
    def viewport(self, left: float, bottom: float, width: float, height: float, nearPlane: float=0.0, farPlane: float=1.0):
        'viewport(self, left:float, bottom:float, width:float, height:float, nearPlane:float=0.0, farPlane:float=1.0)\nviewport(self, rect:PySide2.QtCore.QRectF)'
        pass
    

class QMouseEvent(QInputEvent):
    'QMouseEvent(self, type:PySide2.QtCore.QEvent.Type, localPos:PySide2.QtCore.QPointF, button:PySide2.QtCore.Qt.MouseButton, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)\nQMouseEvent(self, type:PySide2.QtCore.QEvent.Type, localPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF, button:PySide2.QtCore.Qt.MouseButton, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)\nQMouseEvent(self, type:PySide2.QtCore.QEvent.Type, localPos:PySide2.QtCore.QPointF, windowPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF, button:PySide2.QtCore.Qt.MouseButton, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)\nQMouseEvent(self, type:PySide2.QtCore.QEvent.Type, localPos:PySide2.QtCore.QPointF, windowPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF, button:PySide2.QtCore.Qt.MouseButton, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, source:PySide2.QtCore.Qt.MouseEventSource)'
    __class__ = QMouseEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, type: PySide2.QtCore.QEvent.Type, localPos: PySide2.QtCore.QPointF, windowPos: PySide2.QtCore.QPointF, screenPos: PySide2.QtCore.QPointF, button: PySide2.QtCore.Qt.MouseButton, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, source: PySide2.QtCore.Qt.MouseEventSource):
        'QMouseEvent(self, type:PySide2.QtCore.QEvent.Type, localPos:PySide2.QtCore.QPointF, button:PySide2.QtCore.Qt.MouseButton, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)\nQMouseEvent(self, type:PySide2.QtCore.QEvent.Type, localPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF, button:PySide2.QtCore.Qt.MouseButton, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)\nQMouseEvent(self, type:PySide2.QtCore.QEvent.Type, localPos:PySide2.QtCore.QPointF, windowPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF, button:PySide2.QtCore.Qt.MouseButton, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)\nQMouseEvent(self, type:PySide2.QtCore.QEvent.Type, localPos:PySide2.QtCore.QPointF, windowPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF, button:PySide2.QtCore.Qt.MouseButton, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, source:PySide2.QtCore.Qt.MouseEventSource)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def button(self):
        'button(self) -> PySide2.QtCore.Qt.MouseButton'
        return PySide2.QtCore.Qt.MouseButton
    
    def buttons(self):
        'buttons(self) -> PySide2.QtCore.Qt.MouseButtons'
        return PySide2.QtCore.Qt.MouseButtons
    
    @property
    def caps(self):
        pass
    
    def flags(self):
        'flags(self) -> PySide2.QtCore.Qt.MouseEventFlags'
        return PySide2.QtCore.Qt.MouseEventFlags
    
    def globalPos(self):
        'globalPos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def globalX(self):
        'globalX(self) -> int'
        return int
    
    def globalY(self):
        'globalY(self) -> int'
        return int
    
    @property
    def l(self):
        pass
    
    def localPos(self):
        'localPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def pos(self):
        'pos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    @property
    def s(self):
        pass
    
    def screenPos(self):
        'screenPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def setLocalPos(self, localPosition):
        'setLocalPos(self, localPosition:PySide2.QtCore.QPointF)'
        pass
    
    def source(self):
        'source(self) -> PySide2.QtCore.Qt.MouseEventSource'
        return PySide2.QtCore.Qt.MouseEventSource
    
    @property
    def velocity(self):
        pass
    
    @property
    def w(self):
        pass
    
    def windowPos(self):
        'windowPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def x(self):
        'x(self) -> int'
        return int
    
    def y(self):
        'y(self) -> int'
        return int
    

class QMoveEvent(_mod_PySide2_QtCore.QEvent):
    'QMoveEvent(self, pos:PySide2.QtCore.QPoint, oldPos:PySide2.QtCore.QPoint)'
    __class__ = QMoveEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, pos: PySide2.QtCore.QPoint, oldPos: PySide2.QtCore.QPoint):
        'QMoveEvent(self, pos:PySide2.QtCore.QPoint, oldPos:PySide2.QtCore.QPoint)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def oldPos(self):
        'oldPos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def pos(self):
        'pos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    

class QMovie(_mod_PySide2_QtCore.QObject):
    'QMovie(self, device:PySide2.QtCore.QIODevice, format:PySide2.QtCore.QByteArray=Default(QByteArray), parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQMovie(self, fileName:str, format:PySide2.QtCore.QByteArray=Default(QByteArray), parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQMovie(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    CacheAll = CacheMode()
    CacheMode = CacheMode
    CacheNone = CacheMode()
    MovieState = MovieState
    NotRunning = MovieState()
    Paused = MovieState()
    Running = MovieState()
    __class__ = QMovie
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, device: PySide2.QtCore.QIODevice, format: PySide2.QtCore.QByteArray=Default(QByteArray), parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QMovie(self, device:PySide2.QtCore.QIODevice, format:PySide2.QtCore.QByteArray=Default(QByteArray), parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQMovie(self, fileName:str, format:PySide2.QtCore.QByteArray=Default(QByteArray), parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQMovie(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def backgroundColor(self):
        'backgroundColor(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def cacheMode(self):
        'cacheMode(self) -> PySide2.QtGui.QMovie.CacheMode'
        return PySide2.QtGui.QMovie.CacheMode
    
    def currentFrameNumber(self):
        'currentFrameNumber(self) -> int'
        return int
    
    def currentImage(self):
        'currentImage(self) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def currentPixmap(self):
        'currentPixmap(self) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    def device(self):
        'device(self) -> PySide2.QtCore.QIODevice'
        return PySide2.QtCore.QIODevice
    
    def error(self):
        pass
    
    def fileName(self):
        'fileName(self) -> str'
        return str
    
    def finished(self):
        pass
    
    def format(self):
        'format(self) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    def frameChanged(self):
        pass
    
    def frameCount(self):
        'frameCount(self) -> int'
        return int
    
    def frameRect(self):
        'frameRect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def jumpToFrame(self, frameNumber):
        'jumpToFrame(self, frameNumber:int) -> bool'
        return bool
    
    def jumpToNextFrame(self):
        'jumpToNextFrame(self) -> bool'
        return bool
    
    def lastError(self):
        'lastError(self) -> PySide2.QtGui.QImageReader.ImageReaderError'
        return PySide2.QtGui.QImageReader.ImageReaderError
    
    def lastErrorString(self):
        'lastErrorString(self) -> str'
        return str
    
    def loopCount(self):
        'loopCount(self) -> int'
        return int
    
    def nextFrameDelay(self):
        'nextFrameDelay(self) -> int'
        return int
    
    def resized(self):
        pass
    
    def scaledSize(self):
        'scaledSize(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def setBackgroundColor(self, color):
        'setBackgroundColor(self, color:PySide2.QtGui.QColor)'
        pass
    
    def setCacheMode(self, mode):
        'setCacheMode(self, mode:PySide2.QtGui.QMovie.CacheMode)'
        pass
    
    def setDevice(self, device):
        'setDevice(self, device:PySide2.QtCore.QIODevice)'
        pass
    
    def setFileName(self, fileName):
        'setFileName(self, fileName:str)'
        pass
    
    def setFormat(self, format):
        'setFormat(self, format:PySide2.QtCore.QByteArray)'
        pass
    
    def setPaused(self, paused):
        'setPaused(self, paused:bool)'
        pass
    
    def setScaledSize(self, size):
        'setScaledSize(self, size:PySide2.QtCore.QSize)'
        pass
    
    def setSpeed(self, percentSpeed):
        'setSpeed(self, percentSpeed:int)'
        pass
    
    def speed(self):
        'speed(self) -> int'
        return int
    
    def start(self):
        'start(self)'
        pass
    
    def started(self):
        pass
    
    def state(self):
        'state(self) -> PySide2.QtGui.QMovie.MovieState'
        return PySide2.QtGui.QMovie.MovieState
    
    def stateChanged(self):
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def stop(self):
        'stop(self)'
        pass
    
    @classmethod
    def supportedFormats(cls):
        'supportedFormats() -> typing.List'
        return typing.List
    
    def updated(self):
        pass
    

class QNativeGestureEvent(QInputEvent):
    'QNativeGestureEvent(self, type:PySide2.QtCore.Qt.NativeGestureType, dev:PySide2.QtGui.QTouchDevice, localPos:PySide2.QtCore.QPointF, windowPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF, value:float, sequenceId:int, intArgument:int)\nQNativeGestureEvent(self, type:PySide2.QtCore.Qt.NativeGestureType, localPos:PySide2.QtCore.QPointF, windowPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF, value:float, sequenceId:int, intArgument:int)'
    __class__ = QNativeGestureEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, type: PySide2.QtCore.Qt.NativeGestureType, dev: PySide2.QtGui.QTouchDevice, localPos: PySide2.QtCore.QPointF, windowPos: PySide2.QtCore.QPointF, screenPos: PySide2.QtCore.QPointF, value: float, sequenceId: int, intArgument: int):
        'QNativeGestureEvent(self, type:PySide2.QtCore.Qt.NativeGestureType, dev:PySide2.QtGui.QTouchDevice, localPos:PySide2.QtCore.QPointF, windowPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF, value:float, sequenceId:int, intArgument:int)\nQNativeGestureEvent(self, type:PySide2.QtCore.Qt.NativeGestureType, localPos:PySide2.QtCore.QPointF, windowPos:PySide2.QtCore.QPointF, screenPos:PySide2.QtCore.QPointF, value:float, sequenceId:int, intArgument:int)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def device(self):
        'device(self) -> PySide2.QtGui.QTouchDevice'
        return PySide2.QtGui.QTouchDevice
    
    def gestureType(self):
        'gestureType(self) -> PySide2.QtCore.Qt.NativeGestureType'
        return PySide2.QtCore.Qt.NativeGestureType
    
    def globalPos(self):
        'globalPos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def localPos(self):
        'localPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def pos(self):
        'pos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def screenPos(self):
        'screenPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def value(self):
        'value(self) -> float'
        return float
    
    def windowPos(self):
        'windowPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    

class QOffscreenSurface(_mod_PySide2_QtCore.QObject,QSurface):
    'QOffscreenSurface(self, screen:PySide2.QtGui.QScreen, parent:PySide2.QtCore.QObject)\nQOffscreenSurface(self, screen:typing.Union[PySide2.QtGui.QScreen, NoneType]=None)'
    __class__ = QOffscreenSurface
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, screen: PySide2.QtGui.QScreen, parent: PySide2.QtCore.QObject):
        'QOffscreenSurface(self, screen:PySide2.QtGui.QScreen, parent:PySide2.QtCore.QObject)\nQOffscreenSurface(self, screen:typing.Union[PySide2.QtGui.QScreen, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def create(self):
        'create(self)'
        pass
    
    def destroy(self):
        'destroy(self)'
        pass
    
    def format(self):
        'format(self) -> PySide2.QtGui.QSurfaceFormat'
        return PySide2.QtGui.QSurfaceFormat
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def nativeHandle(self):
        'nativeHandle(self) -> int'
        return int
    
    def requestedFormat(self):
        'requestedFormat(self) -> PySide2.QtGui.QSurfaceFormat'
        return PySide2.QtGui.QSurfaceFormat
    
    def screen(self):
        'screen(self) -> PySide2.QtGui.QScreen'
        return PySide2.QtGui.QScreen
    
    def screenChanged(self):
        pass
    
    def setFormat(self, format):
        'setFormat(self, format:PySide2.QtGui.QSurfaceFormat)'
        pass
    
    def setNativeHandle(self, handle):
        'setNativeHandle(self, handle:int)'
        pass
    
    def setScreen(self, screen):
        'setScreen(self, screen:PySide2.QtGui.QScreen)'
        pass
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def surfaceHandle(self):
        'surfaceHandle(self) -> int'
        return int
    
    def surfaceType(self):
        'surfaceType(self) -> PySide2.QtGui.QSurface.SurfaceType'
        return PySide2.QtGui.QSurface.SurfaceType
    

class QOpenGLBuffer(_mod_Shiboken.Object):
    'QOpenGLBuffer(self)\nQOpenGLBuffer(self, other:PySide2.QtGui.QOpenGLBuffer)\nQOpenGLBuffer(self, type:PySide2.QtGui.QOpenGLBuffer.Type)'
    Access = Access
    DynamicCopy = UsagePattern()
    DynamicDraw = UsagePattern()
    DynamicRead = UsagePattern()
    IndexBuffer = Type()
    PixelPackBuffer = Type()
    PixelUnpackBuffer = Type()
    RangeAccessFlag = RangeAccessFlag
    RangeAccessFlags = RangeAccessFlags
    RangeFlushExplicit = RangeAccessFlag()
    RangeInvalidate = RangeAccessFlag()
    RangeInvalidateBuffer = RangeAccessFlag()
    RangeRead = RangeAccessFlag()
    RangeUnsynchronized = RangeAccessFlag()
    RangeWrite = RangeAccessFlag()
    ReadOnly = Access()
    ReadWrite = Access()
    StaticCopy = UsagePattern()
    StaticDraw = UsagePattern()
    StaticRead = UsagePattern()
    StreamCopy = UsagePattern()
    StreamDraw = UsagePattern()
    StreamRead = UsagePattern()
    Type = Type
    UsagePattern = UsagePattern
    VertexBuffer = Type()
    WriteOnly = Access()
    __class__ = QOpenGLBuffer
    __dict__ = {}
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, type: PySide2.QtGui.QOpenGLBuffer.Type):
        'QOpenGLBuffer(self)\nQOpenGLBuffer(self, other:PySide2.QtGui.QOpenGLBuffer)\nQOpenGLBuffer(self, type:PySide2.QtGui.QOpenGLBuffer.Type)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def allocate(self, data: int, count: int):
        'allocate(self, count:int)\nallocate(self, data:int, count:int)'
        pass
    
    def bind(self):
        'bind(self) -> bool'
        return bool
    
    def bufferId(self):
        'bufferId(self) -> int'
        return int
    
    def create(self):
        'create(self) -> bool'
        return bool
    
    def destroy(self):
        'destroy(self)'
        pass
    
    def isCreated(self):
        'isCreated(self) -> bool'
        return bool
    
    def map(self, access):
        'map(self, access:PySide2.QtGui.QOpenGLBuffer.Access) -> int'
        return int
    
    def mapRange(self, offset, count, access):
        'mapRange(self, offset:int, count:int, access:PySide2.QtGui.QOpenGLBuffer.RangeAccessFlags) -> int'
        return int
    
    def read(self, offset, data, count):
        'read(self, offset:int, data:int, count:int) -> bool'
        return bool
    
    @classmethod
    def release(cls, type: PySide2.QtGui.QOpenGLBuffer.Type):
        'release(self)\nrelease(type:PySide2.QtGui.QOpenGLBuffer.Type)'
        pass
    
    def setUsagePattern(self, value):
        'setUsagePattern(self, value:PySide2.QtGui.QOpenGLBuffer.UsagePattern)'
        pass
    
    def size(self):
        'size(self) -> int'
        return int
    
    def type(self):
        'type(self) -> PySide2.QtGui.QOpenGLBuffer.Type'
        return PySide2.QtGui.QOpenGLBuffer.Type
    
    def unmap(self):
        'unmap(self) -> bool'
        return bool
    
    def usagePattern(self):
        'usagePattern(self) -> PySide2.QtGui.QOpenGLBuffer.UsagePattern'
        return PySide2.QtGui.QOpenGLBuffer.UsagePattern
    
    def write(self, offset, data, count):
        'write(self, offset:int, data:int, count:int)'
        pass
    

class QOpenGLContext(_mod_PySide2_QtCore.QObject):
    'QOpenGLContext(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    LibGL = OpenGLModuleType()
    LibGLES = OpenGLModuleType()
    OpenGLModuleType = OpenGLModuleType
    __class__ = QOpenGLContext
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QOpenGLContext(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def aboutToBeDestroyed(self):
        pass
    
    @classmethod
    def areSharing(cls, first, second):
        'areSharing(first:PySide2.QtGui.QOpenGLContext, second:PySide2.QtGui.QOpenGLContext) -> bool'
        return bool
    
    def create(self):
        'create(self) -> bool'
        return bool
    
    @classmethod
    def currentContext(cls):
        'currentContext() -> PySide2.QtGui.QOpenGLContext'
        return PySide2.QtGui.QOpenGLContext
    
    def defaultFramebufferObject(self):
        'defaultFramebufferObject(self) -> int'
        return int
    
    def doneCurrent(self):
        'doneCurrent(self)'
        pass
    
    def extensions(self):
        'extensions(self) -> typing.Set'
        return typing.Set
    
    def extraFunctions(self):
        'extraFunctions(self) -> PySide2.QtGui.QOpenGLExtraFunctions'
        return PySide2.QtGui.QOpenGLExtraFunctions
    
    def format(self):
        'format(self) -> PySide2.QtGui.QSurfaceFormat'
        return PySide2.QtGui.QSurfaceFormat
    
    def functions(self):
        'functions(self) -> PySide2.QtGui.QOpenGLFunctions'
        return PySide2.QtGui.QOpenGLFunctions
    
    @classmethod
    def globalShareContext(cls):
        'globalShareContext() -> PySide2.QtGui.QOpenGLContext'
        return PySide2.QtGui.QOpenGLContext
    
    def hasExtension(self, extension):
        'hasExtension(self, extension:PySide2.QtCore.QByteArray) -> bool'
        return bool
    
    def isOpenGLES(self):
        'isOpenGLES(self) -> bool'
        return bool
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def makeCurrent(self, surface):
        'makeCurrent(self, surface:PySide2.QtGui.QSurface) -> bool'
        return bool
    
    def nativeHandle(self):
        'nativeHandle(self) -> typing.Any'
        return typing.Any
    
    @classmethod
    def openGLModuleHandle(cls):
        'openGLModuleHandle() -> int'
        return int
    
    @classmethod
    def openGLModuleType(cls):
        'openGLModuleType() -> PySide2.QtGui.QOpenGLContext.OpenGLModuleType'
        return PySide2.QtGui.QOpenGLContext.OpenGLModuleType
    
    def screen(self):
        'screen(self) -> PySide2.QtGui.QScreen'
        return PySide2.QtGui.QScreen
    
    def setFormat(self, format):
        'setFormat(self, format:PySide2.QtGui.QSurfaceFormat)'
        pass
    
    def setNativeHandle(self, handle):
        'setNativeHandle(self, handle:typing.Any)'
        pass
    
    def setScreen(self, screen):
        'setScreen(self, screen:PySide2.QtGui.QScreen)'
        pass
    
    def setShareContext(self, shareContext):
        'setShareContext(self, shareContext:PySide2.QtGui.QOpenGLContext)'
        pass
    
    def shareContext(self):
        'shareContext(self) -> PySide2.QtGui.QOpenGLContext'
        return PySide2.QtGui.QOpenGLContext
    
    def shareGroup(self):
        'shareGroup(self) -> PySide2.QtGui.QOpenGLContextGroup'
        return PySide2.QtGui.QOpenGLContextGroup
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    @classmethod
    def supportsThreadedOpenGL(cls):
        'supportsThreadedOpenGL() -> bool'
        return bool
    
    def surface(self):
        'surface(self) -> PySide2.QtGui.QSurface'
        return PySide2.QtGui.QSurface
    
    def swapBuffers(self, surface):
        'swapBuffers(self, surface:PySide2.QtGui.QSurface)'
        pass
    
    def versionFunctions(self, versionProfile):
        'versionFunctions(self, versionProfile:PySide2.QtGui.QOpenGLVersionProfile=Default(QOpenGLVersionProfile)) -> PySide2.QtGui.QAbstractOpenGLFunctions'
        return PySide2.QtGui.QAbstractOpenGLFunctions
    

class QOpenGLContextGroup(_mod_PySide2_QtCore.QObject):
    __class__ = QOpenGLContextGroup
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def currentContextGroup(cls):
        'currentContextGroup() -> PySide2.QtGui.QOpenGLContextGroup'
        return PySide2.QtGui.QOpenGLContextGroup
    
    def shares(self):
        'shares(self) -> typing.List'
        return typing.List
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QOpenGLDebugLogger(_mod_PySide2_QtCore.QObject):
    'QOpenGLDebugLogger(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    AsynchronousLogging = LoggingMode()
    LoggingMode = LoggingMode
    SynchronousLogging = LoggingMode()
    __class__ = QOpenGLDebugLogger
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QOpenGLDebugLogger(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def disableMessages(self, sources: PySide2.QtGui.QOpenGLDebugMessage.Sources=PySide2.QtGui.QOpenGLDebugMessage.Source.AnySource, types: PySide2.QtGui.QOpenGLDebugMessage.Types=PySide2.QtGui.QOpenGLDebugMessage.Type.AnyType, severities: PySide2.QtGui.QOpenGLDebugMessage.Severities=PySide2.QtGui.QOpenGLDebugMessage.Severity.AnySeverity):
        'disableMessages(self, ids:typing.List, sources:PySide2.QtGui.QOpenGLDebugMessage.Sources=PySide2.QtGui.QOpenGLDebugMessage.Source.AnySource, types:PySide2.QtGui.QOpenGLDebugMessage.Types=PySide2.QtGui.QOpenGLDebugMessage.Type.AnyType)\ndisableMessages(self, sources:PySide2.QtGui.QOpenGLDebugMessage.Sources=PySide2.QtGui.QOpenGLDebugMessage.Source.AnySource, types:PySide2.QtGui.QOpenGLDebugMessage.Types=PySide2.QtGui.QOpenGLDebugMessage.Type.AnyType, severities:PySide2.QtGui.QOpenGLDebugMessage.Severities=PySide2.QtGui.QOpenGLDebugMessage.Severity.AnySeverity)'
        pass
    
    def enableMessages(self, sources: PySide2.QtGui.QOpenGLDebugMessage.Sources=PySide2.QtGui.QOpenGLDebugMessage.Source.AnySource, types: PySide2.QtGui.QOpenGLDebugMessage.Types=PySide2.QtGui.QOpenGLDebugMessage.Type.AnyType, severities: PySide2.QtGui.QOpenGLDebugMessage.Severities=PySide2.QtGui.QOpenGLDebugMessage.Severity.AnySeverity):
        'enableMessages(self, ids:typing.List, sources:PySide2.QtGui.QOpenGLDebugMessage.Sources=PySide2.QtGui.QOpenGLDebugMessage.Source.AnySource, types:PySide2.QtGui.QOpenGLDebugMessage.Types=PySide2.QtGui.QOpenGLDebugMessage.Type.AnyType)\nenableMessages(self, sources:PySide2.QtGui.QOpenGLDebugMessage.Sources=PySide2.QtGui.QOpenGLDebugMessage.Source.AnySource, types:PySide2.QtGui.QOpenGLDebugMessage.Types=PySide2.QtGui.QOpenGLDebugMessage.Type.AnyType, severities:PySide2.QtGui.QOpenGLDebugMessage.Severities=PySide2.QtGui.QOpenGLDebugMessage.Severity.AnySeverity)'
        pass
    
    def initialize(self):
        'initialize(self) -> bool'
        return bool
    
    def isLogging(self):
        'isLogging(self) -> bool'
        return bool
    
    def logMessage(self, debugMessage):
        'logMessage(self, debugMessage:PySide2.QtGui.QOpenGLDebugMessage)'
        pass
    
    def loggedMessages(self):
        'loggedMessages(self) -> typing.List'
        return typing.List
    
    def loggingMode(self):
        'loggingMode(self) -> PySide2.QtGui.QOpenGLDebugLogger.LoggingMode'
        return PySide2.QtGui.QOpenGLDebugLogger.LoggingMode
    
    def maximumMessageLength(self):
        'maximumMessageLength(self) -> int'
        return int
    
    def messageLogged(self):
        pass
    
    def popGroup(self):
        'popGroup(self)'
        pass
    
    def pushGroup(self, name, id, source):
        'pushGroup(self, name:str, id:int=0, source:PySide2.QtGui.QOpenGLDebugMessage.Source=PySide2.QtGui.QOpenGLDebugMessage.Source.ApplicationSource)'
        pass
    
    def startLogging(self, loggingMode):
        'startLogging(self, loggingMode:PySide2.QtGui.QOpenGLDebugLogger.LoggingMode=PySide2.QtGui.QOpenGLDebugLogger.LoggingMode.AsynchronousLogging)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def stopLogging(self):
        'stopLogging(self)'
        pass
    

class QOpenGLDebugMessage(_mod_Shiboken.Object):
    'QOpenGLDebugMessage(self)\nQOpenGLDebugMessage(self, debugMessage:PySide2.QtGui.QOpenGLDebugMessage)'
    APISource = Source()
    AnySeverity = Severity()
    AnySource = Source()
    AnyType = Type()
    ApplicationSource = Source()
    DeprecatedBehaviorType = Type()
    ErrorType = Type()
    GroupPopType = Type()
    GroupPushType = Type()
    HighSeverity = Severity()
    InvalidSeverity = Severity()
    InvalidSource = Source()
    InvalidType = Type()
    LastSeverity = Severity()
    LastSource = Source()
    LastType = Type()
    LowSeverity = Severity()
    MarkerType = Type()
    MediumSeverity = Severity()
    NotificationSeverity = Severity()
    OtherSource = Source()
    OtherType = Type()
    PerformanceType = Type()
    PortabilityType = Type()
    Severities = Severities
    Severity = Severity
    ShaderCompilerSource = Source()
    Source = Source
    Sources = Sources
    ThirdPartySource = Source()
    Type = Type
    Types = Types
    UndefinedBehaviorType = Type()
    WindowSystemSource = Source()
    __class__ = QOpenGLDebugMessage
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, debugMessage: PySide2.QtGui.QOpenGLDebugMessage):
        'QOpenGLDebugMessage(self)\nQOpenGLDebugMessage(self, debugMessage:PySide2.QtGui.QOpenGLDebugMessage)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def createApplicationMessage(cls, text, id, severity, type):
        'createApplicationMessage(text:str, id:int=0, severity:PySide2.QtGui.QOpenGLDebugMessage.Severity=PySide2.QtGui.QOpenGLDebugMessage.Severity.NotificationSeverity, type:PySide2.QtGui.QOpenGLDebugMessage.Type=PySide2.QtGui.QOpenGLDebugMessage.Type.OtherType) -> PySide2.QtGui.QOpenGLDebugMessage'
        return PySide2.QtGui.QOpenGLDebugMessage
    
    @classmethod
    def createThirdPartyMessage(cls, text, id, severity, type):
        'createThirdPartyMessage(text:str, id:int=0, severity:PySide2.QtGui.QOpenGLDebugMessage.Severity=PySide2.QtGui.QOpenGLDebugMessage.Severity.NotificationSeverity, type:PySide2.QtGui.QOpenGLDebugMessage.Type=PySide2.QtGui.QOpenGLDebugMessage.Type.OtherType) -> PySide2.QtGui.QOpenGLDebugMessage'
        return PySide2.QtGui.QOpenGLDebugMessage
    
    def id(self):
        'id(self) -> int'
        return int
    
    def message(self):
        'message(self) -> str'
        return str
    
    def severity(self):
        'severity(self) -> PySide2.QtGui.QOpenGLDebugMessage.Severity'
        return PySide2.QtGui.QOpenGLDebugMessage.Severity
    
    def source(self):
        'source(self) -> PySide2.QtGui.QOpenGLDebugMessage.Source'
        return PySide2.QtGui.QOpenGLDebugMessage.Source
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QOpenGLDebugMessage)'
        pass
    
    def type(self):
        'type(self) -> PySide2.QtGui.QOpenGLDebugMessage.Type'
        return PySide2.QtGui.QOpenGLDebugMessage.Type
    

class QOpenGLExtraFunctions(QOpenGLFunctions):
    'QOpenGLExtraFunctions(self)\nQOpenGLExtraFunctions(self, context:PySide2.QtGui.QOpenGLContext)'
    __class__ = QOpenGLExtraFunctions
    __dict__ = {}
    def __init__(self, context: PySide2.QtGui.QOpenGLContext):
        'QOpenGLExtraFunctions(self)\nQOpenGLExtraFunctions(self, context:PySide2.QtGui.QOpenGLContext)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def glActiveShaderProgram(self, pipeline, program):
        'glActiveShaderProgram(self, pipeline:int, program:int)'
        pass
    
    def glBeginQuery(self, target, id):
        'glBeginQuery(self, target:int, id:int)'
        pass
    
    def glBeginTransformFeedback(self, primitiveMode):
        'glBeginTransformFeedback(self, primitiveMode:int)'
        pass
    
    def glBindBufferBase(self, target, index, buffer):
        'glBindBufferBase(self, target:int, index:int, buffer:int)'
        pass
    
    def glBindImageTexture(self, unit, texture, level, layered, layer, access, format):
        'glBindImageTexture(self, unit:int, texture:int, level:int, layered:int, layer:int, access:int, format:int)'
        pass
    
    def glBindProgramPipeline(self, pipeline):
        'glBindProgramPipeline(self, pipeline:int)'
        pass
    
    def glBindSampler(self, unit, sampler):
        'glBindSampler(self, unit:int, sampler:int)'
        pass
    
    def glBindTransformFeedback(self, target, id):
        'glBindTransformFeedback(self, target:int, id:int)'
        pass
    
    def glBindVertexArray(self, array):
        'glBindVertexArray(self, array:int)'
        pass
    
    def glBlendBarrier(self):
        'glBlendBarrier(self)'
        pass
    
    def glBlendEquationSeparatei(self, buf, modeRGB, modeAlpha):
        'glBlendEquationSeparatei(self, buf:int, modeRGB:int, modeAlpha:int)'
        pass
    
    def glBlendEquationi(self, buf, mode):
        'glBlendEquationi(self, buf:int, mode:int)'
        pass
    
    def glBlendFuncSeparatei(self, buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
        'glBlendFuncSeparatei(self, buf:int, srcRGB:int, dstRGB:int, srcAlpha:int, dstAlpha:int)'
        pass
    
    def glBlendFunci(self, buf, src, dst):
        'glBlendFunci(self, buf:int, src:int, dst:int)'
        pass
    
    def glBlitFramebuffer(self, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
        'glBlitFramebuffer(self, srcX0:int, srcY0:int, srcX1:int, srcY1:int, dstX0:int, dstY0:int, dstX1:int, dstY1:int, mask:int, filter:int)'
        pass
    
    def glClearBufferfi(self, buffer, drawbuffer, depth, stencil):
        'glClearBufferfi(self, buffer:int, drawbuffer:int, depth:float, stencil:int)'
        pass
    
    def glClearBufferfv(self, buffer, drawbuffer, value):
        'glClearBufferfv(self, buffer:int, drawbuffer:int, value:typing.Sequence)'
        pass
    
    def glClearBufferiv(self, buffer, drawbuffer, value):
        'glClearBufferiv(self, buffer:int, drawbuffer:int, value:typing.Sequence)'
        pass
    
    def glClearBufferuiv(self, buffer, drawbuffer, value):
        'glClearBufferuiv(self, buffer:int, drawbuffer:int, value:typing.Sequence)'
        pass
    
    def glColorMaski(self, index, r, g, b, a):
        'glColorMaski(self, index:int, r:int, g:int, b:int, a:int)'
        pass
    
    def glCompressedTexImage3D(self, target, level, internalformat, width, height, depth, border, imageSize, data):
        'glCompressedTexImage3D(self, target:int, level:int, internalformat:int, width:int, height:int, depth:int, border:int, imageSize:int, data:int)'
        pass
    
    def glCompressedTexSubImage3D(self, target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
        'glCompressedTexSubImage3D(self, target:int, level:int, xoffset:int, yoffset:int, zoffset:int, width:int, height:int, depth:int, format:int, imageSize:int, data:int)'
        pass
    
    def glCopyImageSubData(self, srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth):
        'glCopyImageSubData(self, srcName:int, srcTarget:int, srcLevel:int, srcX:int, srcY:int, srcZ:int, dstName:int, dstTarget:int, dstLevel:int, dstX:int, dstY:int, dstZ:int, srcWidth:int, srcHeight:int, srcDepth:int)'
        pass
    
    def glCopyTexSubImage3D(self, target, level, xoffset, yoffset, zoffset, x, y, width, height):
        'glCopyTexSubImage3D(self, target:int, level:int, xoffset:int, yoffset:int, zoffset:int, x:int, y:int, width:int, height:int)'
        pass
    
    def glDebugMessageControl(self, source, type, severity, count, ids, enabled):
        'glDebugMessageControl(self, source:int, type:int, severity:int, count:int, ids:typing.Sequence, enabled:int)'
        pass
    
    def glDebugMessageInsert(self, source, type, id, severity, length, buf):
        'glDebugMessageInsert(self, source:int, type:int, id:int, severity:int, length:int, buf:bytes)'
        pass
    
    def glDeleteProgramPipelines(self, n, pipelines):
        'glDeleteProgramPipelines(self, n:int, pipelines:typing.Sequence)'
        pass
    
    def glDeleteQueries(self, n, ids):
        'glDeleteQueries(self, n:int, ids:typing.Sequence)'
        pass
    
    def glDeleteSamplers(self, count, samplers):
        'glDeleteSamplers(self, count:int, samplers:typing.Sequence)'
        pass
    
    def glDeleteTransformFeedbacks(self, n, ids):
        'glDeleteTransformFeedbacks(self, n:int, ids:typing.Sequence)'
        pass
    
    def glDeleteVertexArrays(self, n, arrays):
        'glDeleteVertexArrays(self, n:int, arrays:typing.Sequence)'
        pass
    
    def glDisablei(self, target, index):
        'glDisablei(self, target:int, index:int)'
        pass
    
    def glDispatchCompute(self, num_groups_x, num_groups_y, num_groups_z):
        'glDispatchCompute(self, num_groups_x:int, num_groups_y:int, num_groups_z:int)'
        pass
    
    def glDrawArraysIndirect(self, mode, indirect):
        'glDrawArraysIndirect(self, mode:int, indirect:int)'
        pass
    
    def glDrawArraysInstanced(self, mode, first, count, instancecount):
        'glDrawArraysInstanced(self, mode:int, first:int, count:int, instancecount:int)'
        pass
    
    def glDrawBuffers(self, n, bufs):
        'glDrawBuffers(self, n:int, bufs:typing.Sequence)'
        pass
    
    def glDrawElementsBaseVertex(self, mode, count, type, indices, basevertex):
        'glDrawElementsBaseVertex(self, mode:int, count:int, type:int, indices:int, basevertex:int)'
        pass
    
    def glDrawElementsIndirect(self, mode, type, indirect):
        'glDrawElementsIndirect(self, mode:int, type:int, indirect:int)'
        pass
    
    def glDrawElementsInstanced(self, mode, count, type, indices, instancecount):
        'glDrawElementsInstanced(self, mode:int, count:int, type:int, indices:int, instancecount:int)'
        pass
    
    def glDrawElementsInstancedBaseVertex(self, mode, count, type, indices, instancecount, basevertex):
        'glDrawElementsInstancedBaseVertex(self, mode:int, count:int, type:int, indices:int, instancecount:int, basevertex:int)'
        pass
    
    def glDrawRangeElements(self, mode, start, end, count, type, indices):
        'glDrawRangeElements(self, mode:int, start:int, end:int, count:int, type:int, indices:int)'
        pass
    
    def glDrawRangeElementsBaseVertex(self, mode, start, end, count, type, indices, basevertex):
        'glDrawRangeElementsBaseVertex(self, mode:int, start:int, end:int, count:int, type:int, indices:int, basevertex:int)'
        pass
    
    def glEnablei(self, target, index):
        'glEnablei(self, target:int, index:int)'
        pass
    
    def glEndQuery(self, target):
        'glEndQuery(self, target:int)'
        pass
    
    def glFramebufferParameteri(self, target, pname, param):
        'glFramebufferParameteri(self, target:int, pname:int, param:int)'
        pass
    
    def glFramebufferTexture(self, target, attachment, texture, level):
        'glFramebufferTexture(self, target:int, attachment:int, texture:int, level:int)'
        pass
    
    def glFramebufferTextureLayer(self, target, attachment, texture, level, layer):
        'glFramebufferTextureLayer(self, target:int, attachment:int, texture:int, level:int, layer:int)'
        pass
    
    def glGenProgramPipelines(self, n, pipelines):
        'glGenProgramPipelines(self, n:int, pipelines:typing.Sequence)'
        pass
    
    def glGenQueries(self, n, ids):
        'glGenQueries(self, n:int, ids:typing.Sequence)'
        pass
    
    def glGenSamplers(self, count, samplers):
        'glGenSamplers(self, count:int, samplers:typing.Sequence)'
        pass
    
    def glGenTransformFeedbacks(self, n, ids):
        'glGenTransformFeedbacks(self, n:int, ids:typing.Sequence)'
        pass
    
    def glGenVertexArrays(self, n, arrays):
        'glGenVertexArrays(self, n:int, arrays:typing.Sequence)'
        pass
    
    def glGetActiveUniformBlockiv(self, program, uniformBlockIndex, pname, params):
        'glGetActiveUniformBlockiv(self, program:int, uniformBlockIndex:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetActiveUniformsiv(self, program, uniformCount, uniformIndices, pname, params):
        'glGetActiveUniformsiv(self, program:int, uniformCount:int, uniformIndices:typing.Sequence, pname:int, params:typing.Sequence)'
        pass
    
    def glGetBufferParameteri64v(self, target, pname):
        'glGetBufferParameteri64v(self, target:int, pname:int) -> int'
        return int
    
    def glGetFragDataLocation(self, program, name):
        'glGetFragDataLocation(self, program:int, name:bytes) -> int'
        return int
    
    def glGetFramebufferParameteriv(self, target, pname, params):
        'glGetFramebufferParameteriv(self, target:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetGraphicsResetStatus(self):
        'glGetGraphicsResetStatus(self) -> int'
        return int
    
    def glGetInteger64i_v(self, target, index):
        'glGetInteger64i_v(self, target:int, index:int) -> int'
        return int
    
    def glGetInteger64v(self, pname):
        'glGetInteger64v(self, pname:int) -> int'
        return int
    
    def glGetIntegeri_v(self, target, index, data):
        'glGetIntegeri_v(self, target:int, index:int, data:typing.Sequence)'
        pass
    
    def glGetInternalformativ(self, target, internalformat, pname, bufSize, params):
        'glGetInternalformativ(self, target:int, internalformat:int, pname:int, bufSize:int, params:typing.Sequence)'
        pass
    
    def glGetMultisamplefv(self, pname, index, val):
        'glGetMultisamplefv(self, pname:int, index:int, val:typing.Sequence)'
        pass
    
    def glGetProgramBinary(self, program, bufSize, binary):
        'glGetProgramBinary(self, program:int, bufSize:int, binary:int) -> typing.Tuple'
        return typing.Tuple
    
    def glGetProgramInterfaceiv(self, program, programInterface, pname, params):
        'glGetProgramInterfaceiv(self, program:int, programInterface:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetProgramPipelineiv(self, pipeline, pname, params):
        'glGetProgramPipelineiv(self, pipeline:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetProgramResourceIndex(self, program, programInterface, name):
        'glGetProgramResourceIndex(self, program:int, programInterface:int, name:bytes) -> int'
        return int
    
    def glGetProgramResourceLocation(self, program, programInterface, name):
        'glGetProgramResourceLocation(self, program:int, programInterface:int, name:bytes) -> int'
        return int
    
    def glGetProgramResourceiv(self, program, programInterface, index, propCount, props, bufSize, length, params):
        'glGetProgramResourceiv(self, program:int, programInterface:int, index:int, propCount:int, props:typing.Sequence, bufSize:int, length:typing.Sequence, params:typing.Sequence)'
        pass
    
    def glGetQueryObjectuiv(self, id, pname, params):
        'glGetQueryObjectuiv(self, id:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetQueryiv(self, target, pname, params):
        'glGetQueryiv(self, target:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetSamplerParameterIiv(self, sampler, pname):
        'glGetSamplerParameterIiv(self, sampler:int, pname:int) -> int'
        return int
    
    def glGetSamplerParameterIuiv(self, sampler, pname):
        'glGetSamplerParameterIuiv(self, sampler:int, pname:int) -> int'
        return int
    
    def glGetSamplerParameterfv(self, sampler, pname, params):
        'glGetSamplerParameterfv(self, sampler:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetSamplerParameteriv(self, sampler, pname, params):
        'glGetSamplerParameteriv(self, sampler:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetStringi(self, name, index):
        'glGetStringi(self, name:int, index:int) -> bytes'
        return bytes
    
    def glGetTexLevelParameterfv(self, target, level, pname, params):
        'glGetTexLevelParameterfv(self, target:int, level:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetTexLevelParameteriv(self, target, level, pname, params):
        'glGetTexLevelParameteriv(self, target:int, level:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetTexParameterIiv(self, target, pname):
        'glGetTexParameterIiv(self, target:int, pname:int) -> int'
        return int
    
    def glGetTexParameterIuiv(self, target, pname):
        'glGetTexParameterIuiv(self, target:int, pname:int) -> int'
        return int
    
    def glGetUniformBlockIndex(self, program, uniformBlockName):
        'glGetUniformBlockIndex(self, program:int, uniformBlockName:bytes) -> int'
        return int
    
    def glGetUniformuiv(self, program, location, params):
        'glGetUniformuiv(self, program:int, location:int, params:typing.Sequence)'
        pass
    
    def glGetVertexAttribIiv(self, index, pname, params):
        'glGetVertexAttribIiv(self, index:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetVertexAttribIuiv(self, index, pname, params):
        'glGetVertexAttribIuiv(self, index:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetnUniformfv(self, program, location, bufSize):
        'glGetnUniformfv(self, program:int, location:int, bufSize:int) -> float'
        return float
    
    def glGetnUniformiv(self, program, location, bufSize):
        'glGetnUniformiv(self, program:int, location:int, bufSize:int) -> int'
        return int
    
    def glGetnUniformuiv(self, program, location, bufSize):
        'glGetnUniformuiv(self, program:int, location:int, bufSize:int) -> int'
        return int
    
    def glInvalidateFramebuffer(self, target, numAttachments, attachments):
        'glInvalidateFramebuffer(self, target:int, numAttachments:int, attachments:typing.Sequence)'
        pass
    
    def glInvalidateSubFramebuffer(self, target, numAttachments, attachments, x, y, width, height):
        'glInvalidateSubFramebuffer(self, target:int, numAttachments:int, attachments:typing.Sequence, x:int, y:int, width:int, height:int)'
        pass
    
    def glIsEnabledi(self, target, index):
        'glIsEnabledi(self, target:int, index:int) -> int'
        return int
    
    def glIsProgramPipeline(self, pipeline):
        'glIsProgramPipeline(self, pipeline:int) -> int'
        return int
    
    def glIsQuery(self, id):
        'glIsQuery(self, id:int) -> int'
        return int
    
    def glIsSampler(self, sampler):
        'glIsSampler(self, sampler:int) -> int'
        return int
    
    def glIsTransformFeedback(self, id):
        'glIsTransformFeedback(self, id:int) -> int'
        return int
    
    def glIsVertexArray(self, array):
        'glIsVertexArray(self, array:int) -> int'
        return int
    
    def glMemoryBarrier(self, barriers):
        'glMemoryBarrier(self, barriers:int)'
        pass
    
    def glMemoryBarrierByRegion(self, barriers):
        'glMemoryBarrierByRegion(self, barriers:int)'
        pass
    
    def glMinSampleShading(self, value):
        'glMinSampleShading(self, value:float)'
        pass
    
    def glObjectLabel(self, identifier, name, length, label):
        'glObjectLabel(self, identifier:int, name:int, length:int, label:bytes)'
        pass
    
    def glObjectPtrLabel(self, ptr, length, label):
        'glObjectPtrLabel(self, ptr:int, length:int, label:bytes)'
        pass
    
    def glPatchParameteri(self, pname, value):
        'glPatchParameteri(self, pname:int, value:int)'
        pass
    
    def glPopDebugGroup(self):
        'glPopDebugGroup(self)'
        pass
    
    def glPrimitiveBoundingBox(self, minX, minY, minZ, minW, maxX, maxY, maxZ, maxW):
        'glPrimitiveBoundingBox(self, minX:float, minY:float, minZ:float, minW:float, maxX:float, maxY:float, maxZ:float, maxW:float)'
        pass
    
    def glProgramBinary(self, program, binaryFormat, binary, length):
        'glProgramBinary(self, program:int, binaryFormat:int, binary:int, length:int)'
        pass
    
    def glProgramParameteri(self, program, pname, value):
        'glProgramParameteri(self, program:int, pname:int, value:int)'
        pass
    
    def glProgramUniform1f(self, program, location, v0):
        'glProgramUniform1f(self, program:int, location:int, v0:float)'
        pass
    
    def glProgramUniform1fv(self, program, location, count, value):
        'glProgramUniform1fv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniform1i(self, program, location, v0):
        'glProgramUniform1i(self, program:int, location:int, v0:int)'
        pass
    
    def glProgramUniform1iv(self, program, location, count, value):
        'glProgramUniform1iv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniform1ui(self, program, location, v0):
        'glProgramUniform1ui(self, program:int, location:int, v0:int)'
        pass
    
    def glProgramUniform1uiv(self, program, location, count, value):
        'glProgramUniform1uiv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniform2f(self, program, location, v0, v1):
        'glProgramUniform2f(self, program:int, location:int, v0:float, v1:float)'
        pass
    
    def glProgramUniform2fv(self, program, location, count, value):
        'glProgramUniform2fv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniform2i(self, program, location, v0, v1):
        'glProgramUniform2i(self, program:int, location:int, v0:int, v1:int)'
        pass
    
    def glProgramUniform2iv(self, program, location, count, value):
        'glProgramUniform2iv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniform2ui(self, program, location, v0, v1):
        'glProgramUniform2ui(self, program:int, location:int, v0:int, v1:int)'
        pass
    
    def glProgramUniform2uiv(self, program, location, count, value):
        'glProgramUniform2uiv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniform3f(self, program, location, v0, v1, v2):
        'glProgramUniform3f(self, program:int, location:int, v0:float, v1:float, v2:float)'
        pass
    
    def glProgramUniform3fv(self, program, location, count, value):
        'glProgramUniform3fv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniform3i(self, program, location, v0, v1, v2):
        'glProgramUniform3i(self, program:int, location:int, v0:int, v1:int, v2:int)'
        pass
    
    def glProgramUniform3iv(self, program, location, count, value):
        'glProgramUniform3iv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniform3ui(self, program, location, v0, v1, v2):
        'glProgramUniform3ui(self, program:int, location:int, v0:int, v1:int, v2:int)'
        pass
    
    def glProgramUniform3uiv(self, program, location, count, value):
        'glProgramUniform3uiv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniform4f(self, program, location, v0, v1, v2, v3):
        'glProgramUniform4f(self, program:int, location:int, v0:float, v1:float, v2:float, v3:float)'
        pass
    
    def glProgramUniform4fv(self, program, location, count, value):
        'glProgramUniform4fv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniform4i(self, program, location, v0, v1, v2, v3):
        'glProgramUniform4i(self, program:int, location:int, v0:int, v1:int, v2:int, v3:int)'
        pass
    
    def glProgramUniform4iv(self, program, location, count, value):
        'glProgramUniform4iv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniform4ui(self, program, location, v0, v1, v2, v3):
        'glProgramUniform4ui(self, program:int, location:int, v0:int, v1:int, v2:int, v3:int)'
        pass
    
    def glProgramUniform4uiv(self, program, location, count, value):
        'glProgramUniform4uiv(self, program:int, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glProgramUniformMatrix2fv(self, program, location, count, transpose, value):
        'glProgramUniformMatrix2fv(self, program:int, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glProgramUniformMatrix2x3fv(self, program, location, count, transpose, value):
        'glProgramUniformMatrix2x3fv(self, program:int, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glProgramUniformMatrix2x4fv(self, program, location, count, transpose, value):
        'glProgramUniformMatrix2x4fv(self, program:int, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glProgramUniformMatrix3fv(self, program, location, count, transpose, value):
        'glProgramUniformMatrix3fv(self, program:int, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glProgramUniformMatrix3x2fv(self, program, location, count, transpose, value):
        'glProgramUniformMatrix3x2fv(self, program:int, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glProgramUniformMatrix3x4fv(self, program, location, count, transpose, value):
        'glProgramUniformMatrix3x4fv(self, program:int, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glProgramUniformMatrix4fv(self, program, location, count, transpose, value):
        'glProgramUniformMatrix4fv(self, program:int, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glProgramUniformMatrix4x2fv(self, program, location, count, transpose, value):
        'glProgramUniformMatrix4x2fv(self, program:int, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glProgramUniformMatrix4x3fv(self, program, location, count, transpose, value):
        'glProgramUniformMatrix4x3fv(self, program:int, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glPushDebugGroup(self, source, id, length, message):
        'glPushDebugGroup(self, source:int, id:int, length:int, message:bytes)'
        pass
    
    def glReadBuffer(self, mode):
        'glReadBuffer(self, mode:int)'
        pass
    
    def glReadnPixels(self, x, y, width, height, format, type, bufSize, data):
        'glReadnPixels(self, x:int, y:int, width:int, height:int, format:int, type:int, bufSize:int, data:int)'
        pass
    
    def glRenderbufferStorageMultisample(self, target, samples, internalformat, width, height):
        'glRenderbufferStorageMultisample(self, target:int, samples:int, internalformat:int, width:int, height:int)'
        pass
    
    def glSampleMaski(self, maskNumber, mask):
        'glSampleMaski(self, maskNumber:int, mask:int)'
        pass
    
    def glSamplerParameterIiv(self, sampler, pname, param):
        'glSamplerParameterIiv(self, sampler:int, pname:int, param:typing.Sequence)'
        pass
    
    def glSamplerParameterIuiv(self, sampler, pname, param):
        'glSamplerParameterIuiv(self, sampler:int, pname:int, param:typing.Sequence)'
        pass
    
    def glSamplerParameterf(self, sampler, pname, param):
        'glSamplerParameterf(self, sampler:int, pname:int, param:float)'
        pass
    
    def glSamplerParameterfv(self, sampler, pname, param):
        'glSamplerParameterfv(self, sampler:int, pname:int, param:typing.Sequence)'
        pass
    
    def glSamplerParameteri(self, sampler, pname, param):
        'glSamplerParameteri(self, sampler:int, pname:int, param:int)'
        pass
    
    def glSamplerParameteriv(self, sampler, pname, param):
        'glSamplerParameteriv(self, sampler:int, pname:int, param:typing.Sequence)'
        pass
    
    def glTexBuffer(self, target, internalformat, buffer):
        'glTexBuffer(self, target:int, internalformat:int, buffer:int)'
        pass
    
    def glTexImage3D(self, target, level, internalformat, width, height, depth, border, format, type, pixels):
        'glTexImage3D(self, target:int, level:int, internalformat:int, width:int, height:int, depth:int, border:int, format:int, type:int, pixels:int)'
        pass
    
    def glTexParameterIiv(self, target, pname, params):
        'glTexParameterIiv(self, target:int, pname:int, params:typing.Sequence)'
        pass
    
    def glTexParameterIuiv(self, target, pname, params):
        'glTexParameterIuiv(self, target:int, pname:int, params:typing.Sequence)'
        pass
    
    def glTexStorage2D(self, target, levels, internalformat, width, height):
        'glTexStorage2D(self, target:int, levels:int, internalformat:int, width:int, height:int)'
        pass
    
    def glTexStorage2DMultisample(self, target, samples, internalformat, width, height, fixedsamplelocations):
        'glTexStorage2DMultisample(self, target:int, samples:int, internalformat:int, width:int, height:int, fixedsamplelocations:int)'
        pass
    
    def glTexStorage3D(self, target, levels, internalformat, width, height, depth):
        'glTexStorage3D(self, target:int, levels:int, internalformat:int, width:int, height:int, depth:int)'
        pass
    
    def glTexStorage3DMultisample(self, target, samples, internalformat, width, height, depth, fixedsamplelocations):
        'glTexStorage3DMultisample(self, target:int, samples:int, internalformat:int, width:int, height:int, depth:int, fixedsamplelocations:int)'
        pass
    
    def glTexSubImage3D(self, target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
        'glTexSubImage3D(self, target:int, level:int, xoffset:int, yoffset:int, zoffset:int, width:int, height:int, depth:int, format:int, type:int, pixels:int)'
        pass
    
    def glUniform1ui(self, location, v0):
        'glUniform1ui(self, location:int, v0:int)'
        pass
    
    def glUniform1uiv(self, location, count, value):
        'glUniform1uiv(self, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glUniform2ui(self, location, v0, v1):
        'glUniform2ui(self, location:int, v0:int, v1:int)'
        pass
    
    def glUniform2uiv(self, location, count, value):
        'glUniform2uiv(self, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glUniform3ui(self, location, v0, v1, v2):
        'glUniform3ui(self, location:int, v0:int, v1:int, v2:int)'
        pass
    
    def glUniform3uiv(self, location, count, value):
        'glUniform3uiv(self, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glUniform4ui(self, location, v0, v1, v2, v3):
        'glUniform4ui(self, location:int, v0:int, v1:int, v2:int, v3:int)'
        pass
    
    def glUniform4uiv(self, location, count, value):
        'glUniform4uiv(self, location:int, count:int, value:typing.Sequence)'
        pass
    
    def glUniformBlockBinding(self, program, uniformBlockIndex, uniformBlockBinding):
        'glUniformBlockBinding(self, program:int, uniformBlockIndex:int, uniformBlockBinding:int)'
        pass
    
    def glUniformMatrix2x3fv(self, location, count, transpose, value):
        'glUniformMatrix2x3fv(self, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glUniformMatrix2x4fv(self, location, count, transpose, value):
        'glUniformMatrix2x4fv(self, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glUniformMatrix3x2fv(self, location, count, transpose, value):
        'glUniformMatrix3x2fv(self, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glUniformMatrix3x4fv(self, location, count, transpose, value):
        'glUniformMatrix3x4fv(self, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glUniformMatrix4x2fv(self, location, count, transpose, value):
        'glUniformMatrix4x2fv(self, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glUniformMatrix4x3fv(self, location, count, transpose, value):
        'glUniformMatrix4x3fv(self, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glUnmapBuffer(self, target):
        'glUnmapBuffer(self, target:int) -> int'
        return int
    
    def glUseProgramStages(self, pipeline, stages, program):
        'glUseProgramStages(self, pipeline:int, stages:int, program:int)'
        pass
    
    def glValidateProgramPipeline(self, pipeline):
        'glValidateProgramPipeline(self, pipeline:int)'
        pass
    
    def glVertexAttribBinding(self, attribindex, bindingindex):
        'glVertexAttribBinding(self, attribindex:int, bindingindex:int)'
        pass
    
    def glVertexAttribDivisor(self, index, divisor):
        'glVertexAttribDivisor(self, index:int, divisor:int)'
        pass
    
    def glVertexAttribFormat(self, attribindex, size, type, normalized, relativeoffset):
        'glVertexAttribFormat(self, attribindex:int, size:int, type:int, normalized:int, relativeoffset:int)'
        pass
    
    def glVertexAttribI4i(self, index, x, y, z, w):
        'glVertexAttribI4i(self, index:int, x:int, y:int, z:int, w:int)'
        pass
    
    def glVertexAttribI4iv(self, index, v):
        'glVertexAttribI4iv(self, index:int, v:typing.Sequence)'
        pass
    
    def glVertexAttribI4ui(self, index, x, y, z, w):
        'glVertexAttribI4ui(self, index:int, x:int, y:int, z:int, w:int)'
        pass
    
    def glVertexAttribI4uiv(self, index, v):
        'glVertexAttribI4uiv(self, index:int, v:typing.Sequence)'
        pass
    
    def glVertexAttribIFormat(self, attribindex, size, type, relativeoffset):
        'glVertexAttribIFormat(self, attribindex:int, size:int, type:int, relativeoffset:int)'
        pass
    
    def glVertexAttribIPointer(self, index, size, type, stride, pointer):
        'glVertexAttribIPointer(self, index:int, size:int, type:int, stride:int, pointer:int)'
        pass
    
    def glVertexBindingDivisor(self, bindingindex, divisor):
        'glVertexBindingDivisor(self, bindingindex:int, divisor:int)'
        pass
    

class QOpenGLFramebufferObject(_mod_Shiboken.Object):
    'QOpenGLFramebufferObject(self, size:PySide2.QtCore.QSize, attachment:PySide2.QtGui.QOpenGLFramebufferObject.Attachment, target:int=3553, internalFormat:int=0)\nQOpenGLFramebufferObject(self, size:PySide2.QtCore.QSize, format:PySide2.QtGui.QOpenGLFramebufferObjectFormat)\nQOpenGLFramebufferObject(self, size:PySide2.QtCore.QSize, target:int=3553)\nQOpenGLFramebufferObject(self, width:int, height:int, attachment:PySide2.QtGui.QOpenGLFramebufferObject.Attachment, target:int=3553, internalFormat:int=0)\nQOpenGLFramebufferObject(self, width:int, height:int, format:PySide2.QtGui.QOpenGLFramebufferObjectFormat)\nQOpenGLFramebufferObject(self, width:int, height:int, target:int=3553)'
    Attachment = Attachment
    CombinedDepthStencil = Attachment()
    Depth = Attachment()
    DontRestoreFramebufferBinding = FramebufferRestorePolicy()
    FramebufferRestorePolicy = FramebufferRestorePolicy
    NoAttachment = Attachment()
    RestoreFrameBufferBinding = FramebufferRestorePolicy()
    RestoreFramebufferBindingToDefault = FramebufferRestorePolicy()
    __class__ = QOpenGLFramebufferObject
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, size: PySide2.QtCore.QSize, attachment: PySide2.QtGui.QOpenGLFramebufferObject.Attachment, target: int=3553, internalFormat: int=0):
        'QOpenGLFramebufferObject(self, size:PySide2.QtCore.QSize, attachment:PySide2.QtGui.QOpenGLFramebufferObject.Attachment, target:int=3553, internalFormat:int=0)\nQOpenGLFramebufferObject(self, size:PySide2.QtCore.QSize, format:PySide2.QtGui.QOpenGLFramebufferObjectFormat)\nQOpenGLFramebufferObject(self, size:PySide2.QtCore.QSize, target:int=3553)\nQOpenGLFramebufferObject(self, width:int, height:int, attachment:PySide2.QtGui.QOpenGLFramebufferObject.Attachment, target:int=3553, internalFormat:int=0)\nQOpenGLFramebufferObject(self, width:int, height:int, format:PySide2.QtGui.QOpenGLFramebufferObjectFormat)\nQOpenGLFramebufferObject(self, width:int, height:int, target:int=3553)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addColorAttachment(self, size: PySide2.QtCore.QSize, internalFormat: int=0):
        'addColorAttachment(self, size:PySide2.QtCore.QSize, internalFormat:int=0)\naddColorAttachment(self, width:int, height:int, internalFormat:int=0)'
        pass
    
    def attachment(self):
        'attachment(self) -> PySide2.QtGui.QOpenGLFramebufferObject.Attachment'
        return PySide2.QtGui.QOpenGLFramebufferObject.Attachment
    
    def bind(self):
        'bind(self) -> bool'
        return bool
    
    @classmethod
    def bindDefault(cls):
        'bindDefault() -> bool'
        return bool
    
    @classmethod
    def blitFramebuffer(cls, target: PySide2.QtGui.QOpenGLFramebufferObject, targetRect: PySide2.QtCore.QRect, source: PySide2.QtGui.QOpenGLFramebufferObject, sourceRect: PySide2.QtCore.QRect, buffers: int, filter: int, readColorAttachmentIndex: int, drawColorAttachmentIndex: int, restorePolicy: PySide2.QtGui.QOpenGLFramebufferObject.FramebufferRestorePolicy):
        'blitFramebuffer(target:PySide2.QtGui.QOpenGLFramebufferObject, source:PySide2.QtGui.QOpenGLFramebufferObject, buffers:int=16384, filter:int=9728)\nblitFramebuffer(target:PySide2.QtGui.QOpenGLFramebufferObject, targetRect:PySide2.QtCore.QRect, source:PySide2.QtGui.QOpenGLFramebufferObject, sourceRect:PySide2.QtCore.QRect, buffers:int, filter:int, readColorAttachmentIndex:int, drawColorAttachmentIndex:int)\nblitFramebuffer(target:PySide2.QtGui.QOpenGLFramebufferObject, targetRect:PySide2.QtCore.QRect, source:PySide2.QtGui.QOpenGLFramebufferObject, sourceRect:PySide2.QtCore.QRect, buffers:int, filter:int, readColorAttachmentIndex:int, drawColorAttachmentIndex:int, restorePolicy:PySide2.QtGui.QOpenGLFramebufferObject.FramebufferRestorePolicy)\nblitFramebuffer(target:PySide2.QtGui.QOpenGLFramebufferObject, targetRect:PySide2.QtCore.QRect, source:PySide2.QtGui.QOpenGLFramebufferObject, sourceRect:PySide2.QtCore.QRect, buffers:int=16384, filter:int=9728)'
        pass
    
    def format(self):
        'format(self) -> PySide2.QtGui.QOpenGLFramebufferObjectFormat'
        return PySide2.QtGui.QOpenGLFramebufferObjectFormat
    
    def handle(self):
        'handle(self) -> int'
        return int
    
    @classmethod
    def hasOpenGLFramebufferBlit(cls):
        'hasOpenGLFramebufferBlit() -> bool'
        return bool
    
    @classmethod
    def hasOpenGLFramebufferObjects(cls):
        'hasOpenGLFramebufferObjects() -> bool'
        return bool
    
    def height(self):
        'height(self) -> int'
        return int
    
    def isBound(self):
        'isBound(self) -> bool'
        return bool
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def release(self):
        'release(self) -> bool'
        return bool
    
    def setAttachment(self, attachment):
        'setAttachment(self, attachment:PySide2.QtGui.QOpenGLFramebufferObject.Attachment)'
        pass
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def sizes(self):
        'sizes(self) -> typing.List'
        return typing.List
    
    def takeTexture(self, colorAttachmentIndex: int):
        'takeTexture(self) -> int\ntakeTexture(self, colorAttachmentIndex:int) -> int'
        return 1
    
    def texture(self):
        'texture(self) -> int'
        return int
    
    def textures(self):
        'textures(self) -> typing.List'
        return typing.List
    
    def toImage(self, flipped: bool, colorAttachmentIndex: int):
        'toImage(self) -> PySide2.QtGui.QImage\ntoImage(self, flipped:bool) -> PySide2.QtGui.QImage\ntoImage(self, flipped:bool, colorAttachmentIndex:int) -> PySide2.QtGui.QImage'
        pass
    
    def width(self):
        'width(self) -> int'
        return int
    

class QOpenGLFramebufferObjectFormat(_mod_Shiboken.Object):
    'QOpenGLFramebufferObjectFormat(self)\nQOpenGLFramebufferObjectFormat(self, other:PySide2.QtGui.QOpenGLFramebufferObjectFormat)'
    __class__ = QOpenGLFramebufferObjectFormat
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, other: PySide2.QtGui.QOpenGLFramebufferObjectFormat):
        'QOpenGLFramebufferObjectFormat(self)\nQOpenGLFramebufferObjectFormat(self, other:PySide2.QtGui.QOpenGLFramebufferObjectFormat)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def attachment(self):
        'attachment(self) -> PySide2.QtGui.QOpenGLFramebufferObject.Attachment'
        return PySide2.QtGui.QOpenGLFramebufferObject.Attachment
    
    def internalTextureFormat(self):
        'internalTextureFormat(self) -> int'
        return int
    
    def mipmap(self):
        'mipmap(self) -> bool'
        return bool
    
    def samples(self):
        'samples(self) -> int'
        return int
    
    def setAttachment(self, attachment):
        'setAttachment(self, attachment:PySide2.QtGui.QOpenGLFramebufferObject.Attachment)'
        pass
    
    def setInternalTextureFormat(self, internalTextureFormat):
        'setInternalTextureFormat(self, internalTextureFormat:int)'
        pass
    
    def setMipmap(self, enabled):
        'setMipmap(self, enabled:bool)'
        pass
    
    def setSamples(self, samples):
        'setSamples(self, samples:int)'
        pass
    
    def setTextureTarget(self, target):
        'setTextureTarget(self, target:int)'
        pass
    
    def textureTarget(self):
        'textureTarget(self) -> int'
        return int
    

class QOpenGLFunctions(_mod_Shiboken.Object):
    'QOpenGLFunctions(self)\nQOpenGLFunctions(self, context:PySide2.QtGui.QOpenGLContext)'
    BlendColor = OpenGLFeature()
    BlendEquation = OpenGLFeature()
    BlendEquationAdvanced = OpenGLFeature()
    BlendEquationSeparate = OpenGLFeature()
    BlendFuncSeparate = OpenGLFeature()
    BlendSubtract = OpenGLFeature()
    Buffers = OpenGLFeature()
    CompressedTextures = OpenGLFeature()
    FixedFunctionPipeline = OpenGLFeature()
    Framebuffers = OpenGLFeature()
    MultipleRenderTargets = OpenGLFeature()
    Multisample = OpenGLFeature()
    Multitexture = OpenGLFeature()
    NPOTTextureRepeat = OpenGLFeature()
    NPOTTextures = OpenGLFeature()
    OpenGLFeature = OpenGLFeature
    OpenGLFeatures = OpenGLFeatures
    Shaders = OpenGLFeature()
    StencilSeparate = OpenGLFeature()
    TextureRGFormats = OpenGLFeature()
    __class__ = QOpenGLFunctions
    __dict__ = {}
    def __init__(self, context: PySide2.QtGui.QOpenGLContext):
        'QOpenGLFunctions(self)\nQOpenGLFunctions(self, context:PySide2.QtGui.QOpenGLContext)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def glActiveTexture(self, texture):
        'glActiveTexture(self, texture:int)'
        pass
    
    def glAttachShader(self, program, shader):
        'glAttachShader(self, program:int, shader:int)'
        pass
    
    def glBindAttribLocation(self, program, index, name):
        'glBindAttribLocation(self, program:int, index:int, name:bytes)'
        pass
    
    def glBindBuffer(self, target, buffer):
        'glBindBuffer(self, target:int, buffer:int)'
        pass
    
    def glBindFramebuffer(self, target, framebuffer):
        'glBindFramebuffer(self, target:int, framebuffer:int)'
        pass
    
    def glBindRenderbuffer(self, target, renderbuffer):
        'glBindRenderbuffer(self, target:int, renderbuffer:int)'
        pass
    
    def glBindTexture(self, target, texture):
        'glBindTexture(self, target:int, texture:int)'
        pass
    
    def glBlendColor(self, red, green, blue, alpha):
        'glBlendColor(self, red:float, green:float, blue:float, alpha:float)'
        pass
    
    def glBlendEquation(self, mode):
        'glBlendEquation(self, mode:int)'
        pass
    
    def glBlendEquationSeparate(self, modeRGB, modeAlpha):
        'glBlendEquationSeparate(self, modeRGB:int, modeAlpha:int)'
        pass
    
    def glBlendFunc(self, sfactor, dfactor):
        'glBlendFunc(self, sfactor:int, dfactor:int)'
        pass
    
    def glBlendFuncSeparate(self, srcRGB, dstRGB, srcAlpha, dstAlpha):
        'glBlendFuncSeparate(self, srcRGB:int, dstRGB:int, srcAlpha:int, dstAlpha:int)'
        pass
    
    def glCheckFramebufferStatus(self, target):
        'glCheckFramebufferStatus(self, target:int) -> int'
        return int
    
    def glClear(self, mask):
        'glClear(self, mask:int)'
        pass
    
    def glClearColor(self, red, green, blue, alpha):
        'glClearColor(self, red:float, green:float, blue:float, alpha:float)'
        pass
    
    def glClearDepthf(self, depth):
        'glClearDepthf(self, depth:float)'
        pass
    
    def glClearStencil(self, s):
        'glClearStencil(self, s:int)'
        pass
    
    def glColorMask(self, red, green, blue, alpha):
        'glColorMask(self, red:int, green:int, blue:int, alpha:int)'
        pass
    
    def glCompileShader(self, shader):
        'glCompileShader(self, shader:int)'
        pass
    
    def glCompressedTexImage2D(self, target, level, internalformat, width, height, border, imageSize, data):
        'glCompressedTexImage2D(self, target:int, level:int, internalformat:int, width:int, height:int, border:int, imageSize:int, data:int)'
        pass
    
    def glCompressedTexSubImage2D(self, target, level, xoffset, yoffset, width, height, format, imageSize, data):
        'glCompressedTexSubImage2D(self, target:int, level:int, xoffset:int, yoffset:int, width:int, height:int, format:int, imageSize:int, data:int)'
        pass
    
    def glCopyTexImage2D(self, target, level, internalformat, x, y, width, height, border):
        'glCopyTexImage2D(self, target:int, level:int, internalformat:int, x:int, y:int, width:int, height:int, border:int)'
        pass
    
    def glCopyTexSubImage2D(self, target, level, xoffset, yoffset, x, y, width, height):
        'glCopyTexSubImage2D(self, target:int, level:int, xoffset:int, yoffset:int, x:int, y:int, width:int, height:int)'
        pass
    
    def glCreateProgram(self):
        'glCreateProgram(self) -> int'
        return int
    
    def glCreateShader(self, type):
        'glCreateShader(self, type:int) -> int'
        return int
    
    def glCullFace(self, mode):
        'glCullFace(self, mode:int)'
        pass
    
    def glDeleteBuffers(self, n, buffers):
        'glDeleteBuffers(self, n:int, buffers:typing.Sequence)'
        pass
    
    def glDeleteFramebuffers(self, n, framebuffers):
        'glDeleteFramebuffers(self, n:int, framebuffers:typing.Sequence)'
        pass
    
    def glDeleteProgram(self, program):
        'glDeleteProgram(self, program:int)'
        pass
    
    def glDeleteRenderbuffers(self, n, renderbuffers):
        'glDeleteRenderbuffers(self, n:int, renderbuffers:typing.Sequence)'
        pass
    
    def glDeleteShader(self, shader):
        'glDeleteShader(self, shader:int)'
        pass
    
    def glDeleteTextures(self, n, textures):
        'glDeleteTextures(self, n:int, textures:typing.Sequence)'
        pass
    
    def glDepthFunc(self, func):
        'glDepthFunc(self, func:int)'
        pass
    
    def glDepthMask(self, flag):
        'glDepthMask(self, flag:int)'
        pass
    
    def glDepthRangef(self, zNear, zFar):
        'glDepthRangef(self, zNear:float, zFar:float)'
        pass
    
    def glDetachShader(self, program, shader):
        'glDetachShader(self, program:int, shader:int)'
        pass
    
    def glDisable(self, cap):
        'glDisable(self, cap:int)'
        pass
    
    def glDisableVertexAttribArray(self, index):
        'glDisableVertexAttribArray(self, index:int)'
        pass
    
    def glDrawArrays(self, mode, first, count):
        'glDrawArrays(self, mode:int, first:int, count:int)'
        pass
    
    def glDrawElements(self, mode, count, type, indices):
        'glDrawElements(self, mode:int, count:int, type:int, indices:int)'
        pass
    
    def glEnable(self, cap):
        'glEnable(self, cap:int)'
        pass
    
    def glEnableVertexAttribArray(self, index):
        'glEnableVertexAttribArray(self, index:int)'
        pass
    
    def glFinish(self):
        'glFinish(self)'
        pass
    
    def glFlush(self):
        'glFlush(self)'
        pass
    
    def glFramebufferRenderbuffer(self, target, attachment, renderbuffertarget, renderbuffer):
        'glFramebufferRenderbuffer(self, target:int, attachment:int, renderbuffertarget:int, renderbuffer:int)'
        pass
    
    def glFramebufferTexture2D(self, target, attachment, textarget, texture, level):
        'glFramebufferTexture2D(self, target:int, attachment:int, textarget:int, texture:int, level:int)'
        pass
    
    def glFrontFace(self, mode):
        'glFrontFace(self, mode:int)'
        pass
    
    def glGenBuffers(self, n, buffers):
        'glGenBuffers(self, n:int, buffers:typing.Sequence)'
        pass
    
    def glGenFramebuffers(self, n, framebuffers):
        'glGenFramebuffers(self, n:int, framebuffers:typing.Sequence)'
        pass
    
    def glGenRenderbuffers(self, n, renderbuffers):
        'glGenRenderbuffers(self, n:int, renderbuffers:typing.Sequence)'
        pass
    
    def glGenTextures(self, n, textures):
        'glGenTextures(self, n:int, textures:typing.Sequence)'
        pass
    
    def glGenerateMipmap(self, target):
        'glGenerateMipmap(self, target:int)'
        pass
    
    def glGetAttachedShaders(self, program, maxcount, count, shaders):
        'glGetAttachedShaders(self, program:int, maxcount:int, count:typing.Sequence, shaders:typing.Sequence)'
        pass
    
    def glGetAttribLocation(self, program, name):
        'glGetAttribLocation(self, program:int, name:bytes) -> int'
        return int
    
    def glGetBufferParameteriv(self, target, pname, params):
        'glGetBufferParameteriv(self, target:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetError(self):
        'glGetError(self) -> int'
        return int
    
    def glGetFloatv(self, pname, params):
        'glGetFloatv(self, pname:int, params:typing.Sequence)'
        pass
    
    def glGetFramebufferAttachmentParameteriv(self, target, attachment, pname, params):
        'glGetFramebufferAttachmentParameteriv(self, target:int, attachment:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetIntegerv(self, pname, params):
        'glGetIntegerv(self, pname:int, params:typing.Sequence)'
        pass
    
    def glGetProgramiv(self, program, pname, params):
        'glGetProgramiv(self, program:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetRenderbufferParameteriv(self, target, pname, params):
        'glGetRenderbufferParameteriv(self, target:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetShaderPrecisionFormat(self, shadertype, precisiontype, range, precision):
        'glGetShaderPrecisionFormat(self, shadertype:int, precisiontype:int, range:typing.Sequence, precision:typing.Sequence)'
        pass
    
    def glGetShaderiv(self, shader, pname, params):
        'glGetShaderiv(self, shader:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetString(self, name):
        'glGetString(self, name:int) -> bytes'
        return bytes
    
    def glGetTexParameterfv(self, target, pname, params):
        'glGetTexParameterfv(self, target:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetTexParameteriv(self, target, pname, params):
        'glGetTexParameteriv(self, target:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetUniformLocation(self, program, name):
        'glGetUniformLocation(self, program:int, name:bytes) -> int'
        return int
    
    def glGetUniformfv(self, program, location, params):
        'glGetUniformfv(self, program:int, location:int, params:typing.Sequence)'
        pass
    
    def glGetUniformiv(self, program, location, params):
        'glGetUniformiv(self, program:int, location:int, params:typing.Sequence)'
        pass
    
    def glGetVertexAttribfv(self, index, pname, params):
        'glGetVertexAttribfv(self, index:int, pname:int, params:typing.Sequence)'
        pass
    
    def glGetVertexAttribiv(self, index, pname, params):
        'glGetVertexAttribiv(self, index:int, pname:int, params:typing.Sequence)'
        pass
    
    def glHint(self, target, mode):
        'glHint(self, target:int, mode:int)'
        pass
    
    def glIsBuffer(self, buffer):
        'glIsBuffer(self, buffer:int) -> int'
        return int
    
    def glIsEnabled(self, cap):
        'glIsEnabled(self, cap:int) -> int'
        return int
    
    def glIsFramebuffer(self, framebuffer):
        'glIsFramebuffer(self, framebuffer:int) -> int'
        return int
    
    def glIsProgram(self, program):
        'glIsProgram(self, program:int) -> int'
        return int
    
    def glIsRenderbuffer(self, renderbuffer):
        'glIsRenderbuffer(self, renderbuffer:int) -> int'
        return int
    
    def glIsShader(self, shader):
        'glIsShader(self, shader:int) -> int'
        return int
    
    def glIsTexture(self, texture):
        'glIsTexture(self, texture:int) -> int'
        return int
    
    def glLineWidth(self, width):
        'glLineWidth(self, width:float)'
        pass
    
    def glLinkProgram(self, program):
        'glLinkProgram(self, program:int)'
        pass
    
    def glPixelStorei(self, pname, param):
        'glPixelStorei(self, pname:int, param:int)'
        pass
    
    def glPolygonOffset(self, factor, units):
        'glPolygonOffset(self, factor:float, units:float)'
        pass
    
    def glReadPixels(self, x, y, width, height, format, type, pixels):
        'glReadPixels(self, x:int, y:int, width:int, height:int, format:int, type:int, pixels:int)'
        pass
    
    def glReleaseShaderCompiler(self):
        'glReleaseShaderCompiler(self)'
        pass
    
    def glRenderbufferStorage(self, target, internalformat, width, height):
        'glRenderbufferStorage(self, target:int, internalformat:int, width:int, height:int)'
        pass
    
    def glSampleCoverage(self, value, invert):
        'glSampleCoverage(self, value:float, invert:int)'
        pass
    
    def glScissor(self, x, y, width, height):
        'glScissor(self, x:int, y:int, width:int, height:int)'
        pass
    
    def glShaderBinary(self, n, shaders, binaryformat, binary, length):
        'glShaderBinary(self, n:int, shaders:typing.Sequence, binaryformat:int, binary:int, length:int)'
        pass
    
    def glStencilFunc(self, func, ref, mask):
        'glStencilFunc(self, func:int, ref:int, mask:int)'
        pass
    
    def glStencilFuncSeparate(self, face, func, ref, mask):
        'glStencilFuncSeparate(self, face:int, func:int, ref:int, mask:int)'
        pass
    
    def glStencilMask(self, mask):
        'glStencilMask(self, mask:int)'
        pass
    
    def glStencilMaskSeparate(self, face, mask):
        'glStencilMaskSeparate(self, face:int, mask:int)'
        pass
    
    def glStencilOp(self, fail, zfail, zpass):
        'glStencilOp(self, fail:int, zfail:int, zpass:int)'
        pass
    
    def glStencilOpSeparate(self, face, fail, zfail, zpass):
        'glStencilOpSeparate(self, face:int, fail:int, zfail:int, zpass:int)'
        pass
    
    def glTexImage2D(self, target, level, internalformat, width, height, border, format, type, pixels):
        'glTexImage2D(self, target:int, level:int, internalformat:int, width:int, height:int, border:int, format:int, type:int, pixels:int)'
        pass
    
    def glTexParameterf(self, target, pname, param):
        'glTexParameterf(self, target:int, pname:int, param:float)'
        pass
    
    def glTexParameterfv(self, target, pname, params):
        'glTexParameterfv(self, target:int, pname:int, params:typing.Sequence)'
        pass
    
    def glTexParameteri(self, target, pname, param):
        'glTexParameteri(self, target:int, pname:int, param:int)'
        pass
    
    def glTexParameteriv(self, target, pname, params):
        'glTexParameteriv(self, target:int, pname:int, params:typing.Sequence)'
        pass
    
    def glTexSubImage2D(self, target, level, xoffset, yoffset, width, height, format, type, pixels):
        'glTexSubImage2D(self, target:int, level:int, xoffset:int, yoffset:int, width:int, height:int, format:int, type:int, pixels:int)'
        pass
    
    def glUniform1f(self, location, x):
        'glUniform1f(self, location:int, x:float)'
        pass
    
    def glUniform1fv(self, location, count, v):
        'glUniform1fv(self, location:int, count:int, v:typing.Sequence)'
        pass
    
    def glUniform1i(self, location, x):
        'glUniform1i(self, location:int, x:int)'
        pass
    
    def glUniform1iv(self, location, count, v):
        'glUniform1iv(self, location:int, count:int, v:typing.Sequence)'
        pass
    
    def glUniform2f(self, location, x, y):
        'glUniform2f(self, location:int, x:float, y:float)'
        pass
    
    def glUniform2fv(self, location, count, v):
        'glUniform2fv(self, location:int, count:int, v:typing.Sequence)'
        pass
    
    def glUniform2i(self, location, x, y):
        'glUniform2i(self, location:int, x:int, y:int)'
        pass
    
    def glUniform2iv(self, location, count, v):
        'glUniform2iv(self, location:int, count:int, v:typing.Sequence)'
        pass
    
    def glUniform3f(self, location, x, y, z):
        'glUniform3f(self, location:int, x:float, y:float, z:float)'
        pass
    
    def glUniform3fv(self, location, count, v):
        'glUniform3fv(self, location:int, count:int, v:typing.Sequence)'
        pass
    
    def glUniform3i(self, location, x, y, z):
        'glUniform3i(self, location:int, x:int, y:int, z:int)'
        pass
    
    def glUniform3iv(self, location, count, v):
        'glUniform3iv(self, location:int, count:int, v:typing.Sequence)'
        pass
    
    def glUniform4f(self, location, x, y, z, w):
        'glUniform4f(self, location:int, x:float, y:float, z:float, w:float)'
        pass
    
    def glUniform4fv(self, location, count, v):
        'glUniform4fv(self, location:int, count:int, v:typing.Sequence)'
        pass
    
    def glUniform4i(self, location, x, y, z, w):
        'glUniform4i(self, location:int, x:int, y:int, z:int, w:int)'
        pass
    
    def glUniform4iv(self, location, count, v):
        'glUniform4iv(self, location:int, count:int, v:typing.Sequence)'
        pass
    
    def glUniformMatrix2fv(self, location, count, transpose, value):
        'glUniformMatrix2fv(self, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glUniformMatrix3fv(self, location, count, transpose, value):
        'glUniformMatrix3fv(self, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glUniformMatrix4fv(self, location, count, transpose, value):
        'glUniformMatrix4fv(self, location:int, count:int, transpose:int, value:typing.Sequence)'
        pass
    
    def glUseProgram(self, program):
        'glUseProgram(self, program:int)'
        pass
    
    def glValidateProgram(self, program):
        'glValidateProgram(self, program:int)'
        pass
    
    def glVertexAttrib1f(self, indx, x):
        'glVertexAttrib1f(self, indx:int, x:float)'
        pass
    
    def glVertexAttrib1fv(self, indx, values):
        'glVertexAttrib1fv(self, indx:int, values:typing.Sequence)'
        pass
    
    def glVertexAttrib2f(self, indx, x, y):
        'glVertexAttrib2f(self, indx:int, x:float, y:float)'
        pass
    
    def glVertexAttrib2fv(self, indx, values):
        'glVertexAttrib2fv(self, indx:int, values:typing.Sequence)'
        pass
    
    def glVertexAttrib3f(self, indx, x, y, z):
        'glVertexAttrib3f(self, indx:int, x:float, y:float, z:float)'
        pass
    
    def glVertexAttrib3fv(self, indx, values):
        'glVertexAttrib3fv(self, indx:int, values:typing.Sequence)'
        pass
    
    def glVertexAttrib4f(self, indx, x, y, z, w):
        'glVertexAttrib4f(self, indx:int, x:float, y:float, z:float, w:float)'
        pass
    
    def glVertexAttrib4fv(self, indx, values):
        'glVertexAttrib4fv(self, indx:int, values:typing.Sequence)'
        pass
    
    def glVertexAttribPointer(self, indx, size, type, normalized, stride, ptr):
        'glVertexAttribPointer(self, indx:int, size:int, type:int, normalized:int, stride:int, ptr:int)'
        pass
    
    def glViewport(self, x, y, width, height):
        'glViewport(self, x:int, y:int, width:int, height:int)'
        pass
    
    def hasOpenGLFeature(self, feature):
        'hasOpenGLFeature(self, feature:PySide2.QtGui.QOpenGLFunctions.OpenGLFeature) -> bool'
        return bool
    
    def initializeOpenGLFunctions(self):
        'initializeOpenGLFunctions(self)'
        pass
    
    def openGLFeatures(self):
        'openGLFeatures(self) -> PySide2.QtGui.QOpenGLFunctions.OpenGLFeatures'
        return PySide2.QtGui.QOpenGLFunctions.OpenGLFeatures
    

class QOpenGLPixelTransferOptions(_mod_Shiboken.Object):
    'QOpenGLPixelTransferOptions(self)\nQOpenGLPixelTransferOptions(self, arg__1:PySide2.QtGui.QOpenGLPixelTransferOptions)'
    __class__ = QOpenGLPixelTransferOptions
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, arg__1: PySide2.QtGui.QOpenGLPixelTransferOptions):
        'QOpenGLPixelTransferOptions(self)\nQOpenGLPixelTransferOptions(self, arg__1:PySide2.QtGui.QOpenGLPixelTransferOptions)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def alignment(self):
        'alignment(self) -> int'
        return int
    
    def imageHeight(self):
        'imageHeight(self) -> int'
        return int
    
    def isLeastSignificantBitFirst(self):
        'isLeastSignificantBitFirst(self) -> bool'
        return bool
    
    def isSwapBytesEnabled(self):
        'isSwapBytesEnabled(self) -> bool'
        return bool
    
    def rowLength(self):
        'rowLength(self) -> int'
        return int
    
    def setAlignment(self, alignment):
        'setAlignment(self, alignment:int)'
        pass
    
    def setImageHeight(self, imageHeight):
        'setImageHeight(self, imageHeight:int)'
        pass
    
    def setLeastSignificantByteFirst(self, lsbFirst):
        'setLeastSignificantByteFirst(self, lsbFirst:bool)'
        pass
    
    def setRowLength(self, rowLength):
        'setRowLength(self, rowLength:int)'
        pass
    
    def setSkipImages(self, skipImages):
        'setSkipImages(self, skipImages:int)'
        pass
    
    def setSkipPixels(self, skipPixels):
        'setSkipPixels(self, skipPixels:int)'
        pass
    
    def setSkipRows(self, skipRows):
        'setSkipRows(self, skipRows:int)'
        pass
    
    def setSwapBytesEnabled(self, swapBytes):
        'setSwapBytesEnabled(self, swapBytes:bool)'
        pass
    
    def skipImages(self):
        'skipImages(self) -> int'
        return int
    
    def skipPixels(self):
        'skipPixels(self) -> int'
        return int
    
    def skipRows(self):
        'skipRows(self) -> int'
        return int
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QOpenGLPixelTransferOptions)'
        pass
    

class QOpenGLShader(_mod_PySide2_QtCore.QObject):
    'QOpenGLShader(self, type:PySide2.QtGui.QOpenGLShader.ShaderType, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    Compute = ShaderTypeBit()
    Fragment = ShaderTypeBit()
    Geometry = ShaderTypeBit()
    ShaderType = ShaderType
    ShaderTypeBit = ShaderTypeBit
    TessellationControl = ShaderTypeBit()
    TessellationEvaluation = ShaderTypeBit()
    Vertex = ShaderTypeBit()
    __class__ = QOpenGLShader
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QOpenGLShader(self, type:PySide2.QtGui.QOpenGLShader.ShaderType, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def compileSourceCode(self, source: PySide2.QtCore.QByteArray):
        'compileSourceCode(self, source:PySide2.QtCore.QByteArray) -> bool\ncompileSourceCode(self, source:str) -> bool\ncompileSourceCode(self, source:bytes) -> bool'
        return True
    
    def compileSourceFile(self, fileName):
        'compileSourceFile(self, fileName:str) -> bool'
        return bool
    
    @classmethod
    def hasOpenGLShaders(cls, type, context):
        'hasOpenGLShaders(type:PySide2.QtGui.QOpenGLShader.ShaderType, context:typing.Union[PySide2.QtGui.QOpenGLContext, NoneType]=None) -> bool'
        return bool
    
    def isCompiled(self):
        'isCompiled(self) -> bool'
        return bool
    
    def log(self):
        'log(self) -> str'
        return str
    
    def shaderId(self):
        'shaderId(self) -> int'
        return int
    
    def shaderType(self):
        'shaderType(self) -> PySide2.QtGui.QOpenGLShader.ShaderType'
        return PySide2.QtGui.QOpenGLShader.ShaderType
    
    def sourceCode(self):
        'sourceCode(self) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QOpenGLShaderProgram(_mod_PySide2_QtCore.QObject):
    'QOpenGLShaderProgram(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    __class__ = QOpenGLShaderProgram
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QOpenGLShaderProgram(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addCacheableShaderFromSourceCode(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, source: PySide2.QtCore.QByteArray):
        'addCacheableShaderFromSourceCode(self, type:PySide2.QtGui.QOpenGLShader.ShaderType, source:PySide2.QtCore.QByteArray) -> bool\naddCacheableShaderFromSourceCode(self, type:PySide2.QtGui.QOpenGLShader.ShaderType, source:str) -> bool\naddCacheableShaderFromSourceCode(self, type:PySide2.QtGui.QOpenGLShader.ShaderType, source:bytes) -> bool'
        return True
    
    def addCacheableShaderFromSourceFile(self, type, fileName):
        'addCacheableShaderFromSourceFile(self, type:PySide2.QtGui.QOpenGLShader.ShaderType, fileName:str) -> bool'
        return bool
    
    def addShader(self, shader):
        'addShader(self, shader:PySide2.QtGui.QOpenGLShader) -> bool'
        return bool
    
    def addShaderFromSourceCode(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, source: PySide2.QtCore.QByteArray):
        'addShaderFromSourceCode(self, type:PySide2.QtGui.QOpenGLShader.ShaderType, source:PySide2.QtCore.QByteArray) -> bool\naddShaderFromSourceCode(self, type:PySide2.QtGui.QOpenGLShader.ShaderType, source:str) -> bool\naddShaderFromSourceCode(self, type:PySide2.QtGui.QOpenGLShader.ShaderType, source:bytes) -> bool'
        return True
    
    def addShaderFromSourceFile(self, type, fileName):
        'addShaderFromSourceFile(self, type:PySide2.QtGui.QOpenGLShader.ShaderType, fileName:str) -> bool'
        return bool
    
    def attributeLocation(self, name: PySide2.QtCore.QByteArray):
        'attributeLocation(self, name:PySide2.QtCore.QByteArray) -> int\nattributeLocation(self, name:str) -> int\nattributeLocation(self, name:bytes) -> int'
        return 1
    
    def bind(self):
        'bind(self) -> bool'
        return bool
    
    def bindAttributeLocation(self, name: PySide2.QtCore.QByteArray, location: int):
        'bindAttributeLocation(self, name:PySide2.QtCore.QByteArray, location:int)\nbindAttributeLocation(self, name:str, location:int)\nbindAttributeLocation(self, name:bytes, location:int)'
        pass
    
    def create(self):
        'create(self) -> bool'
        return bool
    
    def defaultInnerTessellationLevels(self):
        'defaultInnerTessellationLevels(self) -> typing.List'
        return typing.List
    
    def defaultOuterTessellationLevels(self):
        'defaultOuterTessellationLevels(self) -> typing.List'
        return typing.List
    
    def disableAttributeArray(self, location: int):
        'disableAttributeArray(self, location:int)\ndisableAttributeArray(self, name:bytes)'
        pass
    
    def enableAttributeArray(self, location: int):
        'enableAttributeArray(self, location:int)\nenableAttributeArray(self, name:bytes)'
        pass
    
    @classmethod
    def hasOpenGLShaderPrograms(cls, context):
        'hasOpenGLShaderPrograms(context:typing.Union[PySide2.QtGui.QOpenGLContext, NoneType]=None) -> bool'
        return bool
    
    def isLinked(self):
        'isLinked(self) -> bool'
        return bool
    
    def link(self):
        'link(self) -> bool'
        return bool
    
    def log(self):
        'log(self) -> str'
        return str
    
    def maxGeometryOutputVertices(self):
        'maxGeometryOutputVertices(self) -> int'
        return int
    
    def patchVertexCount(self):
        'patchVertexCount(self) -> int'
        return int
    
    def programId(self):
        'programId(self) -> int'
        return int
    
    def release(self):
        'release(self)'
        pass
    
    def removeAllShaders(self):
        'removeAllShaders(self)'
        pass
    
    def removeShader(self, shader):
        'removeShader(self, shader:PySide2.QtGui.QOpenGLShader)'
        pass
    
    def setAttributeArray(self, location: int, values: typing.Sequence, tupleSize: int, stride: int=0):
        'setAttributeArray(self, location:int, type:int, values:int, tupleSize:int, stride:int=0)\nsetAttributeArray(self, location:int, values:typing.Sequence, tupleSize:int, stride:int=0)\nsetAttributeArray(self, name:bytes, type:int, values:int, tupleSize:int, stride:int=0)\nsetAttributeArray(self, name:bytes, values:typing.Sequence, tupleSize:int, stride:int=0)'
        pass
    
    def setAttributeBuffer(self, location: int, type: int, offset: int, tupleSize: int, stride: int=0):
        'setAttributeBuffer(self, location:int, type:int, offset:int, tupleSize:int, stride:int=0)\nsetAttributeBuffer(self, name:bytes, type:int, offset:int, tupleSize:int, stride:int=0)'
        pass
    
    def setAttributeValue(self, location: int, values: typing.Sequence, columns: int, rows: int):
        'setAttributeValue(self, location:int, value:PySide2.QtGui.QColor)\nsetAttributeValue(self, location:int, value:PySide2.QtGui.QVector2D)\nsetAttributeValue(self, location:int, value:PySide2.QtGui.QVector3D)\nsetAttributeValue(self, location:int, value:PySide2.QtGui.QVector4D)\nsetAttributeValue(self, location:int, value:float)\nsetAttributeValue(self, location:int, values:typing.Sequence, columns:int, rows:int)\nsetAttributeValue(self, location:int, x:float, y:float)\nsetAttributeValue(self, location:int, x:float, y:float, z:float)\nsetAttributeValue(self, location:int, x:float, y:float, z:float, w:float)\nsetAttributeValue(self, name:bytes, value:PySide2.QtGui.QColor)\nsetAttributeValue(self, name:bytes, value:PySide2.QtGui.QVector2D)\nsetAttributeValue(self, name:bytes, value:PySide2.QtGui.QVector3D)\nsetAttributeValue(self, name:bytes, value:PySide2.QtGui.QVector4D)\nsetAttributeValue(self, name:bytes, value:float)\nsetAttributeValue(self, name:bytes, values:typing.Sequence, columns:int, rows:int)\nsetAttributeValue(self, name:bytes, x:float, y:float)\nsetAttributeValue(self, name:bytes, x:float, y:float, z:float)\nsetAttributeValue(self, name:bytes, x:float, y:float, z:float, w:float)'
        pass
    
    def setDefaultInnerTessellationLevels(self, levels):
        'setDefaultInnerTessellationLevels(self, levels:typing.List)'
        pass
    
    def setDefaultOuterTessellationLevels(self, levels):
        'setDefaultOuterTessellationLevels(self, levels:typing.List)'
        pass
    
    def setPatchVertexCount(self, count):
        'setPatchVertexCount(self, count:int)'
        pass
    
    def setUniformValue(self, location: int, x: float, y: float, z: float, w: float):
        'setUniformValue(self, location:int, color:PySide2.QtGui.QColor)\nsetUniformValue(self, location:int, point:PySide2.QtCore.QPoint)\nsetUniformValue(self, location:int, point:PySide2.QtCore.QPointF)\nsetUniformValue(self, location:int, size:PySide2.QtCore.QSize)\nsetUniformValue(self, location:int, size:PySide2.QtCore.QSizeF)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QMatrix2x2)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QMatrix2x3)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QMatrix2x4)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QMatrix3x2)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QMatrix3x3)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QMatrix3x4)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QMatrix4x2)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QMatrix4x3)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QMatrix4x4)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QTransform)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QVector2D)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QVector3D)\nsetUniformValue(self, location:int, value:PySide2.QtGui.QVector4D)\nsetUniformValue(self, location:int, value:float)\nsetUniformValue(self, location:int, value:typing.Tuple)\nsetUniformValue(self, location:int, value:typing.Tuple)\nsetUniformValue(self, location:int, value:typing.Tuple)\nsetUniformValue(self, location:int, value:int)\nsetUniformValue(self, location:int, value:int)\nsetUniformValue(self, location:int, x:float, y:float)\nsetUniformValue(self, location:int, x:float, y:float, z:float)\nsetUniformValue(self, location:int, x:float, y:float, z:float, w:float)\nsetUniformValue(self, name:bytes, color:PySide2.QtGui.QColor)\nsetUniformValue(self, name:bytes, point:PySide2.QtCore.QPoint)\nsetUniformValue(self, name:bytes, point:PySide2.QtCore.QPointF)\nsetUniformValue(self, name:bytes, size:PySide2.QtCore.QSize)\nsetUniformValue(self, name:bytes, size:PySide2.QtCore.QSizeF)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QMatrix2x2)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QMatrix2x3)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QMatrix2x4)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QMatrix3x2)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QMatrix3x3)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QMatrix3x4)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QMatrix4x2)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QMatrix4x3)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QMatrix4x4)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QTransform)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QVector2D)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QVector3D)\nsetUniformValue(self, name:bytes, value:PySide2.QtGui.QVector4D)\nsetUniformValue(self, name:bytes, value:typing.Tuple)\nsetUniformValue(self, name:bytes, value:typing.Tuple)\nsetUniformValue(self, name:bytes, value:typing.Tuple)\nsetUniformValue(self, name:bytes, x:float, y:float)\nsetUniformValue(self, name:bytes, x:float, y:float, z:float)\nsetUniformValue(self, name:bytes, x:float, y:float, z:float, w:float)'
        pass
    
    def setUniformValue1f(self, arg__1: bytes, arg__2: float):
        'setUniformValue1f(self, arg__1:bytes, arg__2:float)\nsetUniformValue1f(self, arg__1:int, arg__2:float)'
        pass
    
    def setUniformValue1i(self, arg__1: bytes, arg__2: int):
        'setUniformValue1i(self, arg__1:bytes, arg__2:int)\nsetUniformValue1i(self, arg__1:int, arg__2:int)'
        pass
    
    def setUniformValueArray(self, location: int, values: typing.Sequence, count: int, tupleSize: int):
        'setUniformValueArray(self, location:int, values:typing.Sequence, count:int, tupleSize:int)\nsetUniformValueArray(self, location:int, values:typing.Sequence, count:int)\nsetUniformValueArray(self, location:int, values:typing.Sequence, count:int)\nsetUniformValueArray(self, name:bytes, values:typing.Sequence, count:int, tupleSize:int)\nsetUniformValueArray(self, name:bytes, values:typing.Sequence, count:int)\nsetUniformValueArray(self, name:bytes, values:typing.Sequence, count:int)'
        pass
    
    def shaders(self):
        'shaders(self) -> typing.List'
        return typing.List
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def uniformLocation(self, name: PySide2.QtCore.QByteArray):
        'uniformLocation(self, name:PySide2.QtCore.QByteArray) -> int\nuniformLocation(self, name:str) -> int\nuniformLocation(self, name:bytes) -> int'
        return 1
    

class QOpenGLTexture(_mod_Shiboken.Object):
    'QOpenGLTexture(self, image:PySide2.QtGui.QImage, genMipMaps:PySide2.QtGui.QOpenGLTexture.MipMapGeneration=PySide2.QtGui.QOpenGLTexture.MipMapGeneration.GenerateMipMaps)\nQOpenGLTexture(self, target:PySide2.QtGui.QOpenGLTexture.Target)'
    Alpha = PixelFormat()
    AlphaFormat = TextureFormat()
    AlphaValue = SwizzleValue()
    AnisotropicFiltering = Feature()
    BGR = PixelFormat()
    BGRA = PixelFormat()
    BGRA_Integer = PixelFormat()
    BGR_Integer = PixelFormat()
    BindingTarget = BindingTarget
    BindingTarget1D = BindingTarget()
    BindingTarget1DArray = BindingTarget()
    BindingTarget2D = BindingTarget()
    BindingTarget2DArray = BindingTarget()
    BindingTarget2DMultisample = BindingTarget()
    BindingTarget2DMultisampleArray = BindingTarget()
    BindingTarget3D = BindingTarget()
    BindingTargetBuffer = BindingTarget()
    BindingTargetCubeMap = BindingTarget()
    BindingTargetCubeMapArray = BindingTarget()
    BindingTargetRectangle = BindingTarget()
    BlueValue = SwizzleValue()
    ClampToBorder = WrapMode()
    ClampToEdge = WrapMode()
    CommpareNotEqual = ComparisonFunction()
    CompareAlways = ComparisonFunction()
    CompareEqual = ComparisonFunction()
    CompareGreater = ComparisonFunction()
    CompareGreaterEqual = ComparisonFunction()
    CompareLess = ComparisonFunction()
    CompareLessEqual = ComparisonFunction()
    CompareNever = ComparisonFunction()
    CompareNone = ComparisonMode()
    CompareRefToTexture = ComparisonMode()
    ComparisonFunction = ComparisonFunction
    ComparisonMode = ComparisonMode
    CoordinateDirection = CoordinateDirection
    CubeMapFace = CubeMapFace
    CubeMapNegativeX = CubeMapFace()
    CubeMapNegativeY = CubeMapFace()
    CubeMapNegativeZ = CubeMapFace()
    CubeMapPositiveX = CubeMapFace()
    CubeMapPositiveY = CubeMapFace()
    CubeMapPositiveZ = CubeMapFace()
    D16 = TextureFormat()
    D24 = TextureFormat()
    D24S8 = TextureFormat()
    D32 = TextureFormat()
    D32F = TextureFormat()
    D32FS8X24 = TextureFormat()
    Depth = PixelFormat()
    DepthFormat = TextureFormat()
    DepthMode = DepthStencilMode()
    DepthStencil = PixelFormat()
    DepthStencilMode = DepthStencilMode
    DirectionR = CoordinateDirection()
    DirectionS = CoordinateDirection()
    DirectionT = CoordinateDirection()
    DontGenerateMipMaps = MipMapGeneration()
    DontResetTextureUnit = TextureUnitReset()
    Feature = Feature
    Features = Features
    Filter = Filter
    Float16 = PixelType()
    Float16OES = PixelType()
    Float32 = PixelType()
    Float32_D32_UInt32_S8_X24 = PixelType()
    FormatClass_128Bit = TextureFormatClass()
    FormatClass_16Bit = TextureFormatClass()
    FormatClass_24Bit = TextureFormatClass()
    FormatClass_32Bit = TextureFormatClass()
    FormatClass_48Bit = TextureFormatClass()
    FormatClass_64Bit = TextureFormatClass()
    FormatClass_8Bit = TextureFormatClass()
    FormatClass_96Bit = TextureFormatClass()
    FormatClass_BPTC_Float = TextureFormatClass()
    FormatClass_BPTC_Unorm = TextureFormatClass()
    FormatClass_RGTC1_R = TextureFormatClass()
    FormatClass_RGTC2_RG = TextureFormatClass()
    FormatClass_S3TC_DXT1_RGB = TextureFormatClass()
    FormatClass_S3TC_DXT1_RGBA = TextureFormatClass()
    FormatClass_S3TC_DXT3_RGBA = TextureFormatClass()
    FormatClass_S3TC_DXT5_RGBA = TextureFormatClass()
    FormatClass_Unique = TextureFormatClass()
    GenerateMipMaps = MipMapGeneration()
    GreenValue = SwizzleValue()
    ImmutableMultisampleStorage = Feature()
    ImmutableStorage = Feature()
    Int16 = PixelType()
    Int32 = PixelType()
    Int8 = PixelType()
    Linear = Filter()
    LinearMipMapLinear = Filter()
    LinearMipMapNearest = Filter()
    Luminance = PixelFormat()
    LuminanceAlpha = PixelFormat()
    LuminanceAlphaFormat = TextureFormat()
    LuminanceFormat = TextureFormat()
    MaxFeatureFlag = Feature()
    MipMapGeneration = MipMapGeneration
    MirroredRepeat = WrapMode()
    NPOTTextureRepeat = Feature()
    NPOTTextures = Feature()
    Nearest = Filter()
    NearestMipMapLinear = Filter()
    NearestMipMapNearest = Filter()
    NoFormat = TextureFormat()
    NoFormatClass = TextureFormatClass()
    NoPixelType = PixelType()
    NoSourceFormat = PixelFormat()
    OneValue = SwizzleValue()
    PixelFormat = PixelFormat
    PixelType = PixelType
    R11_EAC_SNorm = TextureFormat()
    R11_EAC_UNorm = TextureFormat()
    R16F = TextureFormat()
    R16I = TextureFormat()
    R16U = TextureFormat()
    R16_SNorm = TextureFormat()
    R16_UNorm = TextureFormat()
    R32F = TextureFormat()
    R32I = TextureFormat()
    R32U = TextureFormat()
    R5G6B5 = TextureFormat()
    R8I = TextureFormat()
    R8U = TextureFormat()
    R8_SNorm = TextureFormat()
    R8_UNorm = TextureFormat()
    RG = PixelFormat()
    RG11B10F = TextureFormat()
    RG11_EAC_SNorm = TextureFormat()
    RG11_EAC_UNorm = TextureFormat()
    RG16F = TextureFormat()
    RG16I = TextureFormat()
    RG16U = TextureFormat()
    RG16_SNorm = TextureFormat()
    RG16_UNorm = TextureFormat()
    RG32F = TextureFormat()
    RG32I = TextureFormat()
    RG32U = TextureFormat()
    RG3B2 = TextureFormat()
    RG8I = TextureFormat()
    RG8U = TextureFormat()
    RG8_SNorm = TextureFormat()
    RG8_UNorm = TextureFormat()
    RGB = PixelFormat()
    RGB10A2 = TextureFormat()
    RGB16F = TextureFormat()
    RGB16I = TextureFormat()
    RGB16U = TextureFormat()
    RGB16_SNorm = TextureFormat()
    RGB16_UNorm = TextureFormat()
    RGB32F = TextureFormat()
    RGB32I = TextureFormat()
    RGB32U = TextureFormat()
    RGB5A1 = TextureFormat()
    RGB8I = TextureFormat()
    RGB8U = TextureFormat()
    RGB8_ETC1 = TextureFormat()
    RGB8_ETC2 = TextureFormat()
    RGB8_PunchThrough_Alpha1_ETC2 = TextureFormat()
    RGB8_SNorm = TextureFormat()
    RGB8_UNorm = TextureFormat()
    RGB9E5 = TextureFormat()
    RGBA = PixelFormat()
    RGBA16F = TextureFormat()
    RGBA16I = TextureFormat()
    RGBA16U = TextureFormat()
    RGBA16_SNorm = TextureFormat()
    RGBA16_UNorm = TextureFormat()
    RGBA32F = TextureFormat()
    RGBA32I = TextureFormat()
    RGBA32U = TextureFormat()
    RGBA4 = TextureFormat()
    RGBA8I = TextureFormat()
    RGBA8U = TextureFormat()
    RGBA8_ETC2_EAC = TextureFormat()
    RGBA8_SNorm = TextureFormat()
    RGBA8_UNorm = TextureFormat()
    RGBAFormat = TextureFormat()
    RGBA_ASTC_10x10 = TextureFormat()
    RGBA_ASTC_10x5 = TextureFormat()
    RGBA_ASTC_10x6 = TextureFormat()
    RGBA_ASTC_10x8 = TextureFormat()
    RGBA_ASTC_12x10 = TextureFormat()
    RGBA_ASTC_12x12 = TextureFormat()
    RGBA_ASTC_4x4 = TextureFormat()
    RGBA_ASTC_5x4 = TextureFormat()
    RGBA_ASTC_5x5 = TextureFormat()
    RGBA_ASTC_6x5 = TextureFormat()
    RGBA_ASTC_6x6 = TextureFormat()
    RGBA_ASTC_8x5 = TextureFormat()
    RGBA_ASTC_8x6 = TextureFormat()
    RGBA_ASTC_8x8 = TextureFormat()
    RGBA_DXT1 = TextureFormat()
    RGBA_DXT3 = TextureFormat()
    RGBA_DXT5 = TextureFormat()
    RGBA_Integer = PixelFormat()
    RGBFormat = TextureFormat()
    RGB_BP_SIGNED_FLOAT = TextureFormat()
    RGB_BP_UNSIGNED_FLOAT = TextureFormat()
    RGB_BP_UNorm = TextureFormat()
    RGB_DXT1 = TextureFormat()
    RGB_Integer = PixelFormat()
    RG_ATI2N_SNorm = TextureFormat()
    RG_ATI2N_UNorm = TextureFormat()
    RG_Integer = PixelFormat()
    R_ATI1N_SNorm = TextureFormat()
    R_ATI1N_UNorm = TextureFormat()
    Red = PixelFormat()
    RedValue = SwizzleValue()
    Red_Integer = PixelFormat()
    Repeat = WrapMode()
    ResetTextureUnit = TextureUnitReset()
    S8 = TextureFormat()
    SRGB8 = TextureFormat()
    SRGB8_Alpha8 = TextureFormat()
    SRGB8_Alpha8_ASTC_10x10 = TextureFormat()
    SRGB8_Alpha8_ASTC_10x5 = TextureFormat()
    SRGB8_Alpha8_ASTC_10x6 = TextureFormat()
    SRGB8_Alpha8_ASTC_10x8 = TextureFormat()
    SRGB8_Alpha8_ASTC_12x10 = TextureFormat()
    SRGB8_Alpha8_ASTC_12x12 = TextureFormat()
    SRGB8_Alpha8_ASTC_4x4 = TextureFormat()
    SRGB8_Alpha8_ASTC_5x4 = TextureFormat()
    SRGB8_Alpha8_ASTC_5x5 = TextureFormat()
    SRGB8_Alpha8_ASTC_6x5 = TextureFormat()
    SRGB8_Alpha8_ASTC_6x6 = TextureFormat()
    SRGB8_Alpha8_ASTC_8x5 = TextureFormat()
    SRGB8_Alpha8_ASTC_8x6 = TextureFormat()
    SRGB8_Alpha8_ASTC_8x8 = TextureFormat()
    SRGB8_Alpha8_ETC2_EAC = TextureFormat()
    SRGB8_ETC2 = TextureFormat()
    SRGB8_PunchThrough_Alpha1_ETC2 = TextureFormat()
    SRGB_Alpha_DXT1 = TextureFormat()
    SRGB_Alpha_DXT3 = TextureFormat()
    SRGB_Alpha_DXT5 = TextureFormat()
    SRGB_BP_UNorm = TextureFormat()
    SRGB_DXT1 = TextureFormat()
    Stencil = PixelFormat()
    StencilMode = DepthStencilMode()
    StencilTexturing = Feature()
    Swizzle = Feature()
    SwizzleAlpha = SwizzleComponent()
    SwizzleBlue = SwizzleComponent()
    SwizzleComponent = SwizzleComponent
    SwizzleGreen = SwizzleComponent()
    SwizzleRed = SwizzleComponent()
    SwizzleValue = SwizzleValue
    Target = Target
    Target1D = Target()
    Target1DArray = Target()
    Target2D = Target()
    Target2DArray = Target()
    Target2DMultisample = Target()
    Target2DMultisampleArray = Target()
    Target3D = Target()
    TargetBuffer = Target()
    TargetCubeMap = Target()
    TargetCubeMapArray = Target()
    TargetRectangle = Target()
    Texture1D = Feature()
    Texture3D = Feature()
    TextureArrays = Feature()
    TextureBuffer = Feature()
    TextureComparisonOperators = Feature()
    TextureCubeMapArrays = Feature()
    TextureFormat = TextureFormat
    TextureFormatClass = TextureFormatClass
    TextureMipMapLevel = Feature()
    TextureMultisample = Feature()
    TextureRectangle = Feature()
    TextureUnitReset = TextureUnitReset
    UInt16 = PixelType()
    UInt16_R5G6B5 = PixelType()
    UInt16_R5G6B5_Rev = PixelType()
    UInt16_RGB5A1 = PixelType()
    UInt16_RGB5A1_Rev = PixelType()
    UInt16_RGBA4 = PixelType()
    UInt16_RGBA4_Rev = PixelType()
    UInt32 = PixelType()
    UInt32_D24S8 = PixelType()
    UInt32_RG11B10F = PixelType()
    UInt32_RGB10A2 = PixelType()
    UInt32_RGB10A2_Rev = PixelType()
    UInt32_RGB9_E5 = PixelType()
    UInt32_RGBA8 = PixelType()
    UInt32_RGBA8_Rev = PixelType()
    UInt8 = PixelType()
    UInt8_RG3B2 = PixelType()
    UInt8_RG3B2_Rev = PixelType()
    WrapMode = WrapMode
    ZeroValue = SwizzleValue()
    __class__ = QOpenGLTexture
    __dict__ = {}
    def __init__(self, image: PySide2.QtGui.QImage, genMipMaps: PySide2.QtGui.QOpenGLTexture.MipMapGeneration=PySide2.QtGui.QOpenGLTexture.MipMapGeneration.GenerateMipMaps):
        'QOpenGLTexture(self, image:PySide2.QtGui.QImage, genMipMaps:PySide2.QtGui.QOpenGLTexture.MipMapGeneration=PySide2.QtGui.QOpenGLTexture.MipMapGeneration.GenerateMipMaps)\nQOpenGLTexture(self, target:PySide2.QtGui.QOpenGLTexture.Target)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def allocateStorage(self, pixelFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, pixelType: PySide2.QtGui.QOpenGLTexture.PixelType):
        'allocateStorage(self)\nallocateStorage(self, pixelFormat:PySide2.QtGui.QOpenGLTexture.PixelFormat, pixelType:PySide2.QtGui.QOpenGLTexture.PixelType)'
        pass
    
    def bind(self, unit: int, reset: PySide2.QtGui.QOpenGLTexture.TextureUnitReset=PySide2.QtGui.QOpenGLTexture.TextureUnitReset.DontResetTextureUnit):
        'bind(self)\nbind(self, unit:int, reset:PySide2.QtGui.QOpenGLTexture.TextureUnitReset=PySide2.QtGui.QOpenGLTexture.TextureUnitReset.DontResetTextureUnit)'
        pass
    
    def borderColor(self):
        'borderColor(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    @classmethod
    def boundTextureId(cls, unit: int, target: PySide2.QtGui.QOpenGLTexture.BindingTarget):
        'boundTextureId(target:PySide2.QtGui.QOpenGLTexture.BindingTarget) -> int\nboundTextureId(unit:int, target:PySide2.QtGui.QOpenGLTexture.BindingTarget) -> int'
        return 1
    
    def comparisonFunction(self):
        'comparisonFunction(self) -> PySide2.QtGui.QOpenGLTexture.ComparisonFunction'
        return PySide2.QtGui.QOpenGLTexture.ComparisonFunction
    
    def comparisonMode(self):
        'comparisonMode(self) -> PySide2.QtGui.QOpenGLTexture.ComparisonMode'
        return PySide2.QtGui.QOpenGLTexture.ComparisonMode
    
    def create(self):
        'create(self) -> bool'
        return bool
    
    def createTextureView(self, target, viewFormat, minimumMipmapLevel, maximumMipmapLevel, minimumLayer, maximumLayer):
        'createTextureView(self, target:PySide2.QtGui.QOpenGLTexture.Target, viewFormat:PySide2.QtGui.QOpenGLTexture.TextureFormat, minimumMipmapLevel:int, maximumMipmapLevel:int, minimumLayer:int, maximumLayer:int) -> PySide2.QtGui.QOpenGLTexture'
        return PySide2.QtGui.QOpenGLTexture
    
    def depth(self):
        'depth(self) -> int'
        return int
    
    def depthStencilMode(self):
        'depthStencilMode(self) -> PySide2.QtGui.QOpenGLTexture.DepthStencilMode'
        return PySide2.QtGui.QOpenGLTexture.DepthStencilMode
    
    def destroy(self):
        'destroy(self)'
        pass
    
    def faces(self):
        'faces(self) -> int'
        return int
    
    def format(self):
        'format(self) -> PySide2.QtGui.QOpenGLTexture.TextureFormat'
        return PySide2.QtGui.QOpenGLTexture.TextureFormat
    
    def generateMipMaps(self, baseLevel: int, resetBaseLevel: bool=True):
        'generateMipMaps(self)\ngenerateMipMaps(self, baseLevel:int, resetBaseLevel:bool=True)'
        pass
    
    @classmethod
    def hasFeature(cls, feature):
        'hasFeature(feature:PySide2.QtGui.QOpenGLTexture.Feature) -> bool'
        return bool
    
    def height(self):
        'height(self) -> int'
        return int
    
    def isAutoMipMapGenerationEnabled(self):
        'isAutoMipMapGenerationEnabled(self) -> bool'
        return bool
    
    def isBound(self, unit: int):
        'isBound(self) -> bool\nisBound(self, unit:int) -> bool'
        return True
    
    def isCreated(self):
        'isCreated(self) -> bool'
        return bool
    
    def isFixedSamplePositions(self):
        'isFixedSamplePositions(self) -> bool'
        return bool
    
    def isStorageAllocated(self):
        'isStorageAllocated(self) -> bool'
        return bool
    
    def isTextureView(self):
        'isTextureView(self) -> bool'
        return bool
    
    def layers(self):
        'layers(self) -> int'
        return int
    
    def levelOfDetailRange(self):
        'levelOfDetailRange(self) -> typing.Tuple'
        return typing.Tuple
    
    def levelofDetailBias(self):
        'levelofDetailBias(self) -> float'
        return float
    
    def magnificationFilter(self):
        'magnificationFilter(self) -> PySide2.QtGui.QOpenGLTexture.Filter'
        return PySide2.QtGui.QOpenGLTexture.Filter
    
    def maximumAnisotropy(self):
        'maximumAnisotropy(self) -> float'
        return float
    
    def maximumLevelOfDetail(self):
        'maximumLevelOfDetail(self) -> float'
        return float
    
    def maximumMipLevels(self):
        'maximumMipLevels(self) -> int'
        return int
    
    def minMagFilters(self):
        'minMagFilters(self) -> typing.Tuple'
        return typing.Tuple
    
    def minificationFilter(self):
        'minificationFilter(self) -> PySide2.QtGui.QOpenGLTexture.Filter'
        return PySide2.QtGui.QOpenGLTexture.Filter
    
    def minimumLevelOfDetail(self):
        'minimumLevelOfDetail(self) -> float'
        return float
    
    def mipBaseLevel(self):
        'mipBaseLevel(self) -> int'
        return int
    
    def mipLevelRange(self):
        'mipLevelRange(self) -> typing.Tuple'
        return typing.Tuple
    
    def mipLevels(self):
        'mipLevels(self) -> int'
        return int
    
    def mipMaxLevel(self):
        'mipMaxLevel(self) -> int'
        return int
    
    def release(self, unit: int, reset: PySide2.QtGui.QOpenGLTexture.TextureUnitReset=PySide2.QtGui.QOpenGLTexture.TextureUnitReset.DontResetTextureUnit):
        'release(self)\nrelease(self, unit:int, reset:PySide2.QtGui.QOpenGLTexture.TextureUnitReset=PySide2.QtGui.QOpenGLTexture.TextureUnitReset.DontResetTextureUnit)'
        pass
    
    def samples(self):
        'samples(self) -> int'
        return int
    
    def setAutoMipMapGenerationEnabled(self, enabled):
        'setAutoMipMapGenerationEnabled(self, enabled:bool)'
        pass
    
    def setBorderColor(self, r: float, g: float, b: float, a: float):
        'setBorderColor(self, color:PySide2.QtGui.QColor)\nsetBorderColor(self, r:float, g:float, b:float, a:float)\nsetBorderColor(self, r:int, g:int, b:int, a:int)\nsetBorderColor(self, r:int, g:int, b:int, a:int)'
        pass
    
    def setComparisonFunction(self, function):
        'setComparisonFunction(self, function:PySide2.QtGui.QOpenGLTexture.ComparisonFunction)'
        pass
    
    def setComparisonMode(self, mode):
        'setComparisonMode(self, mode:PySide2.QtGui.QOpenGLTexture.ComparisonMode)'
        pass
    
    def setCompressedData(self, mipLevel: int, layer: int, layerCount: int, cubeFace: PySide2.QtGui.QOpenGLTexture.CubeMapFace, dataSize: int, data: int, options: typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions,NoneType]=None):
        'setCompressedData(self, dataSize:int, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetCompressedData(self, mipLevel:int, dataSize:int, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetCompressedData(self, mipLevel:int, layer:int, cubeFace:PySide2.QtGui.QOpenGLTexture.CubeMapFace, dataSize:int, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetCompressedData(self, mipLevel:int, layer:int, dataSize:int, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetCompressedData(self, mipLevel:int, layer:int, layerCount:int, cubeFace:PySide2.QtGui.QOpenGLTexture.CubeMapFace, dataSize:int, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)'
        pass
    
    def setData(self, xOffset: int, yOffset: int, zOffset: int, width: int, height: int, depth: int, mipLevel: int, layer: int, cubeFace: PySide2.QtGui.QOpenGLTexture.CubeMapFace, layerCount: int, sourceFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType: PySide2.QtGui.QOpenGLTexture.PixelType, data: int, options: typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions,NoneType]=None):
        'setData(self, image:PySide2.QtGui.QImage, genMipMaps:PySide2.QtGui.QOpenGLTexture.MipMapGeneration=PySide2.QtGui.QOpenGLTexture.MipMapGeneration.GenerateMipMaps)\nsetData(self, mipLevel:int, layer:int, cubeFace:PySide2.QtGui.QOpenGLTexture.CubeMapFace, sourceFormat:PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType:PySide2.QtGui.QOpenGLTexture.PixelType, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetData(self, mipLevel:int, layer:int, layerCount:int, cubeFace:PySide2.QtGui.QOpenGLTexture.CubeMapFace, sourceFormat:PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType:PySide2.QtGui.QOpenGLTexture.PixelType, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetData(self, mipLevel:int, layer:int, sourceFormat:PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType:PySide2.QtGui.QOpenGLTexture.PixelType, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetData(self, mipLevel:int, sourceFormat:PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType:PySide2.QtGui.QOpenGLTexture.PixelType, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetData(self, sourceFormat:PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType:PySide2.QtGui.QOpenGLTexture.PixelType, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetData(self, xOffset:int, yOffset:int, zOffset:int, width:int, height:int, depth:int, mipLevel:int, layer:int, cubeFace:PySide2.QtGui.QOpenGLTexture.CubeMapFace, layerCount:int, sourceFormat:PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType:PySide2.QtGui.QOpenGLTexture.PixelType, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetData(self, xOffset:int, yOffset:int, zOffset:int, width:int, height:int, depth:int, mipLevel:int, layer:int, cubeFace:PySide2.QtGui.QOpenGLTexture.CubeMapFace, sourceFormat:PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType:PySide2.QtGui.QOpenGLTexture.PixelType, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetData(self, xOffset:int, yOffset:int, zOffset:int, width:int, height:int, depth:int, mipLevel:int, layer:int, sourceFormat:PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType:PySide2.QtGui.QOpenGLTexture.PixelType, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)\nsetData(self, xOffset:int, yOffset:int, zOffset:int, width:int, height:int, depth:int, sourceFormat:PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType:PySide2.QtGui.QOpenGLTexture.PixelType, data:int, options:typing.Union[PySide2.QtGui.QOpenGLPixelTransferOptions, NoneType]=None)'
        pass
    
    def setDepthStencilMode(self, mode):
        'setDepthStencilMode(self, mode:PySide2.QtGui.QOpenGLTexture.DepthStencilMode)'
        pass
    
    def setFixedSamplePositions(self, fixed):
        'setFixedSamplePositions(self, fixed:bool)'
        pass
    
    def setFormat(self, format):
        'setFormat(self, format:PySide2.QtGui.QOpenGLTexture.TextureFormat)'
        pass
    
    def setLayers(self, layers):
        'setLayers(self, layers:int)'
        pass
    
    def setLevelOfDetailRange(self, min, max):
        'setLevelOfDetailRange(self, min:float, max:float)'
        pass
    
    def setLevelofDetailBias(self, bias):
        'setLevelofDetailBias(self, bias:float)'
        pass
    
    def setMagnificationFilter(self, filter):
        'setMagnificationFilter(self, filter:PySide2.QtGui.QOpenGLTexture.Filter)'
        pass
    
    def setMaximumAnisotropy(self, anisotropy):
        'setMaximumAnisotropy(self, anisotropy:float)'
        pass
    
    def setMaximumLevelOfDetail(self, value):
        'setMaximumLevelOfDetail(self, value:float)'
        pass
    
    def setMinMagFilters(self, minificationFilter, magnificationFilter):
        'setMinMagFilters(self, minificationFilter:PySide2.QtGui.QOpenGLTexture.Filter, magnificationFilter:PySide2.QtGui.QOpenGLTexture.Filter)'
        pass
    
    def setMinificationFilter(self, filter):
        'setMinificationFilter(self, filter:PySide2.QtGui.QOpenGLTexture.Filter)'
        pass
    
    def setMinimumLevelOfDetail(self, value):
        'setMinimumLevelOfDetail(self, value:float)'
        pass
    
    def setMipBaseLevel(self, baseLevel):
        'setMipBaseLevel(self, baseLevel:int)'
        pass
    
    def setMipLevelRange(self, baseLevel, maxLevel):
        'setMipLevelRange(self, baseLevel:int, maxLevel:int)'
        pass
    
    def setMipLevels(self, levels):
        'setMipLevels(self, levels:int)'
        pass
    
    def setMipMaxLevel(self, maxLevel):
        'setMipMaxLevel(self, maxLevel:int)'
        pass
    
    def setSamples(self, samples):
        'setSamples(self, samples:int)'
        pass
    
    def setSize(self, width, height, depth):
        'setSize(self, width:int, height:int=1, depth:int=1)'
        pass
    
    def setSwizzleMask(self, r: PySide2.QtGui.QOpenGLTexture.SwizzleValue, g: PySide2.QtGui.QOpenGLTexture.SwizzleValue, b: PySide2.QtGui.QOpenGLTexture.SwizzleValue, a: PySide2.QtGui.QOpenGLTexture.SwizzleValue):
        'setSwizzleMask(self, component:PySide2.QtGui.QOpenGLTexture.SwizzleComponent, value:PySide2.QtGui.QOpenGLTexture.SwizzleValue)\nsetSwizzleMask(self, r:PySide2.QtGui.QOpenGLTexture.SwizzleValue, g:PySide2.QtGui.QOpenGLTexture.SwizzleValue, b:PySide2.QtGui.QOpenGLTexture.SwizzleValue, a:PySide2.QtGui.QOpenGLTexture.SwizzleValue)'
        pass
    
    def setWrapMode(self, direction: PySide2.QtGui.QOpenGLTexture.CoordinateDirection, mode: PySide2.QtGui.QOpenGLTexture.WrapMode):
        'setWrapMode(self, direction:PySide2.QtGui.QOpenGLTexture.CoordinateDirection, mode:PySide2.QtGui.QOpenGLTexture.WrapMode)\nsetWrapMode(self, mode:PySide2.QtGui.QOpenGLTexture.WrapMode)'
        pass
    
    def swizzleMask(self, component):
        'swizzleMask(self, component:PySide2.QtGui.QOpenGLTexture.SwizzleComponent) -> PySide2.QtGui.QOpenGLTexture.SwizzleValue'
        return PySide2.QtGui.QOpenGLTexture.SwizzleValue
    
    def target(self):
        'target(self) -> PySide2.QtGui.QOpenGLTexture.Target'
        return PySide2.QtGui.QOpenGLTexture.Target
    
    def textureId(self):
        'textureId(self) -> int'
        return int
    
    def width(self):
        'width(self) -> int'
        return int
    
    def wrapMode(self, direction):
        'wrapMode(self, direction:PySide2.QtGui.QOpenGLTexture.CoordinateDirection) -> PySide2.QtGui.QOpenGLTexture.WrapMode'
        return PySide2.QtGui.QOpenGLTexture.WrapMode
    

class QOpenGLTextureBlitter(_mod_Shiboken.Object):
    'QOpenGLTextureBlitter(self)'
    Origin = Origin
    OriginBottomLeft = Origin()
    OriginTopLeft = Origin()
    __class__ = QOpenGLTextureBlitter
    __dict__ = {}
    def __init__(self):
        'QOpenGLTextureBlitter(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bind(self, target):
        'bind(self, target:int=3553)'
        pass
    
    def blit(self, texture: int, targetTransform: PySide2.QtGui.QMatrix4x4, sourceOrigin: PySide2.QtGui.QOpenGLTextureBlitter.Origin):
        'blit(self, texture:int, targetTransform:PySide2.QtGui.QMatrix4x4, sourceOrigin:PySide2.QtGui.QOpenGLTextureBlitter.Origin)\nblit(self, texture:int, targetTransform:PySide2.QtGui.QMatrix4x4, sourceTransform:PySide2.QtGui.QMatrix3x3)'
        pass
    
    def create(self):
        'create(self) -> bool'
        return bool
    
    def destroy(self):
        'destroy(self)'
        pass
    
    def isCreated(self):
        'isCreated(self) -> bool'
        return bool
    
    def release(self):
        'release(self)'
        pass
    
    def setOpacity(self, opacity):
        'setOpacity(self, opacity:float)'
        pass
    
    def setRedBlueSwizzle(self, swizzle):
        'setRedBlueSwizzle(self, swizzle:bool)'
        pass
    
    @classmethod
    def sourceTransform(cls, subTexture, textureSize, origin):
        'sourceTransform(subTexture:PySide2.QtCore.QRectF, textureSize:PySide2.QtCore.QSize, origin:PySide2.QtGui.QOpenGLTextureBlitter.Origin) -> PySide2.QtGui.QMatrix3x3'
        return PySide2.QtGui.QMatrix3x3
    
    def supportsExternalOESTarget(self):
        'supportsExternalOESTarget(self) -> bool'
        return bool
    
    @classmethod
    def targetTransform(cls, target, viewport):
        'targetTransform(target:PySide2.QtCore.QRectF, viewport:PySide2.QtCore.QRect) -> PySide2.QtGui.QMatrix4x4'
        return PySide2.QtGui.QMatrix4x4
    

class QOpenGLTimeMonitor(_mod_PySide2_QtCore.QObject):
    'QOpenGLTimeMonitor(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    __class__ = QOpenGLTimeMonitor
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QOpenGLTimeMonitor(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def create(self):
        'create(self) -> bool'
        return bool
    
    def destroy(self):
        'destroy(self)'
        pass
    
    def isCreated(self):
        'isCreated(self) -> bool'
        return bool
    
    def isResultAvailable(self):
        'isResultAvailable(self) -> bool'
        return bool
    
    def objectIds(self):
        'objectIds(self) -> typing.List'
        return typing.List
    
    def recordSample(self):
        'recordSample(self) -> int'
        return int
    
    def reset(self):
        'reset(self)'
        pass
    
    def sampleCount(self):
        'sampleCount(self) -> int'
        return int
    
    def setSampleCount(self, sampleCount):
        'setSampleCount(self, sampleCount:int)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def waitForIntervals(self):
        'waitForIntervals(self) -> typing.List'
        return typing.List
    
    def waitForSamples(self):
        'waitForSamples(self) -> typing.List'
        return typing.List
    

class QOpenGLTimerQuery(_mod_PySide2_QtCore.QObject):
    'QOpenGLTimerQuery(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    __class__ = QOpenGLTimerQuery
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QOpenGLTimerQuery(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def begin(self):
        'begin(self)'
        pass
    
    def create(self):
        'create(self) -> bool'
        return bool
    
    def destroy(self):
        'destroy(self)'
        pass
    
    def end(self):
        'end(self)'
        pass
    
    def isCreated(self):
        'isCreated(self) -> bool'
        return bool
    
    def isResultAvailable(self):
        'isResultAvailable(self) -> bool'
        return bool
    
    def objectId(self):
        'objectId(self) -> int'
        return int
    
    def recordTimestamp(self):
        'recordTimestamp(self)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def waitForResult(self):
        'waitForResult(self) -> int'
        return int
    
    def waitForTimestamp(self):
        'waitForTimestamp(self) -> int'
        return int
    

class QOpenGLVersionProfile(_mod_Shiboken.Object):
    'QOpenGLVersionProfile(self)\nQOpenGLVersionProfile(self, format:PySide2.QtGui.QSurfaceFormat)\nQOpenGLVersionProfile(self, other:PySide2.QtGui.QOpenGLVersionProfile)'
    __class__ = QOpenGLVersionProfile
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, other: PySide2.QtGui.QOpenGLVersionProfile):
        'QOpenGLVersionProfile(self)\nQOpenGLVersionProfile(self, format:PySide2.QtGui.QSurfaceFormat)\nQOpenGLVersionProfile(self, other:PySide2.QtGui.QOpenGLVersionProfile)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def hasProfiles(self):
        'hasProfiles(self) -> bool'
        return bool
    
    def isLegacyVersion(self):
        'isLegacyVersion(self) -> bool'
        return bool
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def profile(self):
        'profile(self) -> PySide2.QtGui.QSurfaceFormat.OpenGLContextProfile'
        return PySide2.QtGui.QSurfaceFormat.OpenGLContextProfile
    
    def setProfile(self, profile):
        'setProfile(self, profile:PySide2.QtGui.QSurfaceFormat.OpenGLContextProfile)'
        pass
    
    def setVersion(self, majorVersion, minorVersion):
        'setVersion(self, majorVersion:int, minorVersion:int)'
        pass
    
    def version(self):
        'version(self) -> typing.Tuple'
        return typing.Tuple
    

class QOpenGLVertexArrayObject(_mod_PySide2_QtCore.QObject):
    'QOpenGLVertexArrayObject(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    Binder = Binder
    __class__ = QOpenGLVertexArrayObject
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QOpenGLVertexArrayObject(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bind(self):
        'bind(self)'
        pass
    
    def create(self):
        'create(self) -> bool'
        return bool
    
    def destroy(self):
        'destroy(self)'
        pass
    
    def isCreated(self):
        'isCreated(self) -> bool'
        return bool
    
    def objectId(self):
        'objectId(self) -> int'
        return int
    
    def release(self):
        'release(self)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QOpenGLWindow(QPaintDeviceWindow):
    'QOpenGLWindow(self, shareContext:PySide2.QtGui.QOpenGLContext, updateBehavior:PySide2.QtGui.QOpenGLWindow.UpdateBehavior=PySide2.QtGui.QOpenGLWindow.UpdateBehavior.NoPartialUpdate, parent:typing.Union[PySide2.QtGui.QWindow, NoneType]=None)\nQOpenGLWindow(self, updateBehavior:PySide2.QtGui.QOpenGLWindow.UpdateBehavior=PySide2.QtGui.QOpenGLWindow.UpdateBehavior.NoPartialUpdate, parent:typing.Union[PySide2.QtGui.QWindow, NoneType]=None)'
    NoPartialUpdate = UpdateBehavior()
    PartialUpdateBlend = UpdateBehavior()
    PartialUpdateBlit = UpdateBehavior()
    UpdateBehavior = UpdateBehavior
    __class__ = QOpenGLWindow
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, shareContext: PySide2.QtGui.QOpenGLContext, updateBehavior: PySide2.QtGui.QOpenGLWindow.UpdateBehavior=PySide2.QtGui.QOpenGLWindow.UpdateBehavior.NoPartialUpdate, parent: typing.Union[PySide2.QtGui.QWindow,NoneType]=None):
        'QOpenGLWindow(self, shareContext:PySide2.QtGui.QOpenGLContext, updateBehavior:PySide2.QtGui.QOpenGLWindow.UpdateBehavior=PySide2.QtGui.QOpenGLWindow.UpdateBehavior.NoPartialUpdate, parent:typing.Union[PySide2.QtGui.QWindow, NoneType]=None)\nQOpenGLWindow(self, updateBehavior:PySide2.QtGui.QOpenGLWindow.UpdateBehavior=PySide2.QtGui.QOpenGLWindow.UpdateBehavior.NoPartialUpdate, parent:typing.Union[PySide2.QtGui.QWindow, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def context(self):
        'context(self) -> PySide2.QtGui.QOpenGLContext'
        return PySide2.QtGui.QOpenGLContext
    
    def defaultFramebufferObject(self):
        'defaultFramebufferObject(self) -> int'
        return int
    
    def doneCurrent(self):
        'doneCurrent(self)'
        pass
    
    def frameSwapped(self):
        pass
    
    def grabFramebuffer(self):
        'grabFramebuffer(self) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def initializeGL(self):
        'initializeGL(self)'
        pass
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def makeCurrent(self):
        'makeCurrent(self)'
        pass
    
    def metric(self, metric):
        'metric(self, metric:PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int'
        return int
    
    def paintEvent(self, event):
        'paintEvent(self, event:PySide2.QtGui.QPaintEvent)'
        pass
    
    def paintGL(self):
        'paintGL(self)'
        pass
    
    def paintOverGL(self):
        'paintOverGL(self)'
        pass
    
    def paintUnderGL(self):
        'paintUnderGL(self)'
        pass
    
    def redirected(self, arg__1):
        'redirected(self, arg__1:PySide2.QtCore.QPoint) -> PySide2.QtGui.QPaintDevice'
        return PySide2.QtGui.QPaintDevice
    
    def resizeEvent(self, event):
        'resizeEvent(self, event:PySide2.QtGui.QResizeEvent)'
        pass
    
    def resizeGL(self, w, h):
        'resizeGL(self, w:int, h:int)'
        pass
    
    def shareContext(self):
        'shareContext(self) -> PySide2.QtGui.QOpenGLContext'
        return PySide2.QtGui.QOpenGLContext
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def updateBehavior(self):
        'updateBehavior(self) -> PySide2.QtGui.QOpenGLWindow.UpdateBehavior'
        return PySide2.QtGui.QOpenGLWindow.UpdateBehavior
    

class QPageLayout(_mod_Shiboken.Object):
    'QPageLayout(self)\nQPageLayout(self, other:PySide2.QtGui.QPageLayout)\nQPageLayout(self, pageSize:PySide2.QtGui.QPageSize, orientation:PySide2.QtGui.QPageLayout.Orientation, margins:PySide2.QtCore.QMarginsF, units:PySide2.QtGui.QPageLayout.Unit=typing.Tuple[float, float], minMargins:PySide2.QtCore.QMarginsF=Instance(QMarginsF(0, 0, 0, 0)))'
    Cicero = Unit()
    Didot = Unit()
    FullPageMode = Mode()
    Inch = Unit()
    Landscape = Orientation()
    Millimeter = Unit()
    Mode = Mode
    Orientation = Orientation
    Pica = Unit()
    Point = Unit()
    Portrait = Orientation()
    StandardMode = Mode()
    Unit = Unit
    __class__ = QPageLayout
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, pageSize: PySide2.QtGui.QPageSize, orientation: PySide2.QtGui.QPageLayout.Orientation, margins: PySide2.QtCore.QMarginsF, units: PySide2.QtGui.QPageLayout.Unit=typing.Tuple[float,float], minMargins: PySide2.QtCore.QMarginsF=Instance(QMarginsF(0,0,0,0))):
        'QPageLayout(self)\nQPageLayout(self, other:PySide2.QtGui.QPageLayout)\nQPageLayout(self, pageSize:PySide2.QtGui.QPageSize, orientation:PySide2.QtGui.QPageLayout.Orientation, margins:PySide2.QtCore.QMarginsF, units:PySide2.QtGui.QPageLayout.Unit=typing.Tuple[float, float], minMargins:PySide2.QtCore.QMarginsF=Instance(QMarginsF(0, 0, 0, 0)))'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def fullRect(self, units: PySide2.QtGui.QPageLayout.Unit):
        'fullRect(self) -> PySide2.QtCore.QRectF\nfullRect(self, units:PySide2.QtGui.QPageLayout.Unit) -> PySide2.QtCore.QRectF'
        pass
    
    def fullRectPixels(self, resolution):
        'fullRectPixels(self, resolution:int) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def fullRectPoints(self):
        'fullRectPoints(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def isEquivalentTo(self, other):
        'isEquivalentTo(self, other:PySide2.QtGui.QPageLayout) -> bool'
        return bool
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def margins(self, units: PySide2.QtGui.QPageLayout.Unit):
        'margins(self) -> PySide2.QtCore.QMarginsF\nmargins(self, units:PySide2.QtGui.QPageLayout.Unit) -> PySide2.QtCore.QMarginsF'
        pass
    
    def marginsPixels(self, resolution):
        'marginsPixels(self, resolution:int) -> PySide2.QtCore.QMargins'
        return PySide2.QtCore.QMargins
    
    def marginsPoints(self):
        'marginsPoints(self) -> PySide2.QtCore.QMargins'
        return PySide2.QtCore.QMargins
    
    def maximumMargins(self):
        'maximumMargins(self) -> PySide2.QtCore.QMarginsF'
        return PySide2.QtCore.QMarginsF
    
    def minimumMargins(self):
        'minimumMargins(self) -> PySide2.QtCore.QMarginsF'
        return PySide2.QtCore.QMarginsF
    
    def mode(self):
        'mode(self) -> PySide2.QtGui.QPageLayout.Mode'
        return PySide2.QtGui.QPageLayout.Mode
    
    def orientation(self):
        'orientation(self) -> PySide2.QtGui.QPageLayout.Orientation'
        return PySide2.QtGui.QPageLayout.Orientation
    
    def pageSize(self):
        'pageSize(self) -> PySide2.QtGui.QPageSize'
        return PySide2.QtGui.QPageSize
    
    def paintRect(self, units: PySide2.QtGui.QPageLayout.Unit):
        'paintRect(self) -> PySide2.QtCore.QRectF\npaintRect(self, units:PySide2.QtGui.QPageLayout.Unit) -> PySide2.QtCore.QRectF'
        pass
    
    def paintRectPixels(self, resolution):
        'paintRectPixels(self, resolution:int) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def paintRectPoints(self):
        'paintRectPoints(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def setBottomMargin(self, bottomMargin):
        'setBottomMargin(self, bottomMargin:float) -> bool'
        return bool
    
    def setLeftMargin(self, leftMargin):
        'setLeftMargin(self, leftMargin:float) -> bool'
        return bool
    
    def setMargins(self, margins):
        'setMargins(self, margins:PySide2.QtCore.QMarginsF) -> bool'
        return bool
    
    def setMinimumMargins(self, minMargins):
        'setMinimumMargins(self, minMargins:PySide2.QtCore.QMarginsF)'
        pass
    
    def setMode(self, mode):
        'setMode(self, mode:PySide2.QtGui.QPageLayout.Mode)'
        pass
    
    def setOrientation(self, orientation):
        'setOrientation(self, orientation:PySide2.QtGui.QPageLayout.Orientation)'
        pass
    
    def setPageSize(self, pageSize, minMargins):
        'setPageSize(self, pageSize:PySide2.QtGui.QPageSize, minMargins:PySide2.QtCore.QMarginsF=Instance(QMarginsF(0, 0, 0, 0)))'
        pass
    
    def setRightMargin(self, rightMargin):
        'setRightMargin(self, rightMargin:float) -> bool'
        return bool
    
    def setTopMargin(self, topMargin):
        'setTopMargin(self, topMargin:float) -> bool'
        return bool
    
    def setUnits(self, units):
        'setUnits(self, units:PySide2.QtGui.QPageLayout.Unit)'
        pass
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QPageLayout)'
        pass
    
    def units(self):
        'units(self) -> PySide2.QtGui.QPageLayout.Unit'
        return PySide2.QtGui.QPageLayout.Unit
    

class QPageSize(_mod_Shiboken.Object):
    "QPageSize(self)\nQPageSize(self, other:PySide2.QtGui.QPageSize)\nQPageSize(self, pageSizeId:PySide2.QtGui.QPageSize.PageSizeId)\nQPageSize(self, pointSize:PySide2.QtCore.QSize, name:str='', matchPolicy:PySide2.QtGui.QPageSize.SizeMatchPolicy=PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch)\nQPageSize(self, size:PySide2.QtCore.QSizeF, units:PySide2.QtGui.QPageSize.Unit, name:str='', matchPolicy:PySide2.QtGui.QPageSize.SizeMatchPolicy=PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch)"
    A0 = PageSizeId()
    A1 = PageSizeId()
    A10 = PageSizeId()
    A2 = PageSizeId()
    A3 = PageSizeId()
    A3Extra = PageSizeId()
    A4 = PageSizeId()
    A4Extra = PageSizeId()
    A4Plus = PageSizeId()
    A4Small = PageSizeId()
    A5 = PageSizeId()
    A5Extra = PageSizeId()
    A6 = PageSizeId()
    A7 = PageSizeId()
    A8 = PageSizeId()
    A9 = PageSizeId()
    AnsiA = PageSizeId()
    AnsiB = PageSizeId()
    AnsiC = PageSizeId()
    AnsiD = PageSizeId()
    AnsiE = PageSizeId()
    ArchA = PageSizeId()
    ArchB = PageSizeId()
    ArchC = PageSizeId()
    ArchD = PageSizeId()
    ArchE = PageSizeId()
    B0 = PageSizeId()
    B1 = PageSizeId()
    B10 = PageSizeId()
    B2 = PageSizeId()
    B3 = PageSizeId()
    B4 = PageSizeId()
    B5 = PageSizeId()
    B5Extra = PageSizeId()
    B6 = PageSizeId()
    B7 = PageSizeId()
    B8 = PageSizeId()
    B9 = PageSizeId()
    C5E = PageSizeId()
    Cicero = Unit()
    Comm10E = PageSizeId()
    Custom = PageSizeId()
    DLE = PageSizeId()
    Didot = Unit()
    DoublePostcard = PageSizeId()
    Envelope10 = PageSizeId()
    Envelope11 = PageSizeId()
    Envelope12 = PageSizeId()
    Envelope14 = PageSizeId()
    Envelope9 = PageSizeId()
    EnvelopeB4 = PageSizeId()
    EnvelopeB5 = PageSizeId()
    EnvelopeB6 = PageSizeId()
    EnvelopeC0 = PageSizeId()
    EnvelopeC1 = PageSizeId()
    EnvelopeC2 = PageSizeId()
    EnvelopeC3 = PageSizeId()
    EnvelopeC4 = PageSizeId()
    EnvelopeC5 = PageSizeId()
    EnvelopeC6 = PageSizeId()
    EnvelopeC65 = PageSizeId()
    EnvelopeC7 = PageSizeId()
    EnvelopeChou3 = PageSizeId()
    EnvelopeChou4 = PageSizeId()
    EnvelopeDL = PageSizeId()
    EnvelopeInvite = PageSizeId()
    EnvelopeItalian = PageSizeId()
    EnvelopeKaku2 = PageSizeId()
    EnvelopeKaku3 = PageSizeId()
    EnvelopeMonarch = PageSizeId()
    EnvelopePersonal = PageSizeId()
    EnvelopePrc1 = PageSizeId()
    EnvelopePrc10 = PageSizeId()
    EnvelopePrc2 = PageSizeId()
    EnvelopePrc3 = PageSizeId()
    EnvelopePrc4 = PageSizeId()
    EnvelopePrc5 = PageSizeId()
    EnvelopePrc6 = PageSizeId()
    EnvelopePrc7 = PageSizeId()
    EnvelopePrc8 = PageSizeId()
    EnvelopePrc9 = PageSizeId()
    EnvelopeYou4 = PageSizeId()
    ExactMatch = SizeMatchPolicy()
    Executive = PageSizeId()
    ExecutiveStandard = PageSizeId()
    FanFoldGerman = PageSizeId()
    FanFoldGermanLegal = PageSizeId()
    FanFoldUS = PageSizeId()
    Folio = PageSizeId()
    FuzzyMatch = SizeMatchPolicy()
    FuzzyOrientationMatch = SizeMatchPolicy()
    Imperial10x11 = PageSizeId()
    Imperial10x13 = PageSizeId()
    Imperial10x14 = PageSizeId()
    Imperial12x11 = PageSizeId()
    Imperial15x11 = PageSizeId()
    Imperial7x9 = PageSizeId()
    Imperial8x10 = PageSizeId()
    Imperial9x11 = PageSizeId()
    Imperial9x12 = PageSizeId()
    Inch = Unit()
    JisB0 = PageSizeId()
    JisB1 = PageSizeId()
    JisB10 = PageSizeId()
    JisB2 = PageSizeId()
    JisB3 = PageSizeId()
    JisB4 = PageSizeId()
    JisB5 = PageSizeId()
    JisB6 = PageSizeId()
    JisB7 = PageSizeId()
    JisB8 = PageSizeId()
    JisB9 = PageSizeId()
    LastPageSize = PageSizeId()
    Ledger = PageSizeId()
    Legal = PageSizeId()
    LegalExtra = PageSizeId()
    Letter = PageSizeId()
    LetterExtra = PageSizeId()
    LetterPlus = PageSizeId()
    LetterSmall = PageSizeId()
    Millimeter = Unit()
    NPageSize = PageSizeId()
    NPaperSize = PageSizeId()
    Note = PageSizeId()
    PageSizeId = PageSizeId
    Pica = Unit()
    Point = Unit()
    Postcard = PageSizeId()
    Prc16K = PageSizeId()
    Prc32K = PageSizeId()
    Prc32KBig = PageSizeId()
    Quarto = PageSizeId()
    SizeMatchPolicy = SizeMatchPolicy
    Statement = PageSizeId()
    SuperA = PageSizeId()
    SuperB = PageSizeId()
    Tabloid = PageSizeId()
    TabloidExtra = PageSizeId()
    Unit = Unit
    __class__ = QPageSize
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, size: PySide2.QtCore.QSizeF, units: PySide2.QtGui.QPageSize.Unit, name: str='', matchPolicy: PySide2.QtGui.QPageSize.SizeMatchPolicy=PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch):
        "QPageSize(self)\nQPageSize(self, other:PySide2.QtGui.QPageSize)\nQPageSize(self, pageSizeId:PySide2.QtGui.QPageSize.PageSizeId)\nQPageSize(self, pointSize:PySide2.QtCore.QSize, name:str='', matchPolicy:PySide2.QtGui.QPageSize.SizeMatchPolicy=PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch)\nQPageSize(self, size:PySide2.QtCore.QSizeF, units:PySide2.QtGui.QPageSize.Unit, name:str='', matchPolicy:PySide2.QtGui.QPageSize.SizeMatchPolicy=PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch)"
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def definitionSize(cls, pageSizeId: PySide2.QtGui.QPageSize.PageSizeId):
        'definitionSize(pageSizeId:PySide2.QtGui.QPageSize.PageSizeId) -> PySide2.QtCore.QSizeF\ndefinitionSize(self) -> PySide2.QtCore.QSizeF'
        pass
    
    @classmethod
    def definitionUnits(cls, pageSizeId: PySide2.QtGui.QPageSize.PageSizeId):
        'definitionUnits(pageSizeId:PySide2.QtGui.QPageSize.PageSizeId) -> PySide2.QtGui.QPageSize.Unit\ndefinitionUnits(self) -> PySide2.QtGui.QPageSize.Unit'
        pass
    
    @classmethod
    def id(cls, size: PySide2.QtCore.QSizeF, units: PySide2.QtGui.QPageSize.Unit, matchPolicy: PySide2.QtGui.QPageSize.SizeMatchPolicy=PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch):
        'id(pointSize:PySide2.QtCore.QSize, matchPolicy:PySide2.QtGui.QPageSize.SizeMatchPolicy=PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch) -> PySide2.QtGui.QPageSize.PageSizeId\nid(self) -> PySide2.QtGui.QPageSize.PageSizeId\nid(size:PySide2.QtCore.QSizeF, units:PySide2.QtGui.QPageSize.Unit, matchPolicy:PySide2.QtGui.QPageSize.SizeMatchPolicy=PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch) -> PySide2.QtGui.QPageSize.PageSizeId\nid(windowsId:int) -> PySide2.QtGui.QPageSize.PageSizeId'
        pass
    
    def isEquivalentTo(self, other):
        'isEquivalentTo(self, other:PySide2.QtGui.QPageSize) -> bool'
        return bool
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    @classmethod
    def key(cls, pageSizeId: PySide2.QtGui.QPageSize.PageSizeId):
        'key(pageSizeId:PySide2.QtGui.QPageSize.PageSizeId) -> str\nkey(self) -> str'
        return ''
    
    @classmethod
    def name(cls, pageSizeId: PySide2.QtGui.QPageSize.PageSizeId):
        'name(pageSizeId:PySide2.QtGui.QPageSize.PageSizeId) -> str\nname(self) -> str'
        return ''
    
    def rect(self, units):
        'rect(self, units:PySide2.QtGui.QPageSize.Unit) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def rectPixels(self, resolution):
        'rectPixels(self, resolution:int) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def rectPoints(self):
        'rectPoints(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    @classmethod
    def size(cls, pageSizeId: PySide2.QtGui.QPageSize.PageSizeId, units: PySide2.QtGui.QPageSize.Unit):
        'size(pageSizeId:PySide2.QtGui.QPageSize.PageSizeId, units:PySide2.QtGui.QPageSize.Unit) -> PySide2.QtCore.QSizeF\nsize(self, units:PySide2.QtGui.QPageSize.Unit) -> PySide2.QtCore.QSizeF'
        pass
    
    @classmethod
    def sizePixels(cls, pageSizeId: PySide2.QtGui.QPageSize.PageSizeId, resolution: int):
        'sizePixels(pageSizeId:PySide2.QtGui.QPageSize.PageSizeId, resolution:int) -> PySide2.QtCore.QSize\nsizePixels(self, resolution:int) -> PySide2.QtCore.QSize'
        pass
    
    @classmethod
    def sizePoints(cls, pageSizeId: PySide2.QtGui.QPageSize.PageSizeId):
        'sizePoints(pageSizeId:PySide2.QtGui.QPageSize.PageSizeId) -> PySide2.QtCore.QSize\nsizePoints(self) -> PySide2.QtCore.QSize'
        pass
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QPageSize)'
        pass
    
    @classmethod
    def windowsId(cls, pageSizeId: PySide2.QtGui.QPageSize.PageSizeId):
        'windowsId(pageSizeId:PySide2.QtGui.QPageSize.PageSizeId) -> int\nwindowsId(self) -> int'
        return 1
    

class QPagedPaintDevice(QPaintDevice):
    'QPagedPaintDevice(self)'
    A0 = PageSize()
    A1 = PageSize()
    A10 = PageSize()
    A2 = PageSize()
    A3 = PageSize()
    A3Extra = PageSize()
    A4 = PageSize()
    A4Extra = PageSize()
    A4Plus = PageSize()
    A4Small = PageSize()
    A5 = PageSize()
    A5Extra = PageSize()
    A6 = PageSize()
    A7 = PageSize()
    A8 = PageSize()
    A9 = PageSize()
    AnsiA = PageSize()
    AnsiB = PageSize()
    AnsiC = PageSize()
    AnsiD = PageSize()
    AnsiE = PageSize()
    ArchA = PageSize()
    ArchB = PageSize()
    ArchC = PageSize()
    ArchD = PageSize()
    ArchE = PageSize()
    B0 = PageSize()
    B1 = PageSize()
    B10 = PageSize()
    B2 = PageSize()
    B3 = PageSize()
    B4 = PageSize()
    B5 = PageSize()
    B5Extra = PageSize()
    B6 = PageSize()
    B7 = PageSize()
    B8 = PageSize()
    B9 = PageSize()
    C5E = PageSize()
    Comm10E = PageSize()
    Custom = PageSize()
    DLE = PageSize()
    DoublePostcard = PageSize()
    Envelope10 = PageSize()
    Envelope11 = PageSize()
    Envelope12 = PageSize()
    Envelope14 = PageSize()
    Envelope9 = PageSize()
    EnvelopeB4 = PageSize()
    EnvelopeB5 = PageSize()
    EnvelopeB6 = PageSize()
    EnvelopeC0 = PageSize()
    EnvelopeC1 = PageSize()
    EnvelopeC2 = PageSize()
    EnvelopeC3 = PageSize()
    EnvelopeC4 = PageSize()
    EnvelopeC5 = PageSize()
    EnvelopeC6 = PageSize()
    EnvelopeC65 = PageSize()
    EnvelopeC7 = PageSize()
    EnvelopeChou3 = PageSize()
    EnvelopeChou4 = PageSize()
    EnvelopeDL = PageSize()
    EnvelopeInvite = PageSize()
    EnvelopeItalian = PageSize()
    EnvelopeKaku2 = PageSize()
    EnvelopeKaku3 = PageSize()
    EnvelopeMonarch = PageSize()
    EnvelopePersonal = PageSize()
    EnvelopePrc1 = PageSize()
    EnvelopePrc10 = PageSize()
    EnvelopePrc2 = PageSize()
    EnvelopePrc3 = PageSize()
    EnvelopePrc4 = PageSize()
    EnvelopePrc5 = PageSize()
    EnvelopePrc6 = PageSize()
    EnvelopePrc7 = PageSize()
    EnvelopePrc8 = PageSize()
    EnvelopePrc9 = PageSize()
    EnvelopeYou4 = PageSize()
    Executive = PageSize()
    ExecutiveStandard = PageSize()
    FanFoldGerman = PageSize()
    FanFoldGermanLegal = PageSize()
    FanFoldUS = PageSize()
    Folio = PageSize()
    Imperial10x11 = PageSize()
    Imperial10x13 = PageSize()
    Imperial10x14 = PageSize()
    Imperial12x11 = PageSize()
    Imperial15x11 = PageSize()
    Imperial7x9 = PageSize()
    Imperial8x10 = PageSize()
    Imperial9x11 = PageSize()
    Imperial9x12 = PageSize()
    JisB0 = PageSize()
    JisB1 = PageSize()
    JisB10 = PageSize()
    JisB2 = PageSize()
    JisB3 = PageSize()
    JisB4 = PageSize()
    JisB5 = PageSize()
    JisB6 = PageSize()
    JisB7 = PageSize()
    JisB8 = PageSize()
    JisB9 = PageSize()
    LastPageSize = PageSize()
    Ledger = PageSize()
    Legal = PageSize()
    LegalExtra = PageSize()
    Letter = PageSize()
    LetterExtra = PageSize()
    LetterPlus = PageSize()
    LetterSmall = PageSize()
    Margins = Margins
    NPageSize = PageSize()
    NPaperSize = PageSize()
    Note = PageSize()
    PageSize = PageSize
    PdfVersion = PdfVersion
    PdfVersion_1_4 = PdfVersion()
    PdfVersion_1_6 = PdfVersion()
    PdfVersion_A1b = PdfVersion()
    Postcard = PageSize()
    Prc16K = PageSize()
    Prc32K = PageSize()
    Prc32KBig = PageSize()
    Quarto = PageSize()
    Statement = PageSize()
    SuperA = PageSize()
    SuperB = PageSize()
    Tabloid = PageSize()
    TabloidExtra = PageSize()
    __class__ = QPagedPaintDevice
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QPagedPaintDevice(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def devicePageLayout(self):
        'devicePageLayout(self) -> PySide2.QtGui.QPageLayout'
        return PySide2.QtGui.QPageLayout
    
    def margins(self):
        'margins(self) -> PySide2.QtGui.QPagedPaintDevice.Margins'
        return PySide2.QtGui.QPagedPaintDevice.Margins
    
    def newPage(self):
        'newPage(self) -> bool'
        return bool
    
    def pageLayout(self):
        'pageLayout(self) -> PySide2.QtGui.QPageLayout'
        return PySide2.QtGui.QPageLayout
    
    def pageSize(self):
        'pageSize(self) -> PySide2.QtGui.QPagedPaintDevice.PageSize'
        return PySide2.QtGui.QPagedPaintDevice.PageSize
    
    def pageSizeMM(self):
        'pageSizeMM(self) -> PySide2.QtCore.QSizeF'
        return PySide2.QtCore.QSizeF
    
    def setMargins(self, margins):
        'setMargins(self, margins:PySide2.QtGui.QPagedPaintDevice.Margins)'
        pass
    
    def setPageLayout(self, pageLayout):
        'setPageLayout(self, pageLayout:PySide2.QtGui.QPageLayout) -> bool'
        return bool
    
    def setPageMargins(self, margins: PySide2.QtCore.QMarginsF, units: PySide2.QtGui.QPageLayout.Unit):
        'setPageMargins(self, margins:PySide2.QtCore.QMarginsF) -> bool\nsetPageMargins(self, margins:PySide2.QtCore.QMarginsF, units:PySide2.QtGui.QPageLayout.Unit) -> bool'
        return True
    
    def setPageOrientation(self, orientation):
        'setPageOrientation(self, orientation:PySide2.QtGui.QPageLayout.Orientation) -> bool'
        return bool
    
    def setPageSize(self, size: PySide2.QtGui.QPagedPaintDevice.PageSize):
        'setPageSize(self, pageSize:PySide2.QtGui.QPageSize) -> bool\nsetPageSize(self, size:PySide2.QtGui.QPagedPaintDevice.PageSize)'
        return True
    
    def setPageSizeMM(self, size):
        'setPageSizeMM(self, size:PySide2.QtCore.QSizeF)'
        pass
    

class QPaintDevice(_mod_Shiboken.Object):
    'QPaintDevice(self)'
    PaintDeviceMetric = PaintDeviceMetric
    PdmDepth = PaintDeviceMetric()
    PdmDevicePixelRatio = PaintDeviceMetric()
    PdmDevicePixelRatioScaled = PaintDeviceMetric()
    PdmDpiX = PaintDeviceMetric()
    PdmDpiY = PaintDeviceMetric()
    PdmHeight = PaintDeviceMetric()
    PdmHeightMM = PaintDeviceMetric()
    PdmNumColors = PaintDeviceMetric()
    PdmPhysicalDpiX = PaintDeviceMetric()
    PdmPhysicalDpiY = PaintDeviceMetric()
    PdmWidth = PaintDeviceMetric()
    PdmWidthMM = PaintDeviceMetric()
    __class__ = QPaintDevice
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QPaintDevice(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def colorCount(self):
        'colorCount(self) -> int'
        return int
    
    def depth(self):
        'depth(self) -> int'
        return int
    
    def devType(self):
        'devType(self) -> int'
        return int
    
    def devicePixelRatio(self):
        'devicePixelRatio(self) -> int'
        return int
    
    def devicePixelRatioF(self):
        'devicePixelRatioF(self) -> float'
        return float
    
    @classmethod
    def devicePixelRatioFScale(cls):
        'devicePixelRatioFScale() -> float'
        return float
    
    def height(self):
        'height(self) -> int'
        return int
    
    def heightMM(self):
        'heightMM(self) -> int'
        return int
    
    def initPainter(self, painter):
        'initPainter(self, painter:PySide2.QtGui.QPainter)'
        pass
    
    def logicalDpiX(self):
        'logicalDpiX(self) -> int'
        return int
    
    def logicalDpiY(self):
        'logicalDpiY(self) -> int'
        return int
    
    def metric(self, metric):
        'metric(self, metric:PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int'
        return int
    
    def paintEngine(self):
        'paintEngine(self) -> PySide2.QtGui.QPaintEngine'
        return PySide2.QtGui.QPaintEngine
    
    @property
    def painters(self):
        pass
    
    def paintingActive(self):
        'paintingActive(self) -> bool'
        return bool
    
    def physicalDpiX(self):
        'physicalDpiX(self) -> int'
        return int
    
    def physicalDpiY(self):
        'physicalDpiY(self) -> int'
        return int
    
    def redirected(self, offset):
        'redirected(self, offset:PySide2.QtCore.QPoint) -> PySide2.QtGui.QPaintDevice'
        return PySide2.QtGui.QPaintDevice
    
    def sharedPainter(self):
        'sharedPainter(self) -> PySide2.QtGui.QPainter'
        return PySide2.QtGui.QPainter
    
    def width(self):
        'width(self) -> int'
        return int
    
    def widthMM(self):
        'widthMM(self) -> int'
        return int
    

class QPaintDeviceWindow(QWindow,QPaintDevice):
    __class__ = QPaintDeviceWindow
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def event(self, event):
        'event(self, event:PySide2.QtCore.QEvent) -> bool'
        return bool
    
    def exposeEvent(self, arg__1):
        'exposeEvent(self, arg__1:PySide2.QtGui.QExposeEvent)'
        pass
    
    def metric(self, metric):
        'metric(self, metric:PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int'
        return int
    
    def paintEngine(self):
        'paintEngine(self) -> PySide2.QtGui.QPaintEngine'
        return PySide2.QtGui.QPaintEngine
    
    def paintEvent(self, event):
        'paintEvent(self, event:PySide2.QtGui.QPaintEvent)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def update(self, region: PySide2.QtGui.QRegion):
        'update(self)\nupdate(self, rect:PySide2.QtCore.QRect)\nupdate(self, region:PySide2.QtGui.QRegion)'
        pass
    

class QPaintEngine(_mod_Shiboken.Object):
    'QPaintEngine(self, features:PySide2.QtGui.QPaintEngine.PaintEngineFeatures=Default(QPaintEngine.PaintEngineFeatures))'
    AllDirty = DirtyFlag()
    AllFeatures = PaintEngineFeature()
    AlphaBlend = PaintEngineFeature()
    Antialiasing = PaintEngineFeature()
    BlendModes = PaintEngineFeature()
    Blitter = Type()
    BrushStroke = PaintEngineFeature()
    ConicalGradientFill = PaintEngineFeature()
    ConstantOpacity = PaintEngineFeature()
    ConvexMode = PolygonDrawMode()
    CoreGraphics = Type()
    Direct2D = Type()
    Direct3D = Type()
    DirtyBackground = DirtyFlag()
    DirtyBackgroundMode = DirtyFlag()
    DirtyBrush = DirtyFlag()
    DirtyBrushOrigin = DirtyFlag()
    DirtyClipEnabled = DirtyFlag()
    DirtyClipPath = DirtyFlag()
    DirtyClipRegion = DirtyFlag()
    DirtyCompositionMode = DirtyFlag()
    DirtyFlag = DirtyFlag
    DirtyFlags = DirtyFlags
    DirtyFont = DirtyFlag()
    DirtyHints = DirtyFlag()
    DirtyOpacity = DirtyFlag()
    DirtyPen = DirtyFlag()
    DirtyTransform = DirtyFlag()
    LinearGradientFill = PaintEngineFeature()
    MacPrinter = Type()
    MaskedBrush = PaintEngineFeature()
    MaxUser = Type()
    ObjectBoundingModeGradients = PaintEngineFeature()
    OddEvenMode = PolygonDrawMode()
    OpenGL = Type()
    OpenGL2 = Type()
    OpenVG = Type()
    PaintBuffer = Type()
    PaintEngineFeature = PaintEngineFeature
    PaintEngineFeatures = PaintEngineFeatures
    PaintOutsidePaintEvent = PaintEngineFeature()
    PainterPaths = PaintEngineFeature()
    PatternBrush = PaintEngineFeature()
    PatternTransform = PaintEngineFeature()
    Pdf = Type()
    PerspectiveTransform = PaintEngineFeature()
    Picture = Type()
    PixmapTransform = PaintEngineFeature()
    PolygonDrawMode = PolygonDrawMode
    PolylineMode = PolygonDrawMode()
    PorterDuff = PaintEngineFeature()
    PostScript = Type()
    PrimitiveTransform = PaintEngineFeature()
    QWindowSystem = Type()
    QuickDraw = Type()
    RadialGradientFill = PaintEngineFeature()
    Raster = Type()
    RasterOpModes = PaintEngineFeature()
    SVG = Type()
    Type = Type
    User = Type()
    WindingMode = PolygonDrawMode()
    Windows = Type()
    X11 = Type()
    __class__ = QPaintEngine
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, features: PySide2.QtGui.QPaintEngine.PaintEngineFeatures=Default(QPaintEngine.PaintEngineFeatures)):
        'QPaintEngine(self, features:PySide2.QtGui.QPaintEngine.PaintEngineFeatures=Default(QPaintEngine.PaintEngineFeatures))'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def active(self):
        pass
    
    def begin(self, pdev):
        'begin(self, pdev:PySide2.QtGui.QPaintDevice) -> bool'
        return bool
    
    def clearDirty(self, df):
        'clearDirty(self, df:PySide2.QtGui.QPaintEngine.DirtyFlags)'
        pass
    
    def coordinateOffset(self):
        'coordinateOffset(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def drawEllipse(self, r: PySide2.QtCore.QRectF):
        'drawEllipse(self, r:PySide2.QtCore.QRect)\ndrawEllipse(self, r:PySide2.QtCore.QRectF)'
        pass
    
    def drawImage(self, r, pm, sr, flags):
        'drawImage(self, r:PySide2.QtCore.QRectF, pm:PySide2.QtGui.QImage, sr:PySide2.QtCore.QRectF, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor)'
        pass
    
    def drawLines(self, lines: PySide2.QtCore.QLineF, lineCount: int):
        'drawLines(self, lines:PySide2.QtCore.QLine, lineCount:int)\ndrawLines(self, lines:PySide2.QtCore.QLineF, lineCount:int)'
        pass
    
    def drawPath(self, path):
        'drawPath(self, path:PySide2.QtGui.QPainterPath)'
        pass
    
    def drawPixmap(self, r, pm, sr):
        'drawPixmap(self, r:PySide2.QtCore.QRectF, pm:PySide2.QtGui.QPixmap, sr:PySide2.QtCore.QRectF)'
        pass
    
    def drawPoints(self, points: PySide2.QtCore.QPointF, pointCount: int):
        'drawPoints(self, points:PySide2.QtCore.QPoint, pointCount:int)\ndrawPoints(self, points:PySide2.QtCore.QPointF, pointCount:int)'
        pass
    
    def drawPolygon(self, points: PySide2.QtCore.QPointF, pointCount: int, mode: PySide2.QtGui.QPaintEngine.PolygonDrawMode):
        'drawPolygon(self, points:PySide2.QtCore.QPoint, pointCount:int, mode:PySide2.QtGui.QPaintEngine.PolygonDrawMode)\ndrawPolygon(self, points:PySide2.QtCore.QPointF, pointCount:int, mode:PySide2.QtGui.QPaintEngine.PolygonDrawMode)'
        pass
    
    def drawRects(self, rects: PySide2.QtCore.QRectF, rectCount: int):
        'drawRects(self, rects:PySide2.QtCore.QRect, rectCount:int)\ndrawRects(self, rects:PySide2.QtCore.QRectF, rectCount:int)'
        pass
    
    def drawTextItem(self, p, textItem):
        'drawTextItem(self, p:PySide2.QtCore.QPointF, textItem:PySide2.QtGui.QTextItem)'
        pass
    
    def drawTiledPixmap(self, r, pixmap, s):
        'drawTiledPixmap(self, r:PySide2.QtCore.QRectF, pixmap:PySide2.QtGui.QPixmap, s:PySide2.QtCore.QPointF)'
        pass
    
    def end(self):
        'end(self) -> bool'
        return bool
    
    @property
    def extended(self):
        pass
    
    @property
    def gccaps(self):
        pass
    
    def hasFeature(self, feature):
        'hasFeature(self, feature:PySide2.QtGui.QPaintEngine.PaintEngineFeatures) -> bool'
        return bool
    
    def isActive(self):
        'isActive(self) -> bool'
        return bool
    
    def isExtended(self):
        'isExtended(self) -> bool'
        return bool
    
    def paintDevice(self):
        'paintDevice(self) -> PySide2.QtGui.QPaintDevice'
        return PySide2.QtGui.QPaintDevice
    
    def painter(self):
        'painter(self) -> PySide2.QtGui.QPainter'
        return PySide2.QtGui.QPainter
    
    @property
    def selfDestruct(self):
        pass
    
    def setActive(self, newState):
        'setActive(self, newState:bool)'
        pass
    
    def setDirty(self, df):
        'setDirty(self, df:PySide2.QtGui.QPaintEngine.DirtyFlags)'
        pass
    
    def setSystemClip(self, baseClip):
        'setSystemClip(self, baseClip:PySide2.QtGui.QRegion)'
        pass
    
    def setSystemRect(self, rect):
        'setSystemRect(self, rect:PySide2.QtCore.QRect)'
        pass
    
    @property
    def state(self):
        pass
    
    def syncState(self):
        'syncState(self)'
        pass
    
    def systemClip(self):
        'systemClip(self) -> PySide2.QtGui.QRegion'
        return PySide2.QtGui.QRegion
    
    def systemRect(self):
        'systemRect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def testDirty(self, df):
        'testDirty(self, df:PySide2.QtGui.QPaintEngine.DirtyFlags) -> bool'
        return bool
    
    def type(self):
        'type(self) -> PySide2.QtGui.QPaintEngine.Type'
        return PySide2.QtGui.QPaintEngine.Type
    
    def updateState(self, state):
        'updateState(self, state:PySide2.QtGui.QPaintEngineState)'
        pass
    

class QPaintEngineState(_mod_Shiboken.Object):
    'QPaintEngineState(self)'
    __class__ = QPaintEngineState
    __dict__ = {}
    def __init__(self):
        'QPaintEngineState(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def backgroundBrush(self):
        'backgroundBrush(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def backgroundMode(self):
        'backgroundMode(self) -> PySide2.QtCore.Qt.BGMode'
        return PySide2.QtCore.Qt.BGMode
    
    def brush(self):
        'brush(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def brushNeedsResolving(self):
        'brushNeedsResolving(self) -> bool'
        return bool
    
    def brushOrigin(self):
        'brushOrigin(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def clipOperation(self):
        'clipOperation(self) -> PySide2.QtCore.Qt.ClipOperation'
        return PySide2.QtCore.Qt.ClipOperation
    
    def clipPath(self):
        'clipPath(self) -> PySide2.QtGui.QPainterPath'
        return PySide2.QtGui.QPainterPath
    
    def clipRegion(self):
        'clipRegion(self) -> PySide2.QtGui.QRegion'
        return PySide2.QtGui.QRegion
    
    def compositionMode(self):
        'compositionMode(self) -> PySide2.QtGui.QPainter.CompositionMode'
        return PySide2.QtGui.QPainter.CompositionMode
    
    @property
    def dirtyFlags(self):
        pass
    
    def font(self):
        'font(self) -> PySide2.QtGui.QFont'
        return PySide2.QtGui.QFont
    
    def isClipEnabled(self):
        'isClipEnabled(self) -> bool'
        return bool
    
    def matrix(self):
        'matrix(self) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    
    def opacity(self):
        'opacity(self) -> float'
        return float
    
    def painter(self):
        'painter(self) -> PySide2.QtGui.QPainter'
        return PySide2.QtGui.QPainter
    
    def pen(self):
        'pen(self) -> PySide2.QtGui.QPen'
        return PySide2.QtGui.QPen
    
    def penNeedsResolving(self):
        'penNeedsResolving(self) -> bool'
        return bool
    
    def renderHints(self):
        'renderHints(self) -> PySide2.QtGui.QPainter.RenderHints'
        return PySide2.QtGui.QPainter.RenderHints
    
    def state(self):
        'state(self) -> PySide2.QtGui.QPaintEngine.DirtyFlags'
        return PySide2.QtGui.QPaintEngine.DirtyFlags
    
    def transform(self):
        'transform(self) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    

class QPaintEvent(_mod_PySide2_QtCore.QEvent):
    'QPaintEvent(self, paintRect:PySide2.QtCore.QRect)\nQPaintEvent(self, paintRegion:PySide2.QtGui.QRegion)'
    __class__ = QPaintEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, paintRegion: PySide2.QtGui.QRegion):
        'QPaintEvent(self, paintRect:PySide2.QtCore.QRect)\nQPaintEvent(self, paintRegion:PySide2.QtGui.QRegion)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def rect(self):
        'rect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def region(self):
        'region(self) -> PySide2.QtGui.QRegion'
        return PySide2.QtGui.QRegion
    

class QPainter(_mod_Shiboken.Object):
    'QPainter(self)\nQPainter(self, arg__1:PySide2.QtGui.QPaintDevice)'
    Antialiasing = RenderHint()
    CompositionMode = CompositionMode
    CompositionMode_Clear = CompositionMode()
    CompositionMode_ColorBurn = CompositionMode()
    CompositionMode_ColorDodge = CompositionMode()
    CompositionMode_Darken = CompositionMode()
    CompositionMode_Destination = CompositionMode()
    CompositionMode_DestinationAtop = CompositionMode()
    CompositionMode_DestinationIn = CompositionMode()
    CompositionMode_DestinationOut = CompositionMode()
    CompositionMode_DestinationOver = CompositionMode()
    CompositionMode_Difference = CompositionMode()
    CompositionMode_Exclusion = CompositionMode()
    CompositionMode_HardLight = CompositionMode()
    CompositionMode_Lighten = CompositionMode()
    CompositionMode_Multiply = CompositionMode()
    CompositionMode_Overlay = CompositionMode()
    CompositionMode_Plus = CompositionMode()
    CompositionMode_Screen = CompositionMode()
    CompositionMode_SoftLight = CompositionMode()
    CompositionMode_Source = CompositionMode()
    CompositionMode_SourceAtop = CompositionMode()
    CompositionMode_SourceIn = CompositionMode()
    CompositionMode_SourceOut = CompositionMode()
    CompositionMode_SourceOver = CompositionMode()
    CompositionMode_Xor = CompositionMode()
    HighQualityAntialiasing = RenderHint()
    LosslessImageRendering = RenderHint()
    NonCosmeticDefaultPen = RenderHint()
    OpaqueHint = PixmapFragmentHint()
    PixmapFragment = PixmapFragment
    PixmapFragmentHint = PixmapFragmentHint
    PixmapFragmentHints = PixmapFragmentHints
    Qt4CompatiblePainting = RenderHint()
    RasterOp_ClearDestination = CompositionMode()
    RasterOp_NotDestination = CompositionMode()
    RasterOp_NotSource = CompositionMode()
    RasterOp_NotSourceAndDestination = CompositionMode()
    RasterOp_NotSourceAndNotDestination = CompositionMode()
    RasterOp_NotSourceOrDestination = CompositionMode()
    RasterOp_NotSourceOrNotDestination = CompositionMode()
    RasterOp_NotSourceXorDestination = CompositionMode()
    RasterOp_SetDestination = CompositionMode()
    RasterOp_SourceAndDestination = CompositionMode()
    RasterOp_SourceAndNotDestination = CompositionMode()
    RasterOp_SourceOrDestination = CompositionMode()
    RasterOp_SourceOrNotDestination = CompositionMode()
    RasterOp_SourceXorDestination = CompositionMode()
    RenderHint = RenderHint
    RenderHints = RenderHints
    SmoothPixmapTransform = RenderHint()
    TextAntialiasing = RenderHint()
    __class__ = QPainter
    __dict__ = {}
    def __init__(self, arg__1: PySide2.QtGui.QPaintDevice):
        'QPainter(self)\nQPainter(self, arg__1:PySide2.QtGui.QPaintDevice)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def background(self):
        'background(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def backgroundMode(self):
        'backgroundMode(self) -> PySide2.QtCore.Qt.BGMode'
        return PySide2.QtCore.Qt.BGMode
    
    def begin(self, arg__1):
        'begin(self, arg__1:PySide2.QtGui.QPaintDevice) -> bool'
        return bool
    
    def beginNativePainting(self):
        'beginNativePainting(self)'
        pass
    
    def boundingRect(self, rect: PySide2.QtCore.QRectF, text: str, o: PySide2.QtGui.QTextOption=Default(QTextOption)):
        'boundingRect(self, rect:PySide2.QtCore.QRect, flags:int, text:str) -> PySide2.QtCore.QRect\nboundingRect(self, rect:PySide2.QtCore.QRectF, flags:int, text:str) -> PySide2.QtCore.QRectF\nboundingRect(self, rect:PySide2.QtCore.QRectF, text:str, o:PySide2.QtGui.QTextOption=Default(QTextOption)) -> PySide2.QtCore.QRectF\nboundingRect(self, x:int, y:int, w:int, h:int, flags:int, text:str) -> PySide2.QtCore.QRect'
        pass
    
    def brush(self):
        'brush(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def brushOrigin(self):
        'brushOrigin(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def clipBoundingRect(self):
        'clipBoundingRect(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def clipPath(self):
        'clipPath(self) -> PySide2.QtGui.QPainterPath'
        return PySide2.QtGui.QPainterPath
    
    def clipRegion(self):
        'clipRegion(self) -> PySide2.QtGui.QRegion'
        return PySide2.QtGui.QRegion
    
    def combinedMatrix(self):
        'combinedMatrix(self) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    
    def combinedTransform(self):
        'combinedTransform(self) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def compositionMode(self):
        'compositionMode(self) -> PySide2.QtGui.QPainter.CompositionMode'
        return PySide2.QtGui.QPainter.CompositionMode
    
    def device(self):
        'device(self) -> PySide2.QtGui.QPaintDevice'
        return PySide2.QtGui.QPaintDevice
    
    def deviceMatrix(self):
        'deviceMatrix(self) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    
    def deviceTransform(self):
        'deviceTransform(self) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def drawArc(self, arg__1: PySide2.QtCore.QRect, a: int, alen: int):
        'drawArc(self, arg__1:PySide2.QtCore.QRect, a:int, alen:int)\ndrawArc(self, rect:PySide2.QtCore.QRectF, a:int, alen:int)\ndrawArc(self, x:int, y:int, w:int, h:int, a:int, alen:int)'
        pass
    
    def drawChord(self, arg__1: PySide2.QtCore.QRect, a: int, alen: int):
        'drawChord(self, arg__1:PySide2.QtCore.QRect, a:int, alen:int)\ndrawChord(self, rect:PySide2.QtCore.QRectF, a:int, alen:int)\ndrawChord(self, x:int, y:int, w:int, h:int, a:int, alen:int)'
        pass
    
    def drawConvexPolygon(self, polygon: PySide2.QtGui.QPolygonF):
        'drawConvexPolygon(self, arg__1:typing.List)\ndrawConvexPolygon(self, arg__1:typing.List)\ndrawConvexPolygon(self, polygon:PySide2.QtGui.QPolygon)\ndrawConvexPolygon(self, polygon:PySide2.QtGui.QPolygonF)'
        pass
    
    def drawEllipse(self, center: PySide2.QtCore.QPointF, rx: float, ry: float):
        'drawEllipse(self, center:PySide2.QtCore.QPoint, rx:int, ry:int)\ndrawEllipse(self, center:PySide2.QtCore.QPointF, rx:float, ry:float)\ndrawEllipse(self, r:PySide2.QtCore.QRect)\ndrawEllipse(self, r:PySide2.QtCore.QRectF)\ndrawEllipse(self, x:int, y:int, w:int, h:int)'
        pass
    
    def drawImage(self, targetRect: PySide2.QtCore.QRectF, image: PySide2.QtGui.QImage, sourceRect: PySide2.QtCore.QRectF, flags: PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor):
        'drawImage(self, p:PySide2.QtCore.QPoint, image:PySide2.QtGui.QImage)\ndrawImage(self, p:PySide2.QtCore.QPoint, image:PySide2.QtGui.QImage, sr:PySide2.QtCore.QRect, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor)\ndrawImage(self, p:PySide2.QtCore.QPointF, image:PySide2.QtGui.QImage)\ndrawImage(self, p:PySide2.QtCore.QPointF, image:PySide2.QtGui.QImage, sr:PySide2.QtCore.QRectF, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor)\ndrawImage(self, r:PySide2.QtCore.QRect, image:PySide2.QtGui.QImage)\ndrawImage(self, r:PySide2.QtCore.QRectF, image:PySide2.QtGui.QImage)\ndrawImage(self, targetRect:PySide2.QtCore.QRect, image:PySide2.QtGui.QImage, sourceRect:PySide2.QtCore.QRect, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor)\ndrawImage(self, targetRect:PySide2.QtCore.QRectF, image:PySide2.QtGui.QImage, sourceRect:PySide2.QtCore.QRectF, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor)\ndrawImage(self, x:int, y:int, image:PySide2.QtGui.QImage, sx:int=0, sy:int=0, sw:int=-1, sh:int=-1, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor)'
        pass
    
    def drawLine(self, p1: PySide2.QtCore.QPointF, p2: PySide2.QtCore.QPointF):
        'drawLine(self, line:PySide2.QtCore.QLine)\ndrawLine(self, line:PySide2.QtCore.QLineF)\ndrawLine(self, p1:PySide2.QtCore.QPoint, p2:PySide2.QtCore.QPoint)\ndrawLine(self, p1:PySide2.QtCore.QPointF, p2:PySide2.QtCore.QPointF)\ndrawLine(self, x1:int, y1:int, x2:int, y2:int)'
        pass
    
    def drawLines(self, pointPairs: typing.List):
        'drawLines(self, lines:typing.List)\ndrawLines(self, lines:typing.List)\ndrawLines(self, pointPairs:typing.List)\ndrawLines(self, pointPairs:typing.List)'
        pass
    
    def drawPath(self, path):
        'drawPath(self, path:PySide2.QtGui.QPainterPath)'
        pass
    
    def drawPicture(self, p: PySide2.QtCore.QPointF, picture: PySide2.QtGui.QPicture):
        'drawPicture(self, p:PySide2.QtCore.QPoint, picture:PySide2.QtGui.QPicture)\ndrawPicture(self, p:PySide2.QtCore.QPointF, picture:PySide2.QtGui.QPicture)\ndrawPicture(self, x:int, y:int, picture:PySide2.QtGui.QPicture)'
        pass
    
    def drawPie(self, arg__1: PySide2.QtCore.QRect, a: int, alen: int):
        'drawPie(self, arg__1:PySide2.QtCore.QRect, a:int, alen:int)\ndrawPie(self, rect:PySide2.QtCore.QRectF, a:int, alen:int)\ndrawPie(self, x:int, y:int, w:int, h:int, a:int, alen:int)'
        pass
    
    def drawPixmap(self, targetRect: PySide2.QtCore.QRectF, pixmap: PySide2.QtGui.QPixmap, sourceRect: PySide2.QtCore.QRectF):
        'drawPixmap(self, p:PySide2.QtCore.QPoint, pm:PySide2.QtGui.QPixmap)\ndrawPixmap(self, p:PySide2.QtCore.QPoint, pm:PySide2.QtGui.QPixmap, sr:PySide2.QtCore.QRect)\ndrawPixmap(self, p:PySide2.QtCore.QPointF, pm:PySide2.QtGui.QPixmap)\ndrawPixmap(self, p:PySide2.QtCore.QPointF, pm:PySide2.QtGui.QPixmap, sr:PySide2.QtCore.QRectF)\ndrawPixmap(self, r:PySide2.QtCore.QRect, pm:PySide2.QtGui.QPixmap)\ndrawPixmap(self, targetRect:PySide2.QtCore.QRect, pixmap:PySide2.QtGui.QPixmap, sourceRect:PySide2.QtCore.QRect)\ndrawPixmap(self, targetRect:PySide2.QtCore.QRectF, pixmap:PySide2.QtGui.QPixmap, sourceRect:PySide2.QtCore.QRectF)\ndrawPixmap(self, x:int, y:int, pm:PySide2.QtGui.QPixmap)\ndrawPixmap(self, x:int, y:int, pm:PySide2.QtGui.QPixmap, sx:int, sy:int, sw:int, sh:int)\ndrawPixmap(self, x:int, y:int, w:int, h:int, pm:PySide2.QtGui.QPixmap)\ndrawPixmap(self, x:int, y:int, w:int, h:int, pm:PySide2.QtGui.QPixmap, sx:int, sy:int, sw:int, sh:int)'
        pass
    
    def drawPixmapFragments(self, fragments, fragmentCount, pixmap, hints):
        'drawPixmapFragments(self, fragments:PySide2.QtGui.QPainter.PixmapFragment, fragmentCount:int, pixmap:PySide2.QtGui.QPixmap, hints:PySide2.QtGui.QPainter.PixmapFragmentHints=Default(QPainter.PixmapFragmentHints))'
        pass
    
    def drawPoint(self, pt: PySide2.QtCore.QPointF):
        'drawPoint(self, p:PySide2.QtCore.QPoint)\ndrawPoint(self, pt:PySide2.QtCore.QPointF)\ndrawPoint(self, x:int, y:int)'
        pass
    
    def drawPoints(self, points: PySide2.QtGui.QPolygonF):
        'drawPoints(self, arg__1:typing.List)\ndrawPoints(self, arg__1:typing.List)\ndrawPoints(self, points:PySide2.QtGui.QPolygon)\ndrawPoints(self, points:PySide2.QtGui.QPolygonF)'
        pass
    
    def drawPolygon(self, polygon: PySide2.QtGui.QPolygonF, fillRule: PySide2.QtCore.Qt.FillRule=PySide2.QtCore.Qt.FillRule.OddEvenFill):
        'drawPolygon(self, arg__1:typing.List, arg__2:PySide2.QtCore.Qt.FillRule)\ndrawPolygon(self, arg__1:typing.List, arg__2:PySide2.QtCore.Qt.FillRule)\ndrawPolygon(self, polygon:PySide2.QtGui.QPolygon, fillRule:PySide2.QtCore.Qt.FillRule=PySide2.QtCore.Qt.FillRule.OddEvenFill)\ndrawPolygon(self, polygon:PySide2.QtGui.QPolygonF, fillRule:PySide2.QtCore.Qt.FillRule=PySide2.QtCore.Qt.FillRule.OddEvenFill)'
        pass
    
    def drawPolyline(self, polyline: PySide2.QtGui.QPolygonF):
        'drawPolyline(self, arg__1:typing.List)\ndrawPolyline(self, arg__1:typing.List)\ndrawPolyline(self, polygon:PySide2.QtGui.QPolygon)\ndrawPolyline(self, polyline:PySide2.QtGui.QPolygonF)'
        pass
    
    def drawRect(self, x1: int, y1: int, w: int, h: int):
        'drawRect(self, rect:PySide2.QtCore.QRect)\ndrawRect(self, rect:PySide2.QtCore.QRectF)\ndrawRect(self, x1:int, y1:int, w:int, h:int)'
        pass
    
    def drawRects(self, rectangles: typing.List):
        'drawRects(self, rectangles:typing.List)\ndrawRects(self, rectangles:typing.List)'
        pass
    
    def drawRoundRect(self, x: int, y: int, w: int, h: int, xRound: int=25, yRound: int=25):
        'drawRoundRect(self, r:PySide2.QtCore.QRect, xround:int=25, yround:int=25)\ndrawRoundRect(self, r:PySide2.QtCore.QRectF, xround:int=25, yround:int=25)\ndrawRoundRect(self, x:int, y:int, w:int, h:int, xRound:int=25, yRound:int=25)'
        pass
    
    def drawRoundedRect(self, x: int, y: int, w: int, h: int, xRadius: float, yRadius: float, mode: PySide2.QtCore.Qt.SizeMode=PySide2.QtCore.Qt.SizeMode.AbsoluteSize):
        'drawRoundedRect(self, rect:PySide2.QtCore.QRect, xRadius:float, yRadius:float, mode:PySide2.QtCore.Qt.SizeMode=PySide2.QtCore.Qt.SizeMode.AbsoluteSize)\ndrawRoundedRect(self, rect:PySide2.QtCore.QRectF, xRadius:float, yRadius:float, mode:PySide2.QtCore.Qt.SizeMode=PySide2.QtCore.Qt.SizeMode.AbsoluteSize)\ndrawRoundedRect(self, x:int, y:int, w:int, h:int, xRadius:float, yRadius:float, mode:PySide2.QtCore.Qt.SizeMode=PySide2.QtCore.Qt.SizeMode.AbsoluteSize)'
        pass
    
    def drawStaticText(self, topLeftPosition: PySide2.QtCore.QPointF, staticText: PySide2.QtGui.QStaticText):
        'drawStaticText(self, left:int, top:int, staticText:PySide2.QtGui.QStaticText)\ndrawStaticText(self, topLeftPosition:PySide2.QtCore.QPoint, staticText:PySide2.QtGui.QStaticText)\ndrawStaticText(self, topLeftPosition:PySide2.QtCore.QPointF, staticText:PySide2.QtGui.QStaticText)'
        pass
    
    def drawText(self, r: PySide2.QtCore.QRectF, text: str, o: PySide2.QtGui.QTextOption=Default(QTextOption)):
        'drawText(self, p:PySide2.QtCore.QPoint, s:str)\ndrawText(self, p:PySide2.QtCore.QPointF, s:str)\ndrawText(self, r:PySide2.QtCore.QRect, flags:int, text:str, br:PySide2.QtCore.QRect)\ndrawText(self, r:PySide2.QtCore.QRectF, flags:int, text:str, br:PySide2.QtCore.QRectF)\ndrawText(self, r:PySide2.QtCore.QRectF, text:str, o:PySide2.QtGui.QTextOption=Default(QTextOption))\ndrawText(self, x:int, y:int, s:str)\ndrawText(self, x:int, y:int, w:int, h:int, flags:int, text:str, br:PySide2.QtCore.QRect)'
        pass
    
    def drawTextItem(self, p: PySide2.QtCore.QPointF, ti: PySide2.QtGui.QTextItem):
        'drawTextItem(self, p:PySide2.QtCore.QPoint, ti:PySide2.QtGui.QTextItem)\ndrawTextItem(self, p:PySide2.QtCore.QPointF, ti:PySide2.QtGui.QTextItem)\ndrawTextItem(self, x:int, y:int, ti:PySide2.QtGui.QTextItem)'
        pass
    
    def drawTiledPixmap(self, rect: PySide2.QtCore.QRectF, pm: PySide2.QtGui.QPixmap, offset: PySide2.QtCore.QPointF=Default(QPointF)):
        'drawTiledPixmap(self, arg__1:PySide2.QtCore.QRect, arg__2:PySide2.QtGui.QPixmap, pos:PySide2.QtCore.QPoint=Default(QPoint))\ndrawTiledPixmap(self, rect:PySide2.QtCore.QRectF, pm:PySide2.QtGui.QPixmap, offset:PySide2.QtCore.QPointF=Default(QPointF))\ndrawTiledPixmap(self, x:int, y:int, w:int, h:int, arg__5:PySide2.QtGui.QPixmap, sx:int=0, sy:int=0)'
        pass
    
    def end(self):
        'end(self) -> bool'
        return bool
    
    def endNativePainting(self):
        'endNativePainting(self)'
        pass
    
    def eraseRect(self, arg__1: PySide2.QtCore.QRectF):
        'eraseRect(self, arg__1:PySide2.QtCore.QRect)\neraseRect(self, arg__1:PySide2.QtCore.QRectF)\neraseRect(self, x:int, y:int, w:int, h:int)'
        pass
    
    def fillPath(self, path, brush):
        'fillPath(self, path:PySide2.QtGui.QPainterPath, brush:PySide2.QtGui.QBrush)'
        pass
    
    def fillRect(self, x: int, y: int, w: int, h: int, preset: PySide2.QtGui.QGradient.Preset):
        'fillRect(self, arg__1:PySide2.QtCore.QRect, arg__2:PySide2.QtGui.QBrush)\nfillRect(self, arg__1:PySide2.QtCore.QRect, color:PySide2.QtGui.QColor)\nfillRect(self, arg__1:PySide2.QtCore.QRectF, arg__2:PySide2.QtGui.QBrush)\nfillRect(self, arg__1:PySide2.QtCore.QRectF, color:PySide2.QtGui.QColor)\nfillRect(self, r:PySide2.QtCore.QRect, c:PySide2.QtCore.Qt.GlobalColor)\nfillRect(self, r:PySide2.QtCore.QRect, preset:PySide2.QtGui.QGradient.Preset)\nfillRect(self, r:PySide2.QtCore.QRect, style:PySide2.QtCore.Qt.BrushStyle)\nfillRect(self, r:PySide2.QtCore.QRectF, c:PySide2.QtCore.Qt.GlobalColor)\nfillRect(self, r:PySide2.QtCore.QRectF, preset:PySide2.QtGui.QGradient.Preset)\nfillRect(self, r:PySide2.QtCore.QRectF, style:PySide2.QtCore.Qt.BrushStyle)\nfillRect(self, x:int, y:int, w:int, h:int, arg__5:PySide2.QtGui.QBrush)\nfillRect(self, x:int, y:int, w:int, h:int, c:PySide2.QtCore.Qt.GlobalColor)\nfillRect(self, x:int, y:int, w:int, h:int, color:PySide2.QtGui.QColor)\nfillRect(self, x:int, y:int, w:int, h:int, preset:PySide2.QtGui.QGradient.Preset)\nfillRect(self, x:int, y:int, w:int, h:int, style:PySide2.QtCore.Qt.BrushStyle)'
        pass
    
    def font(self):
        'font(self) -> PySide2.QtGui.QFont'
        return PySide2.QtGui.QFont
    
    def fontInfo(self):
        'fontInfo(self) -> PySide2.QtGui.QFontInfo'
        return PySide2.QtGui.QFontInfo
    
    def fontMetrics(self):
        'fontMetrics(self) -> PySide2.QtGui.QFontMetrics'
        return PySide2.QtGui.QFontMetrics
    
    def hasClipping(self):
        'hasClipping(self) -> bool'
        return bool
    
    def initFrom(self, device):
        'initFrom(self, device:PySide2.QtGui.QPaintDevice)'
        pass
    
    def isActive(self):
        'isActive(self) -> bool'
        return bool
    
    def layoutDirection(self):
        'layoutDirection(self) -> PySide2.QtCore.Qt.LayoutDirection'
        return PySide2.QtCore.Qt.LayoutDirection
    
    def matrix(self):
        'matrix(self) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    
    def matrixEnabled(self):
        'matrixEnabled(self) -> bool'
        return bool
    
    def opacity(self):
        'opacity(self) -> float'
        return float
    
    def paintEngine(self):
        'paintEngine(self) -> PySide2.QtGui.QPaintEngine'
        return PySide2.QtGui.QPaintEngine
    
    def pen(self):
        'pen(self) -> PySide2.QtGui.QPen'
        return PySide2.QtGui.QPen
    
    @classmethod
    def redirected(cls, device, offset):
        'redirected(device:PySide2.QtGui.QPaintDevice, offset:typing.Union[PySide2.QtCore.QPoint, NoneType]=None) -> PySide2.QtGui.QPaintDevice'
        return PySide2.QtGui.QPaintDevice
    
    def renderHints(self):
        'renderHints(self) -> PySide2.QtGui.QPainter.RenderHints'
        return PySide2.QtGui.QPainter.RenderHints
    
    def resetMatrix(self):
        'resetMatrix(self)'
        pass
    
    def resetTransform(self):
        'resetTransform(self)'
        pass
    
    def restore(self):
        'restore(self)'
        pass
    
    @classmethod
    def restoreRedirected(cls, device):
        'restoreRedirected(device:PySide2.QtGui.QPaintDevice)'
        pass
    
    def rotate(self, a):
        'rotate(self, a:float)'
        pass
    
    def save(self):
        'save(self)'
        pass
    
    def scale(self, sx, sy):
        'scale(self, sx:float, sy:float)'
        pass
    
    def setBackground(self, bg):
        'setBackground(self, bg:PySide2.QtGui.QBrush)'
        pass
    
    def setBackgroundMode(self, mode):
        'setBackgroundMode(self, mode:PySide2.QtCore.Qt.BGMode)'
        pass
    
    def setBrush(self, style: PySide2.QtCore.Qt.BrushStyle):
        'setBrush(self, brush:PySide2.QtGui.QBrush)\nsetBrush(self, style:PySide2.QtCore.Qt.BrushStyle)'
        pass
    
    def setBrushOrigin(self, arg__1: PySide2.QtCore.QPointF):
        'setBrushOrigin(self, arg__1:PySide2.QtCore.QPoint)\nsetBrushOrigin(self, arg__1:PySide2.QtCore.QPointF)\nsetBrushOrigin(self, x:int, y:int)'
        pass
    
    def setClipPath(self, path, op):
        'setClipPath(self, path:PySide2.QtGui.QPainterPath, op:PySide2.QtCore.Qt.ClipOperation=PySide2.QtCore.Qt.ClipOperation.ReplaceClip)'
        pass
    
    def setClipRect(self, arg__1: PySide2.QtCore.QRectF, op: PySide2.QtCore.Qt.ClipOperation=PySide2.QtCore.Qt.ClipOperation.ReplaceClip):
        'setClipRect(self, arg__1:PySide2.QtCore.QRect, op:PySide2.QtCore.Qt.ClipOperation=PySide2.QtCore.Qt.ClipOperation.ReplaceClip)\nsetClipRect(self, arg__1:PySide2.QtCore.QRectF, op:PySide2.QtCore.Qt.ClipOperation=PySide2.QtCore.Qt.ClipOperation.ReplaceClip)\nsetClipRect(self, x:int, y:int, w:int, h:int, op:PySide2.QtCore.Qt.ClipOperation=PySide2.QtCore.Qt.ClipOperation.ReplaceClip)'
        pass
    
    def setClipRegion(self, arg__1, op):
        'setClipRegion(self, arg__1:PySide2.QtGui.QRegion, op:PySide2.QtCore.Qt.ClipOperation=PySide2.QtCore.Qt.ClipOperation.ReplaceClip)'
        pass
    
    def setClipping(self, enable):
        'setClipping(self, enable:bool)'
        pass
    
    def setCompositionMode(self, mode):
        'setCompositionMode(self, mode:PySide2.QtGui.QPainter.CompositionMode)'
        pass
    
    def setFont(self, f):
        'setFont(self, f:PySide2.QtGui.QFont)'
        pass
    
    def setLayoutDirection(self, direction):
        'setLayoutDirection(self, direction:PySide2.QtCore.Qt.LayoutDirection)'
        pass
    
    def setMatrix(self, matrix, combine):
        'setMatrix(self, matrix:PySide2.QtGui.QMatrix, combine:bool=False)'
        pass
    
    def setMatrixEnabled(self, enabled):
        'setMatrixEnabled(self, enabled:bool)'
        pass
    
    def setOpacity(self, opacity):
        'setOpacity(self, opacity:float)'
        pass
    
    def setPen(self, style: PySide2.QtCore.Qt.PenStyle):
        'setPen(self, color:PySide2.QtGui.QColor)\nsetPen(self, pen:PySide2.QtGui.QPen)\nsetPen(self, style:PySide2.QtCore.Qt.PenStyle)'
        pass
    
    @classmethod
    def setRedirected(cls, device, replacement, offset):
        'setRedirected(device:PySide2.QtGui.QPaintDevice, replacement:PySide2.QtGui.QPaintDevice, offset:PySide2.QtCore.QPoint=Default(QPoint))'
        pass
    
    def setRenderHint(self, hint, on):
        'setRenderHint(self, hint:PySide2.QtGui.QPainter.RenderHint, on:bool=True)'
        pass
    
    def setRenderHints(self, hints, on):
        'setRenderHints(self, hints:PySide2.QtGui.QPainter.RenderHints, on:bool=True)'
        pass
    
    def setTransform(self, transform, combine):
        'setTransform(self, transform:PySide2.QtGui.QTransform, combine:bool=False)'
        pass
    
    def setViewTransformEnabled(self, enable):
        'setViewTransformEnabled(self, enable:bool)'
        pass
    
    def setViewport(self, viewport: PySide2.QtCore.QRect):
        'setViewport(self, viewport:PySide2.QtCore.QRect)\nsetViewport(self, x:int, y:int, w:int, h:int)'
        pass
    
    def setWindow(self, window: PySide2.QtCore.QRect):
        'setWindow(self, window:PySide2.QtCore.QRect)\nsetWindow(self, x:int, y:int, w:int, h:int)'
        pass
    
    def setWorldMatrix(self, matrix, combine):
        'setWorldMatrix(self, matrix:PySide2.QtGui.QMatrix, combine:bool=False)'
        pass
    
    def setWorldMatrixEnabled(self, enabled):
        'setWorldMatrixEnabled(self, enabled:bool)'
        pass
    
    def setWorldTransform(self, matrix, combine):
        'setWorldTransform(self, matrix:PySide2.QtGui.QTransform, combine:bool=False)'
        pass
    
    def shear(self, sh, sv):
        'shear(self, sh:float, sv:float)'
        pass
    
    def strokePath(self, path, pen):
        'strokePath(self, path:PySide2.QtGui.QPainterPath, pen:PySide2.QtGui.QPen)'
        pass
    
    def testRenderHint(self, hint):
        'testRenderHint(self, hint:PySide2.QtGui.QPainter.RenderHint) -> bool'
        return bool
    
    def transform(self):
        'transform(self) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def translate(self, offset: PySide2.QtCore.QPointF):
        'translate(self, dx:float, dy:float)\ntranslate(self, offset:PySide2.QtCore.QPoint)\ntranslate(self, offset:PySide2.QtCore.QPointF)'
        pass
    
    def viewTransformEnabled(self):
        'viewTransformEnabled(self) -> bool'
        return bool
    
    def viewport(self):
        'viewport(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def window(self):
        'window(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def worldMatrix(self):
        'worldMatrix(self) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    
    def worldMatrixEnabled(self):
        'worldMatrixEnabled(self) -> bool'
        return bool
    
    def worldTransform(self):
        'worldTransform(self) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    

class QPainterPath(_mod_Shiboken.Object):
    'QPainterPath(self)\nQPainterPath(self, other:PySide2.QtGui.QPainterPath)\nQPainterPath(self, startPoint:PySide2.QtCore.QPointF)'
    CurveToDataElement = ElementType()
    CurveToElement = ElementType()
    Element = Element
    ElementType = ElementType
    LineToElement = ElementType()
    MoveToElement = ElementType()
    def __add__(self, other):
        '__add__(self, other:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath\n\nReturn self+value.'
        return PySide2.QtGui.QPainterPath
    
    def __and__(self, other):
        '__and__(self, other:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath\n\nReturn self&value.'
        return PySide2.QtGui.QPainterPath
    
    __class__ = QPainterPath
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, other):
        '__iadd__(self, other:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath\n\nReturn self+=value.'
        return PySide2.QtGui.QPainterPath
    
    def __iand__(self, other):
        '__iand__(self, other:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath\n\nReturn self&=value.'
        return PySide2.QtGui.QPainterPath
    
    def __init__(self, startPoint: PySide2.QtCore.QPointF):
        'QPainterPath(self)\nQPainterPath(self, other:PySide2.QtGui.QPainterPath)\nQPainterPath(self, startPoint:PySide2.QtCore.QPointF)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __ior__(self, other):
        '__ior__(self, other:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath\n\nReturn self|=value.'
        return PySide2.QtGui.QPainterPath
    
    def __isub__(self, other):
        '__isub__(self, other:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath\n\nReturn self-=value.'
        return PySide2.QtGui.QPainterPath
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __mul__(self, m: PySide2.QtGui.QTransform):
        '__mul__(self, m:PySide2.QtGui.QMatrix) -> PySide2.QtGui.QPainterPath\n__mul__(self, m:PySide2.QtGui.QTransform) -> PySide2.QtGui.QPainterPath\n\nReturn self*value.'
        return QPainterPath()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __or__(self, other):
        '__or__(self, other:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath\n\nReturn self|value.'
        return PySide2.QtGui.QPainterPath
    
    def __radd__(self, value):
        'Return value+self.'
        return QPainterPath()
    
    def __rand__(self, value):
        'Return value&self.'
        return QPainterPath()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QPainterPath()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QPainterPath()
    
    def __ror__(self, value):
        'Return value|self.'
        return QPainterPath()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QPainterPath()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __rsub__(self, value):
        'Return value-self.'
        return QPainterPath()
    
    def __sub__(self, other):
        '__sub__(self, other:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath\n\nReturn self-value.'
        return PySide2.QtGui.QPainterPath
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addEllipse(self, center: PySide2.QtCore.QPointF, rx: float, ry: float):
        'addEllipse(self, center:PySide2.QtCore.QPointF, rx:float, ry:float)\naddEllipse(self, rect:PySide2.QtCore.QRectF)\naddEllipse(self, x:float, y:float, w:float, h:float)'
        pass
    
    def addPath(self, path):
        'addPath(self, path:PySide2.QtGui.QPainterPath)'
        pass
    
    def addPolygon(self, polygon):
        'addPolygon(self, polygon:PySide2.QtGui.QPolygonF)'
        pass
    
    def addRect(self, x: float, y: float, w: float, h: float):
        'addRect(self, rect:PySide2.QtCore.QRectF)\naddRect(self, x:float, y:float, w:float, h:float)'
        pass
    
    def addRegion(self, region):
        'addRegion(self, region:PySide2.QtGui.QRegion)'
        pass
    
    def addRoundRect(self, x: float, y: float, w: float, h: float, xRnd: int, yRnd: int):
        'addRoundRect(self, rect:PySide2.QtCore.QRectF, roundness:int)\naddRoundRect(self, rect:PySide2.QtCore.QRectF, xRnd:int, yRnd:int)\naddRoundRect(self, x:float, y:float, w:float, h:float, roundness:int)\naddRoundRect(self, x:float, y:float, w:float, h:float, xRnd:int, yRnd:int)'
        pass
    
    def addRoundedRect(self, x: float, y: float, w: float, h: float, xRadius: float, yRadius: float, mode: PySide2.QtCore.Qt.SizeMode=PySide2.QtCore.Qt.SizeMode.AbsoluteSize):
        'addRoundedRect(self, rect:PySide2.QtCore.QRectF, xRadius:float, yRadius:float, mode:PySide2.QtCore.Qt.SizeMode=PySide2.QtCore.Qt.SizeMode.AbsoluteSize)\naddRoundedRect(self, x:float, y:float, w:float, h:float, xRadius:float, yRadius:float, mode:PySide2.QtCore.Qt.SizeMode=PySide2.QtCore.Qt.SizeMode.AbsoluteSize)'
        pass
    
    def addText(self, point: PySide2.QtCore.QPointF, f: PySide2.QtGui.QFont, text: str):
        'addText(self, point:PySide2.QtCore.QPointF, f:PySide2.QtGui.QFont, text:str)\naddText(self, x:float, y:float, f:PySide2.QtGui.QFont, text:str)'
        pass
    
    def angleAtPercent(self, t):
        'angleAtPercent(self, t:float) -> float'
        return float
    
    def arcMoveTo(self, x: float, y: float, w: float, h: float, angle: float):
        'arcMoveTo(self, rect:PySide2.QtCore.QRectF, angle:float)\narcMoveTo(self, x:float, y:float, w:float, h:float, angle:float)'
        pass
    
    def arcTo(self, x: float, y: float, w: float, h: float, startAngle: float, arcLength: float):
        'arcTo(self, rect:PySide2.QtCore.QRectF, startAngle:float, arcLength:float)\narcTo(self, x:float, y:float, w:float, h:float, startAngle:float, arcLength:float)'
        pass
    
    def boundingRect(self):
        'boundingRect(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def capacity(self):
        'capacity(self) -> int'
        return int
    
    def clear(self):
        'clear(self)'
        pass
    
    def closeSubpath(self):
        'closeSubpath(self)'
        pass
    
    def connectPath(self, path):
        'connectPath(self, path:PySide2.QtGui.QPainterPath)'
        pass
    
    def contains(self, p: PySide2.QtGui.QPainterPath):
        'contains(self, p:PySide2.QtGui.QPainterPath) -> bool\ncontains(self, pt:PySide2.QtCore.QPointF) -> bool\ncontains(self, rect:PySide2.QtCore.QRectF) -> bool'
        return True
    
    def controlPointRect(self):
        'controlPointRect(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def cubicTo(self, ctrlPt1: PySide2.QtCore.QPointF, ctrlPt2: PySide2.QtCore.QPointF, endPt: PySide2.QtCore.QPointF):
        'cubicTo(self, ctrlPt1:PySide2.QtCore.QPointF, ctrlPt2:PySide2.QtCore.QPointF, endPt:PySide2.QtCore.QPointF)\ncubicTo(self, ctrlPt1x:float, ctrlPt1y:float, ctrlPt2x:float, ctrlPt2y:float, endPtx:float, endPty:float)'
        pass
    
    def currentPosition(self):
        'currentPosition(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def elementAt(self, i):
        'elementAt(self, i:int) -> PySide2.QtGui.QPainterPath.Element'
        return PySide2.QtGui.QPainterPath.Element
    
    def elementCount(self):
        'elementCount(self) -> int'
        return int
    
    def fillRule(self):
        'fillRule(self) -> PySide2.QtCore.Qt.FillRule'
        return PySide2.QtCore.Qt.FillRule
    
    def intersected(self, r):
        'intersected(self, r:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath'
        return PySide2.QtGui.QPainterPath
    
    def intersects(self, p: PySide2.QtGui.QPainterPath):
        'intersects(self, p:PySide2.QtGui.QPainterPath) -> bool\nintersects(self, rect:PySide2.QtCore.QRectF) -> bool'
        return True
    
    def isEmpty(self):
        'isEmpty(self) -> bool'
        return bool
    
    def length(self):
        'length(self) -> float'
        return float
    
    def lineTo(self, p: PySide2.QtCore.QPointF):
        'lineTo(self, p:PySide2.QtCore.QPointF)\nlineTo(self, x:float, y:float)'
        pass
    
    def moveTo(self, p: PySide2.QtCore.QPointF):
        'moveTo(self, p:PySide2.QtCore.QPointF)\nmoveTo(self, x:float, y:float)'
        pass
    
    def percentAtLength(self, t):
        'percentAtLength(self, t:float) -> float'
        return float
    
    def pointAtPercent(self, t):
        'pointAtPercent(self, t:float) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def quadTo(self, ctrlPt: PySide2.QtCore.QPointF, endPt: PySide2.QtCore.QPointF):
        'quadTo(self, ctrlPt:PySide2.QtCore.QPointF, endPt:PySide2.QtCore.QPointF)\nquadTo(self, ctrlPtx:float, ctrlPty:float, endPtx:float, endPty:float)'
        pass
    
    def reserve(self, size):
        'reserve(self, size:int)'
        pass
    
    def setElementPositionAt(self, i, x, y):
        'setElementPositionAt(self, i:int, x:float, y:float)'
        pass
    
    def setFillRule(self, fillRule):
        'setFillRule(self, fillRule:PySide2.QtCore.Qt.FillRule)'
        pass
    
    def simplified(self):
        'simplified(self) -> PySide2.QtGui.QPainterPath'
        return PySide2.QtGui.QPainterPath
    
    def slopeAtPercent(self, t):
        'slopeAtPercent(self, t:float) -> float'
        return float
    
    def subtracted(self, r):
        'subtracted(self, r:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath'
        return PySide2.QtGui.QPainterPath
    
    def subtractedInverted(self, r):
        'subtractedInverted(self, r:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath'
        return PySide2.QtGui.QPainterPath
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QPainterPath)'
        pass
    
    def toFillPolygon(self, matrix: PySide2.QtGui.QTransform=Default(QTransform)):
        'toFillPolygon(self, matrix:PySide2.QtGui.QMatrix) -> PySide2.QtGui.QPolygonF\ntoFillPolygon(self, matrix:PySide2.QtGui.QTransform=Default(QTransform)) -> PySide2.QtGui.QPolygonF'
        pass
    
    def toFillPolygons(self, matrix: PySide2.QtGui.QTransform=Default(QTransform)):
        'toFillPolygons(self, matrix:PySide2.QtGui.QMatrix) -> typing.List\ntoFillPolygons(self, matrix:PySide2.QtGui.QTransform=Default(QTransform)) -> typing.List'
        pass
    
    def toReversed(self):
        'toReversed(self) -> PySide2.QtGui.QPainterPath'
        return PySide2.QtGui.QPainterPath
    
    def toSubpathPolygons(self, matrix: PySide2.QtGui.QTransform=Default(QTransform)):
        'toSubpathPolygons(self, matrix:PySide2.QtGui.QMatrix) -> typing.List\ntoSubpathPolygons(self, matrix:PySide2.QtGui.QTransform=Default(QTransform)) -> typing.List'
        pass
    
    def translate(self, offset: PySide2.QtCore.QPointF):
        'translate(self, dx:float, dy:float)\ntranslate(self, offset:PySide2.QtCore.QPointF)'
        pass
    
    def translated(self, offset: PySide2.QtCore.QPointF):
        'translated(self, dx:float, dy:float) -> PySide2.QtGui.QPainterPath\ntranslated(self, offset:PySide2.QtCore.QPointF) -> PySide2.QtGui.QPainterPath'
        pass
    
    def united(self, r):
        'united(self, r:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath'
        return PySide2.QtGui.QPainterPath
    

class QPainterPathStroker(_mod_Shiboken.Object):
    'QPainterPathStroker(self)\nQPainterPathStroker(self, pen:PySide2.QtGui.QPen)'
    __class__ = QPainterPathStroker
    __dict__ = {}
    def __init__(self, pen: PySide2.QtGui.QPen):
        'QPainterPathStroker(self)\nQPainterPathStroker(self, pen:PySide2.QtGui.QPen)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def capStyle(self):
        'capStyle(self) -> PySide2.QtCore.Qt.PenCapStyle'
        return PySide2.QtCore.Qt.PenCapStyle
    
    def createStroke(self, path):
        'createStroke(self, path:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath'
        return PySide2.QtGui.QPainterPath
    
    def curveThreshold(self):
        'curveThreshold(self) -> float'
        return float
    
    def dashOffset(self):
        'dashOffset(self) -> float'
        return float
    
    def dashPattern(self):
        'dashPattern(self) -> typing.List'
        return typing.List
    
    def joinStyle(self):
        'joinStyle(self) -> PySide2.QtCore.Qt.PenJoinStyle'
        return PySide2.QtCore.Qt.PenJoinStyle
    
    def miterLimit(self):
        'miterLimit(self) -> float'
        return float
    
    def setCapStyle(self, style):
        'setCapStyle(self, style:PySide2.QtCore.Qt.PenCapStyle)'
        pass
    
    def setCurveThreshold(self, threshold):
        'setCurveThreshold(self, threshold:float)'
        pass
    
    def setDashOffset(self, offset):
        'setDashOffset(self, offset:float)'
        pass
    
    def setDashPattern(self, arg__1: PySide2.QtCore.Qt.PenStyle):
        'setDashPattern(self, arg__1:PySide2.QtCore.Qt.PenStyle)\nsetDashPattern(self, dashPattern:typing.List)'
        pass
    
    def setJoinStyle(self, style):
        'setJoinStyle(self, style:PySide2.QtCore.Qt.PenJoinStyle)'
        pass
    
    def setMiterLimit(self, length):
        'setMiterLimit(self, length:float)'
        pass
    
    def setWidth(self, width):
        'setWidth(self, width:float)'
        pass
    
    def width(self):
        'width(self) -> float'
        return float
    

class QPalette(_mod_Shiboken.Object):
    'QPalette(self)\nQPalette(self, button:PySide2.QtCore.Qt.GlobalColor)\nQPalette(self, button:PySide2.QtGui.QColor)\nQPalette(self, button:PySide2.QtGui.QColor, window:PySide2.QtGui.QColor)\nQPalette(self, palette:PySide2.QtGui.QPalette)\nQPalette(self, windowText:PySide2.QtGui.QBrush, button:PySide2.QtGui.QBrush, light:PySide2.QtGui.QBrush, dark:PySide2.QtGui.QBrush, mid:PySide2.QtGui.QBrush, text:PySide2.QtGui.QBrush, bright_text:PySide2.QtGui.QBrush, base:PySide2.QtGui.QBrush, window:PySide2.QtGui.QBrush)\nQPalette(self, windowText:PySide2.QtGui.QColor, window:PySide2.QtGui.QColor, light:PySide2.QtGui.QColor, dark:PySide2.QtGui.QColor, mid:PySide2.QtGui.QColor, text:PySide2.QtGui.QColor, base:PySide2.QtGui.QColor)'
    Active = ColorGroup()
    All = ColorGroup()
    AlternateBase = ColorRole()
    Background = ColorRole()
    Base = ColorRole()
    BrightText = ColorRole()
    Button = ColorRole()
    ButtonText = ColorRole()
    ColorGroup = ColorGroup
    ColorRole = ColorRole
    Current = ColorGroup()
    Dark = ColorRole()
    Disabled = ColorGroup()
    Foreground = ColorRole()
    Highlight = ColorRole()
    HighlightedText = ColorRole()
    Inactive = ColorGroup()
    Light = ColorRole()
    Link = ColorRole()
    LinkVisited = ColorRole()
    Mid = ColorRole()
    Midlight = ColorRole()
    NColorGroups = ColorGroup()
    NColorRoles = ColorRole()
    NoRole = ColorRole()
    Normal = ColorGroup()
    PlaceholderText = ColorRole()
    Shadow = ColorRole()
    Text = ColorRole()
    ToolTipBase = ColorRole()
    ToolTipText = ColorRole()
    Window = ColorRole()
    WindowText = ColorRole()
    __class__ = QPalette
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, windowText: PySide2.QtGui.QBrush, button: PySide2.QtGui.QBrush, light: PySide2.QtGui.QBrush, dark: PySide2.QtGui.QBrush, mid: PySide2.QtGui.QBrush, text: PySide2.QtGui.QBrush, bright_text: PySide2.QtGui.QBrush, base: PySide2.QtGui.QBrush, window: PySide2.QtGui.QBrush):
        'QPalette(self)\nQPalette(self, button:PySide2.QtCore.Qt.GlobalColor)\nQPalette(self, button:PySide2.QtGui.QColor)\nQPalette(self, button:PySide2.QtGui.QColor, window:PySide2.QtGui.QColor)\nQPalette(self, palette:PySide2.QtGui.QPalette)\nQPalette(self, windowText:PySide2.QtGui.QBrush, button:PySide2.QtGui.QBrush, light:PySide2.QtGui.QBrush, dark:PySide2.QtGui.QBrush, mid:PySide2.QtGui.QBrush, text:PySide2.QtGui.QBrush, bright_text:PySide2.QtGui.QBrush, base:PySide2.QtGui.QBrush, window:PySide2.QtGui.QBrush)\nQPalette(self, windowText:PySide2.QtGui.QColor, window:PySide2.QtGui.QColor, light:PySide2.QtGui.QColor, dark:PySide2.QtGui.QColor, mid:PySide2.QtGui.QColor, text:PySide2.QtGui.QColor, base:PySide2.QtGui.QColor)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, ds):
        '__lshift__(self, ds:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QPalette()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QPalette()
    
    def __rshift__(self, ds):
        '__rshift__(self, ds:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def alternateBase(self):
        'alternateBase(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def background(self):
        'background(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def base(self):
        'base(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def brightText(self):
        'brightText(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def brush(self, cg: PySide2.QtGui.QPalette.ColorGroup, cr: PySide2.QtGui.QPalette.ColorRole):
        'brush(self, cg:PySide2.QtGui.QPalette.ColorGroup, cr:PySide2.QtGui.QPalette.ColorRole) -> PySide2.QtGui.QBrush\nbrush(self, cr:PySide2.QtGui.QPalette.ColorRole) -> PySide2.QtGui.QBrush'
        pass
    
    def button(self):
        'button(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def buttonText(self):
        'buttonText(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def cacheKey(self):
        'cacheKey(self) -> int'
        return int
    
    def color(self, cg: PySide2.QtGui.QPalette.ColorGroup, cr: PySide2.QtGui.QPalette.ColorRole):
        'color(self, cg:PySide2.QtGui.QPalette.ColorGroup, cr:PySide2.QtGui.QPalette.ColorRole) -> PySide2.QtGui.QColor\ncolor(self, cr:PySide2.QtGui.QPalette.ColorRole) -> PySide2.QtGui.QColor'
        pass
    
    def currentColorGroup(self):
        'currentColorGroup(self) -> PySide2.QtGui.QPalette.ColorGroup'
        return PySide2.QtGui.QPalette.ColorGroup
    
    def dark(self):
        'dark(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def foreground(self):
        'foreground(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def highlight(self):
        'highlight(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def highlightedText(self):
        'highlightedText(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def isBrushSet(self, cg, cr):
        'isBrushSet(self, cg:PySide2.QtGui.QPalette.ColorGroup, cr:PySide2.QtGui.QPalette.ColorRole) -> bool'
        return bool
    
    def isCopyOf(self, p):
        'isCopyOf(self, p:PySide2.QtGui.QPalette) -> bool'
        return bool
    
    def isEqual(self, cr1, cr2):
        'isEqual(self, cr1:PySide2.QtGui.QPalette.ColorGroup, cr2:PySide2.QtGui.QPalette.ColorGroup) -> bool'
        return bool
    
    def light(self):
        'light(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def link(self):
        'link(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def linkVisited(self):
        'linkVisited(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def mid(self):
        'mid(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def midlight(self):
        'midlight(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def placeholderText(self):
        'placeholderText(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def resolve(self, arg__1: PySide2.QtGui.QPalette):
        'resolve(self) -> int\nresolve(self, arg__1:PySide2.QtGui.QPalette) -> PySide2.QtGui.QPalette\nresolve(self, mask:int)'
        return 1
    
    def setBrush(self, cg: PySide2.QtGui.QPalette.ColorGroup, cr: PySide2.QtGui.QPalette.ColorRole, brush: PySide2.QtGui.QBrush):
        'setBrush(self, cg:PySide2.QtGui.QPalette.ColorGroup, cr:PySide2.QtGui.QPalette.ColorRole, brush:PySide2.QtGui.QBrush)\nsetBrush(self, cr:PySide2.QtGui.QPalette.ColorRole, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setColor(self, cg: PySide2.QtGui.QPalette.ColorGroup, cr: PySide2.QtGui.QPalette.ColorRole, color: PySide2.QtGui.QColor):
        'setColor(self, cg:PySide2.QtGui.QPalette.ColorGroup, cr:PySide2.QtGui.QPalette.ColorRole, color:PySide2.QtGui.QColor)\nsetColor(self, cr:PySide2.QtGui.QPalette.ColorRole, color:PySide2.QtGui.QColor)'
        pass
    
    def setColorGroup(self, cr, windowText, button, light, dark, mid, text, bright_text, base, window):
        'setColorGroup(self, cr:PySide2.QtGui.QPalette.ColorGroup, windowText:PySide2.QtGui.QBrush, button:PySide2.QtGui.QBrush, light:PySide2.QtGui.QBrush, dark:PySide2.QtGui.QBrush, mid:PySide2.QtGui.QBrush, text:PySide2.QtGui.QBrush, bright_text:PySide2.QtGui.QBrush, base:PySide2.QtGui.QBrush, window:PySide2.QtGui.QBrush)'
        pass
    
    def setCurrentColorGroup(self, cg):
        'setCurrentColorGroup(self, cg:PySide2.QtGui.QPalette.ColorGroup)'
        pass
    
    def shadow(self):
        'shadow(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QPalette)'
        pass
    
    def text(self):
        'text(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def toolTipBase(self):
        'toolTipBase(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def toolTipText(self):
        'toolTipText(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def window(self):
        'window(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def windowText(self):
        'windowText(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    

class QPdfWriter(_mod_PySide2_QtCore.QObject,QPagedPaintDevice):
    'QPdfWriter(self, device:PySide2.QtCore.QIODevice)\nQPdfWriter(self, filename:str)'
    __class__ = QPdfWriter
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, device: PySide2.QtCore.QIODevice):
        'QPdfWriter(self, device:PySide2.QtCore.QIODevice)\nQPdfWriter(self, filename:str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addFileAttachment(self, fileName, data, mimeType):
        "addFileAttachment(self, fileName:str, data:PySide2.QtCore.QByteArray, mimeType:str='')"
        pass
    
    def creator(self):
        'creator(self) -> str'
        return str
    
    def documentXmpMetadata(self):
        'documentXmpMetadata(self) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    def metric(self, id):
        'metric(self, id:PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int'
        return int
    
    def newPage(self):
        'newPage(self) -> bool'
        return bool
    
    def paintEngine(self):
        'paintEngine(self) -> PySide2.QtGui.QPaintEngine'
        return PySide2.QtGui.QPaintEngine
    
    def pdfVersion(self):
        'pdfVersion(self) -> PySide2.QtGui.QPagedPaintDevice.PdfVersion'
        return PySide2.QtGui.QPagedPaintDevice.PdfVersion
    
    def resolution(self):
        'resolution(self) -> int'
        return int
    
    def setCreator(self, creator):
        'setCreator(self, creator:str)'
        pass
    
    def setDocumentXmpMetadata(self, xmpMetadata):
        'setDocumentXmpMetadata(self, xmpMetadata:PySide2.QtCore.QByteArray)'
        pass
    
    def setMargins(self, m):
        'setMargins(self, m:PySide2.QtGui.QPagedPaintDevice.Margins)'
        pass
    
    def setPageSize(self, size):
        'setPageSize(self, size:PySide2.QtGui.QPagedPaintDevice.PageSize)'
        pass
    
    def setPageSizeMM(self, size):
        'setPageSizeMM(self, size:PySide2.QtCore.QSizeF)'
        pass
    
    def setPdfVersion(self, version):
        'setPdfVersion(self, version:PySide2.QtGui.QPagedPaintDevice.PdfVersion)'
        pass
    
    def setResolution(self, resolution):
        'setResolution(self, resolution:int)'
        pass
    
    def setTitle(self, title):
        'setTitle(self, title:str)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def title(self):
        'title(self) -> str'
        return str
    

class QPen(_mod_Shiboken.Object):
    'QPen(self)\nQPen(self, arg__1:PySide2.QtCore.Qt.PenStyle)\nQPen(self, brush:PySide2.QtGui.QBrush, width:float, s:PySide2.QtCore.Qt.PenStyle=PySide2.QtCore.Qt.PenStyle.SolidLine, c:PySide2.QtCore.Qt.PenCapStyle=PySide2.QtCore.Qt.PenCapStyle.SquareCap, j:PySide2.QtCore.Qt.PenJoinStyle=PySide2.QtCore.Qt.PenJoinStyle.BevelJoin)\nQPen(self, color:PySide2.QtGui.QColor)\nQPen(self, pen:PySide2.QtGui.QPen)'
    __class__ = QPen
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, brush: PySide2.QtGui.QBrush, width: float, s: PySide2.QtCore.Qt.PenStyle=PySide2.QtCore.Qt.PenStyle.SolidLine, c: PySide2.QtCore.Qt.PenCapStyle=PySide2.QtCore.Qt.PenCapStyle.SquareCap, j: PySide2.QtCore.Qt.PenJoinStyle=PySide2.QtCore.Qt.PenJoinStyle.BevelJoin):
        'QPen(self)\nQPen(self, arg__1:PySide2.QtCore.Qt.PenStyle)\nQPen(self, brush:PySide2.QtGui.QBrush, width:float, s:PySide2.QtCore.Qt.PenStyle=PySide2.QtCore.Qt.PenStyle.SolidLine, c:PySide2.QtCore.Qt.PenCapStyle=PySide2.QtCore.Qt.PenCapStyle.SquareCap, j:PySide2.QtCore.Qt.PenJoinStyle=PySide2.QtCore.Qt.PenJoinStyle.BevelJoin)\nQPen(self, color:PySide2.QtGui.QColor)\nQPen(self, pen:PySide2.QtGui.QPen)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QPen()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QPen()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def brush(self):
        'brush(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def capStyle(self):
        'capStyle(self) -> PySide2.QtCore.Qt.PenCapStyle'
        return PySide2.QtCore.Qt.PenCapStyle
    
    def color(self):
        'color(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def dashOffset(self):
        'dashOffset(self) -> float'
        return float
    
    def dashPattern(self):
        'dashPattern(self) -> typing.List'
        return typing.List
    
    def isCosmetic(self):
        'isCosmetic(self) -> bool'
        return bool
    
    def isSolid(self):
        'isSolid(self) -> bool'
        return bool
    
    def joinStyle(self):
        'joinStyle(self) -> PySide2.QtCore.Qt.PenJoinStyle'
        return PySide2.QtCore.Qt.PenJoinStyle
    
    def miterLimit(self):
        'miterLimit(self) -> float'
        return float
    
    def setBrush(self, brush):
        'setBrush(self, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setCapStyle(self, pcs):
        'setCapStyle(self, pcs:PySide2.QtCore.Qt.PenCapStyle)'
        pass
    
    def setColor(self, color):
        'setColor(self, color:PySide2.QtGui.QColor)'
        pass
    
    def setCosmetic(self, cosmetic):
        'setCosmetic(self, cosmetic:bool)'
        pass
    
    def setDashOffset(self, doffset):
        'setDashOffset(self, doffset:float)'
        pass
    
    def setDashPattern(self, pattern):
        'setDashPattern(self, pattern:typing.List)'
        pass
    
    def setJoinStyle(self, pcs):
        'setJoinStyle(self, pcs:PySide2.QtCore.Qt.PenJoinStyle)'
        pass
    
    def setMiterLimit(self, limit):
        'setMiterLimit(self, limit:float)'
        pass
    
    def setStyle(self, arg__1):
        'setStyle(self, arg__1:PySide2.QtCore.Qt.PenStyle)'
        pass
    
    def setWidth(self, width):
        'setWidth(self, width:int)'
        pass
    
    def setWidthF(self, width):
        'setWidthF(self, width:float)'
        pass
    
    def style(self):
        'style(self) -> PySide2.QtCore.Qt.PenStyle'
        return PySide2.QtCore.Qt.PenStyle
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QPen)'
        pass
    
    def width(self):
        'width(self) -> int'
        return int
    
    def widthF(self):
        'widthF(self) -> float'
        return float
    

class QPicture(QPaintDevice):
    'QPicture(self, arg__1:PySide2.QtGui.QPicture)\nQPicture(self, formatVersion:int=-1)'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QPicture
    def __copy__(self):
        '__copy__()'
        pass
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, arg__1: PySide2.QtGui.QPicture):
        'QPicture(self, arg__1:PySide2.QtGui.QPicture)\nQPicture(self, formatVersion:int=-1)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    __module__ = 'PySide2.QtGui'
    def __rlshift__(self, value):
        'Return value<<self.'
        return QPicture()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QPicture()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def boundingRect(self):
        'boundingRect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def data(self):
        'data(self) -> bytes'
        return bytes
    
    def devType(self):
        'devType(self) -> int'
        return int
    
    @classmethod
    def inputFormatList(cls):
        'inputFormatList() -> typing.List'
        return typing.List
    
    @classmethod
    def inputFormats(cls):
        'inputFormats() -> typing.List'
        return typing.List
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def load(self, dev: PySide2.QtCore.QIODevice, format: typing.Union[bytes,NoneType]=None):
        'load(self, dev:PySide2.QtCore.QIODevice, format:typing.Union[bytes, NoneType]=None) -> bool\nload(self, fileName:str, format:typing.Union[bytes, NoneType]=None) -> bool'
        return True
    
    def metric(self, m):
        'metric(self, m:PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int'
        return int
    
    @classmethod
    def outputFormatList(cls):
        'outputFormatList() -> typing.List'
        return typing.List
    
    @classmethod
    def outputFormats(cls):
        'outputFormats() -> typing.List'
        return typing.List
    
    def paintEngine(self):
        'paintEngine(self) -> PySide2.QtGui.QPaintEngine'
        return PySide2.QtGui.QPaintEngine
    
    @classmethod
    def pictureFormat(cls, fileName):
        'pictureFormat(fileName:str) -> bytes'
        return bytes
    
    def play(self, p):
        'play(self, p:PySide2.QtGui.QPainter) -> bool'
        return bool
    
    def save(self, dev: PySide2.QtCore.QIODevice, format: typing.Union[bytes,NoneType]=None):
        'save(self, dev:PySide2.QtCore.QIODevice, format:typing.Union[bytes, NoneType]=None) -> bool\nsave(self, fileName:str, format:typing.Union[bytes, NoneType]=None) -> bool'
        return True
    
    def setBoundingRect(self, r):
        'setBoundingRect(self, r:PySide2.QtCore.QRect)'
        pass
    
    def setData(self, data, size):
        'setData(self, data:bytes, size:int)'
        pass
    
    def size(self):
        'size(self) -> int'
        return int
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QPicture)'
        pass
    

class QPictureIO(_mod_Shiboken.Object):
    'QPictureIO(self)\nQPictureIO(self, fileName:str, format:bytes)\nQPictureIO(self, ioDevice:PySide2.QtCore.QIODevice, format:bytes)'
    __class__ = QPictureIO
    __dict__ = {}
    def __init__(self, ioDevice: PySide2.QtCore.QIODevice, format: bytes):
        'QPictureIO(self)\nQPictureIO(self, fileName:str, format:bytes)\nQPictureIO(self, ioDevice:PySide2.QtCore.QIODevice, format:bytes)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def description(self):
        'description(self) -> str'
        return str
    
    def fileName(self):
        'fileName(self) -> str'
        return str
    
    def format(self):
        'format(self) -> bytes'
        return bytes
    
    def gamma(self):
        'gamma(self) -> float'
        return float
    
    @classmethod
    def inputFormats(cls):
        'inputFormats() -> typing.List'
        return typing.List
    
    def ioDevice(self):
        'ioDevice(self) -> PySide2.QtCore.QIODevice'
        return PySide2.QtCore.QIODevice
    
    @classmethod
    def outputFormats(cls):
        'outputFormats() -> typing.List'
        return typing.List
    
    def parameters(self):
        'parameters(self) -> bytes'
        return bytes
    
    def picture(self):
        'picture(self) -> PySide2.QtGui.QPicture'
        return PySide2.QtGui.QPicture
    
    @classmethod
    def pictureFormat(cls, arg__1: PySide2.QtCore.QIODevice):
        'pictureFormat(arg__1:PySide2.QtCore.QIODevice) -> PySide2.QtCore.QByteArray\npictureFormat(fileName:str) -> PySide2.QtCore.QByteArray'
        pass
    
    def quality(self):
        'quality(self) -> int'
        return int
    
    def read(self):
        'read(self) -> bool'
        return bool
    
    def setDescription(self, arg__1):
        'setDescription(self, arg__1:str)'
        pass
    
    def setFileName(self, arg__1):
        'setFileName(self, arg__1:str)'
        pass
    
    def setFormat(self, arg__1):
        'setFormat(self, arg__1:bytes)'
        pass
    
    def setGamma(self, arg__1):
        'setGamma(self, arg__1:float)'
        pass
    
    def setIODevice(self, arg__1):
        'setIODevice(self, arg__1:PySide2.QtCore.QIODevice)'
        pass
    
    def setParameters(self, arg__1):
        'setParameters(self, arg__1:bytes)'
        pass
    
    def setPicture(self, arg__1):
        'setPicture(self, arg__1:PySide2.QtGui.QPicture)'
        pass
    
    def setQuality(self, arg__1):
        'setQuality(self, arg__1:int)'
        pass
    
    def setStatus(self, arg__1):
        'setStatus(self, arg__1:int)'
        pass
    
    def status(self):
        'status(self) -> int'
        return int
    
    def write(self):
        'write(self) -> bool'
        return bool
    

class QPixelFormat(_mod_Shiboken.Object):
    'QPixelFormat(self)\nQPixelFormat(self, QPixelFormat:PySide2.QtGui.QPixelFormat)\nQPixelFormat(self, colorModel:PySide2.QtGui.QPixelFormat.ColorModel, firstSize:int, secondSize:int, thirdSize:int, fourthSize:int, fifthSize:int, alphaSize:int, alphaUsage:PySide2.QtGui.QPixelFormat.AlphaUsage, alphaPosition:PySide2.QtGui.QPixelFormat.AlphaPosition, premultiplied:PySide2.QtGui.QPixelFormat.AlphaPremultiplied, typeInterpretation:PySide2.QtGui.QPixelFormat.TypeInterpretation, byteOrder:PySide2.QtGui.QPixelFormat.ByteOrder=PySide2.QtGui.QPixelFormat.ByteOrder.CurrentSystemEndian, subEnum:int=0)'
    Alpha = ColorModel()
    AlphaPosition = AlphaPosition
    AlphaPremultiplied = AlphaPremultiplied
    AlphaUsage = AlphaUsage
    AtBeginning = AlphaPosition()
    AtEnd = AlphaPosition()
    BGR = ColorModel()
    BigEndian = ByteOrder()
    ByteOrder = ByteOrder
    CMYK = ColorModel()
    ColorModel = ColorModel
    CurrentSystemEndian = ByteOrder()
    FloatingPoint = TypeInterpretation()
    Grayscale = ColorModel()
    HSL = ColorModel()
    HSV = ColorModel()
    IMC1 = YUVLayout()
    IMC2 = YUVLayout()
    IMC3 = YUVLayout()
    IMC4 = YUVLayout()
    IgnoresAlpha = AlphaUsage()
    Indexed = ColorModel()
    LittleEndian = ByteOrder()
    NV12 = YUVLayout()
    NV21 = YUVLayout()
    NotPremultiplied = AlphaPremultiplied()
    Premultiplied = AlphaPremultiplied()
    RGB = ColorModel()
    TypeInterpretation = TypeInterpretation
    UYVY = YUVLayout()
    UnsignedByte = TypeInterpretation()
    UnsignedInteger = TypeInterpretation()
    UnsignedShort = TypeInterpretation()
    UsesAlpha = AlphaUsage()
    Y16 = YUVLayout()
    Y8 = YUVLayout()
    YUV = ColorModel()
    YUV411 = YUVLayout()
    YUV420P = YUVLayout()
    YUV420SP = YUVLayout()
    YUV422 = YUVLayout()
    YUV444 = YUVLayout()
    YUVLayout = YUVLayout
    YUYV = YUVLayout()
    YV12 = YUVLayout()
    __class__ = QPixelFormat
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, colorModel: PySide2.QtGui.QPixelFormat.ColorModel, firstSize: int, secondSize: int, thirdSize: int, fourthSize: int, fifthSize: int, alphaSize: int, alphaUsage: PySide2.QtGui.QPixelFormat.AlphaUsage, alphaPosition: PySide2.QtGui.QPixelFormat.AlphaPosition, premultiplied: PySide2.QtGui.QPixelFormat.AlphaPremultiplied, typeInterpretation: PySide2.QtGui.QPixelFormat.TypeInterpretation, byteOrder: PySide2.QtGui.QPixelFormat.ByteOrder=PySide2.QtGui.QPixelFormat.ByteOrder.CurrentSystemEndian, subEnum: int=0):
        'QPixelFormat(self)\nQPixelFormat(self, QPixelFormat:PySide2.QtGui.QPixelFormat)\nQPixelFormat(self, colorModel:PySide2.QtGui.QPixelFormat.ColorModel, firstSize:int, secondSize:int, thirdSize:int, fourthSize:int, fifthSize:int, alphaSize:int, alphaUsage:PySide2.QtGui.QPixelFormat.AlphaUsage, alphaPosition:PySide2.QtGui.QPixelFormat.AlphaPosition, premultiplied:PySide2.QtGui.QPixelFormat.AlphaPremultiplied, typeInterpretation:PySide2.QtGui.QPixelFormat.TypeInterpretation, byteOrder:PySide2.QtGui.QPixelFormat.ByteOrder=PySide2.QtGui.QPixelFormat.ByteOrder.CurrentSystemEndian, subEnum:int=0)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def alphaPosition(self):
        'alphaPosition(self) -> PySide2.QtGui.QPixelFormat.AlphaPosition'
        return PySide2.QtGui.QPixelFormat.AlphaPosition
    
    def alphaSize(self):
        'alphaSize(self) -> int'
        return int
    
    def alphaUsage(self):
        'alphaUsage(self) -> PySide2.QtGui.QPixelFormat.AlphaUsage'
        return PySide2.QtGui.QPixelFormat.AlphaUsage
    
    def bitsPerPixel(self):
        'bitsPerPixel(self) -> int'
        return int
    
    def blackSize(self):
        'blackSize(self) -> int'
        return int
    
    def blueSize(self):
        'blueSize(self) -> int'
        return int
    
    def brightnessSize(self):
        'brightnessSize(self) -> int'
        return int
    
    def byteOrder(self):
        'byteOrder(self) -> PySide2.QtGui.QPixelFormat.ByteOrder'
        return PySide2.QtGui.QPixelFormat.ByteOrder
    
    def channelCount(self):
        'channelCount(self) -> int'
        return int
    
    def colorModel(self):
        'colorModel(self) -> PySide2.QtGui.QPixelFormat.ColorModel'
        return PySide2.QtGui.QPixelFormat.ColorModel
    
    def cyanSize(self):
        'cyanSize(self) -> int'
        return int
    
    def greenSize(self):
        'greenSize(self) -> int'
        return int
    
    def hueSize(self):
        'hueSize(self) -> int'
        return int
    
    def lightnessSize(self):
        'lightnessSize(self) -> int'
        return int
    
    def magentaSize(self):
        'magentaSize(self) -> int'
        return int
    
    def premultiplied(self):
        'premultiplied(self) -> PySide2.QtGui.QPixelFormat.AlphaPremultiplied'
        return PySide2.QtGui.QPixelFormat.AlphaPremultiplied
    
    def redSize(self):
        'redSize(self) -> int'
        return int
    
    def saturationSize(self):
        'saturationSize(self) -> int'
        return int
    
    def subEnum(self):
        'subEnum(self) -> int'
        return int
    
    def typeInterpretation(self):
        'typeInterpretation(self) -> PySide2.QtGui.QPixelFormat.TypeInterpretation'
        return PySide2.QtGui.QPixelFormat.TypeInterpretation
    
    def yellowSize(self):
        'yellowSize(self) -> int'
        return int
    
    def yuvLayout(self):
        'yuvLayout(self) -> PySide2.QtGui.QPixelFormat.YUVLayout'
        return PySide2.QtGui.QPixelFormat.YUVLayout
    

class QPixmap(QPaintDevice):
    'QPixmap(self)\nQPixmap(self, arg__1:PySide2.QtCore.QSize)\nQPixmap(self, arg__1:PySide2.QtGui.QPixmap)\nQPixmap(self, fileName:str, format:typing.Union[bytes, NoneType]=None, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor)\nQPixmap(self, image:PySide2.QtGui.QImage)\nQPixmap(self, w:int, h:int)\nQPixmap(self, xpm:typing.Sequence)'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QPixmap
    def __copy__(self):
        '__copy__()'
        pass
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, fileName: str, format: typing.Union[bytes,NoneType]=None, flags: PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor):
        'QPixmap(self)\nQPixmap(self, arg__1:PySide2.QtCore.QSize)\nQPixmap(self, arg__1:PySide2.QtGui.QPixmap)\nQPixmap(self, fileName:str, format:typing.Union[bytes, NoneType]=None, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor)\nQPixmap(self, image:PySide2.QtGui.QImage)\nQPixmap(self, w:int, h:int)\nQPixmap(self, xpm:typing.Sequence)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    __module__ = 'PySide2.QtGui'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QPixmap()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QPixmap()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def cacheKey(self):
        'cacheKey(self) -> int'
        return int
    
    def convertFromImage(self, img, flags):
        'convertFromImage(self, img:PySide2.QtGui.QImage, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> bool'
        return bool
    
    def copy(self, rect: PySide2.QtCore.QRect=Default(QRect)):
        'copy(self, rect:PySide2.QtCore.QRect=Default(QRect)) -> PySide2.QtGui.QPixmap\ncopy(self, x:int, y:int, width:int, height:int) -> PySide2.QtGui.QPixmap'
        pass
    
    def createHeuristicMask(self, clipTight):
        'createHeuristicMask(self, clipTight:bool=True) -> PySide2.QtGui.QBitmap'
        return PySide2.QtGui.QBitmap
    
    def createMaskFromColor(self, maskColor, mode):
        'createMaskFromColor(self, maskColor:PySide2.QtGui.QColor, mode:PySide2.QtCore.Qt.MaskMode=PySide2.QtCore.Qt.MaskMode.MaskInColor) -> PySide2.QtGui.QBitmap'
        return PySide2.QtGui.QBitmap
    
    @classmethod
    def defaultDepth(cls):
        'defaultDepth() -> int'
        return int
    
    def depth(self):
        'depth(self) -> int'
        return int
    
    def devType(self):
        'devType(self) -> int'
        return int
    
    def devicePixelRatio(self):
        'devicePixelRatio(self) -> float'
        return float
    
    def fill(self, fillColor: PySide2.QtGui.QColor=PySide2.QtCore.Qt.GlobalColor.white):
        'fill(self, device:PySide2.QtGui.QPaintDevice, ofs:PySide2.QtCore.QPoint)\nfill(self, device:PySide2.QtGui.QPaintDevice, xofs:int, yofs:int)\nfill(self, fillColor:PySide2.QtGui.QColor=PySide2.QtCore.Qt.GlobalColor.white)'
        pass
    
    @classmethod
    def fromImage(cls, image, flags):
        'fromImage(image:PySide2.QtGui.QImage, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    @classmethod
    def fromImageInPlace(cls, image, flags):
        'fromImageInPlace(image:PySide2.QtGui.QImage, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    @classmethod
    def fromImageReader(cls, imageReader, flags):
        'fromImageReader(imageReader:PySide2.QtGui.QImageReader, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    @classmethod
    def grabWidget(cls, widget: PySide2.QtCore.QObject, x: int=0, y: int=0, w: int=-1, h: int=-1):
        'grabWidget(widget:PySide2.QtCore.QObject, rect:PySide2.QtCore.QRect) -> PySide2.QtGui.QPixmap\ngrabWidget(widget:PySide2.QtCore.QObject, x:int=0, y:int=0, w:int=-1, h:int=-1) -> PySide2.QtGui.QPixmap'
        pass
    
    @classmethod
    def grabWindow(cls, arg__1, x, y, w, h):
        'grabWindow(arg__1:int, x:int=0, y:int=0, w:int=-1, h:int=-1) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    def hasAlpha(self):
        'hasAlpha(self) -> bool'
        return bool
    
    def hasAlphaChannel(self):
        'hasAlphaChannel(self) -> bool'
        return bool
    
    def height(self):
        'height(self) -> int'
        return int
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def isQBitmap(self):
        'isQBitmap(self) -> bool'
        return bool
    
    def load(self, fileName, format, flags):
        'load(self, fileName:str, format:typing.Union[bytes, NoneType]=None, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> bool'
        return bool
    
    def loadFromData(self, data: PySide2.QtCore.QByteArray, format: typing.Union[bytes,NoneType]=None, flags: PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor):
        'loadFromData(self, buf:bytes, len:int, format:typing.Union[bytes, NoneType]=None, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> bool\nloadFromData(self, data:PySide2.QtCore.QByteArray, format:typing.Union[bytes, NoneType]=None, flags:PySide2.QtCore.Qt.ImageConversionFlags=PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> bool'
        return True
    
    def mask(self):
        'mask(self) -> PySide2.QtGui.QBitmap'
        return PySide2.QtGui.QBitmap
    
    def metric(self, arg__1):
        'metric(self, arg__1:PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int'
        return int
    
    def paintEngine(self):
        'paintEngine(self) -> PySide2.QtGui.QPaintEngine'
        return PySide2.QtGui.QPaintEngine
    
    def rect(self):
        'rect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def save(self, device: PySide2.QtCore.QIODevice, format: typing.Union[bytes,NoneType]=None, quality: int=-1):
        'save(self, device:PySide2.QtCore.QIODevice, format:typing.Union[bytes, NoneType]=None, quality:int=-1) -> bool\nsave(self, fileName:str, format:typing.Union[bytes, NoneType]=None, quality:int=-1) -> bool'
        return True
    
    def scaled(self, s: PySide2.QtCore.QSize, aspectMode: PySide2.QtCore.Qt.AspectRatioMode=PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, mode: PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation):
        'scaled(self, s:PySide2.QtCore.QSize, aspectMode:PySide2.QtCore.Qt.AspectRatioMode=PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap\nscaled(self, w:int, h:int, aspectMode:PySide2.QtCore.Qt.AspectRatioMode=PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap'
        pass
    
    def scaledToHeight(self, h, mode):
        'scaledToHeight(self, h:int, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    def scaledToWidth(self, w, mode):
        'scaledToWidth(self, w:int, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    def scroll(self, dx: int, dy: int, x: int, y: int, width: int, height: int, exposed: typing.Union[PySide2.QtGui.QRegion,NoneType]=None):
        'scroll(self, dx:int, dy:int, rect:PySide2.QtCore.QRect, exposed:typing.Union[PySide2.QtGui.QRegion, NoneType]=None)\nscroll(self, dx:int, dy:int, x:int, y:int, width:int, height:int, exposed:typing.Union[PySide2.QtGui.QRegion, NoneType]=None)'
        pass
    
    def setDevicePixelRatio(self, scaleFactor):
        'setDevicePixelRatio(self, scaleFactor:float)'
        pass
    
    def setMask(self, arg__1):
        'setMask(self, arg__1:PySide2.QtGui.QBitmap)'
        pass
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QPixmap)'
        pass
    
    def toImage(self):
        'toImage(self) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def transformed(self, arg__1: PySide2.QtGui.QTransform, mode: PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation):
        'transformed(self, arg__1:PySide2.QtGui.QMatrix, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap\ntransformed(self, arg__1:PySide2.QtGui.QTransform, mode:PySide2.QtCore.Qt.TransformationMode=PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap'
        pass
    
    @classmethod
    def trueMatrix(cls, m: PySide2.QtGui.QTransform, w: int, h: int):
        'trueMatrix(m:PySide2.QtGui.QMatrix, w:int, h:int) -> PySide2.QtGui.QMatrix\ntrueMatrix(m:PySide2.QtGui.QTransform, w:int, h:int) -> PySide2.QtGui.QTransform'
        pass
    
    def width(self):
        'width(self) -> int'
        return int
    

class QPixmapCache(_mod_Shiboken.Object):
    'QPixmapCache(self)'
    Key = Key
    __class__ = QPixmapCache
    __dict__ = {}
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self):
        'QPixmapCache(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def cacheLimit(cls):
        'cacheLimit() -> int'
        return int
    
    @classmethod
    def clear(cls):
        'clear()'
        pass
    
    @classmethod
    def find(cls, key: PySide2.QtGui.QPixmapCache.Key, pixmap: PySide2.QtGui.QPixmap):
        'find(key:PySide2.QtGui.QPixmapCache.Key, pixmap:PySide2.QtGui.QPixmap) -> bool\nfind(key:str) -> PySide2.QtGui.QPixmap\nfind(key:str, pixmap:PySide2.QtGui.QPixmap) -> bool\nfind(self, arg__1:PySide2.QtGui.QPixmapCache.Key)'
        return True
    
    @classmethod
    def insert(cls, key: str, pixmap: PySide2.QtGui.QPixmap):
        'insert(key:str, pixmap:PySide2.QtGui.QPixmap) -> bool\ninsert(pixmap:PySide2.QtGui.QPixmap) -> PySide2.QtGui.QPixmapCache.Key'
        return True
    
    @classmethod
    def remove(cls, key: PySide2.QtGui.QPixmapCache.Key):
        'remove(key:PySide2.QtGui.QPixmapCache.Key)\nremove(key:str)'
        pass
    
    @classmethod
    def replace(cls, key, pixmap):
        'replace(key:PySide2.QtGui.QPixmapCache.Key, pixmap:PySide2.QtGui.QPixmap) -> bool'
        return bool
    
    @classmethod
    def setCacheLimit(cls, arg__1):
        'setCacheLimit(arg__1:int)'
        pass
    

class QPointingDeviceUniqueId(_mod_Shiboken.Object):
    'QPointingDeviceUniqueId(self)\nQPointingDeviceUniqueId(self, QPointingDeviceUniqueId:PySide2.QtGui.QPointingDeviceUniqueId)'
    __class__ = QPointingDeviceUniqueId
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, QPointingDeviceUniqueId: PySide2.QtGui.QPointingDeviceUniqueId):
        'QPointingDeviceUniqueId(self)\nQPointingDeviceUniqueId(self, QPointingDeviceUniqueId:PySide2.QtGui.QPointingDeviceUniqueId)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def fromNumericId(cls, id):
        'fromNumericId(id:int) -> PySide2.QtGui.QPointingDeviceUniqueId'
        return PySide2.QtGui.QPointingDeviceUniqueId
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def numericId(self):
        'numericId(self) -> int'
        return int
    

class QPolygon(_mod_Shiboken.Object):
    'QPolygon(self)\nQPolygon(self, other:PySide2.QtGui.QPolygon)\nQPolygon(self, r:PySide2.QtCore.QRect, closed:bool=False)\nQPolygon(self, size:int)\nQPolygon(self, v:typing.List)'
    def __add__(self, l):
        '__add__(self, l:typing.List) -> typing.List\n\nReturn self+value.'
        return typing.List
    
    __class__ = QPolygon
    def __copy__(self):
        '__copy__()'
        pass
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, t):
        '__iadd__(self, t:PySide2.QtCore.QPoint) -> typing.List\n\nReturn self+=value.'
        return typing.List
    
    def __init__(self, r: PySide2.QtCore.QRect, closed: bool=False):
        'QPolygon(self)\nQPolygon(self, other:PySide2.QtGui.QPolygon)\nQPolygon(self, r:PySide2.QtCore.QRect, closed:bool=False)\nQPolygon(self, size:int)\nQPolygon(self, v:typing.List)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lshift__(self, stream: PySide2.QtCore.QDataStream):
        '__lshift__(self, l:typing.List) -> typing.List\n__lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n__lshift__(self, t:PySide2.QtCore.QPoint) -> typing.List\n\nReturn self<<value.'
        return QPolygon()
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __mul__(self, m: PySide2.QtGui.QTransform):
        '__mul__(self, m:PySide2.QtGui.QMatrix) -> PySide2.QtGui.QPolygon\n__mul__(self, m:PySide2.QtGui.QTransform) -> PySide2.QtGui.QPolygon\n\nReturn self*value.'
        return QPolygon()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __radd__(self, value):
        'Return value+self.'
        return QPolygon()
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QPolygon()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QPolygon()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QPolygon()
    
    def __rshift__(self, stream):
        '__rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def append(self, t: PySide2.QtCore.QPoint):
        'append(self, l:typing.List)\nappend(self, t:PySide2.QtCore.QPoint)'
        pass
    
    def at(self, i):
        'at(self, i:int) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def back(self):
        'back(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def boundingRect(self):
        'boundingRect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def capacity(self):
        'capacity(self) -> int'
        return int
    
    def clear(self):
        'clear(self)'
        pass
    
    def constData(self):
        'constData(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def constFirst(self):
        'constFirst(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def constLast(self):
        'constLast(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def contains(self, t):
        'contains(self, t:PySide2.QtCore.QPoint) -> bool'
        return bool
    
    def containsPoint(self, pt, fillRule):
        'containsPoint(self, pt:PySide2.QtCore.QPoint, fillRule:PySide2.QtCore.Qt.FillRule) -> bool'
        return bool
    
    def count(self, t: PySide2.QtCore.QPoint):
        'count(self) -> int\ncount(self, t:PySide2.QtCore.QPoint) -> int'
        return 1
    
    def data(self):
        'data(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def empty(self):
        'empty(self) -> bool'
        return bool
    
    def endsWith(self, t):
        'endsWith(self, t:PySide2.QtCore.QPoint) -> bool'
        return bool
    
    def fill(self, t, size):
        'fill(self, t:PySide2.QtCore.QPoint, size:int=-1) -> typing.List'
        return typing.List
    
    def first(self):
        'first(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    @classmethod
    def fromList(cls, list):
        'fromList(list:typing.Sequence) -> typing.List'
        return typing.List
    
    def front(self):
        'front(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def indexOf(self, t, from_):
        'indexOf(self, t:PySide2.QtCore.QPoint, from_:int=0) -> int'
        return int
    
    def insert(self, i: int, n: int, t: PySide2.QtCore.QPoint):
        'insert(self, i:int, n:int, t:PySide2.QtCore.QPoint)\ninsert(self, i:int, t:PySide2.QtCore.QPoint)'
        pass
    
    def intersected(self, r):
        'intersected(self, r:PySide2.QtGui.QPolygon) -> PySide2.QtGui.QPolygon'
        return PySide2.QtGui.QPolygon
    
    def intersects(self, r):
        'intersects(self, r:PySide2.QtGui.QPolygon) -> bool'
        return bool
    
    def isEmpty(self):
        'isEmpty(self) -> bool'
        return bool
    
    def isSharedWith(self, other):
        'isSharedWith(self, other:typing.List) -> bool'
        return bool
    
    def last(self):
        'last(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def lastIndexOf(self, t, from_):
        'lastIndexOf(self, t:PySide2.QtCore.QPoint, from_:int=-1) -> int'
        return int
    
    def length(self):
        'length(self) -> int'
        return int
    
    def mid(self, pos, len):
        'mid(self, pos:int, len:int=-1) -> typing.List'
        return typing.List
    
    def move(self, from_, to):
        'move(self, from_:int, to:int)'
        pass
    
    def pop_back(self):
        'pop_back(self)'
        pass
    
    def pop_front(self):
        'pop_front(self)'
        pass
    
    def prepend(self, t):
        'prepend(self, t:PySide2.QtCore.QPoint)'
        pass
    
    def push_back(self, t):
        'push_back(self, t:PySide2.QtCore.QPoint)'
        pass
    
    def push_front(self, t):
        'push_front(self, t:PySide2.QtCore.QPoint)'
        pass
    
    def remove(self, i: int, n: int):
        'remove(self, i:int)\nremove(self, i:int, n:int)'
        pass
    
    def removeAll(self, t):
        'removeAll(self, t:PySide2.QtCore.QPoint) -> int'
        return int
    
    def removeAt(self, i):
        'removeAt(self, i:int)'
        pass
    
    def removeFirst(self):
        'removeFirst(self)'
        pass
    
    def removeLast(self):
        'removeLast(self)'
        pass
    
    def removeOne(self, t):
        'removeOne(self, t:PySide2.QtCore.QPoint) -> bool'
        return bool
    
    def replace(self, i, t):
        'replace(self, i:int, t:PySide2.QtCore.QPoint)'
        pass
    
    def reserve(self, size):
        'reserve(self, size:int)'
        pass
    
    def resize(self, size):
        'resize(self, size:int)'
        pass
    
    def setSharable(self, sharable):
        'setSharable(self, sharable:bool)'
        pass
    
    def shrink_to_fit(self):
        'shrink_to_fit(self)'
        pass
    
    def size(self):
        'size(self) -> int'
        return int
    
    def squeeze(self):
        'squeeze(self)'
        pass
    
    def startsWith(self, t):
        'startsWith(self, t:PySide2.QtCore.QPoint) -> bool'
        return bool
    
    def subtracted(self, r):
        'subtracted(self, r:PySide2.QtGui.QPolygon) -> PySide2.QtGui.QPolygon'
        return PySide2.QtGui.QPolygon
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QPolygon)'
        pass
    
    def swapItemsAt(self, i, j):
        'swapItemsAt(self, i:int, j:int)'
        pass
    
    def takeAt(self, i):
        'takeAt(self, i:int) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def takeFirst(self):
        'takeFirst(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def takeLast(self):
        'takeLast(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def toList(self):
        'toList(self) -> typing.List'
        return typing.List
    
    def translate(self, offset: PySide2.QtCore.QPoint):
        'translate(self, dx:int, dy:int)\ntranslate(self, offset:PySide2.QtCore.QPoint)'
        pass
    
    def translated(self, offset: PySide2.QtCore.QPoint):
        'translated(self, dx:int, dy:int) -> PySide2.QtGui.QPolygon\ntranslated(self, offset:PySide2.QtCore.QPoint) -> PySide2.QtGui.QPolygon'
        pass
    
    def united(self, r):
        'united(self, r:PySide2.QtGui.QPolygon) -> PySide2.QtGui.QPolygon'
        return PySide2.QtGui.QPolygon
    
    def value(self, i: int, defaultValue: PySide2.QtCore.QPoint):
        'value(self, i:int) -> PySide2.QtCore.QPoint\nvalue(self, i:int, defaultValue:PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint'
        pass
    

class QPolygonF(_mod_Shiboken.Object):
    'QPolygonF(self)\nQPolygonF(self, a:PySide2.QtGui.QPolygon)\nQPolygonF(self, a:PySide2.QtGui.QPolygonF)\nQPolygonF(self, r:PySide2.QtCore.QRectF)\nQPolygonF(self, size:int)\nQPolygonF(self, v:typing.List)'
    def __add__(self, l):
        '__add__(self, l:typing.List) -> typing.List\n\nReturn self+value.'
        return typing.List
    
    __class__ = QPolygonF
    def __copy__(self):
        '__copy__()'
        pass
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, t):
        '__iadd__(self, t:PySide2.QtCore.QPointF) -> typing.List\n\nReturn self+=value.'
        return typing.List
    
    def __init__(self, a: PySide2.QtGui.QPolygonF):
        'QPolygonF(self)\nQPolygonF(self, a:PySide2.QtGui.QPolygon)\nQPolygonF(self, a:PySide2.QtGui.QPolygonF)\nQPolygonF(self, r:PySide2.QtCore.QRectF)\nQPolygonF(self, size:int)\nQPolygonF(self, v:typing.List)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lshift__(self, stream):
        '__lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __mul__(self, m: PySide2.QtGui.QTransform):
        '__mul__(self, m:PySide2.QtGui.QMatrix) -> PySide2.QtGui.QPolygonF\n__mul__(self, m:PySide2.QtGui.QTransform) -> PySide2.QtGui.QPolygonF\n\nReturn self*value.'
        return QPolygonF()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __radd__(self, value):
        'Return value+self.'
        return QPolygonF()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QPolygonF()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QPolygonF()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QPolygonF()
    
    def __rshift__(self, stream):
        '__rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def append(self, t: PySide2.QtCore.QPointF):
        'append(self, l:typing.List)\nappend(self, t:PySide2.QtCore.QPointF)'
        pass
    
    def at(self, i):
        'at(self, i:int) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def back(self):
        'back(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def boundingRect(self):
        'boundingRect(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def capacity(self):
        'capacity(self) -> int'
        return int
    
    def clear(self):
        'clear(self)'
        pass
    
    def constData(self):
        'constData(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def constFirst(self):
        'constFirst(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def constLast(self):
        'constLast(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def contains(self, t):
        'contains(self, t:PySide2.QtCore.QPointF) -> bool'
        return bool
    
    def containsPoint(self, pt, fillRule):
        'containsPoint(self, pt:PySide2.QtCore.QPointF, fillRule:PySide2.QtCore.Qt.FillRule) -> bool'
        return bool
    
    def count(self, t: PySide2.QtCore.QPointF):
        'count(self) -> int\ncount(self, t:PySide2.QtCore.QPointF) -> int'
        return 1
    
    def data(self):
        'data(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def empty(self):
        'empty(self) -> bool'
        return bool
    
    def endsWith(self, t):
        'endsWith(self, t:PySide2.QtCore.QPointF) -> bool'
        return bool
    
    def fill(self, t, size):
        'fill(self, t:PySide2.QtCore.QPointF, size:int=-1) -> typing.List'
        return typing.List
    
    def first(self):
        'first(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    @classmethod
    def fromList(cls, list):
        'fromList(list:typing.Sequence) -> typing.List'
        return typing.List
    
    def front(self):
        'front(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def indexOf(self, t, from_):
        'indexOf(self, t:PySide2.QtCore.QPointF, from_:int=0) -> int'
        return int
    
    def insert(self, i: int, n: int, t: PySide2.QtCore.QPointF):
        'insert(self, i:int, n:int, t:PySide2.QtCore.QPointF)\ninsert(self, i:int, t:PySide2.QtCore.QPointF)'
        pass
    
    def intersected(self, r):
        'intersected(self, r:PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF'
        return PySide2.QtGui.QPolygonF
    
    def intersects(self, r):
        'intersects(self, r:PySide2.QtGui.QPolygonF) -> bool'
        return bool
    
    def isClosed(self):
        'isClosed(self) -> bool'
        return bool
    
    def isEmpty(self):
        'isEmpty(self) -> bool'
        return bool
    
    def isSharedWith(self, other):
        'isSharedWith(self, other:typing.List) -> bool'
        return bool
    
    def last(self):
        'last(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def lastIndexOf(self, t, from_):
        'lastIndexOf(self, t:PySide2.QtCore.QPointF, from_:int=-1) -> int'
        return int
    
    def length(self):
        'length(self) -> int'
        return int
    
    def mid(self, pos, len):
        'mid(self, pos:int, len:int=-1) -> typing.List'
        return typing.List
    
    def move(self, from_, to):
        'move(self, from_:int, to:int)'
        pass
    
    def pop_back(self):
        'pop_back(self)'
        pass
    
    def pop_front(self):
        'pop_front(self)'
        pass
    
    def prepend(self, t):
        'prepend(self, t:PySide2.QtCore.QPointF)'
        pass
    
    def push_back(self, t):
        'push_back(self, t:PySide2.QtCore.QPointF)'
        pass
    
    def push_front(self, t):
        'push_front(self, t:PySide2.QtCore.QPointF)'
        pass
    
    def remove(self, i: int, n: int):
        'remove(self, i:int)\nremove(self, i:int, n:int)'
        pass
    
    def removeAll(self, t):
        'removeAll(self, t:PySide2.QtCore.QPointF) -> int'
        return int
    
    def removeAt(self, i):
        'removeAt(self, i:int)'
        pass
    
    def removeFirst(self):
        'removeFirst(self)'
        pass
    
    def removeLast(self):
        'removeLast(self)'
        pass
    
    def removeOne(self, t):
        'removeOne(self, t:PySide2.QtCore.QPointF) -> bool'
        return bool
    
    def replace(self, i, t):
        'replace(self, i:int, t:PySide2.QtCore.QPointF)'
        pass
    
    def reserve(self, size):
        'reserve(self, size:int)'
        pass
    
    def resize(self, size):
        'resize(self, size:int)'
        pass
    
    def setSharable(self, sharable):
        'setSharable(self, sharable:bool)'
        pass
    
    def shrink_to_fit(self):
        'shrink_to_fit(self)'
        pass
    
    def size(self):
        'size(self) -> int'
        return int
    
    def squeeze(self):
        'squeeze(self)'
        pass
    
    def startsWith(self, t):
        'startsWith(self, t:PySide2.QtCore.QPointF) -> bool'
        return bool
    
    def subtracted(self, r):
        'subtracted(self, r:PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF'
        return PySide2.QtGui.QPolygonF
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QPolygonF)'
        pass
    
    def swapItemsAt(self, i, j):
        'swapItemsAt(self, i:int, j:int)'
        pass
    
    def takeAt(self, i):
        'takeAt(self, i:int) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def takeFirst(self):
        'takeFirst(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def takeLast(self):
        'takeLast(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def toList(self):
        'toList(self) -> typing.List'
        return typing.List
    
    def toPolygon(self):
        'toPolygon(self) -> PySide2.QtGui.QPolygon'
        return PySide2.QtGui.QPolygon
    
    def translate(self, offset: PySide2.QtCore.QPointF):
        'translate(self, dx:float, dy:float)\ntranslate(self, offset:PySide2.QtCore.QPointF)'
        pass
    
    def translated(self, offset: PySide2.QtCore.QPointF):
        'translated(self, dx:float, dy:float) -> PySide2.QtGui.QPolygonF\ntranslated(self, offset:PySide2.QtCore.QPointF) -> PySide2.QtGui.QPolygonF'
        pass
    
    def united(self, r):
        'united(self, r:PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF'
        return PySide2.QtGui.QPolygonF
    
    def value(self, i: int, defaultValue: PySide2.QtCore.QPointF):
        'value(self, i:int) -> PySide2.QtCore.QPointF\nvalue(self, i:int, defaultValue:PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF'
        pass
    

class QPyTextObject(_mod_PySide2_QtCore.QObject,QTextObjectInterface):
    'QPyTextObject(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    __class__ = QPyTextObject
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QPyTextObject(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def drawObject(self, painter, rect, doc, posInDocument, format):
        'drawObject(self, painter:PySide2.QtGui.QPainter, rect:PySide2.QtCore.QRectF, doc:PySide2.QtGui.QTextDocument, posInDocument:int, format:PySide2.QtGui.QTextFormat)'
        pass
    
    def intrinsicSize(self, doc, posInDocument, format):
        'intrinsicSize(self, doc:PySide2.QtGui.QTextDocument, posInDocument:int, format:PySide2.QtGui.QTextFormat) -> PySide2.QtCore.QSizeF'
        return PySide2.QtCore.QSizeF
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QQuaternion(_mod_Shiboken.Object):
    'QQuaternion(self)\nQQuaternion(self, scalar:float, vector:PySide2.QtGui.QVector3D)\nQQuaternion(self, scalar:float, xpos:float, ypos:float, zpos:float)\nQQuaternion(self, vector:PySide2.QtGui.QVector4D)'
    def __add__(self, q2):
        '__add__(self, q2:PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion\n\nReturn self+value.'
        return PySide2.QtGui.QQuaternion
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QQuaternion
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, quaternion):
        '__iadd__(self, quaternion:PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion\n\nReturn self+=value.'
        return PySide2.QtGui.QQuaternion
    
    def __imul__(self, quaternion: PySide2.QtGui.QQuaternion):
        '__imul__(self, factor:float) -> PySide2.QtGui.QQuaternion\n__imul__(self, quaternion:PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion\n\nReturn self*=value.'
        return None
    
    def __init__(self, scalar: float, xpos: float, ypos: float, zpos: float):
        'QQuaternion(self)\nQQuaternion(self, scalar:float, vector:PySide2.QtGui.QVector3D)\nQQuaternion(self, scalar:float, xpos:float, ypos:float, zpos:float)\nQQuaternion(self, vector:PySide2.QtGui.QVector4D)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, quaternion):
        '__isub__(self, quaternion:PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion\n\nReturn self-=value.'
        return PySide2.QtGui.QQuaternion
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __mul__(self, q2: PySide2.QtGui.QQuaternion):
        '__mul__(self, factor:float) -> PySide2.QtGui.QQuaternion\n__mul__(self, q2:PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion\n\nReturn self*value.'
        return QQuaternion()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '__neg__(self) -> PySide2.QtGui.QQuaternion\n\n-self'
        return PySide2.QtGui.QQuaternion
    
    def __radd__(self, value):
        'Return value+self.'
        return QQuaternion()
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QQuaternion()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QQuaternion()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QQuaternion()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __rsub__(self, value):
        'Return value-self.'
        return QQuaternion()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QQuaternion()
    
    def __sub__(self, q2):
        '__sub__(self, q2:PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion\n\nReturn self-value.'
        return PySide2.QtGui.QQuaternion
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def conjugate(self):
        'conjugate(self) -> PySide2.QtGui.QQuaternion'
        return PySide2.QtGui.QQuaternion
    
    def conjugated(self):
        'conjugated(self) -> PySide2.QtGui.QQuaternion'
        return PySide2.QtGui.QQuaternion
    
    @classmethod
    def dotProduct(cls, q1, q2):
        'dotProduct(q1:PySide2.QtGui.QQuaternion, q2:PySide2.QtGui.QQuaternion) -> float'
        return float
    
    @classmethod
    def fromAxes(cls, xAxis, yAxis, zAxis):
        'fromAxes(xAxis:PySide2.QtGui.QVector3D, yAxis:PySide2.QtGui.QVector3D, zAxis:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QQuaternion'
        return PySide2.QtGui.QQuaternion
    
    @classmethod
    def fromAxisAndAngle(cls, axis: PySide2.QtGui.QVector3D, angle: float):
        'fromAxisAndAngle(axis:PySide2.QtGui.QVector3D, angle:float) -> PySide2.QtGui.QQuaternion\nfromAxisAndAngle(x:float, y:float, z:float, angle:float) -> PySide2.QtGui.QQuaternion'
        pass
    
    @classmethod
    def fromDirection(cls, direction, up):
        'fromDirection(direction:PySide2.QtGui.QVector3D, up:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QQuaternion'
        return PySide2.QtGui.QQuaternion
    
    @classmethod
    def fromEulerAngles(cls, eulerAngles: PySide2.QtGui.QVector3D):
        'fromEulerAngles(eulerAngles:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QQuaternion\nfromEulerAngles(pitch:float, yaw:float, roll:float) -> PySide2.QtGui.QQuaternion'
        pass
    
    @classmethod
    def fromRotationMatrix(cls, rot3x3):
        'fromRotationMatrix(rot3x3:PySide2.QtGui.QMatrix3x3) -> PySide2.QtGui.QQuaternion'
        return PySide2.QtGui.QQuaternion
    
    def getAxes(self, xAxis, yAxis, zAxis):
        'getAxes(self, xAxis:PySide2.QtGui.QVector3D, yAxis:PySide2.QtGui.QVector3D, zAxis:PySide2.QtGui.QVector3D)'
        pass
    
    def inverted(self):
        'inverted(self) -> PySide2.QtGui.QQuaternion'
        return PySide2.QtGui.QQuaternion
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def length(self):
        'length(self) -> float'
        return float
    
    def lengthSquared(self):
        'lengthSquared(self) -> float'
        return float
    
    @classmethod
    def nlerp(cls, q1, q2, t):
        'nlerp(q1:PySide2.QtGui.QQuaternion, q2:PySide2.QtGui.QQuaternion, t:float) -> PySide2.QtGui.QQuaternion'
        return PySide2.QtGui.QQuaternion
    
    def normalize(self):
        'normalize(self)'
        pass
    
    def normalized(self):
        'normalized(self) -> PySide2.QtGui.QQuaternion'
        return PySide2.QtGui.QQuaternion
    
    def rotatedVector(self, vector):
        'rotatedVector(self, vector:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D'
        return PySide2.QtGui.QVector3D
    
    @classmethod
    def rotationTo(cls, from_, to):
        'rotationTo(from_:PySide2.QtGui.QVector3D, to:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QQuaternion'
        return PySide2.QtGui.QQuaternion
    
    def scalar(self):
        'scalar(self) -> float'
        return float
    
    def setScalar(self, scalar):
        'setScalar(self, scalar:float)'
        pass
    
    def setVector(self, vector: PySide2.QtGui.QVector3D):
        'setVector(self, vector:PySide2.QtGui.QVector3D)\nsetVector(self, x:float, y:float, z:float)'
        pass
    
    def setX(self, x):
        'setX(self, x:float)'
        pass
    
    def setY(self, y):
        'setY(self, y:float)'
        pass
    
    def setZ(self, z):
        'setZ(self, z:float)'
        pass
    
    @classmethod
    def slerp(cls, q1, q2, t):
        'slerp(q1:PySide2.QtGui.QQuaternion, q2:PySide2.QtGui.QQuaternion, t:float) -> PySide2.QtGui.QQuaternion'
        return PySide2.QtGui.QQuaternion
    
    def toEulerAngles(self):
        'toEulerAngles(self) -> PySide2.QtGui.QVector3D'
        return PySide2.QtGui.QVector3D
    
    def toRotationMatrix(self):
        'toRotationMatrix(self) -> PySide2.QtGui.QMatrix3x3'
        return PySide2.QtGui.QMatrix3x3
    
    def toVector4D(self):
        'toVector4D(self) -> PySide2.QtGui.QVector4D'
        return PySide2.QtGui.QVector4D
    
    def vector(self):
        'vector(self) -> PySide2.QtGui.QVector3D'
        return PySide2.QtGui.QVector3D
    
    def x(self):
        'x(self) -> float'
        return float
    
    def y(self):
        'y(self) -> float'
        return float
    
    def z(self):
        'z(self) -> float'
        return float
    

class QRadialGradient(QGradient):
    'QRadialGradient(self)\nQRadialGradient(self, QRadialGradient:PySide2.QtGui.QRadialGradient)\nQRadialGradient(self, center:PySide2.QtCore.QPointF, centerRadius:float, focalPoint:PySide2.QtCore.QPointF, focalRadius:float)\nQRadialGradient(self, center:PySide2.QtCore.QPointF, radius:float)\nQRadialGradient(self, center:PySide2.QtCore.QPointF, radius:float, focalPoint:PySide2.QtCore.QPointF)\nQRadialGradient(self, cx:float, cy:float, centerRadius:float, fx:float, fy:float, focalRadius:float)\nQRadialGradient(self, cx:float, cy:float, radius:float)\nQRadialGradient(self, cx:float, cy:float, radius:float, fx:float, fy:float)'
    __class__ = QRadialGradient
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, center: PySide2.QtCore.QPointF, centerRadius: float, focalPoint: PySide2.QtCore.QPointF, focalRadius: float):
        'QRadialGradient(self)\nQRadialGradient(self, QRadialGradient:PySide2.QtGui.QRadialGradient)\nQRadialGradient(self, center:PySide2.QtCore.QPointF, centerRadius:float, focalPoint:PySide2.QtCore.QPointF, focalRadius:float)\nQRadialGradient(self, center:PySide2.QtCore.QPointF, radius:float)\nQRadialGradient(self, center:PySide2.QtCore.QPointF, radius:float, focalPoint:PySide2.QtCore.QPointF)\nQRadialGradient(self, cx:float, cy:float, centerRadius:float, fx:float, fy:float, focalRadius:float)\nQRadialGradient(self, cx:float, cy:float, radius:float)\nQRadialGradient(self, cx:float, cy:float, radius:float, fx:float, fy:float)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def center(self):
        'center(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def centerRadius(self):
        'centerRadius(self) -> float'
        return float
    
    def focalPoint(self):
        'focalPoint(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def focalRadius(self):
        'focalRadius(self) -> float'
        return float
    
    def radius(self):
        'radius(self) -> float'
        return float
    
    def setCenter(self, center: PySide2.QtCore.QPointF):
        'setCenter(self, center:PySide2.QtCore.QPointF)\nsetCenter(self, x:float, y:float)'
        pass
    
    def setCenterRadius(self, radius):
        'setCenterRadius(self, radius:float)'
        pass
    
    def setFocalPoint(self, focalPoint: PySide2.QtCore.QPointF):
        'setFocalPoint(self, focalPoint:PySide2.QtCore.QPointF)\nsetFocalPoint(self, x:float, y:float)'
        pass
    
    def setFocalRadius(self, radius):
        'setFocalRadius(self, radius:float)'
        pass
    
    def setRadius(self, radius):
        'setRadius(self, radius:float)'
        pass
    

class QRasterWindow(QPaintDeviceWindow):
    'QRasterWindow(self, parent:typing.Union[PySide2.QtGui.QWindow, NoneType]=None)'
    __class__ = QRasterWindow
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, parent: typing.Union[PySide2.QtGui.QWindow,NoneType]=None):
        'QRasterWindow(self, parent:typing.Union[PySide2.QtGui.QWindow, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def metric(self, metric):
        'metric(self, metric:PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int'
        return int
    
    def redirected(self, arg__1):
        'redirected(self, arg__1:PySide2.QtCore.QPoint) -> PySide2.QtGui.QPaintDevice'
        return PySide2.QtGui.QPaintDevice
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QRawFont(_mod_Shiboken.Object):
    'QRawFont(self)\nQRawFont(self, fileName:str, pixelSize:float, hintingPreference:PySide2.QtGui.QFont.HintingPreference=PySide2.QtGui.QFont.HintingPreference.PreferDefaultHinting)\nQRawFont(self, fontData:PySide2.QtCore.QByteArray, pixelSize:float, hintingPreference:PySide2.QtGui.QFont.HintingPreference=PySide2.QtGui.QFont.HintingPreference.PreferDefaultHinting)\nQRawFont(self, other:PySide2.QtGui.QRawFont)'
    AntialiasingType = AntialiasingType
    KernedAdvances = LayoutFlag()
    LayoutFlag = LayoutFlag
    LayoutFlags = LayoutFlags
    PixelAntialiasing = AntialiasingType()
    SeparateAdvances = LayoutFlag()
    SubPixelAntialiasing = AntialiasingType()
    UseDesignMetrics = LayoutFlag()
    __class__ = QRawFont
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, fontData: PySide2.QtCore.QByteArray, pixelSize: float, hintingPreference: PySide2.QtGui.QFont.HintingPreference=PySide2.QtGui.QFont.HintingPreference.PreferDefaultHinting):
        'QRawFont(self)\nQRawFont(self, fileName:str, pixelSize:float, hintingPreference:PySide2.QtGui.QFont.HintingPreference=PySide2.QtGui.QFont.HintingPreference.PreferDefaultHinting)\nQRawFont(self, fontData:PySide2.QtCore.QByteArray, pixelSize:float, hintingPreference:PySide2.QtGui.QFont.HintingPreference=PySide2.QtGui.QFont.HintingPreference.PreferDefaultHinting)\nQRawFont(self, other:PySide2.QtGui.QRawFont)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def advancesForGlyphIndexes(self, glyphIndexes: typing.List, layoutFlags: PySide2.QtGui.QRawFont.LayoutFlags):
        'advancesForGlyphIndexes(self, glyphIndexes:typing.List) -> typing.List\nadvancesForGlyphIndexes(self, glyphIndexes:typing.List, layoutFlags:PySide2.QtGui.QRawFont.LayoutFlags) -> typing.List'
        pass
    
    def alphaMapForGlyph(self, glyphIndex, antialiasingType, transform):
        'alphaMapForGlyph(self, glyphIndex:int, antialiasingType:PySide2.QtGui.QRawFont.AntialiasingType=PySide2.QtGui.QRawFont.AntialiasingType.SubPixelAntialiasing, transform:PySide2.QtGui.QTransform=Default(QTransform)) -> PySide2.QtGui.QImage'
        return PySide2.QtGui.QImage
    
    def ascent(self):
        'ascent(self) -> float'
        return float
    
    def averageCharWidth(self):
        'averageCharWidth(self) -> float'
        return float
    
    def boundingRect(self, glyphIndex):
        'boundingRect(self, glyphIndex:int) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def capHeight(self):
        'capHeight(self) -> float'
        return float
    
    def descent(self):
        'descent(self) -> float'
        return float
    
    def familyName(self):
        'familyName(self) -> str'
        return str
    
    def fontTable(self, tagName):
        'fontTable(self, tagName:bytes) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    @classmethod
    def fromFont(cls, font, writingSystem):
        'fromFont(font:PySide2.QtGui.QFont, writingSystem:PySide2.QtGui.QFontDatabase.WritingSystem=PySide2.QtGui.QFontDatabase.WritingSystem.Any) -> PySide2.QtGui.QRawFont'
        return PySide2.QtGui.QRawFont
    
    def glyphIndexesForString(self, text):
        'glyphIndexesForString(self, text:str) -> typing.List'
        return typing.List
    
    def hintingPreference(self):
        'hintingPreference(self) -> PySide2.QtGui.QFont.HintingPreference'
        return PySide2.QtGui.QFont.HintingPreference
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def leading(self):
        'leading(self) -> float'
        return float
    
    def lineThickness(self):
        'lineThickness(self) -> float'
        return float
    
    def loadFromData(self, fontData, pixelSize, hintingPreference):
        'loadFromData(self, fontData:PySide2.QtCore.QByteArray, pixelSize:float, hintingPreference:PySide2.QtGui.QFont.HintingPreference)'
        pass
    
    def loadFromFile(self, fileName, pixelSize, hintingPreference):
        'loadFromFile(self, fileName:str, pixelSize:float, hintingPreference:PySide2.QtGui.QFont.HintingPreference)'
        pass
    
    def maxCharWidth(self):
        'maxCharWidth(self) -> float'
        return float
    
    def pathForGlyph(self, glyphIndex):
        'pathForGlyph(self, glyphIndex:int) -> PySide2.QtGui.QPainterPath'
        return PySide2.QtGui.QPainterPath
    
    def pixelSize(self):
        'pixelSize(self) -> float'
        return float
    
    def setPixelSize(self, pixelSize):
        'setPixelSize(self, pixelSize:float)'
        pass
    
    def style(self):
        'style(self) -> PySide2.QtGui.QFont.Style'
        return PySide2.QtGui.QFont.Style
    
    def styleName(self):
        'styleName(self) -> str'
        return str
    
    def supportedWritingSystems(self):
        'supportedWritingSystems(self) -> typing.List'
        return typing.List
    
    def supportsCharacter(self, character: str):
        'supportsCharacter(self, character:str) -> bool\nsupportsCharacter(self, ucs4:int) -> bool'
        return True
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QRawFont)'
        pass
    
    def underlinePosition(self):
        'underlinePosition(self) -> float'
        return float
    
    def unitsPerEm(self):
        'unitsPerEm(self) -> float'
        return float
    
    def weight(self):
        'weight(self) -> int'
        return int
    
    def xHeight(self):
        'xHeight(self) -> float'
        return float
    

class QRegExpValidator(QValidator):
    'QRegExpValidator(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQRegExpValidator(self, rx:PySide2.QtCore.QRegExp, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    __class__ = QRegExpValidator
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, rx: PySide2.QtCore.QRegExp, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QRegExpValidator(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQRegExpValidator(self, rx:PySide2.QtCore.QRegExp, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def regExp(self):
        'regExp(self) -> PySide2.QtCore.QRegExp'
        return PySide2.QtCore.QRegExp
    
    def regExpChanged(self):
        pass
    
    def setRegExp(self, rx):
        'setRegExp(self, rx:PySide2.QtCore.QRegExp)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def validate(self, input, pos):
        'validate(self, input:str, pos:int) -> PySide2.QtGui.QValidator.State'
        return PySide2.QtGui.QValidator.State
    

class QRegion(_mod_Shiboken.Object):
    'QRegion(self)\nQRegion(self, bitmap:PySide2.QtGui.QBitmap)\nQRegion(self, pa:PySide2.QtGui.QPolygon, fillRule:PySide2.QtCore.Qt.FillRule=PySide2.QtCore.Qt.FillRule.OddEvenFill)\nQRegion(self, r:PySide2.QtCore.QRect, t:PySide2.QtGui.QRegion.RegionType=PySide2.QtGui.QRegion.RegionType.Rectangle)\nQRegion(self, region:PySide2.QtGui.QRegion)\nQRegion(self, x:int, y:int, w:int, h:int, t:PySide2.QtGui.QRegion.RegionType=PySide2.QtGui.QRegion.RegionType.Rectangle)'
    Ellipse = RegionType()
    Rectangle = RegionType()
    RegionType = RegionType
    def __add__(self, r: PySide2.QtGui.QRegion):
        '__add__(self, r:PySide2.QtCore.QRect) -> PySide2.QtGui.QRegion\n__add__(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion\n\nReturn self+value.'
        return QRegion()
    
    def __and__(self, r: PySide2.QtGui.QRegion):
        '__and__(self, r:PySide2.QtCore.QRect) -> PySide2.QtGui.QRegion\n__and__(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion\n\nReturn self&value.'
        return QRegion()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QRegion
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, r: PySide2.QtGui.QRegion):
        '__iadd__(self, r:PySide2.QtCore.QRect) -> PySide2.QtGui.QRegion\n__iadd__(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion\n\nReturn self+=value.'
        return None
    
    def __init__(self, x: int, y: int, w: int, h: int, t: PySide2.QtGui.QRegion.RegionType=PySide2.QtGui.QRegion.RegionType.Rectangle):
        'QRegion(self)\nQRegion(self, bitmap:PySide2.QtGui.QBitmap)\nQRegion(self, pa:PySide2.QtGui.QPolygon, fillRule:PySide2.QtCore.Qt.FillRule=PySide2.QtCore.Qt.FillRule.OddEvenFill)\nQRegion(self, r:PySide2.QtCore.QRect, t:PySide2.QtGui.QRegion.RegionType=PySide2.QtGui.QRegion.RegionType.Rectangle)\nQRegion(self, region:PySide2.QtGui.QRegion)\nQRegion(self, x:int, y:int, w:int, h:int, t:PySide2.QtGui.QRegion.RegionType=PySide2.QtGui.QRegion.RegionType.Rectangle)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __ior__(self, r):
        '__ior__(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion\n\nReturn self|=value.'
        return PySide2.QtGui.QRegion
    
    def __isub__(self, r):
        '__isub__(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion\n\nReturn self-=value.'
        return PySide2.QtGui.QRegion
    
    def __ixor__(self, r):
        '__ixor__(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion\n\nReturn self^=value.'
        return PySide2.QtGui.QRegion
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __mul__(self, m: PySide2.QtGui.QTransform):
        '__mul__(self, m:PySide2.QtGui.QMatrix) -> PySide2.QtGui.QRegion\n__mul__(self, m:PySide2.QtGui.QTransform) -> PySide2.QtGui.QRegion\n\nReturn self*value.'
        return QRegion()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __or__(self, r):
        '__or__(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion\n\nReturn self|value.'
        return PySide2.QtGui.QRegion
    
    def __radd__(self, value):
        'Return value+self.'
        return QRegion()
    
    def __rand__(self, value):
        'Return value&self.'
        return QRegion()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QRegion()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QRegion()
    
    def __ror__(self, value):
        'Return value|self.'
        return QRegion()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QRegion()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __rsub__(self, value):
        'Return value-self.'
        return QRegion()
    
    def __rxor__(self, value):
        'Return value^self.'
        return QRegion()
    
    def __sub__(self, r):
        '__sub__(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion\n\nReturn self-value.'
        return PySide2.QtGui.QRegion
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __xor__(self, r):
        '__xor__(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion\n\nReturn self^value.'
        return PySide2.QtGui.QRegion
    
    def begin(self):
        'begin(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def boundingRect(self):
        'boundingRect(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def cbegin(self):
        'cbegin(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def cend(self):
        'cend(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def contains(self, p: PySide2.QtCore.QPoint):
        'contains(self, p:PySide2.QtCore.QPoint) -> bool\ncontains(self, r:PySide2.QtCore.QRect) -> bool'
        return True
    
    def end(self):
        'end(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def intersected(self, r: PySide2.QtGui.QRegion):
        'intersected(self, r:PySide2.QtCore.QRect) -> PySide2.QtGui.QRegion\nintersected(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion'
        pass
    
    def intersects(self, r: PySide2.QtGui.QRegion):
        'intersects(self, r:PySide2.QtCore.QRect) -> bool\nintersects(self, r:PySide2.QtGui.QRegion) -> bool'
        return True
    
    def isEmpty(self):
        'isEmpty(self) -> bool'
        return bool
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def rectCount(self):
        'rectCount(self) -> int'
        return int
    
    def rects(self):
        'rects(self) -> typing.List'
        return typing.List
    
    def setRects(self, rect, num):
        'setRects(self, rect:PySide2.QtCore.QRect, num:int)'
        pass
    
    def subtracted(self, r):
        'subtracted(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion'
        return PySide2.QtGui.QRegion
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QRegion)'
        pass
    
    def translate(self, p: PySide2.QtCore.QPoint):
        'translate(self, dx:int, dy:int)\ntranslate(self, p:PySide2.QtCore.QPoint)'
        pass
    
    def translated(self, p: PySide2.QtCore.QPoint):
        'translated(self, dx:int, dy:int) -> PySide2.QtGui.QRegion\ntranslated(self, p:PySide2.QtCore.QPoint) -> PySide2.QtGui.QRegion'
        pass
    
    def united(self, r: PySide2.QtGui.QRegion):
        'united(self, r:PySide2.QtCore.QRect) -> PySide2.QtGui.QRegion\nunited(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion'
        pass
    
    def xored(self, r):
        'xored(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion'
        return PySide2.QtGui.QRegion
    

class QRegularExpressionValidator(QValidator):
    'QRegularExpressionValidator(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQRegularExpressionValidator(self, re:PySide2.QtCore.QRegularExpression, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    __class__ = QRegularExpressionValidator
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, re: PySide2.QtCore.QRegularExpression, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QRegularExpressionValidator(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQRegularExpressionValidator(self, re:PySide2.QtCore.QRegularExpression, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def regularExpression(self):
        'regularExpression(self) -> PySide2.QtCore.QRegularExpression'
        return PySide2.QtCore.QRegularExpression
    
    def regularExpressionChanged(self):
        pass
    
    def setRegularExpression(self, re):
        'setRegularExpression(self, re:PySide2.QtCore.QRegularExpression)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def validate(self, input, pos):
        'validate(self, input:str, pos:int) -> PySide2.QtGui.QValidator.State'
        return PySide2.QtGui.QValidator.State
    

class QResizeEvent(_mod_PySide2_QtCore.QEvent):
    'QResizeEvent(self, size:PySide2.QtCore.QSize, oldSize:PySide2.QtCore.QSize)'
    __class__ = QResizeEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, size: PySide2.QtCore.QSize, oldSize: PySide2.QtCore.QSize):
        'QResizeEvent(self, size:PySide2.QtCore.QSize, oldSize:PySide2.QtCore.QSize)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def oldSize(self):
        'oldSize(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    

class QScreen(_mod_PySide2_QtCore.QObject):
    __class__ = QScreen
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def angleBetween(self, a, b):
        'angleBetween(self, a:PySide2.QtCore.Qt.ScreenOrientation, b:PySide2.QtCore.Qt.ScreenOrientation) -> int'
        return int
    
    def availableGeometry(self):
        'availableGeometry(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def availableGeometryChanged(self):
        pass
    
    def availableSize(self):
        'availableSize(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def availableVirtualGeometry(self):
        'availableVirtualGeometry(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def availableVirtualSize(self):
        'availableVirtualSize(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def depth(self):
        'depth(self) -> int'
        return int
    
    def devicePixelRatio(self):
        'devicePixelRatio(self) -> float'
        return float
    
    def geometry(self):
        'geometry(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def geometryChanged(self):
        pass
    
    def grabWindow(self, window, x, y, w, h):
        'grabWindow(self, window:int, x:int=0, y:int=0, w:int=-1, h:int=-1) -> PySide2.QtGui.QPixmap'
        return PySide2.QtGui.QPixmap
    
    def isLandscape(self, orientation):
        'isLandscape(self, orientation:PySide2.QtCore.Qt.ScreenOrientation) -> bool'
        return bool
    
    def isPortrait(self, orientation):
        'isPortrait(self, orientation:PySide2.QtCore.Qt.ScreenOrientation) -> bool'
        return bool
    
    def logicalDotsPerInch(self):
        'logicalDotsPerInch(self) -> float'
        return float
    
    def logicalDotsPerInchChanged(self):
        pass
    
    def logicalDotsPerInchX(self):
        'logicalDotsPerInchX(self) -> float'
        return float
    
    def logicalDotsPerInchY(self):
        'logicalDotsPerInchY(self) -> float'
        return float
    
    def manufacturer(self):
        'manufacturer(self) -> str'
        return str
    
    def mapBetween(self, a, b, rect):
        'mapBetween(self, a:PySide2.QtCore.Qt.ScreenOrientation, b:PySide2.QtCore.Qt.ScreenOrientation, rect:PySide2.QtCore.QRect) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def model(self):
        'model(self) -> str'
        return str
    
    def name(self):
        'name(self) -> str'
        return str
    
    def nativeOrientation(self):
        'nativeOrientation(self) -> PySide2.QtCore.Qt.ScreenOrientation'
        return PySide2.QtCore.Qt.ScreenOrientation
    
    def orientation(self):
        'orientation(self) -> PySide2.QtCore.Qt.ScreenOrientation'
        return PySide2.QtCore.Qt.ScreenOrientation
    
    def orientationChanged(self):
        pass
    
    def orientationUpdateMask(self):
        'orientationUpdateMask(self) -> PySide2.QtCore.Qt.ScreenOrientations'
        return PySide2.QtCore.Qt.ScreenOrientations
    
    def physicalDotsPerInch(self):
        'physicalDotsPerInch(self) -> float'
        return float
    
    def physicalDotsPerInchChanged(self):
        pass
    
    def physicalDotsPerInchX(self):
        'physicalDotsPerInchX(self) -> float'
        return float
    
    def physicalDotsPerInchY(self):
        'physicalDotsPerInchY(self) -> float'
        return float
    
    def physicalSize(self):
        'physicalSize(self) -> PySide2.QtCore.QSizeF'
        return PySide2.QtCore.QSizeF
    
    def physicalSizeChanged(self):
        pass
    
    def primaryOrientation(self):
        'primaryOrientation(self) -> PySide2.QtCore.Qt.ScreenOrientation'
        return PySide2.QtCore.Qt.ScreenOrientation
    
    def primaryOrientationChanged(self):
        pass
    
    def refreshRate(self):
        'refreshRate(self) -> float'
        return float
    
    def refreshRateChanged(self):
        pass
    
    def serialNumber(self):
        'serialNumber(self) -> str'
        return str
    
    def setOrientationUpdateMask(self, mask):
        'setOrientationUpdateMask(self, mask:PySide2.QtCore.Qt.ScreenOrientations)'
        pass
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def transformBetween(self, a, b, target):
        'transformBetween(self, a:PySide2.QtCore.Qt.ScreenOrientation, b:PySide2.QtCore.Qt.ScreenOrientation, target:PySide2.QtCore.QRect) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def virtualGeometry(self):
        'virtualGeometry(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def virtualGeometryChanged(self):
        pass
    
    def virtualSiblingAt(self, point):
        'virtualSiblingAt(self, point:PySide2.QtCore.QPoint) -> PySide2.QtGui.QScreen'
        return PySide2.QtGui.QScreen
    
    def virtualSiblings(self):
        'virtualSiblings(self) -> typing.List'
        return typing.List
    
    def virtualSize(self):
        'virtualSize(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    

class QScrollEvent(_mod_PySide2_QtCore.QEvent):
    'QScrollEvent(self, contentPos:PySide2.QtCore.QPointF, overshoot:PySide2.QtCore.QPointF, scrollState:PySide2.QtGui.QScrollEvent.ScrollState)'
    ScrollFinished = ScrollState()
    ScrollStarted = ScrollState()
    ScrollState = ScrollState
    ScrollUpdated = ScrollState()
    __class__ = QScrollEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, contentPos: PySide2.QtCore.QPointF, overshoot: PySide2.QtCore.QPointF, scrollState: PySide2.QtGui.QScrollEvent.ScrollState):
        'QScrollEvent(self, contentPos:PySide2.QtCore.QPointF, overshoot:PySide2.QtCore.QPointF, scrollState:PySide2.QtGui.QScrollEvent.ScrollState)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def contentPos(self):
        'contentPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def overshootDistance(self):
        'overshootDistance(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def scrollState(self):
        'scrollState(self) -> PySide2.QtGui.QScrollEvent.ScrollState'
        return PySide2.QtGui.QScrollEvent.ScrollState
    

class QScrollPrepareEvent(_mod_PySide2_QtCore.QEvent):
    'QScrollPrepareEvent(self, startPos:PySide2.QtCore.QPointF)'
    __class__ = QScrollPrepareEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, startPos: PySide2.QtCore.QPointF):
        'QScrollPrepareEvent(self, startPos:PySide2.QtCore.QPointF)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def contentPos(self):
        'contentPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def contentPosRange(self):
        'contentPosRange(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def setContentPos(self, pos):
        'setContentPos(self, pos:PySide2.QtCore.QPointF)'
        pass
    
    def setContentPosRange(self, rect):
        'setContentPosRange(self, rect:PySide2.QtCore.QRectF)'
        pass
    
    def setViewportSize(self, size):
        'setViewportSize(self, size:PySide2.QtCore.QSizeF)'
        pass
    
    def startPos(self):
        'startPos(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def viewportSize(self):
        'viewportSize(self) -> PySide2.QtCore.QSizeF'
        return PySide2.QtCore.QSizeF
    

class QSessionManager(_mod_PySide2_QtCore.QObject):
    RestartAnyway = RestartHint()
    RestartHint = RestartHint
    RestartIfRunning = RestartHint()
    RestartImmediately = RestartHint()
    RestartNever = RestartHint()
    __class__ = QSessionManager
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def allowsErrorInteraction(self):
        'allowsErrorInteraction(self) -> bool'
        return bool
    
    def allowsInteraction(self):
        'allowsInteraction(self) -> bool'
        return bool
    
    def cancel(self):
        'cancel(self)'
        pass
    
    def discardCommand(self):
        'discardCommand(self) -> typing.List'
        return typing.List
    
    def isPhase2(self):
        'isPhase2(self) -> bool'
        return bool
    
    def release(self):
        'release(self)'
        pass
    
    def requestPhase2(self):
        'requestPhase2(self)'
        pass
    
    def restartCommand(self):
        'restartCommand(self) -> typing.List'
        return typing.List
    
    def restartHint(self):
        'restartHint(self) -> PySide2.QtGui.QSessionManager.RestartHint'
        return PySide2.QtGui.QSessionManager.RestartHint
    
    def sessionId(self):
        'sessionId(self) -> str'
        return str
    
    def sessionKey(self):
        'sessionKey(self) -> str'
        return str
    
    def setDiscardCommand(self, arg__1):
        'setDiscardCommand(self, arg__1:typing.Sequence)'
        pass
    
    def setManagerProperty(self, name: str, value: typing.Sequence):
        'setManagerProperty(self, name:str, value:str)\nsetManagerProperty(self, name:str, value:typing.Sequence)'
        pass
    
    def setRestartCommand(self, arg__1):
        'setRestartCommand(self, arg__1:typing.Sequence)'
        pass
    
    def setRestartHint(self, arg__1):
        'setRestartHint(self, arg__1:PySide2.QtGui.QSessionManager.RestartHint)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QShortcutEvent(_mod_PySide2_QtCore.QEvent):
    'QShortcutEvent(self, key:PySide2.QtGui.QKeySequence, id:int, ambiguous:bool=False)'
    __class__ = QShortcutEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, key: PySide2.QtGui.QKeySequence, id: int, ambiguous: bool=False):
        'QShortcutEvent(self, key:PySide2.QtGui.QKeySequence, id:int, ambiguous:bool=False)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def isAmbiguous(self):
        'isAmbiguous(self) -> bool'
        return bool
    
    def key(self):
        'key(self) -> PySide2.QtGui.QKeySequence'
        return PySide2.QtGui.QKeySequence
    
    def shortcutId(self):
        'shortcutId(self) -> int'
        return int
    

class QShowEvent(_mod_PySide2_QtCore.QEvent):
    'QShowEvent(self)'
    __class__ = QShowEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QShowEvent(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class QStandardItem(_mod_Shiboken.Object):
    'QStandardItem(self)\nQStandardItem(self, icon:PySide2.QtGui.QIcon, text:str)\nQStandardItem(self, other:PySide2.QtGui.QStandardItem)\nQStandardItem(self, rows:int, columns:int=1)\nQStandardItem(self, text:str)'
    ItemType = ItemType
    Type = ItemType()
    UserType = ItemType()
    __class__ = QStandardItem
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
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
    def __init__(self, icon: PySide2.QtGui.QIcon, text: str):
        'QStandardItem(self)\nQStandardItem(self, icon:PySide2.QtGui.QIcon, text:str)\nQStandardItem(self, other:PySide2.QtGui.QStandardItem)\nQStandardItem(self, rows:int, columns:int=1)\nQStandardItem(self, text:str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, out):
        '__lshift__(self, out:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QStandardItem()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QStandardItem()
    
    def __rshift__(self, in_):
        '__rshift__(self, in_:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def accessibleDescription(self):
        'accessibleDescription(self) -> str'
        return str
    
    def accessibleText(self):
        'accessibleText(self) -> str'
        return str
    
    def appendColumn(self, items):
        'appendColumn(self, items:typing.Sequence)'
        pass
    
    def appendRow(self, item: PySide2.QtGui.QStandardItem):
        'appendRow(self, item:PySide2.QtGui.QStandardItem)\nappendRow(self, items:typing.Sequence)'
        pass
    
    def appendRows(self, items):
        'appendRows(self, items:typing.Sequence)'
        pass
    
    def background(self):
        'background(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def checkState(self):
        'checkState(self) -> PySide2.QtCore.Qt.CheckState'
        return PySide2.QtCore.Qt.CheckState
    
    def child(self, row, column):
        'child(self, row:int, column:int=0) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def clearData(self):
        'clearData(self)'
        pass
    
    def clone(self):
        'clone(self) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def column(self):
        'column(self) -> int'
        return int
    
    def columnCount(self):
        'columnCount(self) -> int'
        return int
    
    def data(self, role):
        'data(self, role:int=257) -> typing.Any'
        return typing.Any
    
    def emitDataChanged(self):
        'emitDataChanged(self)'
        pass
    
    def flags(self):
        'flags(self) -> PySide2.QtCore.Qt.ItemFlags'
        return PySide2.QtCore.Qt.ItemFlags
    
    def font(self):
        'font(self) -> PySide2.QtGui.QFont'
        return PySide2.QtGui.QFont
    
    def foreground(self):
        'foreground(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def hasChildren(self):
        'hasChildren(self) -> bool'
        return bool
    
    def icon(self):
        'icon(self) -> PySide2.QtGui.QIcon'
        return PySide2.QtGui.QIcon
    
    def index(self):
        'index(self) -> PySide2.QtCore.QModelIndex'
        return PySide2.QtCore.QModelIndex
    
    def insertColumn(self, column, items):
        'insertColumn(self, column:int, items:typing.Sequence)'
        pass
    
    def insertColumns(self, column, count):
        'insertColumns(self, column:int, count:int)'
        pass
    
    def insertRow(self, row: int, item: PySide2.QtGui.QStandardItem):
        'insertRow(self, row:int, item:PySide2.QtGui.QStandardItem)\ninsertRow(self, row:int, items:typing.Sequence)'
        pass
    
    def insertRows(self, row: int, items: typing.Sequence):
        'insertRows(self, row:int, count:int)\ninsertRows(self, row:int, items:typing.Sequence)'
        pass
    
    def isAutoTristate(self):
        'isAutoTristate(self) -> bool'
        return bool
    
    def isCheckable(self):
        'isCheckable(self) -> bool'
        return bool
    
    def isDragEnabled(self):
        'isDragEnabled(self) -> bool'
        return bool
    
    def isDropEnabled(self):
        'isDropEnabled(self) -> bool'
        return bool
    
    def isEditable(self):
        'isEditable(self) -> bool'
        return bool
    
    def isEnabled(self):
        'isEnabled(self) -> bool'
        return bool
    
    def isSelectable(self):
        'isSelectable(self) -> bool'
        return bool
    
    def isTristate(self):
        'isTristate(self) -> bool'
        return bool
    
    def isUserTristate(self):
        'isUserTristate(self) -> bool'
        return bool
    
    def model(self):
        'model(self) -> PySide2.QtGui.QStandardItemModel'
        return PySide2.QtGui.QStandardItemModel
    
    def parent(self):
        'parent(self) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def read(self, in_):
        'read(self, in_:PySide2.QtCore.QDataStream)'
        pass
    
    def removeColumn(self, column):
        'removeColumn(self, column:int)'
        pass
    
    def removeColumns(self, column, count):
        'removeColumns(self, column:int, count:int)'
        pass
    
    def removeRow(self, row):
        'removeRow(self, row:int)'
        pass
    
    def removeRows(self, row, count):
        'removeRows(self, row:int, count:int)'
        pass
    
    def row(self):
        'row(self) -> int'
        return int
    
    def rowCount(self):
        'rowCount(self) -> int'
        return int
    
    def setAccessibleDescription(self, accessibleDescription):
        'setAccessibleDescription(self, accessibleDescription:str)'
        pass
    
    def setAccessibleText(self, accessibleText):
        'setAccessibleText(self, accessibleText:str)'
        pass
    
    def setAutoTristate(self, tristate):
        'setAutoTristate(self, tristate:bool)'
        pass
    
    def setBackground(self, brush):
        'setBackground(self, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setCheckState(self, checkState):
        'setCheckState(self, checkState:PySide2.QtCore.Qt.CheckState)'
        pass
    
    def setCheckable(self, checkable):
        'setCheckable(self, checkable:bool)'
        pass
    
    def setChild(self, row: int, column: int, item: PySide2.QtGui.QStandardItem):
        'setChild(self, row:int, column:int, item:PySide2.QtGui.QStandardItem)\nsetChild(self, row:int, item:PySide2.QtGui.QStandardItem)'
        pass
    
    def setColumnCount(self, columns):
        'setColumnCount(self, columns:int)'
        pass
    
    def setData(self, value, role):
        'setData(self, value:typing.Any, role:int=257)'
        pass
    
    def setDragEnabled(self, dragEnabled):
        'setDragEnabled(self, dragEnabled:bool)'
        pass
    
    def setDropEnabled(self, dropEnabled):
        'setDropEnabled(self, dropEnabled:bool)'
        pass
    
    def setEditable(self, editable):
        'setEditable(self, editable:bool)'
        pass
    
    def setEnabled(self, enabled):
        'setEnabled(self, enabled:bool)'
        pass
    
    def setFlags(self, flags):
        'setFlags(self, flags:PySide2.QtCore.Qt.ItemFlags)'
        pass
    
    def setFont(self, font):
        'setFont(self, font:PySide2.QtGui.QFont)'
        pass
    
    def setForeground(self, brush):
        'setForeground(self, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setIcon(self, icon):
        'setIcon(self, icon:PySide2.QtGui.QIcon)'
        pass
    
    def setRowCount(self, rows):
        'setRowCount(self, rows:int)'
        pass
    
    def setSelectable(self, selectable):
        'setSelectable(self, selectable:bool)'
        pass
    
    def setSizeHint(self, sizeHint):
        'setSizeHint(self, sizeHint:PySide2.QtCore.QSize)'
        pass
    
    def setStatusTip(self, statusTip):
        'setStatusTip(self, statusTip:str)'
        pass
    
    def setText(self, text):
        'setText(self, text:str)'
        pass
    
    def setTextAlignment(self, textAlignment):
        'setTextAlignment(self, textAlignment:PySide2.QtCore.Qt.Alignment)'
        pass
    
    def setToolTip(self, toolTip):
        'setToolTip(self, toolTip:str)'
        pass
    
    def setTristate(self, tristate):
        'setTristate(self, tristate:bool)'
        pass
    
    def setUserTristate(self, tristate):
        'setUserTristate(self, tristate:bool)'
        pass
    
    def setWhatsThis(self, whatsThis):
        'setWhatsThis(self, whatsThis:str)'
        pass
    
    def sizeHint(self):
        'sizeHint(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def sortChildren(self, column, order):
        'sortChildren(self, column:int, order:PySide2.QtCore.Qt.SortOrder=PySide2.QtCore.Qt.SortOrder.AscendingOrder)'
        pass
    
    def statusTip(self):
        'statusTip(self) -> str'
        return str
    
    def takeChild(self, row, column):
        'takeChild(self, row:int, column:int=0) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def takeColumn(self, column):
        'takeColumn(self, column:int) -> typing.List'
        return typing.List
    
    def takeRow(self, row):
        'takeRow(self, row:int) -> typing.List'
        return typing.List
    
    def text(self):
        'text(self) -> str'
        return str
    
    def textAlignment(self):
        'textAlignment(self) -> PySide2.QtCore.Qt.Alignment'
        return PySide2.QtCore.Qt.Alignment
    
    def toolTip(self):
        'toolTip(self) -> str'
        return str
    
    def type(self):
        'type(self) -> int'
        return int
    
    def whatsThis(self):
        'whatsThis(self) -> str'
        return str
    
    def write(self, out):
        'write(self, out:PySide2.QtCore.QDataStream)'
        pass
    

class QStandardItemModel(_mod_PySide2_QtCore.QAbstractItemModel):
    'QStandardItemModel(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQStandardItemModel(self, rows:int, columns:int, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    __class__ = QStandardItemModel
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, rows: int, columns: int, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QStandardItemModel(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQStandardItemModel(self, rows:int, columns:int, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def appendColumn(self, items):
        'appendColumn(self, items:typing.Sequence)'
        pass
    
    def appendRow(self, item: PySide2.QtGui.QStandardItem):
        'appendRow(self, item:PySide2.QtGui.QStandardItem)\nappendRow(self, items:typing.Sequence)'
        pass
    
    def clear(self):
        'clear(self)'
        pass
    
    def clearItemData(self, index):
        'clearItemData(self, index:PySide2.QtCore.QModelIndex) -> bool'
        return bool
    
    def columnCount(self, parent):
        'columnCount(self, parent:PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)) -> int'
        return int
    
    def data(self, index, role):
        'data(self, index:PySide2.QtCore.QModelIndex, role:int=PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any'
        return typing.Any
    
    def dropMimeData(self, data, action, row, column, parent):
        'dropMimeData(self, data:PySide2.QtCore.QMimeData, action:PySide2.QtCore.Qt.DropAction, row:int, column:int, parent:PySide2.QtCore.QModelIndex) -> bool'
        return bool
    
    def findItems(self, text, flags, column):
        'findItems(self, text:str, flags:PySide2.QtCore.Qt.MatchFlags=PySide2.QtCore.Qt.MatchFlag.MatchExactly, column:int=0) -> typing.List'
        return typing.List
    
    def flags(self, index):
        'flags(self, index:PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags'
        return PySide2.QtCore.Qt.ItemFlags
    
    def hasChildren(self, parent):
        'hasChildren(self, parent:PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)) -> bool'
        return bool
    
    def headerData(self, section, orientation, role):
        'headerData(self, section:int, orientation:PySide2.QtCore.Qt.Orientation, role:int=PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any'
        return typing.Any
    
    def horizontalHeaderItem(self, column):
        'horizontalHeaderItem(self, column:int) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def index(self, row, column, parent):
        'index(self, row:int, column:int, parent:PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)) -> PySide2.QtCore.QModelIndex'
        return PySide2.QtCore.QModelIndex
    
    def indexFromItem(self, item):
        'indexFromItem(self, item:PySide2.QtGui.QStandardItem) -> PySide2.QtCore.QModelIndex'
        return PySide2.QtCore.QModelIndex
    
    def insertColumn(self, column: int, parent: PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)):
        'insertColumn(self, column:int, items:typing.Sequence)\ninsertColumn(self, column:int, parent:PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)) -> bool'
        pass
    
    def insertColumns(self, column, count, parent):
        'insertColumns(self, column:int, count:int, parent:PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)) -> bool'
        return bool
    
    def insertRow(self, row: int, parent: PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)):
        'insertRow(self, row:int, item:PySide2.QtGui.QStandardItem)\ninsertRow(self, row:int, items:typing.Sequence)\ninsertRow(self, row:int, parent:PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)) -> bool'
        pass
    
    def insertRows(self, row, count, parent):
        'insertRows(self, row:int, count:int, parent:PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)) -> bool'
        return bool
    
    def invisibleRootItem(self):
        'invisibleRootItem(self) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def item(self, row, column):
        'item(self, row:int, column:int=0) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def itemChanged(self):
        pass
    
    def itemData(self, index):
        'itemData(self, index:PySide2.QtCore.QModelIndex) -> typing.Dict'
        return typing.Dict
    
    def itemFromIndex(self, index):
        'itemFromIndex(self, index:PySide2.QtCore.QModelIndex) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def itemPrototype(self):
        'itemPrototype(self) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def mimeData(self, indexes):
        'mimeData(self, indexes:typing.List) -> PySide2.QtCore.QMimeData'
        return PySide2.QtCore.QMimeData
    
    def mimeTypes(self):
        'mimeTypes(self) -> typing.List'
        return typing.List
    
    def parent(self, child: PySide2.QtCore.QModelIndex):
        'parent(self) -> PySide2.QtCore.QObject\nparent(self, child:PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex'
        pass
    
    def removeColumns(self, column, count, parent):
        'removeColumns(self, column:int, count:int, parent:PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)) -> bool'
        return bool
    
    def removeRows(self, row, count, parent):
        'removeRows(self, row:int, count:int, parent:PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)) -> bool'
        return bool
    
    def rowCount(self, parent):
        'rowCount(self, parent:PySide2.QtCore.QModelIndex=Invalid(PySide2.QtCore.QModelIndex)) -> int'
        return int
    
    def setColumnCount(self, columns):
        'setColumnCount(self, columns:int)'
        pass
    
    def setData(self, index, value, role):
        'setData(self, index:PySide2.QtCore.QModelIndex, value:typing.Any, role:int=PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool'
        return bool
    
    def setHeaderData(self, section, orientation, value, role):
        'setHeaderData(self, section:int, orientation:PySide2.QtCore.Qt.Orientation, value:typing.Any, role:int=PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool'
        return bool
    
    def setHorizontalHeaderItem(self, column, item):
        'setHorizontalHeaderItem(self, column:int, item:PySide2.QtGui.QStandardItem)'
        pass
    
    def setHorizontalHeaderLabels(self, labels):
        'setHorizontalHeaderLabels(self, labels:typing.Sequence)'
        pass
    
    def setItem(self, row: int, column: int, item: PySide2.QtGui.QStandardItem):
        'setItem(self, row:int, column:int, item:PySide2.QtGui.QStandardItem)\nsetItem(self, row:int, item:PySide2.QtGui.QStandardItem)'
        pass
    
    def setItemData(self, index, roles):
        'setItemData(self, index:PySide2.QtCore.QModelIndex, roles:typing.Dict) -> bool'
        return bool
    
    def setItemPrototype(self, item):
        'setItemPrototype(self, item:PySide2.QtGui.QStandardItem)'
        pass
    
    def setItemRoleNames(self, roleNames):
        'setItemRoleNames(self, roleNames:typing.Dict)'
        pass
    
    def setRowCount(self, rows):
        'setRowCount(self, rows:int)'
        pass
    
    def setSortRole(self, role):
        'setSortRole(self, role:int)'
        pass
    
    def setVerticalHeaderItem(self, row, item):
        'setVerticalHeaderItem(self, row:int, item:PySide2.QtGui.QStandardItem)'
        pass
    
    def setVerticalHeaderLabels(self, labels):
        'setVerticalHeaderLabels(self, labels:typing.Sequence)'
        pass
    
    def sibling(self, row, column, idx):
        'sibling(self, row:int, column:int, idx:PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex'
        return PySide2.QtCore.QModelIndex
    
    def sort(self, column, order):
        'sort(self, column:int, order:PySide2.QtCore.Qt.SortOrder=PySide2.QtCore.Qt.SortOrder.AscendingOrder)'
        pass
    
    def sortRole(self):
        'sortRole(self) -> int'
        return int
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def supportedDropActions(self):
        'supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions'
        return PySide2.QtCore.Qt.DropActions
    
    def takeColumn(self, column):
        'takeColumn(self, column:int) -> typing.List'
        return typing.List
    
    def takeHorizontalHeaderItem(self, column):
        'takeHorizontalHeaderItem(self, column:int) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def takeItem(self, row, column):
        'takeItem(self, row:int, column:int=0) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def takeRow(self, row):
        'takeRow(self, row:int) -> typing.List'
        return typing.List
    
    def takeVerticalHeaderItem(self, row):
        'takeVerticalHeaderItem(self, row:int) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    
    def verticalHeaderItem(self, row):
        'verticalHeaderItem(self, row:int) -> PySide2.QtGui.QStandardItem'
        return PySide2.QtGui.QStandardItem
    

class QStaticText(_mod_Shiboken.Object):
    'QStaticText(self)\nQStaticText(self, other:PySide2.QtGui.QStaticText)\nQStaticText(self, text:str)'
    AggressiveCaching = PerformanceHint()
    ModerateCaching = PerformanceHint()
    PerformanceHint = PerformanceHint
    __class__ = QStaticText
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, other: PySide2.QtGui.QStaticText):
        'QStaticText(self)\nQStaticText(self, other:PySide2.QtGui.QStaticText)\nQStaticText(self, text:str)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def performanceHint(self):
        'performanceHint(self) -> PySide2.QtGui.QStaticText.PerformanceHint'
        return PySide2.QtGui.QStaticText.PerformanceHint
    
    def prepare(self, matrix, font):
        'prepare(self, matrix:PySide2.QtGui.QTransform=Default(QTransform), font:PySide2.QtGui.QFont=Default(QFont))'
        pass
    
    def setPerformanceHint(self, performanceHint):
        'setPerformanceHint(self, performanceHint:PySide2.QtGui.QStaticText.PerformanceHint)'
        pass
    
    def setText(self, text):
        'setText(self, text:str)'
        pass
    
    def setTextFormat(self, textFormat):
        'setTextFormat(self, textFormat:PySide2.QtCore.Qt.TextFormat)'
        pass
    
    def setTextOption(self, textOption):
        'setTextOption(self, textOption:PySide2.QtGui.QTextOption)'
        pass
    
    def setTextWidth(self, textWidth):
        'setTextWidth(self, textWidth:float)'
        pass
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSizeF'
        return PySide2.QtCore.QSizeF
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QStaticText)'
        pass
    
    def text(self):
        'text(self) -> str'
        return str
    
    def textFormat(self):
        'textFormat(self) -> PySide2.QtCore.Qt.TextFormat'
        return PySide2.QtCore.Qt.TextFormat
    
    def textOption(self):
        'textOption(self) -> PySide2.QtGui.QTextOption'
        return PySide2.QtGui.QTextOption
    
    def textWidth(self):
        'textWidth(self) -> float'
        return float
    

class QStatusTipEvent(_mod_PySide2_QtCore.QEvent):
    'QStatusTipEvent(self, tip:str)'
    __class__ = QStatusTipEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, tip: str):
        'QStatusTipEvent(self, tip:str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def tip(self):
        'tip(self) -> str'
        return str
    

class QStyleHints(_mod_PySide2_QtCore.QObject):
    __class__ = QStyleHints
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def cursorFlashTime(self):
        'cursorFlashTime(self) -> int'
        return int
    
    def cursorFlashTimeChanged(self):
        pass
    
    def fontSmoothingGamma(self):
        'fontSmoothingGamma(self) -> float'
        return float
    
    def keyboardAutoRepeatRate(self):
        'keyboardAutoRepeatRate(self) -> int'
        return int
    
    def keyboardInputInterval(self):
        'keyboardInputInterval(self) -> int'
        return int
    
    def keyboardInputIntervalChanged(self):
        pass
    
    def mouseDoubleClickDistance(self):
        'mouseDoubleClickDistance(self) -> int'
        return int
    
    def mouseDoubleClickInterval(self):
        'mouseDoubleClickInterval(self) -> int'
        return int
    
    def mouseDoubleClickIntervalChanged(self):
        pass
    
    def mousePressAndHoldInterval(self):
        'mousePressAndHoldInterval(self) -> int'
        return int
    
    def mousePressAndHoldIntervalChanged(self):
        pass
    
    def mouseQuickSelectionThreshold(self):
        'mouseQuickSelectionThreshold(self) -> int'
        return int
    
    def mouseQuickSelectionThresholdChanged(self):
        pass
    
    def passwordMaskCharacter(self):
        'passwordMaskCharacter(self) -> str'
        return str
    
    def passwordMaskDelay(self):
        'passwordMaskDelay(self) -> int'
        return int
    
    def setCursorFlashTime(self, cursorFlashTime):
        'setCursorFlashTime(self, cursorFlashTime:int)'
        pass
    
    def setFocusOnTouchRelease(self):
        'setFocusOnTouchRelease(self) -> bool'
        return bool
    
    def setKeyboardInputInterval(self, keyboardInputInterval):
        'setKeyboardInputInterval(self, keyboardInputInterval:int)'
        pass
    
    def setMouseDoubleClickInterval(self, mouseDoubleClickInterval):
        'setMouseDoubleClickInterval(self, mouseDoubleClickInterval:int)'
        pass
    
    def setMousePressAndHoldInterval(self, mousePressAndHoldInterval):
        'setMousePressAndHoldInterval(self, mousePressAndHoldInterval:int)'
        pass
    
    def setMouseQuickSelectionThreshold(self, threshold):
        'setMouseQuickSelectionThreshold(self, threshold:int)'
        pass
    
    def setShowShortcutsInContextMenus(self, showShortcutsInContextMenus):
        'setShowShortcutsInContextMenus(self, showShortcutsInContextMenus:bool)'
        pass
    
    def setStartDragDistance(self, startDragDistance):
        'setStartDragDistance(self, startDragDistance:int)'
        pass
    
    def setStartDragTime(self, startDragTime):
        'setStartDragTime(self, startDragTime:int)'
        pass
    
    def setTabFocusBehavior(self, tabFocusBehavior):
        'setTabFocusBehavior(self, tabFocusBehavior:PySide2.QtCore.Qt.TabFocusBehavior)'
        pass
    
    def setUseHoverEffects(self, useHoverEffects):
        'setUseHoverEffects(self, useHoverEffects:bool)'
        pass
    
    def setWheelScrollLines(self, scrollLines):
        'setWheelScrollLines(self, scrollLines:int)'
        pass
    
    def showIsFullScreen(self):
        'showIsFullScreen(self) -> bool'
        return bool
    
    def showIsMaximized(self):
        'showIsMaximized(self) -> bool'
        return bool
    
    def showShortcutsInContextMenus(self):
        'showShortcutsInContextMenus(self) -> bool'
        return bool
    
    def showShortcutsInContextMenusChanged(self):
        pass
    
    def singleClickActivation(self):
        'singleClickActivation(self) -> bool'
        return bool
    
    def startDragDistance(self):
        'startDragDistance(self) -> int'
        return int
    
    def startDragDistanceChanged(self):
        pass
    
    def startDragTime(self):
        'startDragTime(self) -> int'
        return int
    
    def startDragTimeChanged(self):
        pass
    
    def startDragVelocity(self):
        'startDragVelocity(self) -> int'
        return int
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def tabFocusBehavior(self):
        'tabFocusBehavior(self) -> PySide2.QtCore.Qt.TabFocusBehavior'
        return PySide2.QtCore.Qt.TabFocusBehavior
    
    def tabFocusBehaviorChanged(self):
        pass
    
    def touchDoubleTapDistance(self):
        'touchDoubleTapDistance(self) -> int'
        return int
    
    def useHoverEffects(self):
        'useHoverEffects(self) -> bool'
        return bool
    
    def useHoverEffectsChanged(self):
        pass
    
    def useRtlExtensions(self):
        'useRtlExtensions(self) -> bool'
        return bool
    
    def wheelScrollLines(self):
        'wheelScrollLines(self) -> int'
        return int
    
    def wheelScrollLinesChanged(self):
        pass
    

class QSurface(_mod_Shiboken.Object):
    'QSurface(self, type:PySide2.QtGui.QSurface.SurfaceClass)'
    MetalSurface = SurfaceType()
    Offscreen = SurfaceClass()
    OpenGLSurface = SurfaceType()
    OpenVGSurface = SurfaceType()
    RasterGLSurface = SurfaceType()
    RasterSurface = SurfaceType()
    SurfaceClass = SurfaceClass
    SurfaceType = SurfaceType
    VulkanSurface = SurfaceType()
    Window = SurfaceClass()
    __class__ = QSurface
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, type: PySide2.QtGui.QSurface.SurfaceClass):
        'QSurface(self, type:PySide2.QtGui.QSurface.SurfaceClass)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def format(self):
        'format(self) -> PySide2.QtGui.QSurfaceFormat'
        return PySide2.QtGui.QSurfaceFormat
    
    @property
    def m_type(self):
        pass
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def supportsOpenGL(self):
        'supportsOpenGL(self) -> bool'
        return bool
    
    def surfaceClass(self):
        'surfaceClass(self) -> PySide2.QtGui.QSurface.SurfaceClass'
        return PySide2.QtGui.QSurface.SurfaceClass
    
    def surfaceHandle(self):
        'surfaceHandle(self) -> int'
        return int
    
    def surfaceType(self):
        'surfaceType(self) -> PySide2.QtGui.QSurface.SurfaceType'
        return PySide2.QtGui.QSurface.SurfaceType
    

class QSurfaceFormat(_mod_Shiboken.Object):
    'QSurfaceFormat(self)\nQSurfaceFormat(self, options:PySide2.QtGui.QSurfaceFormat.FormatOptions)\nQSurfaceFormat(self, other:PySide2.QtGui.QSurfaceFormat)'
    ColorSpace = ColorSpace
    CompatibilityProfile = OpenGLContextProfile()
    CoreProfile = OpenGLContextProfile()
    DebugContext = FormatOption()
    DefaultColorSpace = ColorSpace()
    DefaultRenderableType = RenderableType()
    DefaultSwapBehavior = SwapBehavior()
    DeprecatedFunctions = FormatOption()
    DoubleBuffer = SwapBehavior()
    FormatOption = FormatOption
    FormatOptions = FormatOptions
    NoProfile = OpenGLContextProfile()
    OpenGL = RenderableType()
    OpenGLContextProfile = OpenGLContextProfile
    OpenGLES = RenderableType()
    OpenVG = RenderableType()
    RenderableType = RenderableType
    ResetNotification = FormatOption()
    SingleBuffer = SwapBehavior()
    StereoBuffers = FormatOption()
    SwapBehavior = SwapBehavior
    TripleBuffer = SwapBehavior()
    __class__ = QSurfaceFormat
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, options: PySide2.QtGui.QSurfaceFormat.FormatOptions):
        'QSurfaceFormat(self)\nQSurfaceFormat(self, options:PySide2.QtGui.QSurfaceFormat.FormatOptions)\nQSurfaceFormat(self, other:PySide2.QtGui.QSurfaceFormat)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def alphaBufferSize(self):
        'alphaBufferSize(self) -> int'
        return int
    
    def blueBufferSize(self):
        'blueBufferSize(self) -> int'
        return int
    
    def colorSpace(self):
        'colorSpace(self) -> PySide2.QtGui.QSurfaceFormat.ColorSpace'
        return PySide2.QtGui.QSurfaceFormat.ColorSpace
    
    @classmethod
    def defaultFormat(cls):
        'defaultFormat() -> PySide2.QtGui.QSurfaceFormat'
        return PySide2.QtGui.QSurfaceFormat
    
    def depthBufferSize(self):
        'depthBufferSize(self) -> int'
        return int
    
    def greenBufferSize(self):
        'greenBufferSize(self) -> int'
        return int
    
    def hasAlpha(self):
        'hasAlpha(self) -> bool'
        return bool
    
    def majorVersion(self):
        'majorVersion(self) -> int'
        return int
    
    def minorVersion(self):
        'minorVersion(self) -> int'
        return int
    
    def options(self):
        'options(self) -> PySide2.QtGui.QSurfaceFormat.FormatOptions'
        return PySide2.QtGui.QSurfaceFormat.FormatOptions
    
    def profile(self):
        'profile(self) -> PySide2.QtGui.QSurfaceFormat.OpenGLContextProfile'
        return PySide2.QtGui.QSurfaceFormat.OpenGLContextProfile
    
    def redBufferSize(self):
        'redBufferSize(self) -> int'
        return int
    
    def renderableType(self):
        'renderableType(self) -> PySide2.QtGui.QSurfaceFormat.RenderableType'
        return PySide2.QtGui.QSurfaceFormat.RenderableType
    
    sRGBColorSpace = ColorSpace()
    def samples(self):
        'samples(self) -> int'
        return int
    
    def setAlphaBufferSize(self, size):
        'setAlphaBufferSize(self, size:int)'
        pass
    
    def setBlueBufferSize(self, size):
        'setBlueBufferSize(self, size:int)'
        pass
    
    def setColorSpace(self, colorSpace):
        'setColorSpace(self, colorSpace:PySide2.QtGui.QSurfaceFormat.ColorSpace)'
        pass
    
    @classmethod
    def setDefaultFormat(cls, format):
        'setDefaultFormat(format:PySide2.QtGui.QSurfaceFormat)'
        pass
    
    def setDepthBufferSize(self, size):
        'setDepthBufferSize(self, size:int)'
        pass
    
    def setGreenBufferSize(self, size):
        'setGreenBufferSize(self, size:int)'
        pass
    
    def setMajorVersion(self, majorVersion):
        'setMajorVersion(self, majorVersion:int)'
        pass
    
    def setMinorVersion(self, minorVersion):
        'setMinorVersion(self, minorVersion:int)'
        pass
    
    def setOption(self, option: PySide2.QtGui.QSurfaceFormat.FormatOption, on: bool=True):
        'setOption(self, opt:PySide2.QtGui.QSurfaceFormat.FormatOptions)\nsetOption(self, option:PySide2.QtGui.QSurfaceFormat.FormatOption, on:bool=True)'
        pass
    
    def setOptions(self, options):
        'setOptions(self, options:PySide2.QtGui.QSurfaceFormat.FormatOptions)'
        pass
    
    def setProfile(self, profile):
        'setProfile(self, profile:PySide2.QtGui.QSurfaceFormat.OpenGLContextProfile)'
        pass
    
    def setRedBufferSize(self, size):
        'setRedBufferSize(self, size:int)'
        pass
    
    def setRenderableType(self, type):
        'setRenderableType(self, type:PySide2.QtGui.QSurfaceFormat.RenderableType)'
        pass
    
    def setSamples(self, numSamples):
        'setSamples(self, numSamples:int)'
        pass
    
    def setStencilBufferSize(self, size):
        'setStencilBufferSize(self, size:int)'
        pass
    
    def setStereo(self, enable):
        'setStereo(self, enable:bool)'
        pass
    
    def setSwapBehavior(self, behavior):
        'setSwapBehavior(self, behavior:PySide2.QtGui.QSurfaceFormat.SwapBehavior)'
        pass
    
    def setSwapInterval(self, interval):
        'setSwapInterval(self, interval:int)'
        pass
    
    def setVersion(self, major, minor):
        'setVersion(self, major:int, minor:int)'
        pass
    
    def stencilBufferSize(self):
        'stencilBufferSize(self) -> int'
        return int
    
    def stereo(self):
        'stereo(self) -> bool'
        return bool
    
    def swapBehavior(self):
        'swapBehavior(self) -> PySide2.QtGui.QSurfaceFormat.SwapBehavior'
        return PySide2.QtGui.QSurfaceFormat.SwapBehavior
    
    def swapInterval(self):
        'swapInterval(self) -> int'
        return int
    
    def testOption(self, option: PySide2.QtGui.QSurfaceFormat.FormatOption):
        'testOption(self, opt:PySide2.QtGui.QSurfaceFormat.FormatOptions) -> bool\ntestOption(self, option:PySide2.QtGui.QSurfaceFormat.FormatOption) -> bool'
        return True
    
    def version(self):
        'version(self) -> typing.Tuple'
        return typing.Tuple
    

class QSyntaxHighlighter(_mod_PySide2_QtCore.QObject):
    'QSyntaxHighlighter(self, parent:PySide2.QtCore.QObject)\nQSyntaxHighlighter(self, parent:PySide2.QtGui.QTextDocument)'
    __class__ = QSyntaxHighlighter
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, parent: PySide2.QtGui.QTextDocument):
        'QSyntaxHighlighter(self, parent:PySide2.QtCore.QObject)\nQSyntaxHighlighter(self, parent:PySide2.QtGui.QTextDocument)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def currentBlock(self):
        'currentBlock(self) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def currentBlockState(self):
        'currentBlockState(self) -> int'
        return int
    
    def currentBlockUserData(self):
        'currentBlockUserData(self) -> PySide2.QtGui.QTextBlockUserData'
        return PySide2.QtGui.QTextBlockUserData
    
    def document(self):
        'document(self) -> PySide2.QtGui.QTextDocument'
        return PySide2.QtGui.QTextDocument
    
    def format(self, pos):
        'format(self, pos:int) -> PySide2.QtGui.QTextCharFormat'
        return PySide2.QtGui.QTextCharFormat
    
    def highlightBlock(self, text):
        'highlightBlock(self, text:str)'
        pass
    
    def previousBlockState(self):
        'previousBlockState(self) -> int'
        return int
    
    def rehighlight(self):
        'rehighlight(self)'
        pass
    
    def rehighlightBlock(self, block):
        'rehighlightBlock(self, block:PySide2.QtGui.QTextBlock)'
        pass
    
    def setCurrentBlockState(self, newState):
        'setCurrentBlockState(self, newState:int)'
        pass
    
    def setCurrentBlockUserData(self, data):
        'setCurrentBlockUserData(self, data:PySide2.QtGui.QTextBlockUserData)'
        pass
    
    def setDocument(self, doc):
        'setDocument(self, doc:PySide2.QtGui.QTextDocument)'
        pass
    
    def setFormat(self, start: int, count: int, format: PySide2.QtGui.QTextCharFormat):
        'setFormat(self, start:int, count:int, color:PySide2.QtGui.QColor)\nsetFormat(self, start:int, count:int, font:PySide2.QtGui.QFont)\nsetFormat(self, start:int, count:int, format:PySide2.QtGui.QTextCharFormat)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QTabletEvent(QInputEvent):
    'QTabletEvent(self, t:PySide2.QtCore.QEvent.Type, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, device:int, pointerType:int, pressure:float, xTilt:int, yTilt:int, tangentialPressure:float, rotation:float, z:int, keyState:PySide2.QtCore.Qt.KeyboardModifiers, uniqueID:int)\nQTabletEvent(self, t:PySide2.QtCore.QEvent.Type, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, device:int, pointerType:int, pressure:float, xTilt:int, yTilt:int, tangentialPressure:float, rotation:float, z:int, keyState:PySide2.QtCore.Qt.KeyboardModifiers, uniqueID:int, button:PySide2.QtCore.Qt.MouseButton, buttons:PySide2.QtCore.Qt.MouseButtons)'
    Airbrush = TabletDevice()
    Cursor = PointerType()
    Eraser = PointerType()
    FourDMouse = TabletDevice()
    NoDevice = TabletDevice()
    Pen = PointerType()
    PointerType = PointerType
    Puck = TabletDevice()
    RotationStylus = TabletDevice()
    Stylus = TabletDevice()
    TabletDevice = TabletDevice
    UnknownPointer = PointerType()
    XFreeEraser = TabletDevice()
    __class__ = QTabletEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, t: PySide2.QtCore.QEvent.Type, pos: PySide2.QtCore.QPointF, globalPos: PySide2.QtCore.QPointF, device: int, pointerType: int, pressure: float, xTilt: int, yTilt: int, tangentialPressure: float, rotation: float, z: int, keyState: PySide2.QtCore.Qt.KeyboardModifiers, uniqueID: int, button: PySide2.QtCore.Qt.MouseButton, buttons: PySide2.QtCore.Qt.MouseButtons):
        'QTabletEvent(self, t:PySide2.QtCore.QEvent.Type, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, device:int, pointerType:int, pressure:float, xTilt:int, yTilt:int, tangentialPressure:float, rotation:float, z:int, keyState:PySide2.QtCore.Qt.KeyboardModifiers, uniqueID:int)\nQTabletEvent(self, t:PySide2.QtCore.QEvent.Type, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, device:int, pointerType:int, pressure:float, xTilt:int, yTilt:int, tangentialPressure:float, rotation:float, z:int, keyState:PySide2.QtCore.Qt.KeyboardModifiers, uniqueID:int, button:PySide2.QtCore.Qt.MouseButton, buttons:PySide2.QtCore.Qt.MouseButtons)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def button(self):
        'button(self) -> PySide2.QtCore.Qt.MouseButton'
        return PySide2.QtCore.Qt.MouseButton
    
    def buttons(self):
        'buttons(self) -> PySide2.QtCore.Qt.MouseButtons'
        return PySide2.QtCore.Qt.MouseButtons
    
    def device(self):
        'device(self) -> PySide2.QtGui.QTabletEvent.TabletDevice'
        return PySide2.QtGui.QTabletEvent.TabletDevice
    
    def deviceType(self):
        'deviceType(self) -> PySide2.QtGui.QTabletEvent.TabletDevice'
        return PySide2.QtGui.QTabletEvent.TabletDevice
    
    def globalPos(self):
        'globalPos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def globalPosF(self):
        'globalPosF(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def globalX(self):
        'globalX(self) -> int'
        return int
    
    def globalY(self):
        'globalY(self) -> int'
        return int
    
    def hiResGlobalX(self):
        'hiResGlobalX(self) -> float'
        return float
    
    def hiResGlobalY(self):
        'hiResGlobalY(self) -> float'
        return float
    
    def pointerType(self):
        'pointerType(self) -> PySide2.QtGui.QTabletEvent.PointerType'
        return PySide2.QtGui.QTabletEvent.PointerType
    
    def pos(self):
        'pos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def posF(self):
        'posF(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def pressure(self):
        'pressure(self) -> float'
        return float
    
    def rotation(self):
        'rotation(self) -> float'
        return float
    
    def tangentialPressure(self):
        'tangentialPressure(self) -> float'
        return float
    
    def uniqueId(self):
        'uniqueId(self) -> int'
        return int
    
    def x(self):
        'x(self) -> int'
        return int
    
    def xTilt(self):
        'xTilt(self) -> int'
        return int
    
    def y(self):
        'y(self) -> int'
        return int
    
    def yTilt(self):
        'yTilt(self) -> int'
        return int
    
    def z(self):
        'z(self) -> int'
        return int
    

class QTextBlock(_mod_Shiboken.Object):
    'QTextBlock(self)\nQTextBlock(self, o:PySide2.QtGui.QTextBlock)'
    __class__ = QTextBlock
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, o: PySide2.QtGui.QTextBlock):
        'QTextBlock(self)\nQTextBlock(self, o:PySide2.QtGui.QTextBlock)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        '__iter__(self) -> object\n\nImplement iter(self).'
        return object
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def begin(self):
        'begin(self) -> PySide2.QtGui.QTextBlock.iterator'
        return PySide2.QtGui.QTextBlock.iterator
    
    def blockFormat(self):
        'blockFormat(self) -> PySide2.QtGui.QTextBlockFormat'
        return PySide2.QtGui.QTextBlockFormat
    
    def blockFormatIndex(self):
        'blockFormatIndex(self) -> int'
        return int
    
    def blockNumber(self):
        'blockNumber(self) -> int'
        return int
    
    def charFormat(self):
        'charFormat(self) -> PySide2.QtGui.QTextCharFormat'
        return PySide2.QtGui.QTextCharFormat
    
    def charFormatIndex(self):
        'charFormatIndex(self) -> int'
        return int
    
    def clearLayout(self):
        'clearLayout(self)'
        pass
    
    def contains(self, position):
        'contains(self, position:int) -> bool'
        return bool
    
    def document(self):
        'document(self) -> PySide2.QtGui.QTextDocument'
        return PySide2.QtGui.QTextDocument
    
    def end(self):
        'end(self) -> PySide2.QtGui.QTextBlock.iterator'
        return PySide2.QtGui.QTextBlock.iterator
    
    def firstLineNumber(self):
        'firstLineNumber(self) -> int'
        return int
    
    def fragmentIndex(self):
        'fragmentIndex(self) -> int'
        return int
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def isVisible(self):
        'isVisible(self) -> bool'
        return bool
    
    iterator = iterator
    def layout(self):
        'layout(self) -> PySide2.QtGui.QTextLayout'
        return PySide2.QtGui.QTextLayout
    
    def length(self):
        'length(self) -> int'
        return int
    
    def lineCount(self):
        'lineCount(self) -> int'
        return int
    
    def next(self):
        'next(self) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def position(self):
        'position(self) -> int'
        return int
    
    def previous(self):
        'previous(self) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def revision(self):
        'revision(self) -> int'
        return int
    
    def setLineCount(self, count):
        'setLineCount(self, count:int)'
        pass
    
    def setRevision(self, rev):
        'setRevision(self, rev:int)'
        pass
    
    def setUserData(self, data):
        'setUserData(self, data:PySide2.QtGui.QTextBlockUserData)'
        pass
    
    def setUserState(self, state):
        'setUserState(self, state:int)'
        pass
    
    def setVisible(self, visible):
        'setVisible(self, visible:bool)'
        pass
    
    def text(self):
        'text(self) -> str'
        return str
    
    def textDirection(self):
        'textDirection(self) -> PySide2.QtCore.Qt.LayoutDirection'
        return PySide2.QtCore.Qt.LayoutDirection
    
    def textFormats(self):
        'textFormats(self) -> typing.List'
        return typing.List
    
    def textList(self):
        'textList(self) -> PySide2.QtGui.QTextList'
        return PySide2.QtGui.QTextList
    
    def userData(self):
        'userData(self) -> PySide2.QtGui.QTextBlockUserData'
        return PySide2.QtGui.QTextBlockUserData
    
    def userState(self):
        'userState(self) -> int'
        return int
    

class QTextBlockFormat(QTextFormat):
    'QTextBlockFormat(self)\nQTextBlockFormat(self, QTextBlockFormat:PySide2.QtGui.QTextBlockFormat)\nQTextBlockFormat(self, fmt:PySide2.QtGui.QTextFormat)'
    FixedHeight = LineHeightTypes()
    LineDistanceHeight = LineHeightTypes()
    LineHeightTypes = LineHeightTypes
    MarkerType = MarkerType
    MinimumHeight = LineHeightTypes()
    ProportionalHeight = LineHeightTypes()
    SingleHeight = LineHeightTypes()
    __class__ = QTextBlockFormat
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, QTextBlockFormat: PySide2.QtGui.QTextBlockFormat):
        'QTextBlockFormat(self)\nQTextBlockFormat(self, QTextBlockFormat:PySide2.QtGui.QTextBlockFormat)\nQTextBlockFormat(self, fmt:PySide2.QtGui.QTextFormat)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def alignment(self):
        'alignment(self) -> PySide2.QtCore.Qt.Alignment'
        return PySide2.QtCore.Qt.Alignment
    
    def bottomMargin(self):
        'bottomMargin(self) -> float'
        return float
    
    def headingLevel(self):
        'headingLevel(self) -> int'
        return int
    
    def indent(self):
        'indent(self) -> int'
        return int
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def leftMargin(self):
        'leftMargin(self) -> float'
        return float
    
    def lineHeight(self, scriptLineHeight: float, scaling: float):
        'lineHeight(self) -> float\nlineHeight(self, scriptLineHeight:float, scaling:float) -> float'
        return 1.0
    
    def lineHeightType(self):
        'lineHeightType(self) -> int'
        return int
    
    def marker(self):
        'marker(self) -> PySide2.QtGui.QTextBlockFormat.MarkerType'
        return PySide2.QtGui.QTextBlockFormat.MarkerType
    
    def nonBreakableLines(self):
        'nonBreakableLines(self) -> bool'
        return bool
    
    def pageBreakPolicy(self):
        'pageBreakPolicy(self) -> PySide2.QtGui.QTextFormat.PageBreakFlags'
        return PySide2.QtGui.QTextFormat.PageBreakFlags
    
    def rightMargin(self):
        'rightMargin(self) -> float'
        return float
    
    def setAlignment(self, alignment):
        'setAlignment(self, alignment:PySide2.QtCore.Qt.Alignment)'
        pass
    
    def setBottomMargin(self, margin):
        'setBottomMargin(self, margin:float)'
        pass
    
    def setHeadingLevel(self, alevel):
        'setHeadingLevel(self, alevel:int)'
        pass
    
    def setIndent(self, indent):
        'setIndent(self, indent:int)'
        pass
    
    def setLeftMargin(self, margin):
        'setLeftMargin(self, margin:float)'
        pass
    
    def setLineHeight(self, height, heightType):
        'setLineHeight(self, height:float, heightType:int)'
        pass
    
    def setMarker(self, marker):
        'setMarker(self, marker:PySide2.QtGui.QTextBlockFormat.MarkerType)'
        pass
    
    def setNonBreakableLines(self, b):
        'setNonBreakableLines(self, b:bool)'
        pass
    
    def setPageBreakPolicy(self, flags):
        'setPageBreakPolicy(self, flags:PySide2.QtGui.QTextFormat.PageBreakFlags)'
        pass
    
    def setRightMargin(self, margin):
        'setRightMargin(self, margin:float)'
        pass
    
    def setTabPositions(self, tabs):
        'setTabPositions(self, tabs:typing.Sequence)'
        pass
    
    def setTextIndent(self, aindent):
        'setTextIndent(self, aindent:float)'
        pass
    
    def setTopMargin(self, margin):
        'setTopMargin(self, margin:float)'
        pass
    
    def tabPositions(self):
        'tabPositions(self) -> typing.List'
        return typing.List
    
    def textIndent(self):
        'textIndent(self) -> float'
        return float
    
    def topMargin(self):
        'topMargin(self) -> float'
        return float
    

class QTextBlockGroup(QTextObject):
    'QTextBlockGroup(self, doc:PySide2.QtGui.QTextDocument)'
    __class__ = QTextBlockGroup
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, doc: PySide2.QtGui.QTextDocument):
        'QTextBlockGroup(self, doc:PySide2.QtGui.QTextDocument)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def blockFormatChanged(self, block):
        'blockFormatChanged(self, block:PySide2.QtGui.QTextBlock)'
        pass
    
    def blockInserted(self, block):
        'blockInserted(self, block:PySide2.QtGui.QTextBlock)'
        pass
    
    def blockList(self):
        'blockList(self) -> typing.List'
        return typing.List
    
    def blockRemoved(self, block):
        'blockRemoved(self, block:PySide2.QtGui.QTextBlock)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QTextBlockUserData(_mod_Shiboken.Object):
    'QTextBlockUserData(self)'
    __class__ = QTextBlockUserData
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QTextBlockUserData(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class QTextCharFormat(QTextFormat):
    'QTextCharFormat(self)\nQTextCharFormat(self, QTextCharFormat:PySide2.QtGui.QTextCharFormat)\nQTextCharFormat(self, fmt:PySide2.QtGui.QTextFormat)'
    AlignBaseline = VerticalAlignment()
    AlignBottom = VerticalAlignment()
    AlignMiddle = VerticalAlignment()
    AlignNormal = VerticalAlignment()
    AlignSubScript = VerticalAlignment()
    AlignSuperScript = VerticalAlignment()
    AlignTop = VerticalAlignment()
    DashDotDotLine = UnderlineStyle()
    DashDotLine = UnderlineStyle()
    DashUnderline = UnderlineStyle()
    DotLine = UnderlineStyle()
    FontPropertiesAll = FontPropertiesInheritanceBehavior()
    FontPropertiesInheritanceBehavior = FontPropertiesInheritanceBehavior
    FontPropertiesSpecifiedOnly = FontPropertiesInheritanceBehavior()
    NoUnderline = UnderlineStyle()
    SingleUnderline = UnderlineStyle()
    SpellCheckUnderline = UnderlineStyle()
    UnderlineStyle = UnderlineStyle
    VerticalAlignment = VerticalAlignment
    WaveUnderline = UnderlineStyle()
    __class__ = QTextCharFormat
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, QTextCharFormat: PySide2.QtGui.QTextCharFormat):
        'QTextCharFormat(self)\nQTextCharFormat(self, QTextCharFormat:PySide2.QtGui.QTextCharFormat)\nQTextCharFormat(self, fmt:PySide2.QtGui.QTextFormat)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def anchorHref(self):
        'anchorHref(self) -> str'
        return str
    
    def anchorName(self):
        'anchorName(self) -> str'
        return str
    
    def anchorNames(self):
        'anchorNames(self) -> typing.List'
        return typing.List
    
    def font(self):
        'font(self) -> PySide2.QtGui.QFont'
        return PySide2.QtGui.QFont
    
    def fontCapitalization(self):
        'fontCapitalization(self) -> PySide2.QtGui.QFont.Capitalization'
        return PySide2.QtGui.QFont.Capitalization
    
    def fontFamilies(self):
        'fontFamilies(self) -> typing.Any'
        return typing.Any
    
    def fontFamily(self):
        'fontFamily(self) -> str'
        return str
    
    def fontFixedPitch(self):
        'fontFixedPitch(self) -> bool'
        return bool
    
    def fontHintingPreference(self):
        'fontHintingPreference(self) -> PySide2.QtGui.QFont.HintingPreference'
        return PySide2.QtGui.QFont.HintingPreference
    
    def fontItalic(self):
        'fontItalic(self) -> bool'
        return bool
    
    def fontKerning(self):
        'fontKerning(self) -> bool'
        return bool
    
    def fontLetterSpacing(self):
        'fontLetterSpacing(self) -> float'
        return float
    
    def fontLetterSpacingType(self):
        'fontLetterSpacingType(self) -> PySide2.QtGui.QFont.SpacingType'
        return PySide2.QtGui.QFont.SpacingType
    
    def fontOverline(self):
        'fontOverline(self) -> bool'
        return bool
    
    def fontPointSize(self):
        'fontPointSize(self) -> float'
        return float
    
    def fontStretch(self):
        'fontStretch(self) -> int'
        return int
    
    def fontStrikeOut(self):
        'fontStrikeOut(self) -> bool'
        return bool
    
    def fontStyleHint(self):
        'fontStyleHint(self) -> PySide2.QtGui.QFont.StyleHint'
        return PySide2.QtGui.QFont.StyleHint
    
    def fontStyleName(self):
        'fontStyleName(self) -> typing.Any'
        return typing.Any
    
    def fontStyleStrategy(self):
        'fontStyleStrategy(self) -> PySide2.QtGui.QFont.StyleStrategy'
        return PySide2.QtGui.QFont.StyleStrategy
    
    def fontUnderline(self):
        'fontUnderline(self) -> bool'
        return bool
    
    def fontWeight(self):
        'fontWeight(self) -> int'
        return int
    
    def fontWordSpacing(self):
        'fontWordSpacing(self) -> float'
        return float
    
    def isAnchor(self):
        'isAnchor(self) -> bool'
        return bool
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def setAnchor(self, anchor):
        'setAnchor(self, anchor:bool)'
        pass
    
    def setAnchorHref(self, value):
        'setAnchorHref(self, value:str)'
        pass
    
    def setAnchorName(self, name):
        'setAnchorName(self, name:str)'
        pass
    
    def setAnchorNames(self, names):
        'setAnchorNames(self, names:typing.Sequence)'
        pass
    
    def setFont(self, font: PySide2.QtGui.QFont, behavior: PySide2.QtGui.QTextCharFormat.FontPropertiesInheritanceBehavior):
        'setFont(self, font:PySide2.QtGui.QFont)\nsetFont(self, font:PySide2.QtGui.QFont, behavior:PySide2.QtGui.QTextCharFormat.FontPropertiesInheritanceBehavior)'
        pass
    
    def setFontCapitalization(self, capitalization):
        'setFontCapitalization(self, capitalization:PySide2.QtGui.QFont.Capitalization)'
        pass
    
    def setFontFamilies(self, families):
        'setFontFamilies(self, families:typing.Sequence)'
        pass
    
    def setFontFamily(self, family):
        'setFontFamily(self, family:str)'
        pass
    
    def setFontFixedPitch(self, fixedPitch):
        'setFontFixedPitch(self, fixedPitch:bool)'
        pass
    
    def setFontHintingPreference(self, hintingPreference):
        'setFontHintingPreference(self, hintingPreference:PySide2.QtGui.QFont.HintingPreference)'
        pass
    
    def setFontItalic(self, italic):
        'setFontItalic(self, italic:bool)'
        pass
    
    def setFontKerning(self, enable):
        'setFontKerning(self, enable:bool)'
        pass
    
    def setFontLetterSpacing(self, spacing):
        'setFontLetterSpacing(self, spacing:float)'
        pass
    
    def setFontLetterSpacingType(self, letterSpacingType):
        'setFontLetterSpacingType(self, letterSpacingType:PySide2.QtGui.QFont.SpacingType)'
        pass
    
    def setFontOverline(self, overline):
        'setFontOverline(self, overline:bool)'
        pass
    
    def setFontPointSize(self, size):
        'setFontPointSize(self, size:float)'
        pass
    
    def setFontStretch(self, factor):
        'setFontStretch(self, factor:int)'
        pass
    
    def setFontStrikeOut(self, strikeOut):
        'setFontStrikeOut(self, strikeOut:bool)'
        pass
    
    def setFontStyleHint(self, hint, strategy):
        'setFontStyleHint(self, hint:PySide2.QtGui.QFont.StyleHint, strategy:PySide2.QtGui.QFont.StyleStrategy=PySide2.QtGui.QFont.StyleStrategy.PreferDefault)'
        pass
    
    def setFontStyleName(self, styleName):
        'setFontStyleName(self, styleName:str)'
        pass
    
    def setFontStyleStrategy(self, strategy):
        'setFontStyleStrategy(self, strategy:PySide2.QtGui.QFont.StyleStrategy)'
        pass
    
    def setFontUnderline(self, underline):
        'setFontUnderline(self, underline:bool)'
        pass
    
    def setFontWeight(self, weight):
        'setFontWeight(self, weight:int)'
        pass
    
    def setFontWordSpacing(self, spacing):
        'setFontWordSpacing(self, spacing:float)'
        pass
    
    def setTableCellColumnSpan(self, tableCellColumnSpan):
        'setTableCellColumnSpan(self, tableCellColumnSpan:int)'
        pass
    
    def setTableCellRowSpan(self, tableCellRowSpan):
        'setTableCellRowSpan(self, tableCellRowSpan:int)'
        pass
    
    def setTextOutline(self, pen):
        'setTextOutline(self, pen:PySide2.QtGui.QPen)'
        pass
    
    def setToolTip(self, tip):
        'setToolTip(self, tip:str)'
        pass
    
    def setUnderlineColor(self, color):
        'setUnderlineColor(self, color:PySide2.QtGui.QColor)'
        pass
    
    def setUnderlineStyle(self, style):
        'setUnderlineStyle(self, style:PySide2.QtGui.QTextCharFormat.UnderlineStyle)'
        pass
    
    def setVerticalAlignment(self, alignment):
        'setVerticalAlignment(self, alignment:PySide2.QtGui.QTextCharFormat.VerticalAlignment)'
        pass
    
    def tableCellColumnSpan(self):
        'tableCellColumnSpan(self) -> int'
        return int
    
    def tableCellRowSpan(self):
        'tableCellRowSpan(self) -> int'
        return int
    
    def textOutline(self):
        'textOutline(self) -> PySide2.QtGui.QPen'
        return PySide2.QtGui.QPen
    
    def toolTip(self):
        'toolTip(self) -> str'
        return str
    
    def underlineColor(self):
        'underlineColor(self) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def underlineStyle(self):
        'underlineStyle(self) -> PySide2.QtGui.QTextCharFormat.UnderlineStyle'
        return PySide2.QtGui.QTextCharFormat.UnderlineStyle
    
    def verticalAlignment(self):
        'verticalAlignment(self) -> PySide2.QtGui.QTextCharFormat.VerticalAlignment'
        return PySide2.QtGui.QTextCharFormat.VerticalAlignment
    

class QTextCursor(_mod_Shiboken.Object):
    'QTextCursor(self)\nQTextCursor(self, block:PySide2.QtGui.QTextBlock)\nQTextCursor(self, cursor:PySide2.QtGui.QTextCursor)\nQTextCursor(self, document:PySide2.QtGui.QTextDocument)\nQTextCursor(self, frame:PySide2.QtGui.QTextFrame)'
    BlockUnderCursor = SelectionType()
    Document = SelectionType()
    Down = MoveOperation()
    End = MoveOperation()
    EndOfBlock = MoveOperation()
    EndOfLine = MoveOperation()
    EndOfWord = MoveOperation()
    KeepAnchor = MoveMode()
    Left = MoveOperation()
    LineUnderCursor = SelectionType()
    MoveAnchor = MoveMode()
    MoveMode = MoveMode
    MoveOperation = MoveOperation
    NextBlock = MoveOperation()
    NextCell = MoveOperation()
    NextCharacter = MoveOperation()
    NextRow = MoveOperation()
    NextWord = MoveOperation()
    NoMove = MoveOperation()
    PreviousBlock = MoveOperation()
    PreviousCell = MoveOperation()
    PreviousCharacter = MoveOperation()
    PreviousRow = MoveOperation()
    PreviousWord = MoveOperation()
    Right = MoveOperation()
    SelectionType = SelectionType
    Start = MoveOperation()
    StartOfBlock = MoveOperation()
    StartOfLine = MoveOperation()
    StartOfWord = MoveOperation()
    Up = MoveOperation()
    WordLeft = MoveOperation()
    WordRight = MoveOperation()
    WordUnderCursor = SelectionType()
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QTextCursor
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, document: PySide2.QtGui.QTextDocument):
        'QTextCursor(self)\nQTextCursor(self, block:PySide2.QtGui.QTextBlock)\nQTextCursor(self, cursor:PySide2.QtGui.QTextCursor)\nQTextCursor(self, document:PySide2.QtGui.QTextDocument)\nQTextCursor(self, frame:PySide2.QtGui.QTextFrame)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def anchor(self):
        'anchor(self) -> int'
        return int
    
    def atBlockEnd(self):
        'atBlockEnd(self) -> bool'
        return bool
    
    def atBlockStart(self):
        'atBlockStart(self) -> bool'
        return bool
    
    def atEnd(self):
        'atEnd(self) -> bool'
        return bool
    
    def atStart(self):
        'atStart(self) -> bool'
        return bool
    
    def beginEditBlock(self):
        'beginEditBlock(self)'
        pass
    
    def block(self):
        'block(self) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def blockCharFormat(self):
        'blockCharFormat(self) -> PySide2.QtGui.QTextCharFormat'
        return PySide2.QtGui.QTextCharFormat
    
    def blockFormat(self):
        'blockFormat(self) -> PySide2.QtGui.QTextBlockFormat'
        return PySide2.QtGui.QTextBlockFormat
    
    def blockNumber(self):
        'blockNumber(self) -> int'
        return int
    
    def charFormat(self):
        'charFormat(self) -> PySide2.QtGui.QTextCharFormat'
        return PySide2.QtGui.QTextCharFormat
    
    def clearSelection(self):
        'clearSelection(self)'
        pass
    
    def columnNumber(self):
        'columnNumber(self) -> int'
        return int
    
    def createList(self, style: PySide2.QtGui.QTextListFormat.Style):
        'createList(self, format:PySide2.QtGui.QTextListFormat) -> PySide2.QtGui.QTextList\ncreateList(self, style:PySide2.QtGui.QTextListFormat.Style) -> PySide2.QtGui.QTextList'
        pass
    
    def currentFrame(self):
        'currentFrame(self) -> PySide2.QtGui.QTextFrame'
        return PySide2.QtGui.QTextFrame
    
    def currentList(self):
        'currentList(self) -> PySide2.QtGui.QTextList'
        return PySide2.QtGui.QTextList
    
    def currentTable(self):
        'currentTable(self) -> PySide2.QtGui.QTextTable'
        return PySide2.QtGui.QTextTable
    
    def deleteChar(self):
        'deleteChar(self)'
        pass
    
    def deletePreviousChar(self):
        'deletePreviousChar(self)'
        pass
    
    def document(self):
        'document(self) -> PySide2.QtGui.QTextDocument'
        return PySide2.QtGui.QTextDocument
    
    def endEditBlock(self):
        'endEditBlock(self)'
        pass
    
    def hasComplexSelection(self):
        'hasComplexSelection(self) -> bool'
        return bool
    
    def hasSelection(self):
        'hasSelection(self) -> bool'
        return bool
    
    def insertBlock(self, format: PySide2.QtGui.QTextBlockFormat, charFormat: PySide2.QtGui.QTextCharFormat):
        'insertBlock(self)\ninsertBlock(self, format:PySide2.QtGui.QTextBlockFormat)\ninsertBlock(self, format:PySide2.QtGui.QTextBlockFormat, charFormat:PySide2.QtGui.QTextCharFormat)'
        pass
    
    def insertFragment(self, fragment):
        'insertFragment(self, fragment:PySide2.QtGui.QTextDocumentFragment)'
        pass
    
    def insertFrame(self, format):
        'insertFrame(self, format:PySide2.QtGui.QTextFrameFormat) -> PySide2.QtGui.QTextFrame'
        return PySide2.QtGui.QTextFrame
    
    def insertHtml(self, html):
        'insertHtml(self, html:str)'
        pass
    
    def insertImage(self, format: PySide2.QtGui.QTextImageFormat, alignment: PySide2.QtGui.QTextFrameFormat.Position):
        "insertImage(self, format:PySide2.QtGui.QTextImageFormat)\ninsertImage(self, format:PySide2.QtGui.QTextImageFormat, alignment:PySide2.QtGui.QTextFrameFormat.Position)\ninsertImage(self, image:PySide2.QtGui.QImage, name:str='')\ninsertImage(self, name:str)"
        pass
    
    def insertList(self, style: PySide2.QtGui.QTextListFormat.Style):
        'insertList(self, format:PySide2.QtGui.QTextListFormat) -> PySide2.QtGui.QTextList\ninsertList(self, style:PySide2.QtGui.QTextListFormat.Style) -> PySide2.QtGui.QTextList'
        pass
    
    def insertTable(self, rows: int, cols: int, format: PySide2.QtGui.QTextTableFormat):
        'insertTable(self, rows:int, cols:int) -> PySide2.QtGui.QTextTable\ninsertTable(self, rows:int, cols:int, format:PySide2.QtGui.QTextTableFormat) -> PySide2.QtGui.QTextTable'
        pass
    
    def insertText(self, text: str, format: PySide2.QtGui.QTextCharFormat):
        'insertText(self, text:str)\ninsertText(self, text:str, format:PySide2.QtGui.QTextCharFormat)'
        pass
    
    def isCopyOf(self, other):
        'isCopyOf(self, other:PySide2.QtGui.QTextCursor) -> bool'
        return bool
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def joinPreviousEditBlock(self):
        'joinPreviousEditBlock(self)'
        pass
    
    def keepPositionOnInsert(self):
        'keepPositionOnInsert(self) -> bool'
        return bool
    
    def mergeBlockCharFormat(self, modifier):
        'mergeBlockCharFormat(self, modifier:PySide2.QtGui.QTextCharFormat)'
        pass
    
    def mergeBlockFormat(self, modifier):
        'mergeBlockFormat(self, modifier:PySide2.QtGui.QTextBlockFormat)'
        pass
    
    def mergeCharFormat(self, modifier):
        'mergeCharFormat(self, modifier:PySide2.QtGui.QTextCharFormat)'
        pass
    
    def movePosition(self, op, arg__2, n):
        'movePosition(self, op:PySide2.QtGui.QTextCursor.MoveOperation, arg__2:PySide2.QtGui.QTextCursor.MoveMode=PySide2.QtGui.QTextCursor.MoveMode.MoveAnchor, n:int=1) -> bool'
        return bool
    
    def position(self):
        'position(self) -> int'
        return int
    
    def positionInBlock(self):
        'positionInBlock(self) -> int'
        return int
    
    def removeSelectedText(self):
        'removeSelectedText(self)'
        pass
    
    def select(self, selection):
        'select(self, selection:PySide2.QtGui.QTextCursor.SelectionType)'
        pass
    
    def selectedTableCells(self):
        'selectedTableCells(self) -> typing.Tuple'
        return typing.Tuple
    
    def selectedText(self):
        'selectedText(self) -> str'
        return str
    
    def selection(self):
        'selection(self) -> PySide2.QtGui.QTextDocumentFragment'
        return PySide2.QtGui.QTextDocumentFragment
    
    def selectionEnd(self):
        'selectionEnd(self) -> int'
        return int
    
    def selectionStart(self):
        'selectionStart(self) -> int'
        return int
    
    def setBlockCharFormat(self, format):
        'setBlockCharFormat(self, format:PySide2.QtGui.QTextCharFormat)'
        pass
    
    def setBlockFormat(self, format):
        'setBlockFormat(self, format:PySide2.QtGui.QTextBlockFormat)'
        pass
    
    def setCharFormat(self, format):
        'setCharFormat(self, format:PySide2.QtGui.QTextCharFormat)'
        pass
    
    def setKeepPositionOnInsert(self, b):
        'setKeepPositionOnInsert(self, b:bool)'
        pass
    
    def setPosition(self, pos, mode):
        'setPosition(self, pos:int, mode:PySide2.QtGui.QTextCursor.MoveMode=PySide2.QtGui.QTextCursor.MoveMode.MoveAnchor)'
        pass
    
    def setVerticalMovementX(self, x):
        'setVerticalMovementX(self, x:int)'
        pass
    
    def setVisualNavigation(self, b):
        'setVisualNavigation(self, b:bool)'
        pass
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QTextCursor)'
        pass
    
    def verticalMovementX(self):
        'verticalMovementX(self) -> int'
        return int
    
    def visualNavigation(self):
        'visualNavigation(self) -> bool'
        return bool
    

class QTextDocument(_mod_PySide2_QtCore.QObject):
    'QTextDocument(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQTextDocument(self, text:str, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    DocumentTitle = MetaInformation()
    DocumentUrl = MetaInformation()
    FindBackward = FindFlag()
    FindCaseSensitively = FindFlag()
    FindFlag = FindFlag
    FindFlags = FindFlags
    FindWholeWords = FindFlag()
    HtmlResource = ResourceType()
    ImageResource = ResourceType()
    MarkdownDialectCommonMark = MarkdownFeature()
    MarkdownDialectGitHub = MarkdownFeature()
    MarkdownFeature = MarkdownFeature
    MarkdownFeatures = MarkdownFeatures
    MarkdownNoHTML = MarkdownFeature()
    MarkdownResource = ResourceType()
    MetaInformation = MetaInformation
    RedoStack = Stacks()
    ResourceType = ResourceType
    Stacks = Stacks
    StyleSheetResource = ResourceType()
    UndoAndRedoStacks = Stacks()
    UndoStack = Stacks()
    UnknownResource = ResourceType()
    UserResource = ResourceType()
    __class__ = QTextDocument
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, text: str, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QTextDocument(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)\nQTextDocument(self, text:str, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addResource(self, type, name, resource):
        'addResource(self, type:int, name:PySide2.QtCore.QUrl, resource:typing.Any)'
        pass
    
    def adjustSize(self):
        'adjustSize(self)'
        pass
    
    def allFormats(self):
        'allFormats(self) -> typing.List'
        return typing.List
    
    def availableRedoSteps(self):
        'availableRedoSteps(self) -> int'
        return int
    
    def availableUndoSteps(self):
        'availableUndoSteps(self) -> int'
        return int
    
    def baseUrl(self):
        'baseUrl(self) -> PySide2.QtCore.QUrl'
        return PySide2.QtCore.QUrl
    
    def baseUrlChanged(self):
        pass
    
    def begin(self):
        'begin(self) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def blockCount(self):
        'blockCount(self) -> int'
        return int
    
    def blockCountChanged(self):
        pass
    
    def characterAt(self, pos):
        'characterAt(self, pos:int) -> str'
        return str
    
    def characterCount(self):
        'characterCount(self) -> int'
        return int
    
    def clear(self):
        'clear(self)'
        pass
    
    def clearUndoRedoStacks(self, historyToClear):
        'clearUndoRedoStacks(self, historyToClear:PySide2.QtGui.QTextDocument.Stacks=PySide2.QtGui.QTextDocument.Stacks.UndoAndRedoStacks)'
        pass
    
    def clone(self, parent):
        'clone(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None) -> PySide2.QtGui.QTextDocument'
        return PySide2.QtGui.QTextDocument
    
    def contentsChange(self):
        pass
    
    def contentsChanged(self):
        pass
    
    def createObject(self, f):
        'createObject(self, f:PySide2.QtGui.QTextFormat) -> PySide2.QtGui.QTextObject'
        return PySide2.QtGui.QTextObject
    
    def cursorPositionChanged(self):
        pass
    
    def defaultCursorMoveStyle(self):
        'defaultCursorMoveStyle(self) -> PySide2.QtCore.Qt.CursorMoveStyle'
        return PySide2.QtCore.Qt.CursorMoveStyle
    
    def defaultFont(self):
        'defaultFont(self) -> PySide2.QtGui.QFont'
        return PySide2.QtGui.QFont
    
    def defaultStyleSheet(self):
        'defaultStyleSheet(self) -> str'
        return str
    
    def defaultTextOption(self):
        'defaultTextOption(self) -> PySide2.QtGui.QTextOption'
        return PySide2.QtGui.QTextOption
    
    def documentLayout(self):
        'documentLayout(self) -> PySide2.QtGui.QAbstractTextDocumentLayout'
        return PySide2.QtGui.QAbstractTextDocumentLayout
    
    def documentLayoutChanged(self):
        pass
    
    def documentMargin(self):
        'documentMargin(self) -> float'
        return float
    
    def drawContents(self, painter, rect):
        'drawContents(self, painter:PySide2.QtGui.QPainter, rect:PySide2.QtCore.QRectF=Default(QRectF))'
        pass
    
    def end(self):
        'end(self) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def find(self, expr: PySide2.QtCore.QRegularExpression, cursor: PySide2.QtGui.QTextCursor, options: PySide2.QtGui.QTextDocument.FindFlags=Default(QTextDocument.FindFlags)):
        'find(self, expr:PySide2.QtCore.QRegExp, cursor:PySide2.QtGui.QTextCursor, options:PySide2.QtGui.QTextDocument.FindFlags=Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor\nfind(self, expr:PySide2.QtCore.QRegExp, from_:int=0, options:PySide2.QtGui.QTextDocument.FindFlags=Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor\nfind(self, expr:PySide2.QtCore.QRegularExpression, cursor:PySide2.QtGui.QTextCursor, options:PySide2.QtGui.QTextDocument.FindFlags=Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor\nfind(self, expr:PySide2.QtCore.QRegularExpression, from_:int=0, options:PySide2.QtGui.QTextDocument.FindFlags=Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor\nfind(self, subString:str, cursor:PySide2.QtGui.QTextCursor, options:PySide2.QtGui.QTextDocument.FindFlags=Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor\nfind(self, subString:str, from_:int=0, options:PySide2.QtGui.QTextDocument.FindFlags=Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor'
        pass
    
    def findBlock(self, pos):
        'findBlock(self, pos:int) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def findBlockByLineNumber(self, blockNumber):
        'findBlockByLineNumber(self, blockNumber:int) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def findBlockByNumber(self, blockNumber):
        'findBlockByNumber(self, blockNumber:int) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def firstBlock(self):
        'firstBlock(self) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def frameAt(self, pos):
        'frameAt(self, pos:int) -> PySide2.QtGui.QTextFrame'
        return PySide2.QtGui.QTextFrame
    
    def idealWidth(self):
        'idealWidth(self) -> float'
        return float
    
    def indentWidth(self):
        'indentWidth(self) -> float'
        return float
    
    def isEmpty(self):
        'isEmpty(self) -> bool'
        return bool
    
    def isModified(self):
        'isModified(self) -> bool'
        return bool
    
    def isRedoAvailable(self):
        'isRedoAvailable(self) -> bool'
        return bool
    
    def isUndoAvailable(self):
        'isUndoAvailable(self) -> bool'
        return bool
    
    def isUndoRedoEnabled(self):
        'isUndoRedoEnabled(self) -> bool'
        return bool
    
    def lastBlock(self):
        'lastBlock(self) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def lineCount(self):
        'lineCount(self) -> int'
        return int
    
    def loadResource(self, type, name):
        'loadResource(self, type:int, name:PySide2.QtCore.QUrl) -> typing.Any'
        return typing.Any
    
    def markContentsDirty(self, from_, length):
        'markContentsDirty(self, from_:int, length:int)'
        pass
    
    def maximumBlockCount(self):
        'maximumBlockCount(self) -> int'
        return int
    
    def metaInformation(self, info):
        'metaInformation(self, info:PySide2.QtGui.QTextDocument.MetaInformation) -> str'
        return str
    
    def modificationChanged(self):
        pass
    
    def object(self, objectIndex):
        'object(self, objectIndex:int) -> PySide2.QtGui.QTextObject'
        return PySide2.QtGui.QTextObject
    
    def objectForFormat(self, arg__1):
        'objectForFormat(self, arg__1:PySide2.QtGui.QTextFormat) -> PySide2.QtGui.QTextObject'
        return PySide2.QtGui.QTextObject
    
    def pageCount(self):
        'pageCount(self) -> int'
        return int
    
    def pageSize(self):
        'pageSize(self) -> PySide2.QtCore.QSizeF'
        return PySide2.QtCore.QSizeF
    
    def print_(self, printer):
        'print_(self, printer:PySide2.QtGui.QPagedPaintDevice)'
        pass
    
    def redo(self, cursor: PySide2.QtGui.QTextCursor):
        'redo(self)\nredo(self, cursor:PySide2.QtGui.QTextCursor)'
        pass
    
    def redoAvailable(self):
        pass
    
    def resource(self, type, name):
        'resource(self, type:int, name:PySide2.QtCore.QUrl) -> typing.Any'
        return typing.Any
    
    def revision(self):
        'revision(self) -> int'
        return int
    
    def rootFrame(self):
        'rootFrame(self) -> PySide2.QtGui.QTextFrame'
        return PySide2.QtGui.QTextFrame
    
    def setBaseUrl(self, url):
        'setBaseUrl(self, url:PySide2.QtCore.QUrl)'
        pass
    
    def setDefaultCursorMoveStyle(self, style):
        'setDefaultCursorMoveStyle(self, style:PySide2.QtCore.Qt.CursorMoveStyle)'
        pass
    
    def setDefaultFont(self, font):
        'setDefaultFont(self, font:PySide2.QtGui.QFont)'
        pass
    
    def setDefaultStyleSheet(self, sheet):
        'setDefaultStyleSheet(self, sheet:str)'
        pass
    
    def setDefaultTextOption(self, option):
        'setDefaultTextOption(self, option:PySide2.QtGui.QTextOption)'
        pass
    
    def setDocumentLayout(self, layout):
        'setDocumentLayout(self, layout:PySide2.QtGui.QAbstractTextDocumentLayout)'
        pass
    
    def setDocumentMargin(self, margin):
        'setDocumentMargin(self, margin:float)'
        pass
    
    def setHtml(self, html):
        'setHtml(self, html:str)'
        pass
    
    def setIndentWidth(self, width):
        'setIndentWidth(self, width:float)'
        pass
    
    def setMarkdown(self, markdown, features):
        'setMarkdown(self, markdown:str, features:PySide2.QtGui.QTextDocument.MarkdownFeatures=PySide2.QtGui.QTextDocument.MarkdownFeature.MarkdownDialectGitHub)'
        pass
    
    def setMaximumBlockCount(self, maximum):
        'setMaximumBlockCount(self, maximum:int)'
        pass
    
    def setMetaInformation(self, info, arg__2):
        'setMetaInformation(self, info:PySide2.QtGui.QTextDocument.MetaInformation, arg__2:str)'
        pass
    
    def setModified(self, m):
        'setModified(self, m:bool=True)'
        pass
    
    def setPageSize(self, size):
        'setPageSize(self, size:PySide2.QtCore.QSizeF)'
        pass
    
    def setPlainText(self, text):
        'setPlainText(self, text:str)'
        pass
    
    def setTextWidth(self, width):
        'setTextWidth(self, width:float)'
        pass
    
    def setUndoRedoEnabled(self, enable):
        'setUndoRedoEnabled(self, enable:bool)'
        pass
    
    def setUseDesignMetrics(self, b):
        'setUseDesignMetrics(self, b:bool)'
        pass
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSizeF'
        return PySide2.QtCore.QSizeF
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def textWidth(self):
        'textWidth(self) -> float'
        return float
    
    def toHtml(self, encoding):
        'toHtml(self, encoding:PySide2.QtCore.QByteArray=Default(QByteArray)) -> str'
        return str
    
    def toMarkdown(self, features):
        'toMarkdown(self, features:PySide2.QtGui.QTextDocument.MarkdownFeatures=PySide2.QtGui.QTextDocument.MarkdownFeature.MarkdownDialectGitHub) -> str'
        return str
    
    def toPlainText(self):
        'toPlainText(self) -> str'
        return str
    
    def toRawText(self):
        'toRawText(self) -> str'
        return str
    
    def undo(self, cursor: PySide2.QtGui.QTextCursor):
        'undo(self)\nundo(self, cursor:PySide2.QtGui.QTextCursor)'
        pass
    
    def undoAvailable(self):
        pass
    
    def undoCommandAdded(self):
        pass
    
    def useDesignMetrics(self):
        'useDesignMetrics(self) -> bool'
        return bool
    

class QTextDocumentFragment(_mod_Shiboken.Object):
    'QTextDocumentFragment(self)\nQTextDocumentFragment(self, document:PySide2.QtGui.QTextDocument)\nQTextDocumentFragment(self, range:PySide2.QtGui.QTextCursor)\nQTextDocumentFragment(self, rhs:PySide2.QtGui.QTextDocumentFragment)'
    __class__ = QTextDocumentFragment
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, rhs: PySide2.QtGui.QTextDocumentFragment):
        'QTextDocumentFragment(self)\nQTextDocumentFragment(self, document:PySide2.QtGui.QTextDocument)\nQTextDocumentFragment(self, range:PySide2.QtGui.QTextCursor)\nQTextDocumentFragment(self, rhs:PySide2.QtGui.QTextDocumentFragment)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def fromHtml(cls, html: str, resourceProvider: PySide2.QtGui.QTextDocument):
        'fromHtml(html:str) -> PySide2.QtGui.QTextDocumentFragment\nfromHtml(html:str, resourceProvider:PySide2.QtGui.QTextDocument) -> PySide2.QtGui.QTextDocumentFragment'
        pass
    
    @classmethod
    def fromPlainText(cls, plainText):
        'fromPlainText(plainText:str) -> PySide2.QtGui.QTextDocumentFragment'
        return PySide2.QtGui.QTextDocumentFragment
    
    def isEmpty(self):
        'isEmpty(self) -> bool'
        return bool
    
    def toHtml(self, encoding):
        'toHtml(self, encoding:PySide2.QtCore.QByteArray=Default(QByteArray)) -> str'
        return str
    
    def toPlainText(self):
        'toPlainText(self) -> str'
        return str
    

class QTextDocumentWriter(_mod_Shiboken.Object):
    'QTextDocumentWriter(self)\nQTextDocumentWriter(self, device:PySide2.QtCore.QIODevice, format:PySide2.QtCore.QByteArray)\nQTextDocumentWriter(self, fileName:str, format:PySide2.QtCore.QByteArray=Default(QByteArray))'
    __class__ = QTextDocumentWriter
    __dict__ = {}
    def __init__(self, fileName: str, format: PySide2.QtCore.QByteArray=Default(QByteArray)):
        'QTextDocumentWriter(self)\nQTextDocumentWriter(self, device:PySide2.QtCore.QIODevice, format:PySide2.QtCore.QByteArray)\nQTextDocumentWriter(self, fileName:str, format:PySide2.QtCore.QByteArray=Default(QByteArray))'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def codec(self):
        'codec(self) -> PySide2.QtCore.QTextCodec'
        return PySide2.QtCore.QTextCodec
    
    def device(self):
        'device(self) -> PySide2.QtCore.QIODevice'
        return PySide2.QtCore.QIODevice
    
    def fileName(self):
        'fileName(self) -> str'
        return str
    
    def format(self):
        'format(self) -> PySide2.QtCore.QByteArray'
        return PySide2.QtCore.QByteArray
    
    def setCodec(self, codec):
        'setCodec(self, codec:PySide2.QtCore.QTextCodec)'
        pass
    
    def setDevice(self, device):
        'setDevice(self, device:PySide2.QtCore.QIODevice)'
        pass
    
    def setFileName(self, fileName):
        'setFileName(self, fileName:str)'
        pass
    
    def setFormat(self, format):
        'setFormat(self, format:PySide2.QtCore.QByteArray)'
        pass
    
    @classmethod
    def supportedDocumentFormats(cls):
        'supportedDocumentFormats() -> typing.List'
        return typing.List
    
    def write(self, fragment: PySide2.QtGui.QTextDocumentFragment):
        'write(self, document:PySide2.QtGui.QTextDocument) -> bool\nwrite(self, fragment:PySide2.QtGui.QTextDocumentFragment) -> bool'
        return True
    

class QTextFormat(_mod_Shiboken.Object):
    'QTextFormat(self)\nQTextFormat(self, rhs:PySide2.QtGui.QTextFormat)\nQTextFormat(self, type:int)'
    AnchorHref = Property()
    AnchorName = Property()
    BackgroundBrush = Property()
    BackgroundImageUrl = Property()
    BlockAlignment = Property()
    BlockBottomMargin = Property()
    BlockCodeFence = Property()
    BlockCodeLanguage = Property()
    BlockFormat = FormatType()
    BlockIndent = Property()
    BlockLeftMargin = Property()
    BlockMarker = Property()
    BlockNonBreakableLines = Property()
    BlockQuoteLevel = Property()
    BlockRightMargin = Property()
    BlockTopMargin = Property()
    BlockTrailingHorizontalRulerWidth = Property()
    CharFormat = FormatType()
    CssFloat = Property()
    FirstFontProperty = Property()
    FontCapitalization = Property()
    FontFamilies = Property()
    FontFamily = Property()
    FontFixedPitch = Property()
    FontHintingPreference = Property()
    FontItalic = Property()
    FontKerning = Property()
    FontLetterSpacing = Property()
    FontLetterSpacingType = Property()
    FontOverline = Property()
    FontPixelSize = Property()
    FontPointSize = Property()
    FontSizeAdjustment = Property()
    FontSizeIncrement = Property()
    FontStretch = Property()
    FontStrikeOut = Property()
    FontStyleHint = Property()
    FontStyleName = Property()
    FontStyleStrategy = Property()
    FontUnderline = Property()
    FontWeight = Property()
    FontWordSpacing = Property()
    ForegroundBrush = Property()
    FormatType = FormatType
    FrameBorder = Property()
    FrameBorderBrush = Property()
    FrameBorderStyle = Property()
    FrameBottomMargin = Property()
    FrameFormat = FormatType()
    FrameHeight = Property()
    FrameLeftMargin = Property()
    FrameMargin = Property()
    FramePadding = Property()
    FrameRightMargin = Property()
    FrameTopMargin = Property()
    FrameWidth = Property()
    FullWidthSelection = Property()
    HeadingLevel = Property()
    ImageAltText = Property()
    ImageHeight = Property()
    ImageName = Property()
    ImageObject = ObjectTypes()
    ImageQuality = Property()
    ImageTitle = Property()
    ImageWidth = Property()
    InvalidFormat = FormatType()
    IsAnchor = Property()
    LastFontProperty = Property()
    LayoutDirection = Property()
    LineHeight = Property()
    LineHeightType = Property()
    ListFormat = FormatType()
    ListIndent = Property()
    ListNumberPrefix = Property()
    ListNumberSuffix = Property()
    ListStyle = Property()
    NoObject = ObjectTypes()
    ObjectIndex = Property()
    ObjectType = Property()
    ObjectTypes = ObjectTypes
    OutlinePen = Property()
    PageBreakFlag = PageBreakFlag
    PageBreakFlags = PageBreakFlags
    PageBreakPolicy = Property()
    PageBreak_AlwaysAfter = PageBreakFlag()
    PageBreak_AlwaysBefore = PageBreakFlag()
    PageBreak_Auto = PageBreakFlag()
    Property = Property
    TabPositions = Property()
    TableBorderCollapse = Property()
    TableCellBottomBorder = Property()
    TableCellBottomBorderBrush = Property()
    TableCellBottomBorderStyle = Property()
    TableCellBottomPadding = Property()
    TableCellColumnSpan = Property()
    TableCellLeftBorder = Property()
    TableCellLeftBorderBrush = Property()
    TableCellLeftBorderStyle = Property()
    TableCellLeftPadding = Property()
    TableCellObject = ObjectTypes()
    TableCellPadding = Property()
    TableCellRightBorder = Property()
    TableCellRightBorderBrush = Property()
    TableCellRightBorderStyle = Property()
    TableCellRightPadding = Property()
    TableCellRowSpan = Property()
    TableCellSpacing = Property()
    TableCellTopBorder = Property()
    TableCellTopBorderBrush = Property()
    TableCellTopBorderStyle = Property()
    TableCellTopPadding = Property()
    TableColumnWidthConstraints = Property()
    TableColumns = Property()
    TableFormat = FormatType()
    TableHeaderRowCount = Property()
    TableObject = ObjectTypes()
    TextIndent = Property()
    TextOutline = Property()
    TextToolTip = Property()
    TextUnderlineColor = Property()
    TextUnderlineStyle = Property()
    TextVerticalAlignment = Property()
    UserFormat = FormatType()
    UserObject = ObjectTypes()
    UserProperty = Property()
    __class__ = QTextFormat
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, rhs: PySide2.QtGui.QTextFormat):
        'QTextFormat(self)\nQTextFormat(self, rhs:PySide2.QtGui.QTextFormat)\nQTextFormat(self, type:int)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QTextFormat()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QTextFormat()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def background(self):
        'background(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def boolProperty(self, propertyId):
        'boolProperty(self, propertyId:int) -> bool'
        return bool
    
    def brushProperty(self, propertyId):
        'brushProperty(self, propertyId:int) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def clearBackground(self):
        'clearBackground(self)'
        pass
    
    def clearForeground(self):
        'clearForeground(self)'
        pass
    
    def clearProperty(self, propertyId):
        'clearProperty(self, propertyId:int)'
        pass
    
    def colorProperty(self, propertyId):
        'colorProperty(self, propertyId:int) -> PySide2.QtGui.QColor'
        return PySide2.QtGui.QColor
    
    def doubleProperty(self, propertyId):
        'doubleProperty(self, propertyId:int) -> float'
        return float
    
    def foreground(self):
        'foreground(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def hasProperty(self, propertyId):
        'hasProperty(self, propertyId:int) -> bool'
        return bool
    
    def intProperty(self, propertyId):
        'intProperty(self, propertyId:int) -> int'
        return int
    
    def isBlockFormat(self):
        'isBlockFormat(self) -> bool'
        return bool
    
    def isCharFormat(self):
        'isCharFormat(self) -> bool'
        return bool
    
    def isEmpty(self):
        'isEmpty(self) -> bool'
        return bool
    
    def isFrameFormat(self):
        'isFrameFormat(self) -> bool'
        return bool
    
    def isImageFormat(self):
        'isImageFormat(self) -> bool'
        return bool
    
    def isListFormat(self):
        'isListFormat(self) -> bool'
        return bool
    
    def isTableCellFormat(self):
        'isTableCellFormat(self) -> bool'
        return bool
    
    def isTableFormat(self):
        'isTableFormat(self) -> bool'
        return bool
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def layoutDirection(self):
        'layoutDirection(self) -> PySide2.QtCore.Qt.LayoutDirection'
        return PySide2.QtCore.Qt.LayoutDirection
    
    def lengthProperty(self, propertyId):
        'lengthProperty(self, propertyId:int) -> PySide2.QtGui.QTextLength'
        return PySide2.QtGui.QTextLength
    
    def lengthVectorProperty(self, propertyId):
        'lengthVectorProperty(self, propertyId:int) -> typing.List'
        return typing.List
    
    def merge(self, other):
        'merge(self, other:PySide2.QtGui.QTextFormat)'
        pass
    
    def objectIndex(self):
        'objectIndex(self) -> int'
        return int
    
    def objectType(self):
        'objectType(self) -> int'
        return int
    
    def penProperty(self, propertyId):
        'penProperty(self, propertyId:int) -> PySide2.QtGui.QPen'
        return PySide2.QtGui.QPen
    
    def properties(self):
        'properties(self) -> typing.Dict'
        return typing.Dict
    
    def property(self, propertyId):
        'property(self, propertyId:int) -> typing.Any'
        return typing.Any
    
    def propertyCount(self):
        'propertyCount(self) -> int'
        return int
    
    def setBackground(self, brush):
        'setBackground(self, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setForeground(self, brush):
        'setForeground(self, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setLayoutDirection(self, direction):
        'setLayoutDirection(self, direction:PySide2.QtCore.Qt.LayoutDirection)'
        pass
    
    def setObjectIndex(self, object):
        'setObjectIndex(self, object:int)'
        pass
    
    def setObjectType(self, type):
        'setObjectType(self, type:int)'
        pass
    
    def setProperty(self, propertyId: int, lengths: typing.List):
        'setProperty(self, propertyId:int, lengths:typing.List)\nsetProperty(self, propertyId:int, value:typing.Any)'
        pass
    
    def stringProperty(self, propertyId):
        'stringProperty(self, propertyId:int) -> str'
        return str
    
    def swap(self, other):
        'swap(self, other:PySide2.QtGui.QTextFormat)'
        pass
    
    def toBlockFormat(self):
        'toBlockFormat(self) -> PySide2.QtGui.QTextBlockFormat'
        return PySide2.QtGui.QTextBlockFormat
    
    def toCharFormat(self):
        'toCharFormat(self) -> PySide2.QtGui.QTextCharFormat'
        return PySide2.QtGui.QTextCharFormat
    
    def toFrameFormat(self):
        'toFrameFormat(self) -> PySide2.QtGui.QTextFrameFormat'
        return PySide2.QtGui.QTextFrameFormat
    
    def toImageFormat(self):
        'toImageFormat(self) -> PySide2.QtGui.QTextImageFormat'
        return PySide2.QtGui.QTextImageFormat
    
    def toListFormat(self):
        'toListFormat(self) -> PySide2.QtGui.QTextListFormat'
        return PySide2.QtGui.QTextListFormat
    
    def toTableCellFormat(self):
        'toTableCellFormat(self) -> PySide2.QtGui.QTextTableCellFormat'
        return PySide2.QtGui.QTextTableCellFormat
    
    def toTableFormat(self):
        'toTableFormat(self) -> PySide2.QtGui.QTextTableFormat'
        return PySide2.QtGui.QTextTableFormat
    
    def type(self):
        'type(self) -> int'
        return int
    

class QTextFragment(_mod_Shiboken.Object):
    'QTextFragment(self)\nQTextFragment(self, o:PySide2.QtGui.QTextFragment)'
    __class__ = QTextFragment
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, o: PySide2.QtGui.QTextFragment):
        'QTextFragment(self)\nQTextFragment(self, o:PySide2.QtGui.QTextFragment)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def charFormat(self):
        'charFormat(self) -> PySide2.QtGui.QTextCharFormat'
        return PySide2.QtGui.QTextCharFormat
    
    def charFormatIndex(self):
        'charFormatIndex(self) -> int'
        return int
    
    def contains(self, position):
        'contains(self, position:int) -> bool'
        return bool
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def length(self):
        'length(self) -> int'
        return int
    
    def position(self):
        'position(self) -> int'
        return int
    
    def text(self):
        'text(self) -> str'
        return str
    

class QTextFrame(QTextObject):
    'QTextFrame(self, doc:PySide2.QtGui.QTextDocument)'
    __class__ = QTextFrame
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, doc: PySide2.QtGui.QTextDocument):
        'QTextFrame(self, doc:PySide2.QtGui.QTextDocument)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        '__iter__(self) -> object\n\nImplement iter(self).'
        return object
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def begin(self):
        'begin(self) -> PySide2.QtGui.QTextFrame.iterator'
        return PySide2.QtGui.QTextFrame.iterator
    
    def childFrames(self):
        'childFrames(self) -> typing.List'
        return typing.List
    
    def end(self):
        'end(self) -> PySide2.QtGui.QTextFrame.iterator'
        return PySide2.QtGui.QTextFrame.iterator
    
    def firstCursorPosition(self):
        'firstCursorPosition(self) -> PySide2.QtGui.QTextCursor'
        return PySide2.QtGui.QTextCursor
    
    def firstPosition(self):
        'firstPosition(self) -> int'
        return int
    
    def frameFormat(self):
        'frameFormat(self) -> PySide2.QtGui.QTextFrameFormat'
        return PySide2.QtGui.QTextFrameFormat
    
    iterator = iterator
    def lastCursorPosition(self):
        'lastCursorPosition(self) -> PySide2.QtGui.QTextCursor'
        return PySide2.QtGui.QTextCursor
    
    def lastPosition(self):
        'lastPosition(self) -> int'
        return int
    
    def parentFrame(self):
        'parentFrame(self) -> PySide2.QtGui.QTextFrame'
        return PySide2.QtGui.QTextFrame
    
    def setFrameFormat(self, format):
        'setFrameFormat(self, format:PySide2.QtGui.QTextFrameFormat)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QTextFrameFormat(QTextFormat):
    'QTextFrameFormat(self)\nQTextFrameFormat(self, QTextFrameFormat:PySide2.QtGui.QTextFrameFormat)\nQTextFrameFormat(self, fmt:PySide2.QtGui.QTextFormat)'
    BorderStyle = BorderStyle
    BorderStyle_Dashed = BorderStyle()
    BorderStyle_DotDash = BorderStyle()
    BorderStyle_DotDotDash = BorderStyle()
    BorderStyle_Dotted = BorderStyle()
    BorderStyle_Double = BorderStyle()
    BorderStyle_Groove = BorderStyle()
    BorderStyle_Inset = BorderStyle()
    BorderStyle_None = BorderStyle()
    BorderStyle_Outset = BorderStyle()
    BorderStyle_Ridge = BorderStyle()
    BorderStyle_Solid = BorderStyle()
    FloatLeft = Position()
    FloatRight = Position()
    InFlow = Position()
    Position = Position
    __class__ = QTextFrameFormat
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, QTextFrameFormat: PySide2.QtGui.QTextFrameFormat):
        'QTextFrameFormat(self)\nQTextFrameFormat(self, QTextFrameFormat:PySide2.QtGui.QTextFrameFormat)\nQTextFrameFormat(self, fmt:PySide2.QtGui.QTextFormat)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def border(self):
        'border(self) -> float'
        return float
    
    def borderBrush(self):
        'borderBrush(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def borderStyle(self):
        'borderStyle(self) -> PySide2.QtGui.QTextFrameFormat.BorderStyle'
        return PySide2.QtGui.QTextFrameFormat.BorderStyle
    
    def bottomMargin(self):
        'bottomMargin(self) -> float'
        return float
    
    def height(self):
        'height(self) -> PySide2.QtGui.QTextLength'
        return PySide2.QtGui.QTextLength
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def leftMargin(self):
        'leftMargin(self) -> float'
        return float
    
    def margin(self):
        'margin(self) -> float'
        return float
    
    def padding(self):
        'padding(self) -> float'
        return float
    
    def pageBreakPolicy(self):
        'pageBreakPolicy(self) -> PySide2.QtGui.QTextFormat.PageBreakFlags'
        return PySide2.QtGui.QTextFormat.PageBreakFlags
    
    def position(self):
        'position(self) -> PySide2.QtGui.QTextFrameFormat.Position'
        return PySide2.QtGui.QTextFrameFormat.Position
    
    def rightMargin(self):
        'rightMargin(self) -> float'
        return float
    
    def setBorder(self, border):
        'setBorder(self, border:float)'
        pass
    
    def setBorderBrush(self, brush):
        'setBorderBrush(self, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setBorderStyle(self, style):
        'setBorderStyle(self, style:PySide2.QtGui.QTextFrameFormat.BorderStyle)'
        pass
    
    def setBottomMargin(self, margin):
        'setBottomMargin(self, margin:float)'
        pass
    
    def setHeight(self, height: PySide2.QtGui.QTextLength):
        'setHeight(self, height:PySide2.QtGui.QTextLength)\nsetHeight(self, height:float)'
        pass
    
    def setLeftMargin(self, margin):
        'setLeftMargin(self, margin:float)'
        pass
    
    def setMargin(self, margin):
        'setMargin(self, margin:float)'
        pass
    
    def setPadding(self, padding):
        'setPadding(self, padding:float)'
        pass
    
    def setPageBreakPolicy(self, flags):
        'setPageBreakPolicy(self, flags:PySide2.QtGui.QTextFormat.PageBreakFlags)'
        pass
    
    def setPosition(self, f):
        'setPosition(self, f:PySide2.QtGui.QTextFrameFormat.Position)'
        pass
    
    def setRightMargin(self, margin):
        'setRightMargin(self, margin:float)'
        pass
    
    def setTopMargin(self, margin):
        'setTopMargin(self, margin:float)'
        pass
    
    def setWidth(self, length: PySide2.QtGui.QTextLength):
        'setWidth(self, length:PySide2.QtGui.QTextLength)\nsetWidth(self, width:float)'
        pass
    
    def topMargin(self):
        'topMargin(self) -> float'
        return float
    
    def width(self):
        'width(self) -> PySide2.QtGui.QTextLength'
        return PySide2.QtGui.QTextLength
    

class QTextImageFormat(QTextCharFormat):
    'QTextImageFormat(self)\nQTextImageFormat(self, QTextImageFormat:PySide2.QtGui.QTextImageFormat)\nQTextImageFormat(self, format:PySide2.QtGui.QTextFormat)'
    __class__ = QTextImageFormat
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, QTextImageFormat: PySide2.QtGui.QTextImageFormat):
        'QTextImageFormat(self)\nQTextImageFormat(self, QTextImageFormat:PySide2.QtGui.QTextImageFormat)\nQTextImageFormat(self, format:PySide2.QtGui.QTextFormat)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def height(self):
        'height(self) -> float'
        return float
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def name(self):
        'name(self) -> str'
        return str
    
    def quality(self):
        'quality(self) -> int'
        return int
    
    def setHeight(self, height):
        'setHeight(self, height:float)'
        pass
    
    def setName(self, name):
        'setName(self, name:str)'
        pass
    
    def setQuality(self, quality):
        'setQuality(self, quality:int=100)'
        pass
    
    def setWidth(self, width):
        'setWidth(self, width:float)'
        pass
    
    def width(self):
        'width(self) -> float'
        return float
    

class QTextInlineObject(_mod_Shiboken.Object):
    'QTextInlineObject(self)'
    __class__ = QTextInlineObject
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self):
        'QTextInlineObject(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def ascent(self):
        'ascent(self) -> float'
        return float
    
    def descent(self):
        'descent(self) -> float'
        return float
    
    def format(self):
        'format(self) -> PySide2.QtGui.QTextFormat'
        return PySide2.QtGui.QTextFormat
    
    def formatIndex(self):
        'formatIndex(self) -> int'
        return int
    
    def height(self):
        'height(self) -> float'
        return float
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def rect(self):
        'rect(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def setAscent(self, a):
        'setAscent(self, a:float)'
        pass
    
    def setDescent(self, d):
        'setDescent(self, d:float)'
        pass
    
    def setWidth(self, w):
        'setWidth(self, w:float)'
        pass
    
    def textDirection(self):
        'textDirection(self) -> PySide2.QtCore.Qt.LayoutDirection'
        return PySide2.QtCore.Qt.LayoutDirection
    
    def textPosition(self):
        'textPosition(self) -> int'
        return int
    
    def width(self):
        'width(self) -> float'
        return float
    

class QTextItem(_mod_Shiboken.Object):
    'QTextItem(self)'
    Dummy = RenderFlag()
    Overline = RenderFlag()
    RenderFlag = RenderFlag
    RenderFlags = RenderFlags
    RightToLeft = RenderFlag()
    StrikeOut = RenderFlag()
    Underline = RenderFlag()
    __class__ = QTextItem
    __dict__ = {}
    def __init__(self):
        'QTextItem(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def ascent(self):
        'ascent(self) -> float'
        return float
    
    def descent(self):
        'descent(self) -> float'
        return float
    
    def font(self):
        'font(self) -> PySide2.QtGui.QFont'
        return PySide2.QtGui.QFont
    
    def renderFlags(self):
        'renderFlags(self) -> PySide2.QtGui.QTextItem.RenderFlags'
        return PySide2.QtGui.QTextItem.RenderFlags
    
    def text(self):
        'text(self) -> str'
        return str
    
    def width(self):
        'width(self) -> float'
        return float
    

class QTextLayout(_mod_Shiboken.Object):
    'QTextLayout(self)\nQTextLayout(self, b:PySide2.QtGui.QTextBlock)\nQTextLayout(self, text:str)\nQTextLayout(self, text:str, font:PySide2.QtGui.QFont, paintdevice:typing.Union[PySide2.QtGui.QPaintDevice, NoneType]=None)'
    CursorMode = CursorMode
    FormatRange = FormatRange
    SkipCharacters = CursorMode()
    SkipWords = CursorMode()
    __class__ = QTextLayout
    __dict__ = {}
    def __init__(self, text: str, font: PySide2.QtGui.QFont, paintdevice: typing.Union[PySide2.QtGui.QPaintDevice,NoneType]=None):
        'QTextLayout(self)\nQTextLayout(self, b:PySide2.QtGui.QTextBlock)\nQTextLayout(self, text:str)\nQTextLayout(self, text:str, font:PySide2.QtGui.QFont, paintdevice:typing.Union[PySide2.QtGui.QPaintDevice, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def additionalFormats(self):
        'additionalFormats(self) -> typing.List'
        return typing.List
    
    def beginLayout(self):
        'beginLayout(self)'
        pass
    
    def boundingRect(self):
        'boundingRect(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def cacheEnabled(self):
        'cacheEnabled(self) -> bool'
        return bool
    
    def clearAdditionalFormats(self):
        'clearAdditionalFormats(self)'
        pass
    
    def clearFormats(self):
        'clearFormats(self)'
        pass
    
    def clearLayout(self):
        'clearLayout(self)'
        pass
    
    def createLine(self):
        'createLine(self) -> PySide2.QtGui.QTextLine'
        return PySide2.QtGui.QTextLine
    
    def cursorMoveStyle(self):
        'cursorMoveStyle(self) -> PySide2.QtCore.Qt.CursorMoveStyle'
        return PySide2.QtCore.Qt.CursorMoveStyle
    
    def draw(self, p, pos, selections, clip):
        'draw(self, p:PySide2.QtGui.QPainter, pos:PySide2.QtCore.QPointF, selections:typing.List=[], clip:PySide2.QtCore.QRectF=Default(QRectF))'
        pass
    
    def drawCursor(self, p: PySide2.QtGui.QPainter, pos: PySide2.QtCore.QPointF, cursorPosition: int, width: int):
        'drawCursor(self, p:PySide2.QtGui.QPainter, pos:PySide2.QtCore.QPointF, cursorPosition:int)\ndrawCursor(self, p:PySide2.QtGui.QPainter, pos:PySide2.QtCore.QPointF, cursorPosition:int, width:int)'
        pass
    
    def endLayout(self):
        'endLayout(self)'
        pass
    
    def font(self):
        'font(self) -> PySide2.QtGui.QFont'
        return PySide2.QtGui.QFont
    
    def formats(self):
        'formats(self) -> typing.List'
        return typing.List
    
    def isValidCursorPosition(self, pos):
        'isValidCursorPosition(self, pos:int) -> bool'
        return bool
    
    def leftCursorPosition(self, oldPos):
        'leftCursorPosition(self, oldPos:int) -> int'
        return int
    
    def lineAt(self, i):
        'lineAt(self, i:int) -> PySide2.QtGui.QTextLine'
        return PySide2.QtGui.QTextLine
    
    def lineCount(self):
        'lineCount(self) -> int'
        return int
    
    def lineForTextPosition(self, pos):
        'lineForTextPosition(self, pos:int) -> PySide2.QtGui.QTextLine'
        return PySide2.QtGui.QTextLine
    
    def maximumWidth(self):
        'maximumWidth(self) -> float'
        return float
    
    def minimumWidth(self):
        'minimumWidth(self) -> float'
        return float
    
    def nextCursorPosition(self, oldPos, mode):
        'nextCursorPosition(self, oldPos:int, mode:PySide2.QtGui.QTextLayout.CursorMode=PySide2.QtGui.QTextLayout.CursorMode.SkipCharacters) -> int'
        return int
    
    def position(self):
        'position(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def preeditAreaPosition(self):
        'preeditAreaPosition(self) -> int'
        return int
    
    def preeditAreaText(self):
        'preeditAreaText(self) -> str'
        return str
    
    def previousCursorPosition(self, oldPos, mode):
        'previousCursorPosition(self, oldPos:int, mode:PySide2.QtGui.QTextLayout.CursorMode=PySide2.QtGui.QTextLayout.CursorMode.SkipCharacters) -> int'
        return int
    
    def rightCursorPosition(self, oldPos):
        'rightCursorPosition(self, oldPos:int) -> int'
        return int
    
    def setAdditionalFormats(self, overrides):
        'setAdditionalFormats(self, overrides:typing.Sequence)'
        pass
    
    def setCacheEnabled(self, enable):
        'setCacheEnabled(self, enable:bool)'
        pass
    
    def setCursorMoveStyle(self, style):
        'setCursorMoveStyle(self, style:PySide2.QtCore.Qt.CursorMoveStyle)'
        pass
    
    def setFlags(self, flags):
        'setFlags(self, flags:int)'
        pass
    
    def setFont(self, f):
        'setFont(self, f:PySide2.QtGui.QFont)'
        pass
    
    def setFormats(self, overrides):
        'setFormats(self, overrides:typing.List)'
        pass
    
    def setPosition(self, p):
        'setPosition(self, p:PySide2.QtCore.QPointF)'
        pass
    
    def setPreeditArea(self, position, text):
        'setPreeditArea(self, position:int, text:str)'
        pass
    
    def setRawFont(self, rawFont):
        'setRawFont(self, rawFont:PySide2.QtGui.QRawFont)'
        pass
    
    def setText(self, string):
        'setText(self, string:str)'
        pass
    
    def setTextOption(self, option):
        'setTextOption(self, option:PySide2.QtGui.QTextOption)'
        pass
    
    def text(self):
        'text(self) -> str'
        return str
    
    def textOption(self):
        'textOption(self) -> PySide2.QtGui.QTextOption'
        return PySide2.QtGui.QTextOption
    

class QTextLength(_mod_Shiboken.Object):
    'QTextLength(self)\nQTextLength(self, QTextLength:PySide2.QtGui.QTextLength)\nQTextLength(self, type:PySide2.QtGui.QTextLength.Type, value:float)'
    FixedLength = Type()
    PercentageLength = Type()
    Type = Type
    VariableLength = Type()
    __class__ = QTextLength
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, type: PySide2.QtGui.QTextLength.Type, value: float):
        'QTextLength(self)\nQTextLength(self, QTextLength:PySide2.QtGui.QTextLength)\nQTextLength(self, type:PySide2.QtGui.QTextLength.Type, value:float)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QTextLength()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QTextLength()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def rawValue(self):
        'rawValue(self) -> float'
        return float
    
    def type(self):
        'type(self) -> PySide2.QtGui.QTextLength.Type'
        return PySide2.QtGui.QTextLength.Type
    
    def value(self, maximumLength):
        'value(self, maximumLength:float) -> float'
        return float
    

class QTextLine(_mod_Shiboken.Object):
    'QTextLine(self)'
    CursorBetweenCharacters = CursorPosition()
    CursorOnCharacter = CursorPosition()
    CursorPosition = CursorPosition
    Edge = Edge
    Leading = Edge()
    Trailing = Edge()
    __class__ = QTextLine
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self):
        'QTextLine(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def ascent(self):
        'ascent(self) -> float'
        return float
    
    def cursorToX(self, cursorPos, edge):
        'cursorToX(self, cursorPos:int, edge:PySide2.QtGui.QTextLine.Edge=PySide2.QtGui.QTextLine.Edge.Leading) -> float'
        return float
    
    def descent(self):
        'descent(self) -> float'
        return float
    
    def draw(self, p, point, selection):
        'draw(self, p:PySide2.QtGui.QPainter, point:PySide2.QtCore.QPointF, selection:typing.Union[PySide2.QtGui.QTextLayout.FormatRange, NoneType]=None)'
        pass
    
    def height(self):
        'height(self) -> float'
        return float
    
    def horizontalAdvance(self):
        'horizontalAdvance(self) -> float'
        return float
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def leading(self):
        'leading(self) -> float'
        return float
    
    def leadingIncluded(self):
        'leadingIncluded(self) -> bool'
        return bool
    
    def lineNumber(self):
        'lineNumber(self) -> int'
        return int
    
    def naturalTextRect(self):
        'naturalTextRect(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def naturalTextWidth(self):
        'naturalTextWidth(self) -> float'
        return float
    
    def position(self):
        'position(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def rect(self):
        'rect(self) -> PySide2.QtCore.QRectF'
        return PySide2.QtCore.QRectF
    
    def setLeadingIncluded(self, included):
        'setLeadingIncluded(self, included:bool)'
        pass
    
    def setLineWidth(self, width):
        'setLineWidth(self, width:float)'
        pass
    
    def setNumColumns(self, columns: int, alignmentWidth: float):
        'setNumColumns(self, columns:int)\nsetNumColumns(self, columns:int, alignmentWidth:float)'
        pass
    
    def setPosition(self, pos):
        'setPosition(self, pos:PySide2.QtCore.QPointF)'
        pass
    
    def textLength(self):
        'textLength(self) -> int'
        return int
    
    def textStart(self):
        'textStart(self) -> int'
        return int
    
    def width(self):
        'width(self) -> float'
        return float
    
    def x(self):
        'x(self) -> float'
        return float
    
    def xToCursor(self, x, edge):
        'xToCursor(self, x:float, edge:PySide2.QtGui.QTextLine.CursorPosition=PySide2.QtGui.QTextLine.CursorPosition.CursorBetweenCharacters) -> int'
        return int
    
    def y(self):
        'y(self) -> float'
        return float
    

class QTextList(QTextBlockGroup):
    'QTextList(self, doc:PySide2.QtGui.QTextDocument)'
    __class__ = QTextList
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, doc: PySide2.QtGui.QTextDocument):
        'QTextList(self, doc:PySide2.QtGui.QTextDocument)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def add(self, block):
        'add(self, block:PySide2.QtGui.QTextBlock)'
        pass
    
    def count(self):
        'count(self) -> int'
        return int
    
    def format(self):
        'format(self) -> PySide2.QtGui.QTextListFormat'
        return PySide2.QtGui.QTextListFormat
    
    def item(self, i):
        'item(self, i:int) -> PySide2.QtGui.QTextBlock'
        return PySide2.QtGui.QTextBlock
    
    def itemNumber(self, arg__1):
        'itemNumber(self, arg__1:PySide2.QtGui.QTextBlock) -> int'
        return int
    
    def itemText(self, arg__1):
        'itemText(self, arg__1:PySide2.QtGui.QTextBlock) -> str'
        return str
    
    def remove(self, arg__1):
        'remove(self, arg__1:PySide2.QtGui.QTextBlock)'
        pass
    
    def removeItem(self, i):
        'removeItem(self, i:int)'
        pass
    
    def setFormat(self, format: PySide2.QtGui.QTextListFormat):
        'setFormat(self, format:PySide2.QtGui.QTextFormat)\nsetFormat(self, format:PySide2.QtGui.QTextListFormat)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QTextListFormat(QTextFormat):
    'QTextListFormat(self)\nQTextListFormat(self, QTextListFormat:PySide2.QtGui.QTextListFormat)\nQTextListFormat(self, fmt:PySide2.QtGui.QTextFormat)'
    ListCircle = Style()
    ListDecimal = Style()
    ListDisc = Style()
    ListLowerAlpha = Style()
    ListLowerRoman = Style()
    ListSquare = Style()
    ListStyleUndefined = Style()
    ListUpperAlpha = Style()
    ListUpperRoman = Style()
    Style = Style
    __class__ = QTextListFormat
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, QTextListFormat: PySide2.QtGui.QTextListFormat):
        'QTextListFormat(self)\nQTextListFormat(self, QTextListFormat:PySide2.QtGui.QTextListFormat)\nQTextListFormat(self, fmt:PySide2.QtGui.QTextFormat)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def indent(self):
        'indent(self) -> int'
        return int
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def numberPrefix(self):
        'numberPrefix(self) -> str'
        return str
    
    def numberSuffix(self):
        'numberSuffix(self) -> str'
        return str
    
    def setIndent(self, indent):
        'setIndent(self, indent:int)'
        pass
    
    def setNumberPrefix(self, numberPrefix):
        'setNumberPrefix(self, numberPrefix:str)'
        pass
    
    def setNumberSuffix(self, numberSuffix):
        'setNumberSuffix(self, numberSuffix:str)'
        pass
    
    def setStyle(self, style):
        'setStyle(self, style:PySide2.QtGui.QTextListFormat.Style)'
        pass
    
    def style(self):
        'style(self) -> PySide2.QtGui.QTextListFormat.Style'
        return PySide2.QtGui.QTextListFormat.Style
    

class QTextObject(_mod_PySide2_QtCore.QObject):
    'QTextObject(self, doc:PySide2.QtGui.QTextDocument)'
    __class__ = QTextObject
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, doc: PySide2.QtGui.QTextDocument):
        'QTextObject(self, doc:PySide2.QtGui.QTextDocument)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def document(self):
        'document(self) -> PySide2.QtGui.QTextDocument'
        return PySide2.QtGui.QTextDocument
    
    def format(self):
        'format(self) -> PySide2.QtGui.QTextFormat'
        return PySide2.QtGui.QTextFormat
    
    def formatIndex(self):
        'formatIndex(self) -> int'
        return int
    
    def objectIndex(self):
        'objectIndex(self) -> int'
        return int
    
    def setFormat(self, format):
        'setFormat(self, format:PySide2.QtGui.QTextFormat)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QTextObjectInterface(_mod_Shiboken.Object):
    'QTextObjectInterface(self)'
    __class__ = QTextObjectInterface
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self):
        'QTextObjectInterface(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def drawObject(self, painter, rect, doc, posInDocument, format):
        'drawObject(self, painter:PySide2.QtGui.QPainter, rect:PySide2.QtCore.QRectF, doc:PySide2.QtGui.QTextDocument, posInDocument:int, format:PySide2.QtGui.QTextFormat)'
        pass
    
    def intrinsicSize(self, doc, posInDocument, format):
        'intrinsicSize(self, doc:PySide2.QtGui.QTextDocument, posInDocument:int, format:PySide2.QtGui.QTextFormat) -> PySide2.QtCore.QSizeF'
        return PySide2.QtCore.QSizeF
    

class QTextOption(_mod_Shiboken.Object):
    'QTextOption(self)\nQTextOption(self, alignment:PySide2.QtCore.Qt.Alignment)\nQTextOption(self, o:PySide2.QtGui.QTextOption)'
    AddSpaceForLineAndParagraphSeparators = Flag()
    CenterTab = TabType()
    DelimiterTab = TabType()
    Flag = Flag
    Flags = Flags
    IncludeTrailingSpaces = Flag()
    LeftTab = TabType()
    ManualWrap = WrapMode()
    NoWrap = WrapMode()
    RightTab = TabType()
    ShowDocumentTerminator = Flag()
    ShowLineAndParagraphSeparators = Flag()
    ShowTabsAndSpaces = Flag()
    SuppressColors = Flag()
    Tab = Tab
    TabType = TabType
    WordWrap = WrapMode()
    WrapAnywhere = WrapMode()
    WrapAtWordBoundaryOrAnywhere = WrapMode()
    WrapMode = WrapMode
    __class__ = QTextOption
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, alignment: PySide2.QtCore.Qt.Alignment):
        'QTextOption(self)\nQTextOption(self, alignment:PySide2.QtCore.Qt.Alignment)\nQTextOption(self, o:PySide2.QtGui.QTextOption)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def alignment(self):
        'alignment(self) -> PySide2.QtCore.Qt.Alignment'
        return PySide2.QtCore.Qt.Alignment
    
    def flags(self):
        'flags(self) -> PySide2.QtGui.QTextOption.Flags'
        return PySide2.QtGui.QTextOption.Flags
    
    def setAlignment(self, alignment):
        'setAlignment(self, alignment:PySide2.QtCore.Qt.Alignment)'
        pass
    
    def setFlags(self, flags):
        'setFlags(self, flags:PySide2.QtGui.QTextOption.Flags)'
        pass
    
    def setTabArray(self, tabStops):
        'setTabArray(self, tabStops:typing.Sequence)'
        pass
    
    def setTabStop(self, tabStop):
        'setTabStop(self, tabStop:float)'
        pass
    
    def setTabStopDistance(self, tabStopDistance):
        'setTabStopDistance(self, tabStopDistance:float)'
        pass
    
    def setTabs(self, tabStops):
        'setTabs(self, tabStops:typing.Sequence)'
        pass
    
    def setTextDirection(self, aDirection):
        'setTextDirection(self, aDirection:PySide2.QtCore.Qt.LayoutDirection)'
        pass
    
    def setUseDesignMetrics(self, b):
        'setUseDesignMetrics(self, b:bool)'
        pass
    
    def setWrapMode(self, wrap):
        'setWrapMode(self, wrap:PySide2.QtGui.QTextOption.WrapMode)'
        pass
    
    def tabArray(self):
        'tabArray(self) -> typing.List'
        return typing.List
    
    def tabStop(self):
        'tabStop(self) -> float'
        return float
    
    def tabStopDistance(self):
        'tabStopDistance(self) -> float'
        return float
    
    def tabs(self):
        'tabs(self) -> typing.List'
        return typing.List
    
    def textDirection(self):
        'textDirection(self) -> PySide2.QtCore.Qt.LayoutDirection'
        return PySide2.QtCore.Qt.LayoutDirection
    
    def useDesignMetrics(self):
        'useDesignMetrics(self) -> bool'
        return bool
    
    def wrapMode(self):
        'wrapMode(self) -> PySide2.QtGui.QTextOption.WrapMode'
        return PySide2.QtGui.QTextOption.WrapMode
    

class QTextTable(QTextFrame):
    'QTextTable(self, doc:PySide2.QtGui.QTextDocument)'
    __class__ = QTextTable
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, doc: PySide2.QtGui.QTextDocument):
        'QTextTable(self, doc:PySide2.QtGui.QTextDocument)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def appendColumns(self, count):
        'appendColumns(self, count:int)'
        pass
    
    def appendRows(self, count):
        'appendRows(self, count:int)'
        pass
    
    def cellAt(self, c: PySide2.QtGui.QTextCursor):
        'cellAt(self, c:PySide2.QtGui.QTextCursor) -> PySide2.QtGui.QTextTableCell\ncellAt(self, position:int) -> PySide2.QtGui.QTextTableCell\ncellAt(self, row:int, col:int) -> PySide2.QtGui.QTextTableCell'
        pass
    
    def columns(self):
        'columns(self) -> int'
        return int
    
    def format(self):
        'format(self) -> PySide2.QtGui.QTextTableFormat'
        return PySide2.QtGui.QTextTableFormat
    
    def insertColumns(self, pos, num):
        'insertColumns(self, pos:int, num:int)'
        pass
    
    def insertRows(self, pos, num):
        'insertRows(self, pos:int, num:int)'
        pass
    
    def mergeCells(self, row: int, col: int, numRows: int, numCols: int):
        'mergeCells(self, cursor:PySide2.QtGui.QTextCursor)\nmergeCells(self, row:int, col:int, numRows:int, numCols:int)'
        pass
    
    def removeColumns(self, pos, num):
        'removeColumns(self, pos:int, num:int)'
        pass
    
    def removeRows(self, pos, num):
        'removeRows(self, pos:int, num:int)'
        pass
    
    def resize(self, rows, cols):
        'resize(self, rows:int, cols:int)'
        pass
    
    def rowEnd(self, c):
        'rowEnd(self, c:PySide2.QtGui.QTextCursor) -> PySide2.QtGui.QTextCursor'
        return PySide2.QtGui.QTextCursor
    
    def rowStart(self, c):
        'rowStart(self, c:PySide2.QtGui.QTextCursor) -> PySide2.QtGui.QTextCursor'
        return PySide2.QtGui.QTextCursor
    
    def rows(self):
        'rows(self) -> int'
        return int
    
    def setFormat(self, format: PySide2.QtGui.QTextTableFormat):
        'setFormat(self, format:PySide2.QtGui.QTextFormat)\nsetFormat(self, format:PySide2.QtGui.QTextTableFormat)'
        pass
    
    def splitCell(self, row, col, numRows, numCols):
        'splitCell(self, row:int, col:int, numRows:int, numCols:int)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()

class QTextTableCell(_mod_Shiboken.Object):
    'QTextTableCell(self)\nQTextTableCell(self, o:PySide2.QtGui.QTextTableCell)'
    __class__ = QTextTableCell
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __init__(self, o: PySide2.QtGui.QTextTableCell):
        'QTextTableCell(self)\nQTextTableCell(self, o:PySide2.QtGui.QTextTableCell)'
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
    
    __module__ = 'PySide2.QtGui'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def begin(self):
        'begin(self) -> PySide2.QtGui.QTextFrame.iterator'
        return PySide2.QtGui.QTextFrame.iterator
    
    def column(self):
        'column(self) -> int'
        return int
    
    def columnSpan(self):
        'columnSpan(self) -> int'
        return int
    
    def end(self):
        'end(self) -> PySide2.QtGui.QTextFrame.iterator'
        return PySide2.QtGui.QTextFrame.iterator
    
    def firstCursorPosition(self):
        'firstCursorPosition(self) -> PySide2.QtGui.QTextCursor'
        return PySide2.QtGui.QTextCursor
    
    def firstPosition(self):
        'firstPosition(self) -> int'
        return int
    
    def format(self):
        'format(self) -> PySide2.QtGui.QTextCharFormat'
        return PySide2.QtGui.QTextCharFormat
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def lastCursorPosition(self):
        'lastCursorPosition(self) -> PySide2.QtGui.QTextCursor'
        return PySide2.QtGui.QTextCursor
    
    def lastPosition(self):
        'lastPosition(self) -> int'
        return int
    
    def row(self):
        'row(self) -> int'
        return int
    
    def rowSpan(self):
        'rowSpan(self) -> int'
        return int
    
    def setFormat(self, format):
        'setFormat(self, format:PySide2.QtGui.QTextCharFormat)'
        pass
    
    def tableCellFormatIndex(self):
        'tableCellFormatIndex(self) -> int'
        return int
    

class QTextTableCellFormat(QTextCharFormat):
    'QTextTableCellFormat(self)\nQTextTableCellFormat(self, QTextTableCellFormat:PySide2.QtGui.QTextTableCellFormat)\nQTextTableCellFormat(self, fmt:PySide2.QtGui.QTextFormat)'
    __class__ = QTextTableCellFormat
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, QTextTableCellFormat: PySide2.QtGui.QTextTableCellFormat):
        'QTextTableCellFormat(self)\nQTextTableCellFormat(self, QTextTableCellFormat:PySide2.QtGui.QTextTableCellFormat)\nQTextTableCellFormat(self, fmt:PySide2.QtGui.QTextFormat)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bottomBorder(self):
        'bottomBorder(self) -> float'
        return float
    
    def bottomBorderBrush(self):
        'bottomBorderBrush(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def bottomBorderStyle(self):
        'bottomBorderStyle(self) -> PySide2.QtGui.QTextFrameFormat.BorderStyle'
        return PySide2.QtGui.QTextFrameFormat.BorderStyle
    
    def bottomPadding(self):
        'bottomPadding(self) -> float'
        return float
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def leftBorder(self):
        'leftBorder(self) -> float'
        return float
    
    def leftBorderBrush(self):
        'leftBorderBrush(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def leftBorderStyle(self):
        'leftBorderStyle(self) -> PySide2.QtGui.QTextFrameFormat.BorderStyle'
        return PySide2.QtGui.QTextFrameFormat.BorderStyle
    
    def leftPadding(self):
        'leftPadding(self) -> float'
        return float
    
    def rightBorder(self):
        'rightBorder(self) -> float'
        return float
    
    def rightBorderBrush(self):
        'rightBorderBrush(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def rightBorderStyle(self):
        'rightBorderStyle(self) -> PySide2.QtGui.QTextFrameFormat.BorderStyle'
        return PySide2.QtGui.QTextFrameFormat.BorderStyle
    
    def rightPadding(self):
        'rightPadding(self) -> float'
        return float
    
    def setBorder(self, width):
        'setBorder(self, width:float)'
        pass
    
    def setBorderBrush(self, brush):
        'setBorderBrush(self, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setBorderStyle(self, style):
        'setBorderStyle(self, style:PySide2.QtGui.QTextFrameFormat.BorderStyle)'
        pass
    
    def setBottomBorder(self, width):
        'setBottomBorder(self, width:float)'
        pass
    
    def setBottomBorderBrush(self, brush):
        'setBottomBorderBrush(self, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setBottomBorderStyle(self, style):
        'setBottomBorderStyle(self, style:PySide2.QtGui.QTextFrameFormat.BorderStyle)'
        pass
    
    def setBottomPadding(self, padding):
        'setBottomPadding(self, padding:float)'
        pass
    
    def setLeftBorder(self, width):
        'setLeftBorder(self, width:float)'
        pass
    
    def setLeftBorderBrush(self, brush):
        'setLeftBorderBrush(self, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setLeftBorderStyle(self, style):
        'setLeftBorderStyle(self, style:PySide2.QtGui.QTextFrameFormat.BorderStyle)'
        pass
    
    def setLeftPadding(self, padding):
        'setLeftPadding(self, padding:float)'
        pass
    
    def setPadding(self, padding):
        'setPadding(self, padding:float)'
        pass
    
    def setRightBorder(self, width):
        'setRightBorder(self, width:float)'
        pass
    
    def setRightBorderBrush(self, brush):
        'setRightBorderBrush(self, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setRightBorderStyle(self, style):
        'setRightBorderStyle(self, style:PySide2.QtGui.QTextFrameFormat.BorderStyle)'
        pass
    
    def setRightPadding(self, padding):
        'setRightPadding(self, padding:float)'
        pass
    
    def setTopBorder(self, width):
        'setTopBorder(self, width:float)'
        pass
    
    def setTopBorderBrush(self, brush):
        'setTopBorderBrush(self, brush:PySide2.QtGui.QBrush)'
        pass
    
    def setTopBorderStyle(self, style):
        'setTopBorderStyle(self, style:PySide2.QtGui.QTextFrameFormat.BorderStyle)'
        pass
    
    def setTopPadding(self, padding):
        'setTopPadding(self, padding:float)'
        pass
    
    def topBorder(self):
        'topBorder(self) -> float'
        return float
    
    def topBorderBrush(self):
        'topBorderBrush(self) -> PySide2.QtGui.QBrush'
        return PySide2.QtGui.QBrush
    
    def topBorderStyle(self):
        'topBorderStyle(self) -> PySide2.QtGui.QTextFrameFormat.BorderStyle'
        return PySide2.QtGui.QTextFrameFormat.BorderStyle
    
    def topPadding(self):
        'topPadding(self) -> float'
        return float
    

class QTextTableFormat(QTextFrameFormat):
    'QTextTableFormat(self)\nQTextTableFormat(self, QTextTableFormat:PySide2.QtGui.QTextTableFormat)\nQTextTableFormat(self, fmt:PySide2.QtGui.QTextFormat)'
    __class__ = QTextTableFormat
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
    def __init__(self, QTextTableFormat: PySide2.QtGui.QTextTableFormat):
        'QTextTableFormat(self)\nQTextTableFormat(self, QTextTableFormat:PySide2.QtGui.QTextTableFormat)\nQTextTableFormat(self, fmt:PySide2.QtGui.QTextFormat)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def alignment(self):
        'alignment(self) -> PySide2.QtCore.Qt.Alignment'
        return PySide2.QtCore.Qt.Alignment
    
    def borderCollapse(self):
        'borderCollapse(self) -> bool'
        return bool
    
    def cellPadding(self):
        'cellPadding(self) -> float'
        return float
    
    def cellSpacing(self):
        'cellSpacing(self) -> float'
        return float
    
    def clearColumnWidthConstraints(self):
        'clearColumnWidthConstraints(self)'
        pass
    
    def columnWidthConstraints(self):
        'columnWidthConstraints(self) -> typing.List'
        return typing.List
    
    def columns(self):
        'columns(self) -> int'
        return int
    
    def headerRowCount(self):
        'headerRowCount(self) -> int'
        return int
    
    def isValid(self):
        'isValid(self) -> bool'
        return bool
    
    def setAlignment(self, alignment):
        'setAlignment(self, alignment:PySide2.QtCore.Qt.Alignment)'
        pass
    
    def setBorderCollapse(self, borderCollapse):
        'setBorderCollapse(self, borderCollapse:bool)'
        pass
    
    def setCellPadding(self, padding):
        'setCellPadding(self, padding:float)'
        pass
    
    def setCellSpacing(self, spacing):
        'setCellSpacing(self, spacing:float)'
        pass
    
    def setColumnWidthConstraints(self, constraints):
        'setColumnWidthConstraints(self, constraints:typing.List)'
        pass
    
    def setColumns(self, columns):
        'setColumns(self, columns:int)'
        pass
    
    def setHeaderRowCount(self, count):
        'setHeaderRowCount(self, count:int)'
        pass
    

class QToolBarChangeEvent(_mod_PySide2_QtCore.QEvent):
    'QToolBarChangeEvent(self, t:bool)'
    __class__ = QToolBarChangeEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, t: bool):
        'QToolBarChangeEvent(self, t:bool)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def toggle(self):
        'toggle(self) -> bool'
        return bool
    

class QTouchDevice(_mod_Shiboken.Object):
    'QTouchDevice(self)'
    Area = CapabilityFlag()
    Capabilities = Capabilities
    CapabilityFlag = CapabilityFlag
    DeviceType = DeviceType
    MouseEmulation = CapabilityFlag()
    NormalizedPosition = CapabilityFlag()
    Position = CapabilityFlag()
    Pressure = CapabilityFlag()
    RawPositions = CapabilityFlag()
    TouchPad = DeviceType()
    TouchScreen = DeviceType()
    Velocity = CapabilityFlag()
    __class__ = QTouchDevice
    __dict__ = {}
    def __init__(self):
        'QTouchDevice(self)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def capabilities(self):
        'capabilities(self) -> PySide2.QtGui.QTouchDevice.Capabilities'
        return PySide2.QtGui.QTouchDevice.Capabilities
    
    @classmethod
    def devices(cls):
        'devices() -> typing.List'
        return typing.List
    
    def maximumTouchPoints(self):
        'maximumTouchPoints(self) -> int'
        return int
    
    def name(self):
        'name(self) -> str'
        return str
    
    def setCapabilities(self, caps):
        'setCapabilities(self, caps:PySide2.QtGui.QTouchDevice.Capabilities)'
        pass
    
    def setMaximumTouchPoints(self, max):
        'setMaximumTouchPoints(self, max:int)'
        pass
    
    def setName(self, name):
        'setName(self, name:str)'
        pass
    
    def setType(self, devType):
        'setType(self, devType:PySide2.QtGui.QTouchDevice.DeviceType)'
        pass
    
    def type(self):
        'type(self) -> PySide2.QtGui.QTouchDevice.DeviceType'
        return PySide2.QtGui.QTouchDevice.DeviceType
    

class QTouchEvent(QInputEvent):
    'QTouchEvent(self, eventType:PySide2.QtCore.QEvent.Type, device:typing.Union[PySide2.QtGui.QTouchDevice, NoneType]=None, modifiers:PySide2.QtCore.Qt.KeyboardModifiers=PySide2.QtCore.Qt.KeyboardModifier.NoModifier, touchPointStates:PySide2.QtCore.Qt.TouchPointStates=Default(Qt.TouchPointStates), touchPoints:typing.Sequence=Default(QList< QTouchEvent.TouchPoint >))'
    TouchPoint = TouchPoint
    __class__ = QTouchEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, eventType: PySide2.QtCore.QEvent.Type, device: typing.Union[PySide2.QtGui.QTouchDevice,NoneType]=None, modifiers: PySide2.QtCore.Qt.KeyboardModifiers=PySide2.QtCore.Qt.KeyboardModifier.NoModifier, touchPointStates: PySide2.QtCore.Qt.TouchPointStates=Default(Qt.TouchPointStates), touchPoints: typing.Sequence=None):
        'QTouchEvent(self, eventType:PySide2.QtCore.QEvent.Type, device:typing.Union[PySide2.QtGui.QTouchDevice, NoneType]=None, modifiers:PySide2.QtCore.Qt.KeyboardModifiers=PySide2.QtCore.Qt.KeyboardModifier.NoModifier, touchPointStates:PySide2.QtCore.Qt.TouchPointStates=Default(Qt.TouchPointStates), touchPoints:typing.Sequence=Default(QList< QTouchEvent.TouchPoint >))'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _target(self):
        pass
    
    def device(self):
        'device(self) -> PySide2.QtGui.QTouchDevice'
        return PySide2.QtGui.QTouchDevice
    
    def setDevice(self, adevice):
        'setDevice(self, adevice:PySide2.QtGui.QTouchDevice)'
        pass
    
    def setTarget(self, atarget):
        'setTarget(self, atarget:PySide2.QtCore.QObject)'
        pass
    
    def setTouchPointStates(self, aTouchPointStates):
        'setTouchPointStates(self, aTouchPointStates:PySide2.QtCore.Qt.TouchPointStates)'
        pass
    
    def setTouchPoints(self, atouchPoints):
        'setTouchPoints(self, atouchPoints:typing.Sequence)'
        pass
    
    def setWindow(self, awindow):
        'setWindow(self, awindow:PySide2.QtGui.QWindow)'
        pass
    
    def target(self):
        'target(self) -> PySide2.QtCore.QObject'
        return PySide2.QtCore.QObject
    
    def touchPointStates(self):
        'touchPointStates(self) -> PySide2.QtCore.Qt.TouchPointStates'
        return PySide2.QtCore.Qt.TouchPointStates
    
    def touchPoints(self):
        'touchPoints(self) -> typing.List'
        return typing.List
    
    def window(self):
        'window(self) -> PySide2.QtGui.QWindow'
        return PySide2.QtGui.QWindow
    

class QTransform(_mod_Shiboken.Object):
    'QTransform(self)\nQTransform(self, h11:float, h12:float, h13:float, h21:float, h22:float, h23:float, h31:float, h32:float, h33:float=1.0)\nQTransform(self, h11:float, h12:float, h21:float, h22:float, dx:float, dy:float)\nQTransform(self, mtx:PySide2.QtGui.QMatrix)\nQTransform(self, other:PySide2.QtGui.QTransform)'
    TransformationType = TransformationType
    TxNone = TransformationType()
    TxProject = TransformationType()
    TxRotate = TransformationType()
    TxScale = TransformationType()
    TxShear = TransformationType()
    TxTranslate = TransformationType()
    def __add__(self, n):
        '__add__(self, n:float) -> PySide2.QtGui.QTransform\n\nReturn self+value.'
        return PySide2.QtGui.QTransform
    
    __class__ = QTransform
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, div):
        '__iadd__(self, div:float) -> PySide2.QtGui.QTransform\n\nReturn self+=value.'
        return PySide2.QtGui.QTransform
    
    def __imul__(self, arg__1: PySide2.QtGui.QTransform):
        '__imul__(self, arg__1:PySide2.QtGui.QTransform) -> PySide2.QtGui.QTransform\n__imul__(self, div:float) -> PySide2.QtGui.QTransform\n\nReturn self*=value.'
        return None
    
    def __init__(self, h11: float, h12: float, h13: float, h21: float, h22: float, h23: float, h31: float, h32: float, h33: float=1.0):
        'QTransform(self)\nQTransform(self, h11:float, h12:float, h13:float, h21:float, h22:float, h23:float, h31:float, h32:float, h33:float=1.0)\nQTransform(self, h11:float, h12:float, h21:float, h22:float, dx:float, dy:float)\nQTransform(self, mtx:PySide2.QtGui.QMatrix)\nQTransform(self, other:PySide2.QtGui.QTransform)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, div):
        '__isub__(self, div:float) -> PySide2.QtGui.QTransform\n\nReturn self-=value.'
        return PySide2.QtGui.QTransform
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __mul__(self, o: PySide2.QtGui.QTransform):
        '__mul__(self, l:PySide2.QtCore.QLine) -> PySide2.QtCore.QLine\n__mul__(self, l:PySide2.QtCore.QLineF) -> PySide2.QtCore.QLineF\n__mul__(self, n:float) -> PySide2.QtGui.QTransform\n__mul__(self, o:PySide2.QtGui.QTransform) -> PySide2.QtGui.QTransform\n__mul__(self, p:PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint\n__mul__(self, p:PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF\n\nReturn self*value.'
        return QTransform()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __radd__(self, value):
        'Return value+self.'
        return QTransform()
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QTransform()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QTransform()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QTransform()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __rsub__(self, value):
        'Return value-self.'
        return QTransform()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QTransform()
    
    def __sub__(self, n):
        '__sub__(self, n:float) -> PySide2.QtGui.QTransform\n\nReturn self-value.'
        return PySide2.QtGui.QTransform
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def adjoint(self):
        'adjoint(self) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def det(self):
        'det(self) -> float'
        return float
    
    def determinant(self):
        'determinant(self) -> float'
        return float
    
    def dx(self):
        'dx(self) -> float'
        return float
    
    def dy(self):
        'dy(self) -> float'
        return float
    
    @classmethod
    def fromScale(cls, dx, dy):
        'fromScale(dx:float, dy:float) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    @classmethod
    def fromTranslate(cls, dx, dy):
        'fromTranslate(dx:float, dy:float) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def inverted(self):
        'inverted(self) -> typing.Tuple'
        return typing.Tuple
    
    def isAffine(self):
        'isAffine(self) -> bool'
        return bool
    
    def isIdentity(self):
        'isIdentity(self) -> bool'
        return bool
    
    def isInvertible(self):
        'isInvertible(self) -> bool'
        return bool
    
    def isRotating(self):
        'isRotating(self) -> bool'
        return bool
    
    def isScaling(self):
        'isScaling(self) -> bool'
        return bool
    
    def isTranslating(self):
        'isTranslating(self) -> bool'
        return bool
    
    def m11(self):
        'm11(self) -> float'
        return float
    
    def m12(self):
        'm12(self) -> float'
        return float
    
    def m13(self):
        'm13(self) -> float'
        return float
    
    def m21(self):
        'm21(self) -> float'
        return float
    
    def m22(self):
        'm22(self) -> float'
        return float
    
    def m23(self):
        'm23(self) -> float'
        return float
    
    def m31(self):
        'm31(self) -> float'
        return float
    
    def m32(self):
        'm32(self) -> float'
        return float
    
    def m33(self):
        'm33(self) -> float'
        return float
    
    def map(self, p: PySide2.QtGui.QPainterPath):
        'map(self, a:PySide2.QtGui.QPolygon) -> PySide2.QtGui.QPolygon\nmap(self, a:PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF\nmap(self, l:PySide2.QtCore.QLine) -> PySide2.QtCore.QLine\nmap(self, l:PySide2.QtCore.QLineF) -> PySide2.QtCore.QLineF\nmap(self, p:PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint\nmap(self, p:PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF\nmap(self, p:PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath\nmap(self, r:PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion\nmap(self, x:float, y:float) -> typing.Tuple'
        pass
    
    def mapRect(self, arg__1: PySide2.QtCore.QRectF):
        'mapRect(self, arg__1:PySide2.QtCore.QRect) -> PySide2.QtCore.QRect\nmapRect(self, arg__1:PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF'
        pass
    
    def mapToPolygon(self, r):
        'mapToPolygon(self, r:PySide2.QtCore.QRect) -> PySide2.QtGui.QPolygon'
        return PySide2.QtGui.QPolygon
    
    @classmethod
    def quadToQuad(cls, one: PySide2.QtGui.QPolygonF, two: PySide2.QtGui.QPolygonF, result: PySide2.QtGui.QTransform):
        'quadToQuad(arg__1:PySide2.QtGui.QPolygonF, arg__2:PySide2.QtGui.QPolygonF) -> object\nquadToQuad(one:PySide2.QtGui.QPolygonF, two:PySide2.QtGui.QPolygonF, result:PySide2.QtGui.QTransform) -> bool'
        pass
    
    @classmethod
    def quadToSquare(cls, quad: PySide2.QtGui.QPolygonF, result: PySide2.QtGui.QTransform):
        'quadToSquare(arg__1:PySide2.QtGui.QPolygonF) -> object\nquadToSquare(quad:PySide2.QtGui.QPolygonF, result:PySide2.QtGui.QTransform) -> bool'
        pass
    
    def reset(self):
        'reset(self)'
        pass
    
    def rotate(self, a, axis):
        'rotate(self, a:float, axis:PySide2.QtCore.Qt.Axis=PySide2.QtCore.Qt.Axis.ZAxis) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def rotateRadians(self, a, axis):
        'rotateRadians(self, a:float, axis:PySide2.QtCore.Qt.Axis=PySide2.QtCore.Qt.Axis.ZAxis) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def scale(self, sx, sy):
        'scale(self, sx:float, sy:float) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def setMatrix(self, m11, m12, m13, m21, m22, m23, m31, m32, m33):
        'setMatrix(self, m11:float, m12:float, m13:float, m21:float, m22:float, m23:float, m31:float, m32:float, m33:float)'
        pass
    
    def shear(self, sh, sv):
        'shear(self, sh:float, sv:float) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    @classmethod
    def squareToQuad(cls, square: PySide2.QtGui.QPolygonF, result: PySide2.QtGui.QTransform):
        'squareToQuad(arg__1:PySide2.QtGui.QPolygonF) -> object\nsquareToQuad(square:PySide2.QtGui.QPolygonF, result:PySide2.QtGui.QTransform) -> bool'
        pass
    
    def toAffine(self):
        'toAffine(self) -> PySide2.QtGui.QMatrix'
        return PySide2.QtGui.QMatrix
    
    def translate(self, dx, dy):
        'translate(self, dx:float, dy:float) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def transposed(self):
        'transposed(self) -> PySide2.QtGui.QTransform'
        return PySide2.QtGui.QTransform
    
    def type(self):
        'type(self) -> PySide2.QtGui.QTransform.TransformationType'
        return PySide2.QtGui.QTransform.TransformationType
    

class QValidator(_mod_PySide2_QtCore.QObject):
    'QValidator(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
    Acceptable = State()
    Intermediate = State()
    Invalid = State()
    State = State
    __class__ = QValidator
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject,NoneType]=None):
        'QValidator(self, parent:typing.Union[PySide2.QtCore.QObject, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def changed(self):
        pass
    
    def fixup(self, arg__1):
        'fixup(self, arg__1:str)'
        pass
    
    def locale(self):
        'locale(self) -> PySide2.QtCore.QLocale'
        return PySide2.QtCore.QLocale
    
    def setLocale(self, locale):
        'setLocale(self, locale:PySide2.QtCore.QLocale)'
        pass
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def validate(self, arg__1, arg__2):
        'validate(self, arg__1:str, arg__2:int) -> PySide2.QtGui.QValidator.State'
        return PySide2.QtGui.QValidator.State
    

class QVector2D(_mod_Shiboken.Object):
    'QVector2D(self)\nQVector2D(self, point:PySide2.QtCore.QPoint)\nQVector2D(self, point:PySide2.QtCore.QPointF)\nQVector2D(self, vector:PySide2.QtGui.QVector3D)\nQVector2D(self, vector:PySide2.QtGui.QVector4D)\nQVector2D(self, xpos:float, ypos:float)'
    def __add__(self, v2):
        '__add__(self, v2:PySide2.QtGui.QVector2D) -> PySide2.QtGui.QVector2D\n\nReturn self+value.'
        return PySide2.QtGui.QVector2D
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QVector2D
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, vector):
        '__iadd__(self, vector:PySide2.QtGui.QVector2D) -> PySide2.QtGui.QVector2D\n\nReturn self+=value.'
        return PySide2.QtGui.QVector2D
    
    def __imul__(self, vector: PySide2.QtGui.QVector2D):
        '__imul__(self, factor:float) -> PySide2.QtGui.QVector2D\n__imul__(self, vector:PySide2.QtGui.QVector2D) -> PySide2.QtGui.QVector2D\n\nReturn self*=value.'
        return None
    
    def __init__(self, vector: PySide2.QtGui.QVector4D):
        'QVector2D(self)\nQVector2D(self, point:PySide2.QtCore.QPoint)\nQVector2D(self, point:PySide2.QtCore.QPointF)\nQVector2D(self, vector:PySide2.QtGui.QVector3D)\nQVector2D(self, vector:PySide2.QtGui.QVector4D)\nQVector2D(self, xpos:float, ypos:float)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, vector):
        '__isub__(self, vector:PySide2.QtGui.QVector2D) -> PySide2.QtGui.QVector2D\n\nReturn self-=value.'
        return PySide2.QtGui.QVector2D
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __mul__(self, v2: PySide2.QtGui.QVector2D):
        '__mul__(self, factor:float) -> PySide2.QtGui.QVector2D\n__mul__(self, v2:PySide2.QtGui.QVector2D) -> PySide2.QtGui.QVector2D\n\nReturn self*value.'
        return QVector2D()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '__neg__(self) -> PySide2.QtGui.QVector2D\n\n-self'
        return PySide2.QtGui.QVector2D
    
    def __radd__(self, value):
        'Return value+self.'
        return QVector2D()
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QVector2D()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QVector2D()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QVector2D()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __rsub__(self, value):
        'Return value-self.'
        return QVector2D()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QVector2D()
    
    def __sub__(self, v2):
        '__sub__(self, v2:PySide2.QtGui.QVector2D) -> PySide2.QtGui.QVector2D\n\nReturn self-value.'
        return PySide2.QtGui.QVector2D
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def distanceToLine(self, point, direction):
        'distanceToLine(self, point:PySide2.QtGui.QVector2D, direction:PySide2.QtGui.QVector2D) -> float'
        return float
    
    def distanceToPoint(self, point):
        'distanceToPoint(self, point:PySide2.QtGui.QVector2D) -> float'
        return float
    
    @classmethod
    def dotProduct(cls, v1, v2):
        'dotProduct(v1:PySide2.QtGui.QVector2D, v2:PySide2.QtGui.QVector2D) -> float'
        return float
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def length(self):
        'length(self) -> float'
        return float
    
    def lengthSquared(self):
        'lengthSquared(self) -> float'
        return float
    
    def normalize(self):
        'normalize(self)'
        pass
    
    def normalized(self):
        'normalized(self) -> PySide2.QtGui.QVector2D'
        return PySide2.QtGui.QVector2D
    
    def setX(self, x):
        'setX(self, x:float)'
        pass
    
    def setY(self, y):
        'setY(self, y:float)'
        pass
    
    def toPoint(self):
        'toPoint(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def toPointF(self):
        'toPointF(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def toTuple(self):
        'toTuple(self) -> object'
        return object
    
    def toVector3D(self):
        'toVector3D(self) -> PySide2.QtGui.QVector3D'
        return PySide2.QtGui.QVector3D
    
    def toVector4D(self):
        'toVector4D(self) -> PySide2.QtGui.QVector4D'
        return PySide2.QtGui.QVector4D
    
    def x(self):
        'x(self) -> float'
        return float
    
    def y(self):
        'y(self) -> float'
        return float
    

class QVector3D(_mod_Shiboken.Object):
    'QVector3D(self)\nQVector3D(self, point:PySide2.QtCore.QPoint)\nQVector3D(self, point:PySide2.QtCore.QPointF)\nQVector3D(self, vector:PySide2.QtGui.QVector2D)\nQVector3D(self, vector:PySide2.QtGui.QVector2D, zpos:float)\nQVector3D(self, vector:PySide2.QtGui.QVector4D)\nQVector3D(self, xpos:float, ypos:float, zpos:float)'
    def __add__(self, v2):
        '__add__(self, v2:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D\n\nReturn self+value.'
        return PySide2.QtGui.QVector3D
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QVector3D
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, vector):
        '__iadd__(self, vector:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D\n\nReturn self+=value.'
        return PySide2.QtGui.QVector3D
    
    def __imul__(self, vector: PySide2.QtGui.QVector3D):
        '__imul__(self, factor:float) -> PySide2.QtGui.QVector3D\n__imul__(self, vector:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D\n\nReturn self*=value.'
        return None
    
    def __init__(self, vector: PySide2.QtGui.QVector2D, zpos: float):
        'QVector3D(self)\nQVector3D(self, point:PySide2.QtCore.QPoint)\nQVector3D(self, point:PySide2.QtCore.QPointF)\nQVector3D(self, vector:PySide2.QtGui.QVector2D)\nQVector3D(self, vector:PySide2.QtGui.QVector2D, zpos:float)\nQVector3D(self, vector:PySide2.QtGui.QVector4D)\nQVector3D(self, xpos:float, ypos:float, zpos:float)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, vector):
        '__isub__(self, vector:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D\n\nReturn self-=value.'
        return PySide2.QtGui.QVector3D
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __mul__(self, quaternion: PySide2.QtGui.QQuaternion):
        '__mul__(self, factor:float) -> PySide2.QtGui.QVector3D\n__mul__(self, matrix:PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QVector3D\n__mul__(self, quaternion:PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QVector3D\n__mul__(self, v2:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D\n\nReturn self*value.'
        return QVector3D()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '__neg__(self) -> PySide2.QtGui.QVector3D\n\n-self'
        return PySide2.QtGui.QVector3D
    
    def __radd__(self, value):
        'Return value+self.'
        return QVector3D()
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QVector3D()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QVector3D()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QVector3D()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __rsub__(self, value):
        'Return value-self.'
        return QVector3D()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QVector3D()
    
    def __sub__(self, v2):
        '__sub__(self, v2:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D\n\nReturn self-value.'
        return PySide2.QtGui.QVector3D
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    @classmethod
    def crossProduct(cls, v1, v2):
        'crossProduct(v1:PySide2.QtGui.QVector3D, v2:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D'
        return PySide2.QtGui.QVector3D
    
    def distanceToLine(self, point, direction):
        'distanceToLine(self, point:PySide2.QtGui.QVector3D, direction:PySide2.QtGui.QVector3D) -> float'
        return float
    
    def distanceToPlane(self, plane1: PySide2.QtGui.QVector3D, plane2: PySide2.QtGui.QVector3D, plane3: PySide2.QtGui.QVector3D):
        'distanceToPlane(self, plane1:PySide2.QtGui.QVector3D, plane2:PySide2.QtGui.QVector3D, plane3:PySide2.QtGui.QVector3D) -> float\ndistanceToPlane(self, plane:PySide2.QtGui.QVector3D, normal:PySide2.QtGui.QVector3D) -> float'
        return 1.0
    
    def distanceToPoint(self, point):
        'distanceToPoint(self, point:PySide2.QtGui.QVector3D) -> float'
        return float
    
    @classmethod
    def dotProduct(cls, v1, v2):
        'dotProduct(v1:PySide2.QtGui.QVector3D, v2:PySide2.QtGui.QVector3D) -> float'
        return float
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def length(self):
        'length(self) -> float'
        return float
    
    def lengthSquared(self):
        'lengthSquared(self) -> float'
        return float
    
    @classmethod
    def normal(cls, v1: PySide2.QtGui.QVector3D, v2: PySide2.QtGui.QVector3D, v3: PySide2.QtGui.QVector3D):
        'normal(v1:PySide2.QtGui.QVector3D, v2:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D\nnormal(v1:PySide2.QtGui.QVector3D, v2:PySide2.QtGui.QVector3D, v3:PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D'
        pass
    
    def normalize(self):
        'normalize(self)'
        pass
    
    def normalized(self):
        'normalized(self) -> PySide2.QtGui.QVector3D'
        return PySide2.QtGui.QVector3D
    
    def project(self, modelView, projection, viewport):
        'project(self, modelView:PySide2.QtGui.QMatrix4x4, projection:PySide2.QtGui.QMatrix4x4, viewport:PySide2.QtCore.QRect) -> PySide2.QtGui.QVector3D'
        return PySide2.QtGui.QVector3D
    
    def setX(self, x):
        'setX(self, x:float)'
        pass
    
    def setY(self, y):
        'setY(self, y:float)'
        pass
    
    def setZ(self, z):
        'setZ(self, z:float)'
        pass
    
    def toPoint(self):
        'toPoint(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def toPointF(self):
        'toPointF(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def toTuple(self):
        'toTuple(self) -> object'
        return object
    
    def toVector2D(self):
        'toVector2D(self) -> PySide2.QtGui.QVector2D'
        return PySide2.QtGui.QVector2D
    
    def toVector4D(self):
        'toVector4D(self) -> PySide2.QtGui.QVector4D'
        return PySide2.QtGui.QVector4D
    
    def unproject(self, modelView, projection, viewport):
        'unproject(self, modelView:PySide2.QtGui.QMatrix4x4, projection:PySide2.QtGui.QMatrix4x4, viewport:PySide2.QtCore.QRect) -> PySide2.QtGui.QVector3D'
        return PySide2.QtGui.QVector3D
    
    def x(self):
        'x(self) -> float'
        return float
    
    def y(self):
        'y(self) -> float'
        return float
    
    def z(self):
        'z(self) -> float'
        return float
    

class QVector4D(_mod_Shiboken.Object):
    'QVector4D(self)\nQVector4D(self, point:PySide2.QtCore.QPoint)\nQVector4D(self, point:PySide2.QtCore.QPointF)\nQVector4D(self, vector:PySide2.QtGui.QVector2D)\nQVector4D(self, vector:PySide2.QtGui.QVector2D, zpos:float, wpos:float)\nQVector4D(self, vector:PySide2.QtGui.QVector3D)\nQVector4D(self, vector:PySide2.QtGui.QVector3D, wpos:float)\nQVector4D(self, xpos:float, ypos:float, zpos:float, wpos:float)'
    def __add__(self, v2):
        '__add__(self, v2:PySide2.QtGui.QVector4D) -> PySide2.QtGui.QVector4D\n\nReturn self+value.'
        return PySide2.QtGui.QVector4D
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QVector4D
    def __copy__(self):
        '__copy__()'
        pass
    
    __dict__ = {}
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
    def __iadd__(self, vector):
        '__iadd__(self, vector:PySide2.QtGui.QVector4D) -> PySide2.QtGui.QVector4D\n\nReturn self+=value.'
        return PySide2.QtGui.QVector4D
    
    def __imul__(self, vector: PySide2.QtGui.QVector4D):
        '__imul__(self, factor:float) -> PySide2.QtGui.QVector4D\n__imul__(self, vector:PySide2.QtGui.QVector4D) -> PySide2.QtGui.QVector4D\n\nReturn self*=value.'
        return None
    
    def __init__(self, vector: PySide2.QtGui.QVector2D, zpos: float, wpos: float):
        'QVector4D(self)\nQVector4D(self, point:PySide2.QtCore.QPoint)\nQVector4D(self, point:PySide2.QtCore.QPointF)\nQVector4D(self, vector:PySide2.QtGui.QVector2D)\nQVector4D(self, vector:PySide2.QtGui.QVector2D, zpos:float, wpos:float)\nQVector4D(self, vector:PySide2.QtGui.QVector3D)\nQVector4D(self, vector:PySide2.QtGui.QVector3D, wpos:float)\nQVector4D(self, xpos:float, ypos:float, zpos:float, wpos:float)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, vector):
        '__isub__(self, vector:PySide2.QtGui.QVector4D) -> PySide2.QtGui.QVector4D\n\nReturn self-=value.'
        return PySide2.QtGui.QVector4D
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, arg__1):
        '__lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self<<value.'
        return PySide2.QtCore.QDataStream
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PySide2.QtGui'
    def __mul__(self, matrix: PySide2.QtGui.QMatrix4x4):
        '__mul__(self, factor:float) -> PySide2.QtGui.QVector4D\n__mul__(self, matrix:PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QVector4D\n__mul__(self, v2:PySide2.QtGui.QVector4D) -> PySide2.QtGui.QVector4D\n\nReturn self*value.'
        return QVector4D()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '__neg__(self) -> PySide2.QtGui.QVector4D\n\n-self'
        return PySide2.QtGui.QVector4D
    
    def __radd__(self, value):
        'Return value+self.'
        return QVector4D()
    
    def __reduce__(self):
        '__reduce__(self) -> object'
        return object
    
    def __repr__(self):
        '__repr__(self) -> object\n\nReturn repr(self).'
        return object
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return QVector4D()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QVector4D()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QVector4D()
    
    def __rshift__(self, arg__1):
        '__rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream\n\nReturn self>>value.'
        return PySide2.QtCore.QDataStream
    
    def __rsub__(self, value):
        'Return value-self.'
        return QVector4D()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QVector4D()
    
    def __sub__(self, v2):
        '__sub__(self, v2:PySide2.QtGui.QVector4D) -> PySide2.QtGui.QVector4D\n\nReturn self-value.'
        return PySide2.QtGui.QVector4D
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    @classmethod
    def dotProduct(cls, v1, v2):
        'dotProduct(v1:PySide2.QtGui.QVector4D, v2:PySide2.QtGui.QVector4D) -> float'
        return float
    
    def isNull(self):
        'isNull(self) -> bool'
        return bool
    
    def length(self):
        'length(self) -> float'
        return float
    
    def lengthSquared(self):
        'lengthSquared(self) -> float'
        return float
    
    def normalize(self):
        'normalize(self)'
        pass
    
    def normalized(self):
        'normalized(self) -> PySide2.QtGui.QVector4D'
        return PySide2.QtGui.QVector4D
    
    def setW(self, w):
        'setW(self, w:float)'
        pass
    
    def setX(self, x):
        'setX(self, x:float)'
        pass
    
    def setY(self, y):
        'setY(self, y:float)'
        pass
    
    def setZ(self, z):
        'setZ(self, z:float)'
        pass
    
    def toPoint(self):
        'toPoint(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def toPointF(self):
        'toPointF(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def toTuple(self):
        'toTuple(self) -> object'
        return object
    
    def toVector2D(self):
        'toVector2D(self) -> PySide2.QtGui.QVector2D'
        return PySide2.QtGui.QVector2D
    
    def toVector2DAffine(self):
        'toVector2DAffine(self) -> PySide2.QtGui.QVector2D'
        return PySide2.QtGui.QVector2D
    
    def toVector3D(self):
        'toVector3D(self) -> PySide2.QtGui.QVector3D'
        return PySide2.QtGui.QVector3D
    
    def toVector3DAffine(self):
        'toVector3DAffine(self) -> PySide2.QtGui.QVector3D'
        return PySide2.QtGui.QVector3D
    
    def w(self):
        'w(self) -> float'
        return float
    
    def x(self):
        'x(self) -> float'
        return float
    
    def y(self):
        'y(self) -> float'
        return float
    
    def z(self):
        'z(self) -> float'
        return float
    

class QWhatsThisClickedEvent(_mod_PySide2_QtCore.QEvent):
    'QWhatsThisClickedEvent(self, href:str)'
    __class__ = QWhatsThisClickedEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, href: str):
        'QWhatsThisClickedEvent(self, href:str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def href(self):
        'href(self) -> str'
        return str
    

class QWheelEvent(QInputEvent):
    'QWheelEvent(self, pos:PySide2.QtCore.QPointF, delta:int, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, orient:PySide2.QtCore.Qt.Orientation=PySide2.QtCore.Qt.Orientation.Vertical)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, delta:int, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, orient:PySide2.QtCore.Qt.Orientation=PySide2.QtCore.Qt.Orientation.Vertical)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, pixelDelta:PySide2.QtCore.QPoint, angleDelta:PySide2.QtCore.QPoint, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, phase:PySide2.QtCore.Qt.ScrollPhase, inverted:bool, source:PySide2.QtCore.Qt.MouseEventSource=PySide2.QtCore.Qt.MouseEventSource.MouseEventNotSynthesized)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, pixelDelta:PySide2.QtCore.QPoint, angleDelta:PySide2.QtCore.QPoint, qt4Delta:int, qt4Orientation:PySide2.QtCore.Qt.Orientation, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, pixelDelta:PySide2.QtCore.QPoint, angleDelta:PySide2.QtCore.QPoint, qt4Delta:int, qt4Orientation:PySide2.QtCore.Qt.Orientation, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, phase:PySide2.QtCore.Qt.ScrollPhase)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, pixelDelta:PySide2.QtCore.QPoint, angleDelta:PySide2.QtCore.QPoint, qt4Delta:int, qt4Orientation:PySide2.QtCore.Qt.Orientation, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, phase:PySide2.QtCore.Qt.ScrollPhase, source:PySide2.QtCore.Qt.MouseEventSource)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, pixelDelta:PySide2.QtCore.QPoint, angleDelta:PySide2.QtCore.QPoint, qt4Delta:int, qt4Orientation:PySide2.QtCore.Qt.Orientation, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, phase:PySide2.QtCore.Qt.ScrollPhase, source:PySide2.QtCore.Qt.MouseEventSource, inverted:bool)'
    __class__ = QWheelEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, pos: PySide2.QtCore.QPointF, globalPos: PySide2.QtCore.QPointF, pixelDelta: PySide2.QtCore.QPoint, angleDelta: PySide2.QtCore.QPoint, qt4Delta: int, qt4Orientation: PySide2.QtCore.Qt.Orientation, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, phase: PySide2.QtCore.Qt.ScrollPhase, source: PySide2.QtCore.Qt.MouseEventSource, inverted: bool):
        'QWheelEvent(self, pos:PySide2.QtCore.QPointF, delta:int, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, orient:PySide2.QtCore.Qt.Orientation=PySide2.QtCore.Qt.Orientation.Vertical)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, delta:int, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, orient:PySide2.QtCore.Qt.Orientation=PySide2.QtCore.Qt.Orientation.Vertical)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, pixelDelta:PySide2.QtCore.QPoint, angleDelta:PySide2.QtCore.QPoint, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, phase:PySide2.QtCore.Qt.ScrollPhase, inverted:bool, source:PySide2.QtCore.Qt.MouseEventSource=PySide2.QtCore.Qt.MouseEventSource.MouseEventNotSynthesized)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, pixelDelta:PySide2.QtCore.QPoint, angleDelta:PySide2.QtCore.QPoint, qt4Delta:int, qt4Orientation:PySide2.QtCore.Qt.Orientation, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, pixelDelta:PySide2.QtCore.QPoint, angleDelta:PySide2.QtCore.QPoint, qt4Delta:int, qt4Orientation:PySide2.QtCore.Qt.Orientation, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, phase:PySide2.QtCore.Qt.ScrollPhase)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, pixelDelta:PySide2.QtCore.QPoint, angleDelta:PySide2.QtCore.QPoint, qt4Delta:int, qt4Orientation:PySide2.QtCore.Qt.Orientation, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, phase:PySide2.QtCore.Qt.ScrollPhase, source:PySide2.QtCore.Qt.MouseEventSource)\nQWheelEvent(self, pos:PySide2.QtCore.QPointF, globalPos:PySide2.QtCore.QPointF, pixelDelta:PySide2.QtCore.QPoint, angleDelta:PySide2.QtCore.QPoint, qt4Delta:int, qt4Orientation:PySide2.QtCore.Qt.Orientation, buttons:PySide2.QtCore.Qt.MouseButtons, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, phase:PySide2.QtCore.Qt.ScrollPhase, source:PySide2.QtCore.Qt.MouseEventSource, inverted:bool)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _unused_(self):
        pass
    
    @property
    def angleD(self):
        pass
    
    def angleDelta(self):
        'angleDelta(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def buttons(self):
        'buttons(self) -> PySide2.QtCore.Qt.MouseButtons'
        return PySide2.QtCore.Qt.MouseButtons
    
    def delta(self):
        'delta(self) -> int'
        return int
    
    def globalPos(self):
        'globalPos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def globalPosF(self):
        'globalPosF(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def globalPosition(self):
        'globalPosition(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def globalX(self):
        'globalX(self) -> int'
        return int
    
    def globalY(self):
        'globalY(self) -> int'
        return int
    
    def inverted(self):
        'inverted(self) -> bool'
        return bool
    
    @property
    def invertedScrolling(self):
        pass
    
    def orientation(self):
        'orientation(self) -> PySide2.QtCore.Qt.Orientation'
        return PySide2.QtCore.Qt.Orientation
    
    @property
    def ph(self):
        pass
    
    def phase(self):
        'phase(self) -> PySide2.QtCore.Qt.ScrollPhase'
        return PySide2.QtCore.Qt.ScrollPhase
    
    @property
    def pixelD(self):
        pass
    
    def pixelDelta(self):
        'pixelDelta(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def pos(self):
        'pos(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def posF(self):
        'posF(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    def position(self):
        'position(self) -> PySide2.QtCore.QPointF'
        return PySide2.QtCore.QPointF
    
    @property
    def qt4D(self):
        pass
    
    @property
    def qt4O(self):
        pass
    
    @property
    def reserved(self):
        pass
    
    def source(self):
        'source(self) -> PySide2.QtCore.Qt.MouseEventSource'
        return PySide2.QtCore.Qt.MouseEventSource
    
    @property
    def src(self):
        pass
    
    def x(self):
        'x(self) -> int'
        return int
    
    def y(self):
        'y(self) -> int'
        return int
    

class QWindow(_mod_PySide2_QtCore.QObject,QSurface):
    'QWindow(self, parent:PySide2.QtGui.QWindow)\nQWindow(self, screen:typing.Union[PySide2.QtGui.QScreen, NoneType]=None)'
    AncestorMode = AncestorMode
    AutomaticVisibility = Visibility()
    ExcludeTransients = AncestorMode()
    FullScreen = Visibility()
    Hidden = Visibility()
    IncludeTransients = AncestorMode()
    Maximized = Visibility()
    Minimized = Visibility()
    Visibility = Visibility
    Windowed = Visibility()
    __class__ = QWindow
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, screen: typing.Union[PySide2.QtGui.QScreen,NoneType]=None):
        'QWindow(self, parent:PySide2.QtGui.QWindow)\nQWindow(self, screen:typing.Union[PySide2.QtGui.QScreen, NoneType]=None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def accessibleRoot(self):
        'accessibleRoot(self) -> PySide2.QtGui.QAccessibleInterface'
        return PySide2.QtGui.QAccessibleInterface
    
    def activeChanged(self):
        pass
    
    def alert(self, msec):
        'alert(self, msec:int)'
        pass
    
    def baseSize(self):
        'baseSize(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def close(self):
        'close(self) -> bool'
        return bool
    
    def contentOrientation(self):
        'contentOrientation(self) -> PySide2.QtCore.Qt.ScreenOrientation'
        return PySide2.QtCore.Qt.ScreenOrientation
    
    def contentOrientationChanged(self):
        pass
    
    def create(self):
        'create(self)'
        pass
    
    def cursor(self):
        'cursor(self) -> PySide2.QtGui.QCursor'
        return PySide2.QtGui.QCursor
    
    def destroy(self):
        'destroy(self)'
        pass
    
    def devicePixelRatio(self):
        'devicePixelRatio(self) -> float'
        return float
    
    def event(self, arg__1):
        'event(self, arg__1:PySide2.QtCore.QEvent) -> bool'
        return bool
    
    def exposeEvent(self, arg__1):
        'exposeEvent(self, arg__1:PySide2.QtGui.QExposeEvent)'
        pass
    
    def filePath(self):
        'filePath(self) -> str'
        return str
    
    def flags(self):
        'flags(self) -> PySide2.QtCore.Qt.WindowFlags'
        return PySide2.QtCore.Qt.WindowFlags
    
    def focusInEvent(self, arg__1):
        'focusInEvent(self, arg__1:PySide2.QtGui.QFocusEvent)'
        pass
    
    def focusObject(self):
        'focusObject(self) -> PySide2.QtCore.QObject'
        return PySide2.QtCore.QObject
    
    def focusObjectChanged(self):
        pass
    
    def focusOutEvent(self, arg__1):
        'focusOutEvent(self, arg__1:PySide2.QtGui.QFocusEvent)'
        pass
    
    def format(self):
        'format(self) -> PySide2.QtGui.QSurfaceFormat'
        return PySide2.QtGui.QSurfaceFormat
    
    def frameGeometry(self):
        'frameGeometry(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def frameMargins(self):
        'frameMargins(self) -> PySide2.QtCore.QMargins'
        return PySide2.QtCore.QMargins
    
    def framePosition(self):
        'framePosition(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    @classmethod
    def fromWinId(cls, id):
        'fromWinId(id:int) -> PySide2.QtGui.QWindow'
        return PySide2.QtGui.QWindow
    
    def geometry(self):
        'geometry(self) -> PySide2.QtCore.QRect'
        return PySide2.QtCore.QRect
    
    def height(self):
        'height(self) -> int'
        return int
    
    def heightChanged(self):
        pass
    
    def hide(self):
        'hide(self)'
        pass
    
    def hideEvent(self, arg__1):
        'hideEvent(self, arg__1:PySide2.QtGui.QHideEvent)'
        pass
    
    def icon(self):
        'icon(self) -> PySide2.QtGui.QIcon'
        return PySide2.QtGui.QIcon
    
    def isActive(self):
        'isActive(self) -> bool'
        return bool
    
    def isAncestorOf(self, child, mode):
        'isAncestorOf(self, child:PySide2.QtGui.QWindow, mode:PySide2.QtGui.QWindow.AncestorMode=PySide2.QtGui.QWindow.AncestorMode.IncludeTransients) -> bool'
        return bool
    
    def isExposed(self):
        'isExposed(self) -> bool'
        return bool
    
    def isModal(self):
        'isModal(self) -> bool'
        return bool
    
    def isTopLevel(self):
        'isTopLevel(self) -> bool'
        return bool
    
    def isVisible(self):
        'isVisible(self) -> bool'
        return bool
    
    def keyPressEvent(self, arg__1):
        'keyPressEvent(self, arg__1:PySide2.QtGui.QKeyEvent)'
        pass
    
    def keyReleaseEvent(self, arg__1):
        'keyReleaseEvent(self, arg__1:PySide2.QtGui.QKeyEvent)'
        pass
    
    def lower(self):
        'lower(self)'
        pass
    
    def mapFromGlobal(self, pos):
        'mapFromGlobal(self, pos:PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def mapToGlobal(self, pos):
        'mapToGlobal(self, pos:PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def mask(self):
        'mask(self) -> PySide2.QtGui.QRegion'
        return PySide2.QtGui.QRegion
    
    def maximumHeight(self):
        'maximumHeight(self) -> int'
        return int
    
    def maximumHeightChanged(self):
        pass
    
    def maximumSize(self):
        'maximumSize(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def maximumWidth(self):
        'maximumWidth(self) -> int'
        return int
    
    def maximumWidthChanged(self):
        pass
    
    def minimumHeight(self):
        'minimumHeight(self) -> int'
        return int
    
    def minimumHeightChanged(self):
        pass
    
    def minimumSize(self):
        'minimumSize(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def minimumWidth(self):
        'minimumWidth(self) -> int'
        return int
    
    def minimumWidthChanged(self):
        pass
    
    def modality(self):
        'modality(self) -> PySide2.QtCore.Qt.WindowModality'
        return PySide2.QtCore.Qt.WindowModality
    
    def modalityChanged(self):
        pass
    
    def mouseDoubleClickEvent(self, arg__1):
        'mouseDoubleClickEvent(self, arg__1:PySide2.QtGui.QMouseEvent)'
        pass
    
    def mouseMoveEvent(self, arg__1):
        'mouseMoveEvent(self, arg__1:PySide2.QtGui.QMouseEvent)'
        pass
    
    def mousePressEvent(self, arg__1):
        'mousePressEvent(self, arg__1:PySide2.QtGui.QMouseEvent)'
        pass
    
    def mouseReleaseEvent(self, arg__1):
        'mouseReleaseEvent(self, arg__1:PySide2.QtGui.QMouseEvent)'
        pass
    
    def moveEvent(self, arg__1):
        'moveEvent(self, arg__1:PySide2.QtGui.QMoveEvent)'
        pass
    
    def nativeEvent(self, eventType, message):
        'nativeEvent(self, eventType:PySide2.QtCore.QByteArray, message:int) -> typing.Tuple'
        return typing.Tuple
    
    def opacity(self):
        'opacity(self) -> float'
        return float
    
    def opacityChanged(self):
        pass
    
    def parent(self, mode: PySide2.QtGui.QWindow.AncestorMode):
        'parent(self) -> PySide2.QtGui.QWindow\nparent(self, mode:PySide2.QtGui.QWindow.AncestorMode) -> PySide2.QtGui.QWindow'
        pass
    
    def position(self):
        'position(self) -> PySide2.QtCore.QPoint'
        return PySide2.QtCore.QPoint
    
    def raise_(self):
        'raise_(self)'
        pass
    
    def reportContentOrientationChange(self, orientation):
        'reportContentOrientationChange(self, orientation:PySide2.QtCore.Qt.ScreenOrientation)'
        pass
    
    def requestActivate(self):
        'requestActivate(self)'
        pass
    
    def requestUpdate(self):
        'requestUpdate(self)'
        pass
    
    def requestedFormat(self):
        'requestedFormat(self) -> PySide2.QtGui.QSurfaceFormat'
        return PySide2.QtGui.QSurfaceFormat
    
    def resize(self, newSize: PySide2.QtCore.QSize):
        'resize(self, newSize:PySide2.QtCore.QSize)\nresize(self, w:int, h:int)'
        pass
    
    def resizeEvent(self, arg__1):
        'resizeEvent(self, arg__1:PySide2.QtGui.QResizeEvent)'
        pass
    
    def screen(self):
        'screen(self) -> PySide2.QtGui.QScreen'
        return PySide2.QtGui.QScreen
    
    def screenChanged(self):
        pass
    
    def setBaseSize(self, size):
        'setBaseSize(self, size:PySide2.QtCore.QSize)'
        pass
    
    def setCursor(self, arg__1):
        'setCursor(self, arg__1:PySide2.QtGui.QCursor)'
        pass
    
    def setFilePath(self, filePath):
        'setFilePath(self, filePath:str)'
        pass
    
    def setFlag(self, arg__1, on):
        'setFlag(self, arg__1:PySide2.QtCore.Qt.WindowType, on:bool=True)'
        pass
    
    def setFlags(self, flags):
        'setFlags(self, flags:PySide2.QtCore.Qt.WindowFlags)'
        pass
    
    def setFormat(self, format):
        'setFormat(self, format:PySide2.QtGui.QSurfaceFormat)'
        pass
    
    def setFramePosition(self, point):
        'setFramePosition(self, point:PySide2.QtCore.QPoint)'
        pass
    
    def setGeometry(self, posx: int, posy: int, w: int, h: int):
        'setGeometry(self, posx:int, posy:int, w:int, h:int)\nsetGeometry(self, rect:PySide2.QtCore.QRect)'
        pass
    
    def setHeight(self, arg):
        'setHeight(self, arg:int)'
        pass
    
    def setIcon(self, icon):
        'setIcon(self, icon:PySide2.QtGui.QIcon)'
        pass
    
    def setKeyboardGrabEnabled(self, grab):
        'setKeyboardGrabEnabled(self, grab:bool) -> bool'
        return bool
    
    def setMask(self, region):
        'setMask(self, region:PySide2.QtGui.QRegion)'
        pass
    
    def setMaximumHeight(self, h):
        'setMaximumHeight(self, h:int)'
        pass
    
    def setMaximumSize(self, size):
        'setMaximumSize(self, size:PySide2.QtCore.QSize)'
        pass
    
    def setMaximumWidth(self, w):
        'setMaximumWidth(self, w:int)'
        pass
    
    def setMinimumHeight(self, h):
        'setMinimumHeight(self, h:int)'
        pass
    
    def setMinimumSize(self, size):
        'setMinimumSize(self, size:PySide2.QtCore.QSize)'
        pass
    
    def setMinimumWidth(self, w):
        'setMinimumWidth(self, w:int)'
        pass
    
    def setModality(self, modality):
        'setModality(self, modality:PySide2.QtCore.Qt.WindowModality)'
        pass
    
    def setMouseGrabEnabled(self, grab):
        'setMouseGrabEnabled(self, grab:bool) -> bool'
        return bool
    
    def setOpacity(self, level):
        'setOpacity(self, level:float)'
        pass
    
    def setParent(self, parent: PySide2.QtCore.QObject):
        'setParent(self, parent:PySide2.QtCore.QObject)\nsetParent(self, parent:PySide2.QtGui.QWindow)'
        pass
    
    def setPosition(self, pt: PySide2.QtCore.QPoint):
        'setPosition(self, posx:int, posy:int)\nsetPosition(self, pt:PySide2.QtCore.QPoint)'
        pass
    
    def setScreen(self, screen):
        'setScreen(self, screen:PySide2.QtGui.QScreen)'
        pass
    
    def setSizeIncrement(self, size):
        'setSizeIncrement(self, size:PySide2.QtCore.QSize)'
        pass
    
    def setSurfaceType(self, surfaceType):
        'setSurfaceType(self, surfaceType:PySide2.QtGui.QSurface.SurfaceType)'
        pass
    
    def setTitle(self, arg__1):
        'setTitle(self, arg__1:str)'
        pass
    
    def setTransientParent(self, parent):
        'setTransientParent(self, parent:PySide2.QtGui.QWindow)'
        pass
    
    def setVisibility(self, v):
        'setVisibility(self, v:PySide2.QtGui.QWindow.Visibility)'
        pass
    
    def setVisible(self, visible):
        'setVisible(self, visible:bool)'
        pass
    
    def setWidth(self, arg):
        'setWidth(self, arg:int)'
        pass
    
    def setWindowState(self, state):
        'setWindowState(self, state:PySide2.QtCore.Qt.WindowState)'
        pass
    
    def setWindowStates(self, states):
        'setWindowStates(self, states:PySide2.QtCore.Qt.WindowStates)'
        pass
    
    def setX(self, arg):
        'setX(self, arg:int)'
        pass
    
    def setY(self, arg):
        'setY(self, arg:int)'
        pass
    
    def show(self):
        'show(self)'
        pass
    
    def showEvent(self, arg__1):
        'showEvent(self, arg__1:PySide2.QtGui.QShowEvent)'
        pass
    
    def showFullScreen(self):
        'showFullScreen(self)'
        pass
    
    def showMaximized(self):
        'showMaximized(self)'
        pass
    
    def showMinimized(self):
        'showMinimized(self)'
        pass
    
    def showNormal(self):
        'showNormal(self)'
        pass
    
    def size(self):
        'size(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def sizeIncrement(self):
        'sizeIncrement(self) -> PySide2.QtCore.QSize'
        return PySide2.QtCore.QSize
    
    def startSystemMove(self):
        'startSystemMove(self) -> bool'
        return bool
    
    def startSystemResize(self, edges):
        'startSystemResize(self, edges:PySide2.QtCore.Qt.Edges) -> bool'
        return bool
    
    staticMetaObject = _mod_PySide2_QtCore.QMetaObject()
    def surfaceHandle(self):
        'surfaceHandle(self) -> int'
        return int
    
    def surfaceType(self):
        'surfaceType(self) -> PySide2.QtGui.QSurface.SurfaceType'
        return PySide2.QtGui.QSurface.SurfaceType
    
    def tabletEvent(self, arg__1):
        'tabletEvent(self, arg__1:PySide2.QtGui.QTabletEvent)'
        pass
    
    def title(self):
        'title(self) -> str'
        return str
    
    def touchEvent(self, arg__1):
        'touchEvent(self, arg__1:PySide2.QtGui.QTouchEvent)'
        pass
    
    def transientParent(self):
        'transientParent(self) -> PySide2.QtGui.QWindow'
        return PySide2.QtGui.QWindow
    
    def transientParentChanged(self):
        pass
    
    def type(self):
        'type(self) -> PySide2.QtCore.Qt.WindowType'
        return PySide2.QtCore.Qt.WindowType
    
    def unsetCursor(self):
        'unsetCursor(self)'
        pass
    
    def visibility(self):
        'visibility(self) -> PySide2.QtGui.QWindow.Visibility'
        return PySide2.QtGui.QWindow.Visibility
    
    def visibilityChanged(self):
        pass
    
    def visibleChanged(self):
        pass
    
    def wheelEvent(self, arg__1):
        'wheelEvent(self, arg__1:PySide2.QtGui.QWheelEvent)'
        pass
    
    def width(self):
        'width(self) -> int'
        return int
    
    def widthChanged(self):
        pass
    
    def winId(self):
        'winId(self) -> int'
        return int
    
    def windowState(self):
        'windowState(self) -> PySide2.QtCore.Qt.WindowState'
        return PySide2.QtCore.Qt.WindowState
    
    def windowStateChanged(self):
        pass
    
    def windowStates(self):
        'windowStates(self) -> PySide2.QtCore.Qt.WindowStates'
        return PySide2.QtCore.Qt.WindowStates
    
    def windowTitleChanged(self):
        pass
    
    def x(self):
        'x(self) -> int'
        return int
    
    def xChanged(self):
        pass
    
    def y(self):
        'y(self) -> int'
        return int
    
    def yChanged(self):
        pass
    

class QWindowStateChangeEvent(_mod_PySide2_QtCore.QEvent):
    'QWindowStateChangeEvent(self, aOldState:PySide2.QtCore.Qt.WindowStates, isOverride:bool=False)'
    __class__ = QWindowStateChangeEvent
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __init__(self, aOldState: PySide2.QtCore.Qt.WindowStates, isOverride: bool=False):
        'QWindowStateChangeEvent(self, aOldState:PySide2.QtCore.Qt.WindowStates, isOverride:bool=False)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def isOverride(self):
        'isOverride(self) -> bool'
        return bool
    
    def oldState(self):
        'oldState(self) -> PySide2.QtCore.Qt.WindowStates'
        return PySide2.QtCore.Qt.WindowStates
    

class Qt(_mod_PySide2_QtCore.Qt):
    __class__ = Qt
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PySide2.QtGui'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def codecForHtml(cls, ba):
        'codecForHtml(ba:PySide2.QtCore.QByteArray) -> PySide2.QtCore.QTextCodec'
        return PySide2.QtCore.QTextCodec
    
    @classmethod
    def convertFromPlainText(cls, plain, mode):
        'convertFromPlainText(plain:str, mode:PySide2.QtCore.Qt.WhiteSpaceMode=PySide2.QtCore.Qt.WhiteSpaceMode.WhiteSpacePre) -> str'
        return str
    
    @classmethod
    def mightBeRichText(cls, arg__1):
        'mightBeRichText(arg__1:str) -> bool'
        return bool
    

__doc__ = None
__file__ = '/Users/shuike/anaconda3/envs/py36QT/lib/python3.6/site-packages/PySide2/QtGui.abi3.so'
__name__ = 'PySide2.QtGui'
__package__ = 'PySide2'
def qAlpha(rgb):
    'qAlpha(rgb:int) -> int'
    return int

def qBlue(rgb):
    'qBlue(rgb:int) -> int'
    return int

def qGray(r: int, g: int, b: int):
    'qGray(r:int, g:int, b:int) -> int\nqGray(rgb:int) -> int'
    return 1

def qGreen(rgb):
    'qGreen(rgb:int) -> int'
    return int

def qIsGray(rgb):
    'qIsGray(rgb:int) -> bool'
    return bool

def qRed(rgb):
    'qRed(rgb:int) -> int'
    return int

def qRgb(r, g, b):
    'qRgb(r:int, g:int, b:int) -> int'
    return int

def qRgba(r, g, b, a):
    'qRgba(r:int, g:int, b:int, a:int) -> int'
    return int

