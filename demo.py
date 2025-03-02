# from src.logger import logging

# logging.debug("this is debug message")
# logging.info("this is info message")
# logging.warning("this is warning message")
# logging.error("this is error message")
# logging.critical("this is critical message")

# from src. logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()
