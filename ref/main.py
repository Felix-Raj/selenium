import logging
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout, datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)
stdout = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter('%(asctime)s %(funcName)s %(lineno)d %(message)s')
stdout.setFormatter(formatter)
logger.addHandler(stdout)
logger.setLevel(logging.INFO)