# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fetch the identities and attack index of the top clickers within your organization for a given period"


class Input:
    WINDOW = "window"
    

class Output:
    INTERVAL = "interval"
    TOTALTOPCLICKERS = "totalTopClickers"
    USERS = "users"
    

class GetTopClickersInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "window": {
      "type": "integer",
      "title": "Window",
      "description": "An integer indicating how many days the data should be retrieved for",
      "enum": [
        14,
        30,
        90
      ],
      "order": 1
    }
  },
  "required": [
    "window"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetTopClickersOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "interval": {
      "type": "string",
      "title": "Interval",
      "description": "An ISO8601-formatted interval showing what time the response was calculated for",
      "order": 3
    },
    "totalTopClickers": {
      "type": "integer",
      "title": "Total Top Clickers",
      "description": "An integer describing the total number of top clickers in the time interval",
      "order": 2
    },
    "users": {
      "type": "array",
      "title": "Users",
      "description": "An array of user objects that contain information about the user's identity and statistics of the clicking behavior",
      "items": {
        "$ref": "#/definitions/user"
      },
      "order": 1
    }
  },
  "definitions": {
    "clickStatistics": {
      "type": "object",
      "title": "clickStatistics",
      "properties": {
        "clickCount": {
          "type": "integer",
          "title": "Click Count",
          "description": "Total number of clicks from this user in the time interval",
          "order": 1
        },
        "families": {
          "type": "array",
          "title": "Families",
          "description": "List of threat families",
          "items": {
            "$ref": "#/definitions/families"
          },
          "order": 2
        }
      },
      "definitions": {
        "families": {
          "type": "object",
          "title": "families",
          "properties": {
            "clicks": {
              "type": "integer",
              "title": "Clicks",
              "description": "Total number of clicks on threats belong to this threat family",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the threat family",
              "order": 1
            }
          }
        }
      }
    },
    "families": {
      "type": "object",
      "title": "families",
      "properties": {
        "clicks": {
          "type": "integer",
          "title": "Clicks",
          "description": "Total number of clicks on threats belong to this threat family",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the threat family",
          "order": 1
        }
      }
    },
    "identity": {
      "type": "object",
      "title": "identity",
      "properties": {
        "customerUserId": {
          "type": "string",
          "title": "Customer User ID",
          "description": "Identifier associated with the user which was provided by the customer",
          "order": 2
        },
        "department": {
          "type": "string",
          "title": "Department",
          "description": "Department of the user",
          "order": 5
        },
        "emails": {
          "type": "array",
          "title": "Emails",
          "description": "List of email addresses associated with the user",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "guid": {
          "type": "string",
          "title": "GUID",
          "description": "Unique identifier within Proofpoint's system",
          "order": 1
        },
        "location": {
          "type": "string",
          "title": "Location",
          "description": "Location of the user",
          "order": 6
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the user",
          "order": 4
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title of the user",
          "order": 7
        },
        "vip": {
          "type": "boolean",
          "title": "VIP",
          "description": "Whether the user has been identified as a VIP",
          "order": 8
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "clickStatistics": {
          "$ref": "#/definitions/clickStatistics",
          "title": "Click Statistics",
          "description": "Click statistics",
          "order": 2
        },
        "identity": {
          "$ref": "#/definitions/identity",
          "title": "Identity",
          "description": "Identity",
          "order": 1
        }
      },
      "definitions": {
        "clickStatistics": {
          "type": "object",
          "title": "clickStatistics",
          "properties": {
            "clickCount": {
              "type": "integer",
              "title": "Click Count",
              "description": "Total number of clicks from this user in the time interval",
              "order": 1
            },
            "families": {
              "type": "array",
              "title": "Families",
              "description": "List of threat families",
              "items": {
                "$ref": "#/definitions/families"
              },
              "order": 2
            }
          },
          "definitions": {
            "families": {
              "type": "object",
              "title": "families",
              "properties": {
                "clicks": {
                  "type": "integer",
                  "title": "Clicks",
                  "description": "Total number of clicks on threats belong to this threat family",
                  "order": 2
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name of the threat family",
                  "order": 1
                }
              }
            }
          }
        },
        "families": {
          "type": "object",
          "title": "families",
          "properties": {
            "clicks": {
              "type": "integer",
              "title": "Clicks",
              "description": "Total number of clicks on threats belong to this threat family",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the threat family",
              "order": 1
            }
          }
        },
        "identity": {
          "type": "object",
          "title": "identity",
          "properties": {
            "customerUserId": {
              "type": "string",
              "title": "Customer User ID",
              "description": "Identifier associated with the user which was provided by the customer",
              "order": 2
            },
            "department": {
              "type": "string",
              "title": "Department",
              "description": "Department of the user",
              "order": 5
            },
            "emails": {
              "type": "array",
              "title": "Emails",
              "description": "List of email addresses associated with the user",
              "items": {
                "type": "string"
              },
              "order": 3
            },
            "guid": {
              "type": "string",
              "title": "GUID",
              "description": "Unique identifier within Proofpoint's system",
              "order": 1
            },
            "location": {
              "type": "string",
              "title": "Location",
              "description": "Location of the user",
              "order": 6
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the user",
              "order": 4
            },
            "title": {
              "type": "string",
              "title": "Title",
              "description": "Title of the user",
              "order": 7
            },
            "vip": {
              "type": "boolean",
              "title": "VIP",
              "description": "Whether the user has been identified as a VIP",
              "order": 8
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)