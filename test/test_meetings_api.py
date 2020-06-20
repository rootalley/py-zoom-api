# coding: utf-8

"""
    Zoom API

    The Zoom API allows developers to safely and securely access information from Zoom. You can use this API to build private services or public applications on the [Zoom App Marketplace](http://marketplace.zoom.us). To learn how to get your credentials and create private/public applications, read our [Authorization Guide](https://marketplace.zoom.us/docs/guides/authorization/credentials). All endpoints are available via `https` and are located at `api.zoom.us/v2/`.  For instance you can list all users on an account via `https://api.zoom.us/v2/users/`.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: developersupport@zoom.us
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.meetings_api import MeetingsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMeetingsApi(unittest.TestCase):
    """MeetingsApi unit test stubs"""

    def setUp(self):
        self.api = api.meetings_api.MeetingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_past_meeting_files(self):
        """Test case for list_past_meeting_files

        List Past Meeting Files  # noqa: E501
        """
        pass

    def test_list_past_meeting_polls(self):
        """Test case for list_past_meeting_polls

        List Past Meeting's Poll Results  # noqa: E501
        """
        pass

    def test_meeting(self):
        """Test case for meeting

        Get a Meeting  # noqa: E501
        """
        pass

    def test_meeting_create(self):
        """Test case for meeting_create

        Create a Meeting  # noqa: E501
        """
        pass

    def test_meeting_delete(self):
        """Test case for meeting_delete

        Delete a Meeting  # noqa: E501
        """
        pass

    def test_meeting_invitation(self):
        """Test case for meeting_invitation

        Get Meeting Invitation  # noqa: E501
        """
        pass

    def test_meeting_live_stream_status_update(self):
        """Test case for meeting_live_stream_status_update

        Update Live Stream Status  # noqa: E501
        """
        pass

    def test_meeting_live_stream_update(self):
        """Test case for meeting_live_stream_update

        Update Live Stream  # noqa: E501
        """
        pass

    def test_meeting_poll_create(self):
        """Test case for meeting_poll_create

        Create a Meeting Poll  # noqa: E501
        """
        pass

    def test_meeting_poll_delete(self):
        """Test case for meeting_poll_delete

        Delete a Meeting Poll  # noqa: E501
        """
        pass

    def test_meeting_poll_get(self):
        """Test case for meeting_poll_get

        Get a Meeting Poll  # noqa: E501
        """
        pass

    def test_meeting_poll_update(self):
        """Test case for meeting_poll_update

        Update a Meeting Poll  # noqa: E501
        """
        pass

    def test_meeting_polls(self):
        """Test case for meeting_polls

        List Meeting Polls  # noqa: E501
        """
        pass

    def test_meeting_registrant_create(self):
        """Test case for meeting_registrant_create

        Add Meeting Registrant  # noqa: E501
        """
        pass

    def test_meeting_registrant_question_update(self):
        """Test case for meeting_registrant_question_update

        Update Registration Questions  # noqa: E501
        """
        pass

    def test_meeting_registrant_status(self):
        """Test case for meeting_registrant_status

        Update Meeting Registrant Status  # noqa: E501
        """
        pass

    def test_meeting_registrants(self):
        """Test case for meeting_registrants

        List Meeting Registrants  # noqa: E501
        """
        pass

    def test_meeting_registrants_questions_get(self):
        """Test case for meeting_registrants_questions_get

        List Registration Questions   # noqa: E501
        """
        pass

    def test_meeting_status(self):
        """Test case for meeting_status

        Update Meeting Status  # noqa: E501
        """
        pass

    def test_meeting_update(self):
        """Test case for meeting_update

        Update a Meeting  # noqa: E501
        """
        pass

    def test_meetings(self):
        """Test case for meetings

        List Meetings  # noqa: E501
        """
        pass

    def test_past_meeting_details(self):
        """Test case for past_meeting_details

        Get Past Meeting Details  # noqa: E501
        """
        pass

    def test_past_meeting_participants(self):
        """Test case for past_meeting_participants

        Get Past Meeting Participants  # noqa: E501
        """
        pass

    def test_past_meetings(self):
        """Test case for past_meetings

        List Ended Meeting Instances  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()