"""
message_reference automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
class MessageReference(BaseModel):
    message_id: Optional[str] = Field(default=None, alias="message_id")
    channel_id: Optional[str] = Field(default=None, alias="channel_id")
    guild_id: Optional[str] = Field(default=None, alias="guild_id")
    fail_if_not_exists: Optional[bool] = Field(default=None, alias="fail_if_not_exists")
    pass
