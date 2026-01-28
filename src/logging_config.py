import os
import logging
from config import log_file

def logging_configuration():

    if not log_file:
            print("ERROR: LOG_FILE_PATH is not set or is none!")
            return logging.getLogger()
    try:
        logging.basicConfig(level=logging.DEBUG, 
        format="%(asctime)s:%(levelname)s:%(message)s",
        handlers=[logging.FileHandler(filename=log_file, 
        mode="w"), logging.StreamHandler()])
        logger = logging.getLogger()
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        logging.info("Logging setup complete!")
        return logger
    
    except PermissionError:
        print(f"Permission denied: Cannot write to {log_file}.")
        return logging.getLogger()

    except FileNotFoundError:
        print(f"File path not found: {log_file}")
        return logging.getLogger()
    
    except Exception as e:
        print(f"ERROR: Logging setup failed to complete {e}")
        logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
        logging.warning("Falling back to basic level configuration.")
        return logging.getLogger()

if __name__ == "__main__":
    logging_configuration()