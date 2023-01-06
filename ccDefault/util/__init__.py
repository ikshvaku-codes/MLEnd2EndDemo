import yaml
from ccDefault.exception import CCDefaultException
import sys
def read_yaml(filepath: str)->dict:
    try:
        with open(filepath, 'rb') as f:
            return yaml.safe_load(f)
    except Exception as e:
            raise CCDefaultException(e,sys) from e