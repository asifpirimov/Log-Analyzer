from analyzer import analyze

def test_valid_log():
    assert analyze("./logs/app.log") == (2,1,1)

def test_empty_file():
    assert analyze("./logs/api.log") == ("File is empty")

def test_file_not_found():
    assert analyze("./logs/a.log") == ("File not found")