import pytest
from requests import Session
from pytest import fixture
from pytest import mark

@mark.login
@mark.smoke
class LoginTests:

    def test_can_login_using_api_request(self, logged_in_session):
        lsession = logged_in_session
        print(lsession)
        if 'authorization' not in lsession:
            raise Exception("Did not login successfully")