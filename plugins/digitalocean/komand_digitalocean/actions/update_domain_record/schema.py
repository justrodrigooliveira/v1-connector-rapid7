# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Updates a domain record on the domain name"


class Input:
    DOMAIN_NAME = "domain_name"
    PROPERTY = "property"
    RECORD_ID = "record_id"
    VALUE = "value"
    

class Output:
    SUCCESS = "success"
    

class UpdateDomainRecordInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain_name": {
      "type": "string",
      "title": "Host",
      "description": "IP address or hostname to knock",
      "order": 1
    },
    "property": {
      "type": "string",
      "title": "Domain record property",
      "description": "The property on the domain record to update, eg. 'name', 'priority', 'weight', etc",
      "order": 3
    },
    "record_id": {
      "type": "string",
      "title": "Record ID",
      "description": "ID of the domain record",
      "order": 2
    },
    "value": {
      "type": "string",
      "title": "Updated value",
      "description": "The updated value for the domain record property",
      "order": 4
    }
  },
  "required": [
    "domain_name",
    "property",
    "record_id",
    "value"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateDomainRecordOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Successful",
      "description": "Update status. True if successful, false otherwise",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)