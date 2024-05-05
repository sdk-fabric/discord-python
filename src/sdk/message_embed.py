"""
message_embed automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
class MessageEmbed(BaseModel):
    title: Optional[str] = Field(default=None, alias="title")
    type: Optional[str] = Field(default=None, alias="type")
    description: Optional[str] = Field(default=None, alias="description")
    url: Optional[str] = Field(default=None, alias="url")
    timestamp: Optional[str] = Field(default=None, alias="timestamp")
    color: Optional[int] = Field(default=None, alias="color")
    pass