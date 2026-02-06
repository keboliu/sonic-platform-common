'''
Test PwmBase module
'''

from sonic_platform_base.pwm_base import PwmBase


class TestPwmBase:
    '''
    Collection of PwmBase test methods
    '''

    @staticmethod
    def test_pwm_base():
        '''
        Verify unimplemented methods
        '''
        pwm = PwmBase()
        not_implemented_methods = [
            (pwm.get_pwm_value,),
            (pwm.get_pwm_max_threshold,),
            (pwm.get_pwm_min_threshold,)]

        for method in not_implemented_methods:
            expected_exception = False
            try:
                func = method[0]
                args = method[1:]
                func(*args)
            except Exception as exc:
                expected_exception = isinstance(exc, NotImplementedError)
            assert expected_exception

    @staticmethod
    def test_pwm_base_inherits_device_base():
        '''
        Verify PwmBase inherits from DeviceBase
        '''
        from sonic_platform_base.device_base import DeviceBase
        pwm = PwmBase()
        assert isinstance(pwm, DeviceBase)

        # Verify inherited methods from DeviceBase raise NotImplementedError
        device_base_methods = [
            (pwm.get_name,),
            (pwm.get_presence,),
            (pwm.get_model,),
            (pwm.get_serial,),
            (pwm.get_revision,),
            (pwm.get_status,),
            (pwm.get_position_in_parent,),
            (pwm.is_replaceable,)]

        for method in device_base_methods:
            expected_exception = False
            try:
                func = method[0]
                args = method[1:]
                func(*args)
            except Exception as exc:
                expected_exception = isinstance(exc, NotImplementedError)
            assert expected_exception
