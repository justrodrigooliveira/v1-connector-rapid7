# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get hosts blocked with shun command"


class Input:
    pass

class Output:
    HOSTS = "hosts"
    

class GetBlockedHostsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetBlockedHostsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hosts": {
      "type": "array",
      "title": "Hosts",
      "description": "List of hosts blocked with shun command",
      "items": {
        "$ref": "#/definitions/hosts"
      },
      "order": 1
    }
  },
  "required": [
    "hosts"
  ],
  "definitions": {
    "hosts": {
      "type": "object",
      "title": "hosts",
      "properties": {
        "dest_ip": {
          "type": "string",
          "title": "Destination IP",
          "description": "Destination IP address",
          "order": 2
        },
        "dest_port": {
          "type": "string",
          "title": "Destination Port",
          "description": "Destination port",
          "order": 4
        },
        "protocol": {
          "type": "string",
          "title": "Protocol",
          "description": "Protocol",
          "order": 5
        },
        "source_ip": {
          "type": "string",
          "title": "Source IP",
          "description": "Source IP address",
          "order": 1
        },
        "source_port": {
          "type": "string",
          "title": "Source Port",
          "description": "Source port",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)