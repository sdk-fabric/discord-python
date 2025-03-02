"""
ChannelTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .channel import Channel
from .channel_invite import ChannelInvite
from .channel_update import ChannelUpdate
from .error import Error
from .error_exception import ErrorException
from .message import Message

class ChannelTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get(self, channel_id: str) -> Channel:
        """
        Get a channel by ID. Returns a channel object.
        """
        try:
            path_params = {}
            path_params['channel_id'] = channel_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/channels/:channel_id', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = Channel.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def update(self, channel_id: str, payload: ChannelUpdate) -> Channel:
        """
        Update a channel&#039;s settings. Returns a channel on success, and a 400 BAD REQUEST on invalid parameters.
        """
        try:
            path_params = {}
            path_params['channel_id'] = channel_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/channels/:channel_id', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)

            options['json'] = payload.model_dump(by_alias=True)

            options['headers']['Content-Type'] = 'application/json'

            response = self.http_client.request('PATCH', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = Channel.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def delete(self, channel_id: str) -> Channel:
        """
        Delete a channel, or close a private message. Requires the MANAGE_CHANNELS permission for the guild, or MANAGE_THREADS if the channel is a thread. Deleting a category does not delete its child channels; they will have their parent_id removed and a Channel Update Gateway event will fire for each of them. Returns a channel object on success. Fires a Channel Delete Gateway event (or Thread Delete if the channel was a thread).
        """
        try:
            path_params = {}
            path_params['channel_id'] = channel_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/channels/:channel_id', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('DELETE', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = Channel.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def get_pins(self, channel_id: str) -> List[Message]:
        """
        Returns all pinned messages in the channel as an array of message objects.
        """
        try:
            path_params = {}
            path_params['channel_id'] = channel_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/channels/:channel_id/pins', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = List[Message].model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))

    def create_invite(self, channel_id: str, payload: ChannelInvite) -> ChannelInvite:
        """
        Create a new invite object for the channel. Only usable for guild channels. Requires the CREATE_INSTANT_INVITE permission. All JSON parameters for this route are optional, however the request body is not. If you are not sending any fields, you still have to send an empty JSON object ({}). Returns an invite object. Fires an Invite Create Gateway event.
        """
        try:
            path_params = {}
            path_params['channel_id'] = channel_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/channels/:channel_id/invites', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)

            options['json'] = payload.model_dump(by_alias=True)

            options['headers']['Content-Type'] = 'application/json'

            response = self.http_client.request('POST', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = ChannelInvite.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = Error.model_validate_json(json_data=response.content)

                raise ErrorException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))



