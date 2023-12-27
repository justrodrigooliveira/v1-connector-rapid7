# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Creates a PublicHTTPBased policy"


class Input:
    POLICY = "policy"
    

class Output:
    RESPONSE = "response"
    

class CreatePublicnonhttpbasedpolicyInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "policy": {
      "$ref": "#/definitions/publicnonhttpbasedpolicy",
      "title": "PublicHTTPBased Policy Settings",
      "description": "PublicHTTPBased policy settings",
      "order": 1
    }
  },
  "definitions": {
    "publicnonhttpbasedpolicy": {
      "type": "object",
      "title": "publicnonhttpbasedpolicy",
      "properties": {
        "DataAccounting": {
          "type": "string",
          "title": "Data Accounting",
          "description": "Data Accounting",
          "default": "Exclude",
          "enum": [
            "Include",
            "Exclude"
          ],
          "order": 13
        },
        "HostedAddress": {
          "type": "string",
          "title": "Hosted Address",
          "description": "Hosted Address",
          "order": 3
        },
        "Identity": {
          "type": "array",
          "title": "Identity",
          "description": "Users or groups",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "LogTraffic": {
          "type": "string",
          "title": "Log Traffic",
          "description": "Log Traffic",
          "default": "Disable",
          "enum": [
            "Enable",
            "Disable"
          ],
          "order": 14
        },
        "MatchIdentity": {
          "type": "string",
          "title": "Match Identity",
          "description": "Match Identity",
          "default": "Disable",
          "enum": [
            "Enable",
            "Disable"
          ],
          "order": 11
        },
        "OutboundAddress": {
          "type": "string",
          "title": "Outbound Address",
          "description": "Outbound address",
          "order": 10
        },
        "RewriteSourceAddress": {
          "type": "string",
          "title": "Rewrite Source Address",
          "description": "Rewrite source address",
          "default": "Disable",
          "enum": [
            "Enable",
            "Disable"
          ],
          "order": 9
        },
        "ScanIMAP": {
          "type": "string",
          "title": "Scan IMAP",
          "description": "Scan IMAP",
          "default": "Disable",
          "enum": [
            "Enable",
            "Disable"
          ],
          "order": 5
        },
        "ScanPOP3": {
          "type": "string",
          "title": "Scan POP3",
          "description": "Scan POP3",
          "default": "Disable",
          "enum": [
            "Enable",
            "Disable"
          ],
          "order": 6
        },
        "ScanPOP3S": {
          "type": "string",
          "title": "Scan POP3S",
          "description": "Scan POP3S",
          "default": "Disable",
          "enum": [
            "Enable",
            "Disable"
          ],
          "order": 8
        },
        "ScanSMTP": {
          "type": "string",
          "title": "Scan SMTP",
          "description": "Scan SMTP",
          "default": "Disable",
          "enum": [
            "Enable",
            "Disable"
          ],
          "order": 4
        },
        "ScanSMTPS": {
          "type": "string",
          "title": "Scan SMTPS",
          "description": "Scan SMTPS",
          "default": "Disable",
          "enum": [
            "Enable",
            "Disable"
          ],
          "order": 7
        },
        "SecurityPolicy": {
          "$ref": "#/definitions/securitypolicy",
          "title": "Security Policy",
          "description": "General security policy settings",
          "order": 1
        },
        "SourceZones": {
          "type": "array",
          "title": "Source Zones",
          "description": "Zones for Source Zone",
          "items": {
            "type": "string"
          },
          "order": 2
        }
      },
      "definitions": {
        "securitypolicy": {
          "type": "object",
          "title": "securitypolicy",
          "properties": {
            "Description": {
              "type": "string",
              "title": "Description",
              "description": "Policy Description",
              "order": 2
            },
            "DestSecurityHeartbeat": {
              "type": "string",
              "title": "DestSecurityHeartbeat",
              "description": "DestSecurityHeartbeat",
              "default": "Disable",
              "enum": [
                "Disable",
                "Enable"
              ],
              "order": 10
            },
            "IPFamily": {
              "type": "string",
              "title": "IP Family",
              "description": "IP Family type",
              "default": "IPv4",
              "enum": [
                "IPv4",
                "IPv6"
              ],
              "order": 4
            },
            "IntrusionPrevention": {
              "type": "string",
              "title": "Intrusion Prevention",
              "description": "Intrusion Prevention",
              "default": "None",
              "order": 7
            },
            "Name": {
              "type": "string",
              "title": "Name",
              "description": "Policy Name",
              "order": 1
            },
            "Position": {
              "type": "string",
              "title": "Position",
              "description": "Security Policy position",
              "default": "top",
              "enum": [
                "top",
                "bottom",
                "after",
                "before"
              ],
              "order": 5
            },
            "PositionPolicyName": {
              "type": "string",
              "title": "Position Policy Name",
              "description": "Name of policy that this policy is to be placed before or after",
              "order": 6
            },
            "SourceSecurityHeartbeat": {
              "type": "string",
              "title": "SourceSecurityHeartbeat",
              "description": "SourceSecurityHeartbeat",
              "default": "Disable",
              "enum": [
                "Disable",
                "Enable"
              ],
              "order": 9
            },
            "Status": {
              "type": "string",
              "title": "Status",
              "description": "Policy Status",
              "default": "Disable",
              "enum": [
                "Disable",
                "Enable"
              ],
              "order": 3
            },
            "TrafficShapingPolicy": {
              "type": "string",
              "title": "Traffic Shaping Policy",
              "description": "Traffic Shaping Policy",
              "default": "None",
              "order": 8
            }
          },
          "required": [
            "Name",
            "Position"
          ]
        }
      }
    },
    "securitypolicy": {
      "type": "object",
      "title": "securitypolicy",
      "properties": {
        "Description": {
          "type": "string",
          "title": "Description",
          "description": "Policy Description",
          "order": 2
        },
        "DestSecurityHeartbeat": {
          "type": "string",
          "title": "DestSecurityHeartbeat",
          "description": "DestSecurityHeartbeat",
          "default": "Disable",
          "enum": [
            "Disable",
            "Enable"
          ],
          "order": 10
        },
        "IPFamily": {
          "type": "string",
          "title": "IP Family",
          "description": "IP Family type",
          "default": "IPv4",
          "enum": [
            "IPv4",
            "IPv6"
          ],
          "order": 4
        },
        "IntrusionPrevention": {
          "type": "string",
          "title": "Intrusion Prevention",
          "description": "Intrusion Prevention",
          "default": "None",
          "order": 7
        },
        "Name": {
          "type": "string",
          "title": "Name",
          "description": "Policy Name",
          "order": 1
        },
        "Position": {
          "type": "string",
          "title": "Position",
          "description": "Security Policy position",
          "default": "top",
          "enum": [
            "top",
            "bottom",
            "after",
            "before"
          ],
          "order": 5
        },
        "PositionPolicyName": {
          "type": "string",
          "title": "Position Policy Name",
          "description": "Name of policy that this policy is to be placed before or after",
          "order": 6
        },
        "SourceSecurityHeartbeat": {
          "type": "string",
          "title": "SourceSecurityHeartbeat",
          "description": "SourceSecurityHeartbeat",
          "default": "Disable",
          "enum": [
            "Disable",
            "Enable"
          ],
          "order": 9
        },
        "Status": {
          "type": "string",
          "title": "Status",
          "description": "Policy Status",
          "default": "Disable",
          "enum": [
            "Disable",
            "Enable"
          ],
          "order": 3
        },
        "TrafficShapingPolicy": {
          "type": "string",
          "title": "Traffic Shaping Policy",
          "description": "Traffic Shaping Policy",
          "default": "None",
          "order": 8
        }
      },
      "required": [
        "Name",
        "Position"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreatePublicnonhttpbasedpolicyOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/response",
      "title": "Response",
      "description": "Returns the response from creating a policy",
      "order": 1
    }
  },
  "definitions": {
    "response": {
      "type": "object",
      "title": "response",
      "properties": {
        "invalid_params": {
          "type": "string",
          "title": "Invalid Params",
          "description": "Invalid params that have been set, otherwise 'None'",
          "order": 3
        },
        "status_code": {
          "type": "string",
          "title": "Status Code",
          "description": "The status code from the response",
          "order": 1
        },
        "status_response": {
          "type": "string",
          "title": "Status Response",
          "description": "Description of the response",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)