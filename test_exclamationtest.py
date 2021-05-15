import exclamation

def test_remove_one_at_end():
    assert exclamation.remove_exclamation_marks("ggg!") == "ggg"

def test_remove_one_at_middle():
    assert exclamation.remove_exclamation_marks("gg!g") == "ggg"

def test_remove_one_at_start():
    assert exclamation.remove_exclamation_marks("!ggg") == "ggg"

def test_remove_multiple():
    assert exclamation.remove_exclamation_marks("ff!sfs!dsdgg!g!") == "ffsfsdsdggg"