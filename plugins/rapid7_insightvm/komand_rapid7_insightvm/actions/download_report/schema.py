# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Returns the contents of a generated report"


class Input:
    ID = "id"
    INSTANCE = "instance"
    

class Output:
    REPORT = "report"
    

class DownloadReportInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "Report ID",
      "description": "Identifier of the report to download",
      "order": 1
    },
    "instance": {
      "type": "string",
      "title": "Instance",
      "description": "The identifier of the report instance, 'latest' or ID",
      "order": 2
    }
  },
  "required": [
    "id",
    "instance"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DownloadReportOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "report": {
      "type": "string",
      "title": "Report",
      "displayType": "bytes",
      "description": "Base64 encoded report",
      "format": "bytes",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)