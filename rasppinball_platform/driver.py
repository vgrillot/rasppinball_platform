"""
RaspPinball Driver management
"""

# !!181104:VG:Creation (refactoring, splitter main unit)
# !!181221:VG:Migrating to V5


import logging
from mpf.platforms.interfaces.driver_platform_interface import DriverPlatformInterface, PulseSettings, HoldSettings


class RASPDriver(DriverPlatformInterface):

    def __init__(self, config, number, platform):
        """Initialise driver."""
        super().__init__(config, number)
        self.platform = platform
        self.log = logging.getLogger('RASPDriver')
        self.log.info("Driver Settings for %s", self.number)

    def disable(self):
        """Disable the driver."""
        self.log.info("RASPDriver.Disable(%s)" % self.number)
        self.platform.communicator.driver_disable(self.number)

    def enable(self, pulse_settings: PulseSettings, hold_settings: HoldSettings):
        """Enable this driver, which means it's held "on" indefinitely until it's explicitly disabled."""
        self.log.info("RASPDriver.Enable(%s)" % self.number)
        self.platform.communicator.driver_enable(self.number)

    def get_board_name(self):
        """Return the name of the board of this driver."""
        pass

    def pulse(self, pulse_settings: PulseSettings):
        """Pulse a driver.

        Pulse this driver for a pre-determined amount of time, after which
        this driver is turned off automatically. Note that on most platforms,
        pulse times are a max of 255ms. (Beyond that MPF will send separate
        enable() and disable() commands.
        """
        ms = pulse_settings.duration
        self.log.info("RASPDriver.Pulse(%s, %d ms)" % (self.number, ms))
        self.platform.communicator.driver_pulse(self.number, ms)
        return ms
