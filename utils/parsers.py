# -*- coding: utf-8 -*-

from django.conf import settings
from rest_framework.settings import api_settings
from rest_framework.parsers import BaseParser
from rest_framework.exceptions import ParseError

from .renderers import UJSONRenderer
import ujson

import codecs


__author__ = 'y.gavenchuk aka murminathor'
__all__ = ['UJSONParser', ]


def strict_constant(o):
    raise ValueError('Out of range float values are not JSON compliant: ' + repr(o))


class UJSONParser(BaseParser):
    """
    Parses JSON-serialized data by ujson parser.
    """

    media_type = 'application/json'
    renderer_class = UJSONRenderer
    strict = api_settings.STRICT_JSON

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            decoded_stream = codecs.getreader(encoding)(stream)
            parse_constant = strict_constant if self.strict else None
            return ujson.load(decoded_stream, parse_constant=parse_constant)
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % str(exc))
