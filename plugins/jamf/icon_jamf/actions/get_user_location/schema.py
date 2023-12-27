# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get user location details by device ID"


class Input:
    ID = "ID"
    

class Output:
    USER_LOCATION_DETAIL = "user_location_detail"
    

class GetUserLocationInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ID": {
      "type": "string",
      "title": "Device ID",
      "description": "Device ID",
      "order": 1
    }
  },
  "required": [
    "ID"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetUserLocationOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_location_detail": {
      "$ref": "#/definitions/user_location_detail",
      "title": "User Location Details",
      "description": "User location details",
      "order": 1
    }
  },
  "required": [
    "user_location_detail"
  ],
  "definitions": {
    "user_location_detail": {
      "type": "object",
      "title": "user_location_detail",
      "properties": {
        "building": {
          "type": "string",
          "title": "Building",
          "description": "Building",
          "order": 7
        },
        "department": {
          "type": "string",
          "title": "Department",
          "description": "Department",
          "order": 6
        },
        "email_address": {
          "type": "string",
          "title": "Email Address",
          "description": "Email address",
          "order": 3
        },
        "phone": {
          "type": "string",
          "title": "Phone",
          "description": "Phone",
          "order": 5
        },
        "position": {
          "type": "string",
          "title": "Position",
          "description": "Position",
          "order": 4
        },
        "real_name": {
          "type": "string",
          "title": "Real Name",
          "description": "Real name",
          "order": 2
        },
        "room": {
          "type": "string",
          "title": "Room Number",
          "description": "Room number",
          "order": 8
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "Username",
          "order": 1
        }
      },
      "required": [
        "building",
        "department",
        "email_address",
        "phone",
        "position",
        "real_name",
        "room",
        "username"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)