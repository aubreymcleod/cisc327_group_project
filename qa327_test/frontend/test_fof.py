import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

"""
This file defines all unit tests for the 404 error page.

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.backend.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

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