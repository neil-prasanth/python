class Television:
    """
    A class to represent a television with power, channel, volume, and mute controls.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize a new Television instance with default values.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the power status of the TV.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggle the mute status of the TV when it is on.
        If TV is off, muting has no effect.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel number by 1 when the TV is on.
        If at maximum channel, wrap around to minimum channel.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the channel number by 1 when the TV is on.
        If at minimum channel, wrap around to maximum channel.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increase the volume by 1 when the TV is on.
        If at maximum volume, volume does not change.
        If TV was muted, unmute it.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume by 1 when the TV is on.
        If at minimum volume, volume does not change.
        If TV was muted, unmute it.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a string representation of the TV's current state.
        Format: Power = [status], Channel = [channel], Volume = [volume]
        When muted, return the volume as 0 regardless of actual volume.
        """
        display_volume = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}"