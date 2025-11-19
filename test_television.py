"""
IMPORTANT NOTE:
I asked Professor Reestman about the muted and power function. I asked if the muted variable should be set to false when
status is also set to false from power(). He said that this detail was not a part of the instructions or rubric but
said that the muted variable should be set to false when the status is also set to false. Therefore, I added that feature.
You can find the same note in television.py.
"""

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

    def test_channel_up(self):
        self.tv.channel_up() # Attempts to increase channel while status is False
        self.assertEqual(self.tv._Television__channel, 0) # TV channel should remain MIN_CHANNEL/0

        self.tv.power() # Toggles status to True
        self.tv.channel_up()
        self.tv.channel_up() # Increase channel by 2
        self.assertEqual(self.tv._Television__channel, 2) # TV channel should be 2

        for _ in range(5): # Increases channel by 2, loop back to 0, then increase by 3
            self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, 3) # TV channel should loop and increase to 3

        self.tv.power() # Toggles status to False
        self.assertEqual(self.tv._Television__channel, 3) # TV channel should remain 3

    def test_channel_down(self):
        self.tv.channel_down()  # Attempts to decrease channel while status is False
        self.assertEqual(self.tv._Television__channel, 0)  # TV channel should remain MIN_CHANNEL/0

        self.tv.power()  # Toggles status to True
        self.tv.channel_up() # Increase channel by 1
        self.tv.channel_down() # Decrease channel by 1
        self.assertEqual(self.tv._Television__channel, 0) # TV channel should be 0

        for _ in range(5):  # Decrease channel by 1, loop back to 0, then decrease by 4, and loop again
            self.tv.channel_down()
        self.assertEqual(self.tv._Television__channel, 3)  # TV channel should be 3

        self.tv.power()  # Toggles status to False
        self.assertEqual(self.tv._Television__channel, 3)  # TV channel should remain 3

    def test_volume_up(self):
        self.tv.volume_up() # Attempts to increase volume while status is False
        self.assertEqual(self.tv._Television__volume, 0) # TV volume should remain MIN_VOLUME/0

        self.tv.power() # Toggles status to True
        self.tv.volume_up() # Increase volume by 1
        self.assertEqual(self.tv._Television__volume, 1) # TV volume should be 1

        for _ in range(8): # Attempts to increase volume 8 times
            self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, 2) # TV volume should be 2

        self.tv.mute() # Toggles muted to True
        self.assertTrue(self.tv._Television__muted) # Confirms that muted is set to True
        self.assertEqual(self.tv._Television__volume, 2) # TV volume should remain at 2, despite being muted and display volume is 0

        self.tv.volume_down()
        self.tv.volume_down()
        self.tv.volume_up() # Decrease volume by 2 then increase volume by 1
        self.assertFalse(self.tv._Television__muted) # Muted should be set to False despite not being called
        self.assertEqual(self.tv._Television__volume, 1)

        self.tv.power() # Toggles status to False
        self.assertEqual(self.tv._Television__volume, 1) # TV volume should remain at 1

    def test_volume_down(self):
        self.tv.volume_down() # Attempts to decrease volume while status is False
        self.assertEqual(self.tv._Television__volume, 0) # TV volume should remain MIN_VOLUME/0

        self.tv.power() # Toggles status to True
        self.tv.volume_up()
        self.tv.volume_down() # Increase volume by 1 then decrease by 1
        self.assertEqual(self.tv._Television__volume, 0) # TV volume should be 0

        for _ in range(8): # Attempts to decrease volume 8 times
            self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, 0) # TV volume should be 0

        self.tv.mute() # Toggles muted to True
        self.assertTrue(self.tv._Television__muted) # Confirms that muted is set to True
        self.assertEqual(self.tv._Television__volume, 0) # TV volume should remain at 0

        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down() # Increase volume by 2 then decrease volume by 1
        self.assertFalse(self.tv._Television__muted) # Muted should be set to False despite not being called
        self.assertEqual(self.tv._Television__volume, 1)

        self.tv.power() # Toggles status to False
        self.assertEqual(self.tv._Television__volume, 1) # TV volume should remain at 1

if __name__ == '__main__':
    ut.main()