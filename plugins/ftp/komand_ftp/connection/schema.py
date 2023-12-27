# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CREDENTIALS = "credentials"
    HOST = "host"
    PASSIVE = "passive"
    SECURE = "secure"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "FTP Username and Password",
      "description": "FTP username and password",
      "order": 1
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Address of FTP server",
      "order": 2
    },
    "passive": {
      "type": "boolean",
      "title": "Passive",
      "description": "Passive connection for FTP server",
      "default": false,
      "order": 4
    },
    "secure": {
      "type": "boolean",
      "title": "SSL/TLS",
      "description": "Whether TLS encryption should be used",
      "default": false,
      "order": 3
    }
  },
  "required": [
    "host"
  ],
  "definitions": {
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password"
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with"
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)