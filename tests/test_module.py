import snakemd


def test_new_doc():
    doc = snakemd.new_doc()
    assert isinstance(doc, snakemd.Document)
