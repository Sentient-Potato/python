class Television:
  min_volume = 0
  max_volume = 2
  min_channel = 0
  max_channel = 3

  def __init__(self):
    self.__status = False
    self.__muted = False
    self.__volume = Television.min_volume
    self.__channel = Television.min_channel
    self.__previous_volume = 0

  def power(self):
    self.__status = not self.__status

  def mute(self):
    if self.__status:
      self.__muted = not self.__muted

  def channel_up(self):
    if self.__status:
      if self.__channel < Television.max_channel:
        self.__channel += 1
      else:
        self.__channel = Television.min_channel

  def channel_down(self):
    if self.__status:
      if self.__channel > Television.min_channel:
        self.__channel -= 1
      else:
        self.__channel = Television.max_channel

  def volume_up(self):
    if self.__status:
      if self.__muted:
        self.__muted = False
      if self.__volume < Television.max_volume:
        self.__volume += 1

  def volume_down(self):
    if self.__status:
      if self.__muted:
        self.__muted = False
      if self.__volume > Television.min_volume:
        self.__volume -= 1


  def __str__(self):
    pow_stat = True if self.__status else False
    volume_stuff = 0 if self.__muted else self.__volume
    return f"Power = {pow_stat}, Channel = {self.__channel}, Volume = {volume_stuff}"