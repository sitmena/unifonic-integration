# -*- coding: utf-8 -*-

"""
    unifonicnextgen

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from unifonicnextgen.api_helper import APIHelper
from unifonicnextgen.configuration import Configuration
from unifonicnextgen.controllers.base_controller import BaseController
from unifonicnextgen.http.auth.basic_auth import BasicAuth
from unifonicnextgen.models.get_scheduled_message_response import GetScheduledMessageResponse
from unifonicnextgen.models.send_response import SendResponse
from unifonicnextgen.models.send_scheduledmessages_response import SendScheduledmessagesResponse
from unifonicnextgen.models.stop_scheduled_messages_response import StopScheduledMessagesResponse
from unifonicnextgen.models.get_messages_details_response import GetMessagesDetailsResponse
from unifonicnextgen.exceptions.api_exception import APIException

class RestController(BaseController):

    """A Controller to access Endpoints in the unifonicnextgen API."""


    def get_scheduled_message_details(self,
                                      app_sid):
        """Does a GET request to /rest/SMS/messages/scheduledmessages.

        Unifonic Scheduled message details allows you to get details of
        scheduled messages through simple RESTful APIs

        Args:
            app_sid (string): A character string that uniquely identifies your
                app

        Returns:
            GetScheduledMessageResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(app_sid=app_sid)

        # Prepare query URL
        _url_path = '/rest/SMS/messages/scheduledmessages'
        _query_builder = Configuration.get_base_uri(Configuration.Server.BASE_URL)
        _query_builder += _url_path
        _query_parameters = {
            'AppSid': app_sid
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Authentication failed', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetScheduledMessageResponse.from_dictionary)

    def create_send_message(self,
                            app_sid,
                            sender_id,
                            body,
                            recipient,
                            response_type=None,
                            correlation_id=None,
                            base_encode=None,
                            status_callback=None):
        """Does a POST request to /rest/SMS/messages.

        Unifonic Send API allows you to send  text messages to users around
        the globe through simple RESTful APIs

        Args:
            app_sid (string): A character string that uniquely identifies your
                app
            sender_id (string): The SenderID to send from, App default
                SenderID is used unless else stated
            body (string): Message body supports both English and unicodes
                characters, concatenated messages is supported
            recipient (long|int): Destination mobile number, mobile numbers
                must be in international format without 00 or + Example:
                (4452023498)
            response_type (string, optional): Support json format only
            correlation_id (string, optional): Is a unique identifier value
                that is attached to requests and messages
            base_encode (bool, optional): Binary-to-text encoding schemes that
                represent binary data in an ASCII string format
            status_callback (string, optional): Filter messages report
                according to a specific message status, "Sent", "Queued",
                "Rejected" or "Failed
            async (bool, optional): It specifies that the request will be
                executed asynchronously as soon as it is sent

        Returns:
            SendResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(app_sid=app_sid,
                                 sender_id=sender_id,
                                 body=body,
                                 recipient=recipient)

        # Prepare query URL
        _url_path = '/rest/SMS/messages'
        _query_builder = Configuration.get_base_uri(Configuration.Server.BASE_URL)
        _query_builder += _url_path
        _query_parameters = {
            'AppSid': app_sid,
            'SenderID': sender_id,
            'Body': body,
            'Recipient': recipient,
            'responseType': response_type,
            'CorrelationID': correlation_id,
            'baseEncode': base_encode,
            'statusCallback': status_callback
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Authentication failed', _context)
        elif _context.response.status_code == 449:
            raise APIException('Message body is empty', _context)
        elif _context.response.status_code == 480:
            raise APIException('This user cannot use specified SenderID', _context)
        elif _context.response.status_code == 482:
            raise APIException('Invalid dest num', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, SendResponse.from_dictionary)

    def create_send_scheduled_messages(self,
                                       app_sid,
                                       sender_id,
                                       recipient,
                                       body,
                                       time_scheduled,
                                       response_type=None,
                                       correlation_id=None,
                                       base_encode=None):
        """Does a POST request to /rest/SMS/messages/scheduledmessages.

        Unifonic Send Scheduled API allows you to schedule text messages to
        users around the globe through simple RESTful API to be sent in
        future.

        Args:
            app_sid (string): A character string that uniquely identifies your
                app
            sender_id (string): The SenderID to send from, App default
                SenderID is used unless else stated
            recipient (long|int): Destination mobile number, mobile numbers
                must be in international format without 00 or + Example:
                (4452023498)
            body (string): Message body supports both English and unicodes
                characters, concatenated messages is supported
            time_scheduled (datetime): Schedule send messages, in the
                following format yyyy-mm-dd HH:mm:ss
            response_type (string, optional): Support json format only
            correlation_id (string, optional): Is a unique identifier value
                that is attached to requests and messages
            base_encode (bool, optional): Binary-to-text encoding schemes that
                represent binary data in an ASCII string format

        Returns:
            SendScheduledmessagesResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(app_sid=app_sid,
                                 sender_id=sender_id,
                                 recipient=recipient,
                                 body=body,
                                 time_scheduled=time_scheduled)

        # Prepare query URL
        _url_path = '/rest/SMS/messages/scheduledmessages'
        _query_builder = Configuration.get_base_uri(Configuration.Server.BASE_URL)
        _query_builder += _url_path
        _query_parameters = {
            'AppSid': app_sid,
            'SenderID': sender_id,
            'Recipient': recipient,
            'Body': body,
            'TimeScheduled': APIHelper.when_defined(APIHelper.HttpDateTime, time_scheduled),
            'responseType': response_type,
            'CorrelationID': correlation_id,
            'baseEncode': base_encode
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Authentication failed', _context)
        elif _context.response.status_code == 406:
            raise APIException('Wrong parameter format', _context)
        elif _context.response.status_code == 449:
            raise APIException('Message body is empty', _context)
        elif _context.response.status_code == 451:
            raise APIException('TimeScheduled parameter must indicate time in the future', _context)
        elif _context.response.status_code == 480:
            raise APIException('This user cannot use specified SenderID', _context)
        elif _context.response.status_code == 482:
            raise APIException('Invalid dest num', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, SendScheduledmessagesResponse.from_dictionary)

    def delete_stop_scheduled_messages(self,
                                       app_sid,
                                       message_id=None,
                                       response_format=None,
                                       base_encode=None):
        """Does a DELETE request to /rest/SMS/messages/scheduledmessages.

        Unifonic Stop scheduled messages API allows you to Delete (Stops)
        scheduled message,If MessageID is specified only one message is
        stopped, Otherwise all messages are stopped through simple RESTful
        APIs.

        Args:
            app_sid (string): A character string that uniquely identifies your
                app
            message_id (long|int, optional): A unique ID that identifies a
                message
            response_format (string, optional): support json format only
            base_encode (bool, optional): Binary-to-text encoding schemes that
                represent binary data in an ASCII string format

        Returns:
            StopScheduledMessagesResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(app_sid=app_sid)

        # Prepare query URL
        _url_path = '/rest/SMS/messages/scheduledmessages'
        _query_builder = Configuration.get_base_uri(Configuration.Server.BASE_URL)
        _query_builder += _url_path
        _query_parameters = {
            'AppSid': app_sid,
            'MessageID': message_id,
            'responseFormat': response_format,
            'baseEncode': base_encode
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Authentication failed', _context)
        elif _context.response.status_code == 455:
            raise APIException('Scheduled message not found for this User', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, StopScheduledMessagesResponse.from_dictionary)

    def create_get_message_details(self,
                                   app_sid,
                                   message_id=None,
                                   sender_id=None,
                                   recipient=None,
                                   date_from=None,
                                   date_to=None,
                                   correlation_id=None,
                                   limit=None,
                                   base_encode=None):
        """Does a POST request to /rest/SMS/Messages/GetMessagesDetails.

        Unifonic Get message details API allows you to get details of messages
        with optional filters,returns paginated messages, next page or
        previous page through simple RESTful APIs

        Args:
            app_sid (string): A character string that uniquely identifies your
                app
            message_id (long|int, optional): A unique ID that identifies a
                message
            sender_id (string, optional): The SenderID to send from, App
                default SenderID is used unless else stated
            recipient (long|int, optional): Destination mobile number, mobile
                numbers must be in international format without 00 or +
                Example: (4452023498)
            date_from (date, optional): The start date for the report time
                interval, date format should be yyyy-mm-dd
            date_to (date, optional): The end date for the report time
                interval, date format should be yyyy-mm-dd
            correlation_id (string, optional): Is a unique identifier value
                that is attached to requests and messages
            limit (long|int, optional): The maximum number of messages
                details
            base_encode (bool, optional): Binary-to-text encoding schemes that
                represent binary data in an ASCII string format

        Returns:
            GetMessagesDetailsResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(app_sid=app_sid)

        # Prepare query URL
        _url_path = '/rest/SMS/Messages/GetMessagesDetails'
        _query_builder = Configuration.get_base_uri(Configuration.Server.BASE_URL)
        _query_builder += _url_path
        _query_parameters = {
            'AppSid': app_sid,
            'MessageID': message_id,
            'senderID': sender_id,
            'Recipient': recipient,
            'dateFrom': date_from,
            'dateTo': date_to,
            'CorrelationID': correlation_id,
            'Limit': limit,
            'baseEncode': base_encode
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Authentication failed', _context)
        elif _context.response.status_code == 432:
            raise APIException('MessageId must be numeric', _context)
        elif _context.response.status_code == 599:
            raise APIException('Request failed', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetMessagesDetailsResponse.from_dictionary)
