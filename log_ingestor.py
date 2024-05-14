import logging
import json
from logging.handlers import RotatingFileHandler
from datetime import datetime

# Load configuration
def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

# Setup loggers for each API
def setup_loggers(config):
    loggers = {}
    for api, settings in config['apis'].items():
        logger = logging.getLogger(api)
        logger.setLevel(getattr(logging, settings['log_level'].upper()))
        handler = RotatingFileHandler(settings['file_path'], maxBytes=1000000, backupCount=3)
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        loggers[api] = logger
    return loggers

# Example function to log messages
def log_message(api, level, message, loggers, config):
    if api in loggers:
        logger = loggers[api]
        timestamp = datetime.utcnow().isoformat() + 'Z'
        log_entry = {
            "level": level,
            "log_string": message,
            "timestamp": timestamp,
            "metadata": {
                "source": config['apis'][api]['file_path']
            }
        }
        logger.log(getattr(logging, level.upper()), json.dumps(log_entry))

# Example API integration
def api_function(api_name, loggers, config):
    try:
        # API logic here
        log_message(api_name, 'info', 'API function called successfully.', loggers, config)
    except Exception as e:
        log_message(api_name, 'error', f'API function failed: {e}', loggers, config)

if __name__ == '__main__':
    config = load_config()
    loggers = setup_loggers(config)
    
    # Simulate API function calls
    api_function('api1', loggers, config)
    api_function('api2', loggers, config)
    api_function('api3', loggers, config)
