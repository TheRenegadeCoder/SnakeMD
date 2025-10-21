from snakemd.elements import Inline
from snakemd.templates import Alerts

def test_alerts_note():
    alert = Alerts("Hello, World!", Alerts.Kind.NOTE)
    assert str(alert) == "> [!NOTE]\n> Hello, World!"    

def test_alerts_tip():
    alert = Alerts("Hello, World!", Alerts.Kind.TIP)
    assert str(alert) == "> [!TIP]\n> Hello, World!"    

def test_alerts_important():
    alert = Alerts("Hello, World!", Alerts.Kind.IMPORTANT)
    assert str(alert) == "> [!IMPORTANT]\n> Hello, World!"  

def test_alerts_warning():
    alert = Alerts("Hello, World!", Alerts.Kind.WARNING)
    assert str(alert) == "> [!WARNING]\n> Hello, World!" 
    
def test_alerts_caution():
    alert = Alerts("Hello, World!", Alerts.Kind.CAUTION, )
    assert str(alert) == "> [!CAUTION]\n> Hello, World!" 
    
def test_alerts_inline():
    alert = Alerts(Inline("Hello, World!", italics=True), Alerts.Kind.NOTE)
    assert str(alert) == "> [!NOTE]\n> _Hello, World!_" 
