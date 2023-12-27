# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Downloads the investigation package based on submission ID"


class Input:
    ID = "id"
    POLL = "poll"
    POLL_TIME_SEC = "poll_time_sec"
    

class Output:
    FILE = "file"
    

class DownloadSandboxInvestigationPackageInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Unique alphanumeric string that identifies the analysis results of a submission",
      "order": 1
    },
    "poll": {
      "type": "boolean",
      "title": "Poll",
      "description": "If script should wait until the task is finished before returning the result (enabled by default)",
      "default": true,
      "order": 2
    },
    "poll_time_sec": {
      "type": "number",
      "title": "Poll Time in Seconds",
      "description": "Maximum time to wait for the result to be available",
      "default": 30,
      "order": 3
    }
  },
  "required": [
    "id",
    "poll"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DownloadSandboxInvestigationPackageOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file": {
      "$ref": "#/definitions/file",
      "title": "File",
      "description": "The output is a .zip file",
      "order": 1
    }
  },
  "required": [
    "file"
  ],
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)