# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update the sites to which a user has access in bulk. It can be used to remove sites as well"


class Input:
    SITE_IDS = "site_ids"
    USER_ID = "user_id"
    

class Output:
    LINKS = "links"
    

class UpdateUserSiteAccessInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "site_ids": {
      "type": "array",
      "title": "Site IDs",
      "description": "The identifiers of the sites to which the user account should be granted access, ignored if the user has access to all sites",
      "items": {
        "type": "integer"
      },
      "order": 2
    },
    "user_id": {
      "type": "integer",
      "title": "User ID",
      "description": "The identifier of the user account",
      "order": 1
    }
  },
  "required": [
    "site_ids",
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateUserSiteAccessOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "links": {
      "type": "array",
      "title": "Links",
      "description": "Hypermedia links to corresponding or related resources",
      "items": {
        "$ref": "#/definitions/link"
      },
      "order": 1
    }
  },
  "required": [
    "links"
  ],
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "URL",
          "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Link relation type following RFC 5988",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)