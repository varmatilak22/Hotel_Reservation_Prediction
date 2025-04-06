import traceback
import sys


class CustomException(Exception):
    def __init__(self,error_msg,error_details:sys):
        super().__init__(error_msg)
        self.error_msg=self.get_detailed_error_msg(error_msg)
    
    @staticmethod
    def get_detailed_error_msg(error_msg):
        _,_,exc_tb=sys.exc_info()
        file_name=exc_tb.tb_frame.f_code.co_filename
        line_number=exc_tb.tb_lineno # type: ignore
        return f"Error in {file_name},line {line_number} : {error_msg}"
    
    def __str__(self):
        return self.error_msg



