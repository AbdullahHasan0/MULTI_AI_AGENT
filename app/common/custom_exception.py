import sys

class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception = None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message: str, error_detail):
        _, _, exc_tb = sys.exc_info()
        if exc_tb is not None:
            line_number = exc_tb.tb_lineno
            file_name = exc_tb.tb_frame.f_code.co_filename
            detailed_message = f"Error occurred in file: {file_name}, line number: {line_number}, message: {message}"
        else:
            detailed_message = message
        if error_detail:
            detailed_message += f" | Additional details: {str(error_detail)}"
        return detailed_message
    
   
    def __str__(self):
        return self.error_message