"""
IMPORTANT NOTE:
I asked Professor Reestman about the muted and power function. I asked if the muted variable should be set to false when
status is also set to false from power(). He said that this detail was not a part of the instructions or rubric but
said that the muted variable should be set to false when the status is also set to false. Therefore, I added that feature.
"""

class Television:
    # Class variables to determine the minimum and maximum value for volume and channel
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Declares the default status of private variables
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self): # Toggles self.__status when called
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False
        return self.__status

    def mute(self): # Toggles self.__muted when called and if self.__status = True
        if self.__status:
            self.__muted = not self.__muted
        return self.__muted

    def channel_up(self): # Increases channel number by 1 when called and if self.__status = True
        if self.__status:
            if self.__channel == self.MAX_CHANNEL: # Sets self.__channel to MIN_CHANNEL if self.__channel = self.MAX_CHANNEL
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
        return self.__channel

    def channel_down(self): # Decreases channel number by 1 when called and if self.__status = True
        if self.__status:
            if self.__channel == self.MIN_CHANNEL: # Sets self.__channel to MAX_CHANNEL if self.__channel = self.MIN_CHANNEL
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
        return self.__channel

    def volume_up(self): # Increases volume number by 1 when called and if self.__status = True
        if self.__status:
            if self.__muted: # Sets self.__muted = False if self.__muted had previously been True
                self.__muted = False
            if self.__volume == self.MAX_VOLUME: # Maintains MAX_VOLUME if self.__volume = self.MAX_VOLUME
                self.__volume = self.MAX_VOLUME
            else:
                self.__volume += 1
        return self.__volume

    def volume_down(self): # Decreases volume number by 1 when called and if self.__status = True
        if self.__status:
            if self.__muted: #Sets self.__muted = False if self.__muted had previously been True
                self.__muted = False
            if self.__volume == self.MIN_VOLUME: # Maintains MIN_VOLUME if self.__volume = self.MIN_VOLUME
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume -= 1
        return self.__volume

    def __str__(self):
        displayed_volume = 0 if (self.__status and self.__muted) else self.__volume # If self.__muted = True, then displayed volume will be 0. Otherwise, it should get self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {displayed_volume}" # Display message