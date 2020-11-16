import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

class FrontEndFOFTest(BaseCase):
    ### Test case R8.1 -  For any other requests except the ones above, the system should return a 404 error.
    def test_fof(self, *_):
        """
        If the user has entered a new unknown branch, do they get a 404 error?
        """
        #open /logout to invalidate the current session
        self.open(base_url+'/logout')
        #open invalid route
        self.open(base_url+'/foobar')
        #validate request cannot be matched to an existing case
        self.assert_element('#fof-header')
        #404 returned