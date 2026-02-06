"""
    pwm_base.py

    Abstract base class for interfacing with a PWM device in SONiC
"""

from sonic_platform_base.device_base import DeviceBase


class PwmBase(DeviceBase):
    """
    Abstract base class for interfacing with a PWM device
    """

    def get_pwm_value(self):
        """
        Retrieves the current PWM value

        Returns:
            int: The current PWM value
        """
        raise NotImplementedError

    def get_pwm_max_threshold(self):
        """
        Retrieves the maximum PWM threshold value

        Returns:
            int: The maximum PWM threshold value
        """
        raise NotImplementedError

    def get_pwm_min_threshold(self):
        """
        Retrieves the minimum PWM threshold value

        Returns:
            int: The minimum PWM threshold value
        """
        raise NotImplementedError
