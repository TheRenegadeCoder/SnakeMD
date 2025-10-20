from snakemd.elements import MDList
from snakemd.templates import Checklist

def test_checklist_one_item_true():
    checklist = Checklist(["Write code"], True)
    assert str(checklist) == "- [X] Write code"
    
def test_checklist_one_item_false():
    checklist = Checklist(["Write code"], False)
    assert str(checklist) == "- [ ] Write code"
    
def test_checklist_one_item_explicit():
    checklist = Checklist(["Write code"], [False])
    assert str(checklist) == "- [ ] Write code"
    
def test_checklist_many_items_true():
    checklist = Checklist(["Write code", "Do Laundry"], True)
    assert str(checklist) == "- [X] Write code\n- [X] Do Laundry"
    
def test_checklist_many_items_nested_true():
    checklist = Checklist(["Write code", Checklist(["Implement TODO"], True), "Do Laundry"], True)
    assert str(checklist) == "- [X] Write code\n  - [X] Implement TODO\n- [X] Do Laundry"
    
def test_checklist_many_items_nested_mdlist_true():
    checklist = Checklist(["Write code", MDList(["Implement TODO"]), "Do Laundry"], True)
    assert str(checklist) == "- [X] Write code\n  - Implement TODO\n- [X] Do Laundry"
