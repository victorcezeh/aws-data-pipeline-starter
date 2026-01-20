import os
import logging
from dotenv import load_dotenv

try:

 load_dotenv()
except Exception as e:
    print(f"Failed to load the .env file {e}")

log_file = os.getenv("LOG_FILE_PATH")

def logging_configuration():
    try:
        if not log_file:
            raise TypeError("LOG_FILE_PATH is not set or is None")

        logging.basicConfig(level=logging.DEBUG, 
        format="%(asctime)s:%(levelname)s:%(message)s",
        handlers=[logging.FileHandler(filename=log_file, 
        mode="w"), logging.StreamHandler()])
        logger = logging.getLogger()
        logging.info("Logging setup complete!")
        return logger
    
    except TypeError as e:
        print(f"Error: Log file path invalid: {e}.")
        return logging.getLogger()
    
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