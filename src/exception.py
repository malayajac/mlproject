import sys
import logging

def error_message_details(error, error_detail:sys):
	_, _, exc_tb = error_detail.exc_info()

	file_name = exc_tb.tb_frame.f_code.co_filename
	lineno = exc_tb.tb_lineno
	err_msg = str(error)
	error_message = f"Error occured in python script [{file_name}],\nline number [{lineno}],\nerror message [{err_msg}]"

	return error_message


class CustomException(Exception):
	def __init__(self, error_message, error_detail:sys):
		super().__init__(error_message)
		self.error_message = error_message_details(error_message, error_detail=error_detail)

	def __str__(self):
		return self.error_message

#-------------------------------------------------------------------
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)


FORMAT = '[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(
	filename=LOG_FILE_PATH,
	format=FORMAT,
	level=logging.INFO,
)
#-------------------------------------------------------------------
if __name__=="__main__":
	try:
		a = 1/0
	except Exception as e:
		logging.info("Divide by zero")
		raise CustomException(e, sys)