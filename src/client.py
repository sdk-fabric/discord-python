"""
Client automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .channel_tag import ChannelTag

class Client(sdkgen.ClientAbstract):
    def __init__(self, base_url: str, credentials: sdkgen.CredentialsInterface):
        super().__init__(base_url, credentials)

    def channel(self) -> ChannelTag:
        return ChannelTag(
            self.http_client,
            self.parser
        )



    @staticmethod
    def build(clientId: str, clientSecret: str, tokenStore: sdkgen.TokenStoreInterface, scopes: List[str]):
        return Client("https://discord.com/api/v10", sdkgen.OAuth2(clientId, clientSecret, "https://discord.com/api/oauth2/token", "https://discord.com/oauth2/authorize", tokenStore, scopes))
