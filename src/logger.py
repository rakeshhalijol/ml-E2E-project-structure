from datetime import datetime
import logging
import os

LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(log_path, exist_ok=True)


LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)


# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,  # Log all levels (DEBUG and above)
    format="%(asctime)s - [Line: %(lineno)d] - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


# Create a custom logger
# logger = logging.getLogger("MyLogger")
# logger.debug("Debug message")
# logger.info("Info message")
