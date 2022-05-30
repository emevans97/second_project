from second_project.lib import try_me

def test_try_me():
    assert try_me(2, 3) == 8
    assert try_me(3, 2) > 8
