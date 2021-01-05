from src.ch1.p1_is_unique import allUnique, allUniqueVer2

class TestAllUnique(object):
    ''''''
    def test_one(self):
        string = "How now brown cow"
        assert allUnique(string) == False
        assert allUniqueVer2(string) == False
        
    def test_unique(self):
        string = "abcdefghijklmnopqrstuvwxyz"
        assert allUnique(string) == True
        assert allUniqueVer2(string) == True
        
    def test_alphanumeric(self):
        string = "123asdrflk"
        assert allUnique(string) == True
        assert allUniqueVer2(string) == True
        
    def test_empty(self):
        string = ""
        assert allUnique(string) == False
        assert allUniqueVer2(string) == False