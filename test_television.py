from television import Television

def testing():
    tv = Television()

    assert str(tv) == "Power = False, Channel = 0, Volume = 0" #TV should start off with default values

    tv.volume_up()
    tv.channel_up() #Nothing should change due to Power being false
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power() #Only Power should change as the TV turns on
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.channel_up() #Channel should increase ONCE
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    tv.channel_up()
    tv.channel_up() #Channel should increase TWICE to 3
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    tv.channel_up() #Channel should reset to default
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_up() #Volume should increase ONCE
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume_down() #Volume decreases back to default
    tv.volume_down() #Volume should not change
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_up()
    tv.volume_up() #Volume should increase to 2
    tv.volume_up() #Volume should not change
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    tv.mute() #Volume should be set to 0
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.mute() #Volume should be set back to 2
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    tv.mute()  #Sets the volume back to 0
    tv.volume_down() #Volume should be set back to 2 and be reduced ONCE
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.power() #Power should be off
    tv.mute() #Nothing should change, volume should remain 1
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"
