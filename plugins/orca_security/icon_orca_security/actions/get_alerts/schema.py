# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get alerts that match the specified filter criteria. If no filters are given, all alerts will be returned"


class Input:
    FILTERS = "filters"
    LIMIT = "limit"
    

class Output:
    ALERTS = "alerts"
    

class GetAlertsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filters": {
      "type": "object",
      "title": "Filters",
      "description": "The object containing the fields against which the alerts will be filtered",
      "order": 1
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Maximum number of alerts returned (max value: 1000)",
      "default": 20,
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAlertsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alerts": {
      "type": "array",
      "title": "Alerts",
      "description": "Results containing information about alerts",
      "items": {
        "$ref": "#/definitions/alert"
      },
      "order": 1
    }
  },
  "definitions": {
    "alert": {
      "type": "object",
      "title": "alert",
      "properties": {
        "alert_labels": {
          "type": "array",
          "title": "Alert Labels",
          "description": "Alert labels",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "asset_auto_updates": {
          "type": "string",
          "title": "Asset Auto Updates",
          "description": "Asset auto updates",
          "order": 2
        },
        "asset_availability_zones": {
          "type": "array",
          "title": "Asset Availability Zones",
          "description": "Asset availability zones",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "asset_distribution_major_version": {
          "type": "string",
          "title": "Asset Distribution Major Version",
          "description": "Asset distribution major version",
          "order": 4
        },
        "asset_distribution_name": {
          "type": "string",
          "title": "Asset Distribution Name",
          "description": "Asset distribution name",
          "order": 5
        },
        "asset_distribution_version": {
          "type": "string",
          "title": "Asset Distribution Version",
          "description": "Asset distribution version",
          "order": 6
        },
        "asset_extra_data": {
          "type": "object",
          "title": "Asset Extra Data",
          "description": "Asset extra data",
          "order": 7
        },
        "asset_first_private_dnss": {
          "type": "array",
          "title": "Asset First Private DNSs",
          "description": "Asset first private DNSs",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "asset_first_private_ips": {
          "type": "array",
          "title": "Asset First Private IPs",
          "description": "Asset first private IPs",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "asset_first_public_dnss": {
          "type": "array",
          "title": "Asset First Public DNSs",
          "description": "Asset first public DNSs",
          "items": {
            "type": "string"
          },
          "order": 10
        },
        "asset_first_public_ips": {
          "type": "array",
          "title": "Asset First Public IPs",
          "description": "Asset first public IPs",
          "items": {
            "type": "string"
          },
          "order": 11
        },
        "asset_image_id": {
          "type": "string",
          "title": "Asset Image ID",
          "description": "Asset image ID",
          "order": 13
        },
        "asset_info": {
          "type": "object",
          "title": "Asset Info",
          "description": "Asset info",
          "order": 12
        },
        "asset_ingress_ports": {
          "type": "array",
          "title": "Asset Ingress Ports",
          "description": "Asset ingress ports",
          "items": {
            "type": "string"
          },
          "order": 14
        },
        "asset_num_private_dnss": {
          "type": "integer",
          "title": "Asset Num Private DNSs",
          "description": "Asset num private DNSs",
          "order": 15
        },
        "asset_num_private_ips": {
          "type": "integer",
          "title": "Asset Num Private IPs",
          "description": "Asset num private IPs",
          "order": 16
        },
        "asset_num_public_dnss": {
          "type": "integer",
          "title": "Asset Num Public DNSs",
          "description": "Asset num public DNSs",
          "order": 17
        },
        "asset_num_public_ips": {
          "type": "integer",
          "title": "Asset Num Public IPs",
          "description": "Asset Num public IPs",
          "order": 18
        },
        "asset_regions": {
          "type": "array",
          "title": "Asset Regions",
          "description": "Asset regions",
          "items": {
            "type": "string"
          },
          "order": 19
        },
        "asset_regions_names": {
          "type": "array",
          "title": "Asset Regions Names",
          "description": "Asset regions names",
          "items": {
            "type": "string"
          },
          "order": 20
        },
        "asset_role_names": {
          "type": "array",
          "title": "Asset Role Names",
          "description": "Asset role names",
          "items": {
            "type": "string"
          },
          "order": 21
        },
        "asset_state": {
          "type": "string",
          "title": "Asset State",
          "description": "Asset state",
          "order": 22
        },
        "asset_stopped": {
          "type": "boolean",
          "title": "Asset Stopped",
          "description": "Asset stopped",
          "order": 23
        },
        "asset_tags_info_list": {
          "type": "array",
          "title": "Asset Tags Info List",
          "description": "Asset tags info list",
          "items": {
            "type": "string"
          },
          "order": 24
        },
        "asset_vpcs": {
          "type": "array",
          "title": "Asset VPCs",
          "description": "Asset VPCs",
          "items": {
            "type": "string"
          },
          "order": 25
        },
        "category": {
          "type": "string",
          "title": "Category",
          "description": "Category",
          "order": 26
        },
        "configuration": {
          "$ref": "#/definitions/configuration",
          "title": "Configuration",
          "description": "Configuration",
          "order": 27
        },
        "container_image_name": {
          "type": "string",
          "title": "Container Image Name",
          "description": "Container image name",
          "order": 29
        },
        "container_k8s_pod_namespace": {
          "type": "string",
          "title": "Container K8s Pod Namespace",
          "description": "Container K8s pod namespace",
          "order": 28
        },
        "container_service_name": {
          "type": "string",
          "title": "Container Service Name",
          "description": "Container service name",
          "order": 30
        },
        "cve_list": {
          "type": "array",
          "title": "CVE List",
          "description": "CVE list",
          "items": {
            "type": "string"
          },
          "order": 31
        },
        "data": {
          "$ref": "#/definitions/alert_data",
          "title": "Data",
          "description": "Data",
          "order": 32
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 33
        },
        "details": {
          "type": "string",
          "title": "Details",
          "description": "Details",
          "order": 34
        },
        "finding_schema": {
          "type": "object",
          "title": "Finding Schema",
          "description": "Finding schema",
          "order": 35
        },
        "git_repo_sensitive_data_rules": {
          "type": "array",
          "title": "Git Repo Sensitive Data Rules",
          "description": "Git repo sensitive data rules",
          "items": {
            "type": "string"
          },
          "order": 36
        },
        "git_repo_sensitive_data_tags": {
          "type": "array",
          "title": "Git Repo Sensitive Data Tags",
          "description": "Git repo sensitive data tags",
          "items": {
            "type": "string"
          },
          "order": 37
        },
        "is_compliance": {
          "type": "boolean",
          "title": "Is Compliance",
          "description": "Is compliance",
          "order": 38
        },
        "is_rule": {
          "type": "boolean",
          "title": "Is Rule",
          "description": "Is rule",
          "order": 39
        },
        "num_children_unique_ids": {
          "type": "integer",
          "title": "Num Children Unique IDs",
          "description": "Num children unique IDs",
          "order": 40
        },
        "priv": {
          "$ref": "#/definitions/priv",
          "title": "Priv",
          "description": "Priv",
          "order": 41
        },
        "recommendation": {
          "type": "string",
          "title": "Recommendation",
          "description": "Recommendation",
          "order": 42
        },
        "rule_id": {
          "type": "string",
          "title": "Rule ID",
          "description": "Rule ID",
          "order": 43
        },
        "rule_query": {
          "type": "string",
          "title": "Rule Query",
          "description": "Rule query",
          "order": 44
        },
        "severity_contributing_factors": {
          "type": "array",
          "title": "Severity Contributing Factors",
          "description": "Severity contributing factors",
          "items": {
            "type": "string"
          },
          "order": 45
        },
        "severity_reducing_factors": {
          "type": "array",
          "title": "Severity Reducing Factors",
          "description": "Severity reducing factors",
          "items": {
            "type": "string"
          },
          "order": 46
        },
        "state": {
          "$ref": "#/definitions/state",
          "title": "State",
          "description": "State",
          "order": 47
        },
        "subject_type": {
          "type": "string",
          "title": "Subject Type",
          "description": "Subject type",
          "order": 48
        },
        "tags_info_list": {
          "type": "array",
          "title": "Tags Info List",
          "description": "Tags info list",
          "items": {
            "type": "string"
          },
          "order": 49
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 50
        },
        "type_key": {
          "type": "string",
          "title": "Type Key",
          "description": "Type key",
          "order": 51
        },
        "type_string": {
          "type": "string",
          "title": "Type String",
          "description": "Type string",
          "order": 52
        },
        "user_defined": {
          "type": "boolean",
          "title": "User Defined",
          "description": "User defined",
          "order": 53
        }
      },
      "definitions": {
        "alert_data": {
          "type": "object",
          "title": "alert_data",
          "properties": {
            "details": {
              "type": "string",
              "title": "Details",
              "description": "Details",
              "order": 4
            },
            "headline": {
              "type": "string",
              "title": "Headline",
              "description": "Headline",
              "order": 1
            },
            "mitre_category": {
              "type": "string",
              "title": "Mitre Category",
              "description": "Mitre category",
              "order": 3
            },
            "more_details": {
              "type": "array",
              "title": "More Details",
              "description": "More details",
              "items": {
                "type": "string"
              },
              "order": 2
            },
            "recommendation": {
              "type": "string",
              "title": "Recommendation",
              "description": "Recommendation",
              "order": 5
            },
            "remediation_actions": {
              "type": "array",
              "title": "Remediation Actions",
              "description": "Remediation actions",
              "items": {
                "type": "string"
              },
              "order": 7
            },
            "remediation_cli": {
              "type": "array",
              "title": "Remediation CLI",
              "description": "Remediation CLI",
              "items": {
                "type": "string"
              },
              "order": 9
            },
            "remediation_console": {
              "type": "array",
              "title": "Remediation Console",
              "description": "Remediation console",
              "items": {
                "type": "string"
              },
              "order": 8
            },
            "time_series_field": {
              "type": "string",
              "title": "Time Series Field",
              "description": "Time series field",
              "order": 10
            },
            "title": {
              "type": "string",
              "title": "Title",
              "description": "Title",
              "order": 6
            }
          }
        },
        "configuration": {
          "type": "object",
          "title": "configuration",
          "properties": {
            "comments_count": {
              "type": "integer",
              "title": "Comments Count",
              "description": "Comments count",
              "order": 6
            },
            "jira_issue": {
              "type": "string",
              "title": "Jira Issue",
              "description": "Jira issue",
              "order": 4
            },
            "jira_issue_link": {
              "type": "string",
              "title": "Jira Issue Link",
              "description": "Jira issue link",
              "order": 5
            },
            "last_verified_event": {
              "type": "string",
              "title": "Last Verified Event",
              "description": "Last verified event",
              "order": 7
            },
            "snooze_until": {
              "type": "string",
              "title": "Snooze Until",
              "description": "Snooze until",
              "order": 2
            },
            "user_score": {
              "type": "integer",
              "title": "User Score",
              "description": "User score",
              "order": 3
            },
            "user_status": {
              "type": "string",
              "title": "User Status",
              "description": "User status",
              "order": 1
            }
          }
        },
        "priv": {
          "type": "object",
          "title": "priv",
          "properties": {
            "alert_id": {
              "type": "string",
              "title": "Alert ID",
              "description": "Alert ID",
              "order": 5
            },
            "full_scan_time": {
              "type": "string",
              "title": "Full Scan Time",
              "description": "Full scan time",
              "order": 4
            },
            "key": {
              "type": "string",
              "title": "Key",
              "description": "Key",
              "order": 1
            },
            "orig_score": {
              "type": "integer",
              "title": "Original Score",
              "description": "Original score",
              "order": 3
            },
            "score": {
              "type": "integer",
              "title": "Score",
              "description": "Score",
              "order": 2
            }
          }
        },
        "state": {
          "type": "object",
          "title": "state",
          "properties": {
            "alert_id": {
              "type": "string",
              "title": "Alert ID",
              "description": "Alert ID",
              "order": 1
            },
            "closed_reason": {
              "type": "string",
              "title": "Closed Reason",
              "description": "Closed reason",
              "order": 12
            },
            "created_at": {
              "type": "string",
              "title": "Created At",
              "description": "Created at",
              "order": 6
            },
            "high_since": {
              "type": "string",
              "title": "High Since",
              "description": "High since",
              "order": 9
            },
            "in_verification": {
              "type": "boolean",
              "title": "In Verification",
              "description": "In verification",
              "order": 10
            },
            "last_seen": {
              "type": "string",
              "title": "Last Seen",
              "description": "Last seen",
              "order": 7
            },
            "last_updated": {
              "type": "string",
              "title": "Last Updated",
              "description": "Last updated",
              "order": 13
            },
            "low_since": {
              "type": "string",
              "title": "Low Since",
              "description": "Low since",
              "order": 8
            },
            "score": {
              "type": "integer",
              "title": "Score",
              "description": "Score",
              "order": 4
            },
            "severity": {
              "type": "string",
              "title": "Severity",
              "description": "Severity",
              "order": 5
            },
            "status": {
              "type": "string",
              "title": "Status",
              "description": "Status",
              "order": 2
            },
            "status_time": {
              "type": "string",
              "title": "Status Time",
              "description": "Status time",
              "order": 3
            },
            "verification_status": {
              "type": "string",
              "title": "Verification Status",
              "description": "Verification status",
              "order": 11
            }
          }
        }
      }
    },
    "alert_data": {
      "type": "object",
      "title": "alert_data",
      "properties": {
        "details": {
          "type": "string",
          "title": "Details",
          "description": "Details",
          "order": 4
        },
        "headline": {
          "type": "string",
          "title": "Headline",
          "description": "Headline",
          "order": 1
        },
        "mitre_category": {
          "type": "string",
          "title": "Mitre Category",
          "description": "Mitre category",
          "order": 3
        },
        "more_details": {
          "type": "array",
          "title": "More Details",
          "description": "More details",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "recommendation": {
          "type": "string",
          "title": "Recommendation",
          "description": "Recommendation",
          "order": 5
        },
        "remediation_actions": {
          "type": "array",
          "title": "Remediation Actions",
          "description": "Remediation actions",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "remediation_cli": {
          "type": "array",
          "title": "Remediation CLI",
          "description": "Remediation CLI",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "remediation_console": {
          "type": "array",
          "title": "Remediation Console",
          "description": "Remediation console",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "time_series_field": {
          "type": "string",
          "title": "Time Series Field",
          "description": "Time series field",
          "order": 10
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 6
        }
      }
    },
    "configuration": {
      "type": "object",
      "title": "configuration",
      "properties": {
        "comments_count": {
          "type": "integer",
          "title": "Comments Count",
          "description": "Comments count",
          "order": 6
        },
        "jira_issue": {
          "type": "string",
          "title": "Jira Issue",
          "description": "Jira issue",
          "order": 4
        },
        "jira_issue_link": {
          "type": "string",
          "title": "Jira Issue Link",
          "description": "Jira issue link",
          "order": 5
        },
        "last_verified_event": {
          "type": "string",
          "title": "Last Verified Event",
          "description": "Last verified event",
          "order": 7
        },
        "snooze_until": {
          "type": "string",
          "title": "Snooze Until",
          "description": "Snooze until",
          "order": 2
        },
        "user_score": {
          "type": "integer",
          "title": "User Score",
          "description": "User score",
          "order": 3
        },
        "user_status": {
          "type": "string",
          "title": "User Status",
          "description": "User status",
          "order": 1
        }
      }
    },
    "priv": {
      "type": "object",
      "title": "priv",
      "properties": {
        "alert_id": {
          "type": "string",
          "title": "Alert ID",
          "description": "Alert ID",
          "order": 5
        },
        "full_scan_time": {
          "type": "string",
          "title": "Full Scan Time",
          "description": "Full scan time",
          "order": 4
        },
        "key": {
          "type": "string",
          "title": "Key",
          "description": "Key",
          "order": 1
        },
        "orig_score": {
          "type": "integer",
          "title": "Original Score",
          "description": "Original score",
          "order": 3
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "description": "Score",
          "order": 2
        }
      }
    },
    "state": {
      "type": "object",
      "title": "state",
      "properties": {
        "alert_id": {
          "type": "string",
          "title": "Alert ID",
          "description": "Alert ID",
          "order": 1
        },
        "closed_reason": {
          "type": "string",
          "title": "Closed Reason",
          "description": "Closed reason",
          "order": 12
        },
        "created_at": {
          "type": "string",
          "title": "Created At",
          "description": "Created at",
          "order": 6
        },
        "high_since": {
          "type": "string",
          "title": "High Since",
          "description": "High since",
          "order": 9
        },
        "in_verification": {
          "type": "boolean",
          "title": "In Verification",
          "description": "In verification",
          "order": 10
        },
        "last_seen": {
          "type": "string",
          "title": "Last Seen",
          "description": "Last seen",
          "order": 7
        },
        "last_updated": {
          "type": "string",
          "title": "Last Updated",
          "description": "Last updated",
          "order": 13
        },
        "low_since": {
          "type": "string",
          "title": "Low Since",
          "description": "Low since",
          "order": 8
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "description": "Score",
          "order": 4
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity",
          "order": 5
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 2
        },
        "status_time": {
          "type": "string",
          "title": "Status Time",
          "description": "Status time",
          "order": 3
        },
        "verification_status": {
          "type": "string",
          "title": "Verification Status",
          "description": "Verification status",
          "order": 11
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)