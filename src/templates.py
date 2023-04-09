from datetime import datetime
from typing import Dict, Union

from pydantic import BaseModel, root_validator


class Date(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, str):
            try:
                datetime.strptime(v, '%d.%m.%Y').date()
            except ValueError:
                datetime.strptime(v, '%Y-%m-%d').date()
            return cls(v)
        raise ValueError


class NameField(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, str):
            splited_value = v.split('_')
            if splited_value == 3 and \
                    splited_value[0] == 'field' and type(splited_value[2]) is int and splited_value[1] == 'name':
                return cls(v)
        raise ValueError


class Phone(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, str) and v[0:2] == "+7" and len(v) == 12:
            return cls(v)
        raise ValueError


class Email(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, str) and '@' in v:
            return cls(v)
        raise ValueError


class Text(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, str):
            return cls(v)
        raise ValueError


class GetFormTemplate(BaseModel):
    fields: Dict[str, Union[Date, Phone, Email, Text]]

    @root_validator
    def calculate_type(cls, values):
        fields = values["fields"]
        for name in fields:
            fields[name] = type(fields[name]).__name__.lower()
        return values
