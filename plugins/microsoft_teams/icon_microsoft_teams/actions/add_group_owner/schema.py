# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add a user to the group's list of owners"


class Input:
    GROUP_NAME = "group_name"
    MEMBER_LOGIN = "member_login"


class Output:
    SUCCESS = "success"


class AddGroupOwnerInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group_name": {
      "type": "string",
      "title": "Group Name",
      "description": "Name of the group or team to which the member is to be added as the owner",
      "order": 2
    },
    "member_login": {
      "type": "string",
      "title": "Member Login",
      "description": "The login of the group member to be added as the owner",
      "order": 1
    }
  },
  "required": [
    "group_name",
    "member_login"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddGroupOwnerOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Boolean indicating if this action was successful",
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