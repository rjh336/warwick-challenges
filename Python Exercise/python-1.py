import re
import unittest

def check_ip(ip):
    """ check_ip(ip) -> Boolean

    Check whether the given IP Address is valid.
    
    Parameters
    ==========
    ip (string): input IP Address"""
    
    # regular expression to verify structure of input string. Must verify:
    # 1. string has four distinct groups of numbers
    # 2. each group separated by '.'
    # 3. each group consists of only numbers
    # 4. 1-3 comprise of the entire input string
    regex = re.compile("\A(?P<one>[0-9]{,3})\.(?P<two>[0-9]{,3})\.(?P<three>[0-9]{,3})\.(?P<four>[0-9]{,3})\Z")
    groups = regex.groupindex.keys()
    # check for a match to regex
    match_obj = re.match(regex, ip)
    if match_obj:
        # iterate through the four groups to check whether numbers
        # in each group are between 0 and 255 inclusive
        for g in groups:
            number = int(match_obj.group(g))
            if not(number >= 0 and number <= 255):
                print("Invalid Address:  position {} not in range 0-255".format(g))
                return False
        # 'ip' is valid, print off its segments and length of each segment
        for i, segment in enumerate(match_obj.groups()):
            print("segment {} contains {} of length {}".format(i, segment, len(segment)))
    # 'ip' is invalid - does not contain the structure of regex
    else:
        print("Invalid Address:  Input string does not match the sequence '{0-255}.{0-255}.{0-255}.{0-255}'")
        return False
    return True

class TestIP(unittest.TestCase):

    def test1(self):
        self.assertTrue(check_ip("0.0.0.0"))
    def test2(self):
        self.assertTrue(check_ip("12.123.223.3"))
    def test3(self):
        self.assertFalse(check_ip("666.222.012.424"))
    def test4(self):
        self.assertFalse(check_ip(""))
    def test5(self):
        self.assertFalse('+?.@#.)(.#'.isupper())


if __name__ == '__main__':
    unittest.main()