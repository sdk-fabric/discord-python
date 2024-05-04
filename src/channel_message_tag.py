"""
ChannelMessageTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .message import Message

class ChannelMessageTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get_all(self, channel_id: str, around: str, before: str, after: str, limit: int) -> List[Message]:
        """
        Retrieves the messages in a channel.
        """
        try:
            path_params = {}
            path_params["channel_id"] = channel_id

            query_params = {}
            query_params["around"] = around
            query_params["before"] = before
            query_params["after"] = after
            query_params["limit"] = limit

            query_struct_names = []

            url = self.parser.url("/channels/:channel_id/messages", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return List[Message].model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get(self, channel_id: str, message_id: str) -> Message:
        """
        Retrieves a specific message in the channel. Returns a message object on success.
        """
        try:
            path_params = {}
            path_params["channel_id"] = channel_id
            path_params["message_id"] = message_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/channels/:channel_id/messages/:message_id", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return Message.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def create(self, channel_id: str, payload: Message) -> Message:
        """
        Post a message to a guild text or DM channel. Returns a message object. Fires a Message Create Gateway event. See message formatting for more information on how to properly format messages.
        """
        try:
            path_params = {}
            path_params["channel_id"] = channel_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/channels/:channel_id/messages", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.post(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return Message.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def update(self, channel_id: str, message_id: str, payload: Message) -> Message:
        """
        Edit a previously sent message. The fields content, embeds, and flags can be edited by the original message author. Other users can only edit flags and only if they have the MANAGE_MESSAGES permission in the corresponding channel. When specifying flags, ensure to include all previously set flags/bits in addition to ones that you are modifying. Only flags documented in the table below may be modified by users (unsupported flag changes are currently ignored without error).
        """
        try:
            path_params = {}
            path_params["channel_id"] = channel_id
            path_params["message_id"] = message_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/channels/:channel_id/messages/:message_id", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.patch(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return Message.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def remove(self, channel_id: str, message_id: str):
        """
        Delete a message. If operating on a guild channel and trying to delete a message that was not sent by the current user, this endpoint requires the MANAGE_MESSAGES permission.
        """
        try:
            path_params = {}
            path_params["channel_id"] = channel_id
            path_params["message_id"] = message_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/channels/:channel_id/messages/:message_id", path_params)

            headers = {}

            response = self.http_client.delete(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def crosspost(self, channel_id: str, message_id: str) -> Message:
        """
        Crosspost a message in an Announcement Channel to following channels. This endpoint requires the SEND_MESSAGES permission, if the current user sent the message, or additionally the MANAGE_MESSAGES permission, for all other messages, to be present for the current user.
        """
        try:
            path_params = {}
            path_params["channel_id"] = channel_id
            path_params["message_id"] = message_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/channels/:channel_id/messages/:message_id/crosspost", path_params)

            headers = {}

            response = self.http_client.post(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return Message.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


