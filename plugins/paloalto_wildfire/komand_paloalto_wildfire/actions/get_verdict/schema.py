# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Query for a files classification"


class Input:
    HASH = "hash"
    

class Output:
    VERDICT = "verdict"
    

class GetVerdictInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "The MD5 or SHA-256 hash value of the sample",
      "order": 1
    }
  },
  "required": [
    "hash"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetVerdictOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "verdict": {
      "type": "string",
      "title": "Verdict",
      "description": "One of the following verdicts: Benign, Malware, Greyware, Pending, Error, or Not found",
      "order": 1
    }
  },
  "required": [
    "verdict"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)