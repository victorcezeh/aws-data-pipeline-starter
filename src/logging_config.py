import os
import logging
from dotenv import load_dotenv

try:

 load_dotenv()
except Exception as e:
    print(f"Failed to load the .env file {e}")

log_file = os.getenv("LOG_FILE_PATH")

def logging_config():
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
    
    except PermissionError:
        print(f"Permission denied: Cannot write to {log_file}.")

    except FileNotFoundError:
        print(f"File path not found: {log_file}")
    
    except Exception as e:
        print(f"ERROR: Logging setup failed to complete {e}")
        logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
        logging.warning("Falling back to basic level configuration.")

if __name__ == "__main__":
    try:
        logger = logging_config()
        logger.info("Testing 1,2,3!")
    except AttributeError:
        print("There is a problem with your function!")