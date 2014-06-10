#!/usr/bin/env python
# coding: utf-8

try:
    import ujson as json
    JsonParseError = ValueError
except ImportError:
    try:
        import jsonlib2 as json
        JsonParseError = json.ReadError
    except ImportError:
        try:
            import simplejson as json
            JsonParseError = json.JSONDecodeError
        except ImportError:
            import json
            JsonParseError = ValueError

