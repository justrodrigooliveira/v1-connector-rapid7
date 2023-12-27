# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Exempt an item from conviction"


class Input:
    COMMENT = "comment"
    ORIGINENDPOINTID = "originEndpointId"
    ORIGINPERSONID = "originPersonId"
    PROPERTIESCERTIFICATESIGNER = "propertiesCertificateSigner"
    PROPERTIESFILENAME = "propertiesFileName"
    PROPERTIESPATH = "propertiesPath"
    PROPERTIESSHA256 = "propertiesSha256"
    TYPE = "type"
    

class Output:
    ALLOWEDITEM = "allowedItem"
    

class AddAllowedItemInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Comment indicating why the item should be allowed",
      "order": 6
    },
    "originEndpointId": {
      "type": "string",
      "title": "Origin Endpoint ID",
      "description": "Endpoint where the item to be allowed was last seen",
      "order": 8
    },
    "originPersonId": {
      "type": "string",
      "title": "Origin Person ID",
      "description": "Person associated with the endpoint where the item to be allowed was last seen",
      "order": 7
    },
    "propertiesCertificateSigner": {
      "type": "string",
      "title": "Properties Certificate Signer",
      "description": "Properties value saved for the certificateSigner. Required if 'certificateSigner' is selected in the Type input",
      "order": 5
    },
    "propertiesFileName": {
      "type": "string",
      "title": "Properties File Name",
      "description": "Properties file name for the application",
      "order": 2
    },
    "propertiesPath": {
      "type": "string",
      "title": "Properties Path",
      "description": "Properties path for the application. Required if 'path' is selected in the Type input",
      "order": 3
    },
    "propertiesSha256": {
      "type": "string",
      "title": "Properties SHA256",
      "description": "Properties SHA256 value for the application. Required if 'SHA256' is selected in the Type input",
      "order": 4
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Property by which an item is allowed. You need to fill in the input starting with 'properties' for the selected type",
      "enum": [
        "sha256",
        "path",
        "certificateSigner"
      ],
      "order": 1
    }
  },
  "required": [
    "comment",
    "type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddAllowedItemOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "allowedItem": {
      "$ref": "#/definitions/item",
      "title": "Allowed Item",
      "description": "Allowed item created",
      "order": 1
    }
  },
  "definitions": {
    "item": {
      "type": "object",
      "title": "item",
      "properties": {
        "comment": {
          "type": "string",
          "title": "Comment",
          "description": "Comment indicating why the item was blocked or allowed",
          "order": 5
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "Date and time (UTC) when the item was created",
          "order": 2
        },
        "createdBy": {
          "$ref": "#/definitions/userObject",
          "title": "Created By",
          "description": "Created by",
          "order": 7
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Item ID",
          "order": 1
        },
        "originEndpoint": {
          "$ref": "#/definitions/objectId",
          "title": "Origin Endpoint",
          "description": "Represents a referenced object",
          "order": 9
        },
        "originPerson": {
          "$ref": "#/definitions/userObject",
          "title": "Origin Person",
          "description": "Origin person",
          "order": 8
        },
        "properties": {
          "$ref": "#/definitions/properties",
          "title": "Properties",
          "description": "Item properties",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Property by which an item is blocked or allowed",
          "order": 6
        },
        "updatedAt": {
          "type": "string",
          "title": "Updated At",
          "description": "Date and time (UTC) when the item was updated",
          "order": 3
        }
      },
      "definitions": {
        "objectId": {
          "type": "object",
          "title": "objectId",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "The ID of the referenced object",
              "order": 1
            }
          }
        },
        "properties": {
          "type": "object",
          "title": "properties",
          "properties": {
            "certificateSigner": {
              "type": "string",
              "title": "Certificate Signer",
              "description": "Value saved for the certificateSigner",
              "order": 4
            },
            "fileName": {
              "type": "string",
              "title": "File Name",
              "description": "File name",
              "order": 1
            },
            "path": {
              "type": "string",
              "title": "Path",
              "description": "Path for the application",
              "order": 2
            },
            "sha256": {
              "type": "string",
              "title": "SHA256",
              "description": "SHA256 value for the application",
              "order": 3
            }
          }
        },
        "userObject": {
          "type": "object",
          "title": "userObject",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Unique ID for the user",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Person's name",
              "order": 2
            }
          }
        }
      }
    },
    "objectId": {
      "type": "object",
      "title": "objectId",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The ID of the referenced object",
          "order": 1
        }
      }
    },
    "properties": {
      "type": "object",
      "title": "properties",
      "properties": {
        "certificateSigner": {
          "type": "string",
          "title": "Certificate Signer",
          "description": "Value saved for the certificateSigner",
          "order": 4
        },
        "fileName": {
          "type": "string",
          "title": "File Name",
          "description": "File name",
          "order": 1
        },
        "path": {
          "type": "string",
          "title": "Path",
          "description": "Path for the application",
          "order": 2
        },
        "sha256": {
          "type": "string",
          "title": "SHA256",
          "description": "SHA256 value for the application",
          "order": 3
        }
      }
    },
    "userObject": {
      "type": "object",
      "title": "userObject",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Unique ID for the user",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Person's name",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)