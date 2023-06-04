import os 
import sys
import logging

loging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs_details"
log_filename = "running_logs_cnn.log"
log_file_path = os.path.join(log_dir, log_filename)
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=loging_str,

    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]

)
logger = logging.getLogger("cnnClassifierLogger")
