import unittest as ut
from television import Television

class TestTelevision(ut.TestCase):

    def setUp(self): # Sets up tv = Television() for all test functions
        self.tv = Television()

    def test_init(self):
        self.assertFalse(self.tv._Television__status) # TV status should start as False on default

        self.tv.power() # Toggles TV status to true

        self.assertTrue(self.tv._Television__status) # TV status should toggle to True

        self.tv.power()
        self.tv.power() # To test calling back to back

        self.assertEqual(self.tv._Television__channel, self.tv.MIN_CHANNEL) # TV channel should start as MIN_CHANNEL

        self.assertEqual(self.tv._Television__volume, self.tv.MIN_VOLUME) # TV volume should start as MIN_VOLUME



if __name__ == '__main__':
    ut.main()
