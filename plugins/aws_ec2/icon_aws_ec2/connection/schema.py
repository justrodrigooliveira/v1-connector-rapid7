# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    AWS_ACCESS_KEY_ID = "aws_access_key_id"
    AWS_SECRET_ACCESS_KEY = "aws_secret_access_key"
    EXTERNAL_ID = "external_id"
    REGION = "region"
    ROLE_ARN = "role_arn"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "aws_access_key_id": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "AWS Access Key ID",
      "description": "The ID of the AWS Access Key to use for authentication with AWS",
      "order": 1
    },
    "aws_secret_access_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "AWS Secret Access Key",
      "description": "The AWS Secret Access Key used for signing requests with the given AWS Access Key ID. Note: Domain is not required",
      "order": 2
    },
    "external_id": {
      "type": "string",
      "title": "External ID",
      "description": "External ID given during role creation",
      "order": 5
    },
    "region": {
      "type": "string",
      "title": "Region",
      "description": "The AWS Region to use for requests. An example would be us-east-1",
      "order": 3
    },
    "role_arn": {
      "type": "string",
      "title": "Role ARN",
      "description": "AWS IAM role ARN to assume",
      "order": 4
    }
  },
  "required": [
    "aws_access_key_id",
    "aws_secret_access_key",
    "region"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)