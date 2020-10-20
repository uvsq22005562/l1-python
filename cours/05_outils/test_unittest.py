import unittest

<<<<<<< HEAD

=======
>>>>>>> 0e241ebee3e6dd3305bdb5ede220d7c42fe1a4e8
def is_even(nbr):
    """
    Cette fonction teste si un nombre est pair.
    """
    return nbr % 2 == 0


def is_prime(nbr):
    """
    Cette fonction teste si un nombre est pair.
    """
<<<<<<< HEAD
    for i in range(2, nbr):
=======
    for i in range(2,nbr):
>>>>>>> 0e241ebee3e6dd3305bdb5ede220d7c42fe1a4e8
        if nbr % i == 0:
            return False
    return True

<<<<<<< HEAD

=======
>>>>>>> 0e241ebee3e6dd3305bdb5ede220d7c42fe1a4e8
class MyTest(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(1))
<<<<<<< HEAD

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(15))

=======
        
    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(15))    
>>>>>>> 0e241ebee3e6dd3305bdb5ede220d7c42fe1a4e8

if __name__ == '__main__':
    unittest.main()
