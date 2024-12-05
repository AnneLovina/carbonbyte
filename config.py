# config.py
from forms import ServerInfrastructureForm, StorageForm, NetworkingForm

FORM_CONFIG = {
    1: {
        "title": "TITEL",
        "description": "description",
        "form_class": ServerInfrastructureForm,
        "session_key": "server_data",
        "data_mapping": {
            "server_location": "location",
            "server_type": "type",
            "cpu_usage": "cpu_usage",
        },
    },
    2: {
        "title": "TITEL",
        "description": "description",
        "form_class": StorageForm,
        "session_key": "storage_data",
        "data_mapping": {"storage_type": "type", "storage_amount": "amount"},
    },
    3: {
        "title": "TITEL",
        "description": "description",
        "form_class": NetworkingForm,
        "session_key": "networking_data",
        "data_mapping": {"monthly_bandwidth": "bandwidth", "cdn_usage": "cdn"},
    },
}
