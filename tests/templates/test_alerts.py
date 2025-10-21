from snakemd.elements import Inline
from snakemd.templates import Alert

def test_alert_note():
    alert = Alert("Hello, World!", Alert.Kind.NOTE)
    assert str(alert) == "> [!NOTE]\n> Hello, World!"    

def test_alert_tip():
    alert = Alert("Hello, World!", Alert.Kind.TIP)
    assert str(alert) == "> [!TIP]\n> Hello, World!"    

def test_alert_important():
    alert = Alert("Hello, World!", Alert.Kind.IMPORTANT)
    assert str(alert) == "> [!IMPORTANT]\n> Hello, World!"  

def test_alert_warning():
    alert = Alert("Hello, World!", Alert.Kind.WARNING)
    assert str(alert) == "> [!WARNING]\n> Hello, World!" 
    
def test_alert_caution():
    alert = Alert("Hello, World!", Alert.Kind.CAUTION, )
    assert str(alert) == "> [!CAUTION]\n> Hello, World!" 
    
def test_alert_inline():
    alert = Alert(Inline("Hello, World!", italics=True), Alert.Kind.NOTE)
    assert str(alert) == "> [!NOTE]\n> _Hello, World!_" 
