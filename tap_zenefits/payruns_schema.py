import json


class Payruns:
    schema = {
        "properties": {
            "company": {
                "url": {
                    "type": ["string", "null"]
                },
                "object": {
                    "type": ["string", "null"]
                },
                "ref_object": {
                    "type": ["string", "null"]
                }
            },
            "check_date": {
                "type": ["string", "null"]
            },
            "original_check_date": {
                "type": ["string", "null"]
            },
            "payrun_type": {
                "type": ["string", "null"]
            },
            "status": {
                "type": ["string", "null"]
            },
            "start_date": {
                "type": ["string", "null"]
            },
            "end_date": {
                "type": ["string", "null"]
            },
            "people": {
                "url": {
                    "type": ["string", "null"]
                },
                "object": {
                    "type": ["string", "null"]
                },
                "ref_object": {
                    "type": ["string", "null"]
                }
            },
            "url": {
                "type": ["string", "null"]
            },
            "object": {
                "type": ["string", "null"]
            },
            "id": {
                "type": ["string", "null"],
                "key": True
            }
        }
    }