# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Delete a user. This operation on a user that hasn't been deactivated causes that user to be deactivated. A second delete operation is required to delete the user. Warning, this action cannot be recovered"


class Input:
    SENDADMINEMAIL = "sendAdminEmail"
    USERLOGIN = "userLogin"


class Output:
    SUCCESS = "success"


class DeleteUserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "sendAdminEmail": {
      "type": "boolean",
      "title": "Send Admin Email",
      "description": "Sends a deactivation email to the administrator if true. Default value is false",
      "default": false,
      "order": 2
    },
    "userLogin": {
      "type": "string",
      "title": "Okta User Login",
      "description": "The login of the user to delete",
      "order": 1
    }
  },
  "required": [
    "sendAdminEmail",
    "userLogin"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteUserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether deactivation was successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)