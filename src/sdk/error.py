"""
error automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class Error(BaseModel):
    code: Optional[int] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")
    errors: Optional[Any] = Field(default=None, alias="errors")
    pass


