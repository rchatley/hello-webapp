from app import process_query


def test_knows_name():
    assert process_query("what is your name?") == "Rob"
