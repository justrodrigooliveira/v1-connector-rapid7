# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a new project with default preset and configuration settings"


class Input:
    ISPUBLIC = "isPublic"
    NAME = "name"
    OWNINGTEAM = "owningTeam"
    

class Output:
    ID = "id"
    LINK = "link"
    

class CreateProjectInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "isPublic": {
      "type": "boolean",
      "title": "Is Public",
      "description": "Whether the project is public or not",
      "default": false,
      "order": 3
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of the project",
      "order": 1
    },
    "owningTeam": {
      "type": "string",
      "title": "Owning Team",
      "description": "ID of the team that owns the project",
      "order": 2
    }
  },
  "required": [
    "isPublic",
    "name",
    "owningTeam"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateProjectOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "ID of the created project",
      "order": 1
    },
    "link": {
      "$ref": "#/definitions/link",
      "title": "Link",
      "description": "Metadata about the project",
      "order": 2
    }
  },
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Relation of the link",
          "order": 1
        },
        "uri": {
          "type": "string",
          "title": "URI",
          "description": "Relative URL of the project",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)