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
