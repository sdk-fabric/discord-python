"""
channel_invite automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class ChannelInvite(BaseModel):
    max_age: Optional[int] = Field(default=None, alias="max_age")
    max_uses: Optional[int] = Field(default=None, alias="max_uses")
    temporary: Optional[bool] = Field(default=None, alias="temporary")
    unique: Optional[bool] = Field(default=None, alias="unique")
    target_type: Optional[int] = Field(default=None, alias="target_type")
    target_user_id: Optional[str] = Field(default=None, alias="target_user_id")
    target_application_id: Optional[str] = Field(default=None, alias="target_application_id")
    pass


