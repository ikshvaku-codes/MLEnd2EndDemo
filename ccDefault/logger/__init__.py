import logging, os
from datetime import datetime
LOG_DIR = "ccDefault_logs"

CURRENT_TIMESTAMP = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

LOG_FILENAME = f'log_{CURRENT_TIMESTAMP}.log'

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILEPATH = os.path.join(LOG_DIR, LOG_FILENAME)

logging.basicConfig(filename=LOG_FILEPATH,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level= logging.INFO
)