from snakemd.elements import Inline
from snakemd.templates import Alerts

def test_alerts_note():
    alert = Alerts(Alerts.Kind.NOTE, "Hello, World!")
    assert str(alert) == "> [!NOTE]\n> Hello, World!"    

def test_alerts_tip():
    alert = Alerts(Alerts.Kind.TIP, "Hello, World!")
    assert str(alert) == "> [!TIP]\n> Hello, World!"    

def test_alerts_important():
    alert = Alerts(Alerts.Kind.IMPORTANT, "Hello, World!")
    assert str(alert) == "> [!IMPORTANT]\n> Hello, World!"  

def test_alerts_warning():
    alert = Alerts(Alerts.Kind.WARNING, "Hello, World!")
    assert str(alert) == "> [!WARNING]\n> Hello, World!" 
    
def test_alerts_caution():
    alert = Alerts(Alerts.Kind.CAUTION, "Hello, World!")
    assert str(alert) == "> [!CAUTION]\n> Hello, World!" 
    
def test_alerts_inline():
    alert = Alerts(Alerts.Kind.NOTE, Inline("Hello, World!", italics=True))
    assert str(alert) == "> [!NOTE]\n> _Hello, World!_" 
