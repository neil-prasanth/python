import pytest
from television import Television


def test_init():
    """Test the initial state of the Television."""
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power():
    """Test the power method."""
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute():
    """Test the mute functionality."""
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"


def test_channel_up():
    """Test the channel_up method."""
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down():
    """Test the channel_down method."""
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()  # Turn on
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"


def test_volume_up():
    """Test the volume_up method."""
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()  # Turn on
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down():
    """Test the volume_down method."""
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.volume_up()
    tv.volume_up()

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_main_py_scenario():
    """Test the exact scenario from main.py to ensure correct behavior."""
    tv_1 = Television()
    tv_1.power()
    assert str(tv_1) == "Power = True, Channel = 0, Volume = 0"

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_up()
    assert str(tv_1) == "Power = True, Channel = 2, Volume = 1"

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_down()
    tv_1.volume_down()
    assert str(tv_1) == "Power = True, Channel = 1, Volume = 0"

    tv_1.power()
    tv_1.volume_up()
    tv_1.channel_down()
    assert str(tv_1) == "Power = False, Channel = 1, Volume = 0"

    tv_1.power()
    tv_1.volume_up()
    tv_1.volume_up()
    tv_1.volume_up()
    tv_1.channel_down()
    tv_1.channel_down()
    assert str(tv_1) == "Power = True, Channel = 3, Volume = 2"

    tv_2 = Television()
    tv_2.power()
    tv_2.channel_up()
    tv_2.volume_up()
    assert str(tv_2) == "Power = True, Channel = 1, Volume = 1"

    tv_1.mute()
    assert str(tv_1) == "Power = True, Channel = 3, Volume = 0"
    tv_1.volume_down()
    assert str(tv_1) == "Power = True, Channel = 3, Volume = 1"
    tv_1.mute()
    assert str(tv_1) == "Power = True, Channel = 3, Volume = 0"
    tv_1.volume_up()
    assert str(tv_1) == "Power = True, Channel = 3, Volume = 2"
    tv_1.power()
    tv_1.mute()
    assert str(tv_1) == "Power = False, Channel = 3, Volume = 2"