"""
message automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from .message_embed import MessageEmbed
from .message_allowed_mentions import MessageAllowedMentions
class Message(BaseModel):
    content: Optional[str] = Field(default=None, alias="content")
    nonce: Optional[str] = Field(default=None, alias="nonce")
    tts: Optional[bool] = Field(default=None, alias="tts")
    embeds: Optional[List[MessageEmbed]] = Field(default=None, alias="embeds")
    allowed_mentions: Optional[MessageAllowedMentions] = Field(default=None, alias="allowed_mentions")
    message_reference: Optional[str] = Field(default=None, alias="message_reference")
    flags: Optional[int] = Field(default=None, alias="flags")
    enforce_nonce: Optional[bool] = Field(default=None, alias="enforce_nonce")
    pass
