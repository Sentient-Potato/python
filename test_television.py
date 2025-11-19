import unittest as ut
from television import Television

class TestTelevision(ut.TestCase):

    def setUp(self): # Sets up tv = Television() for all test functions
        self.tv = Television()

    def test_init(self): # Tests if all default variables are correct
        self.assertFalse(self.tv._Television__status) # TV status should start as False on default

        self.assertEqual(self.tv._Television__channel, self.tv.MIN_CHANNEL) # TV channel should start as MIN_CHANNEL

        self.assertEqual(self.tv._Television__volume, self.tv.MIN_VOLUME) # TV volume should start as MIN_VOLUME

    def test_power(self): # Tests power() function
        self.tv.power() # Toggles TV status to true
        self.assertTrue(self.tv._Television__status) # TV status should toggle to True

        self.tv.power()
        self.assertFalse(self.tv._Television__status)  # TV status should toggle to False

    def test_mute(self):
        self.tv.power() # Toggles status to True
        self.tv.volume_up() # Increases volume to 1
        self.tv.mute() # Toggles mute status from False to True
        self.assertTrue(self.tv._Television__muted) # TV muted should be True

        self.tv.volume_up() # Increase volume to 2 and disables muted
        self.assertFalse(self.tv._Television__muted)  # TV muted should be False

        # Testing if muted remains false after status was toggled to False
        self.tv.power() # Toggles status to False
        self.tv.mute() # Attempts to toggle muted to True while status is False
        self.assertFalse(self.tv._Television__muted)  # TV muted should be False

        # Testing if muted remains false after being set as false before status was toggled to False
        self.tv.power() # Toggles status to True
        self.tv.mute() # Toggles muted to True
        self.tv.power() # Toggles status to False
        self.tv.mute() # Attempts to toggle muted. Muted should be false due to power() also setting muted to false
        self.assertFalse(self.tv._Television__muted)  # TV muted should be False


if __name__ == '__main__':
    ut.main()
