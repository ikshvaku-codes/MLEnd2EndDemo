import os, sys


class CCDefaultException(Exception):
    def __init__(self, error_message:Exception, error_detail:sys):
        """
        error_message:Exception module will raise this exception message
        error_detail:sys module will return the details about the exception like in which file and line is causing the error etc.
        """
        super().__init__(error_message)
        self.error_message = CCDefaultException.get_error_message(error_message=error_message,
                                                                  error_detail=error_detail)

    @staticmethod
    def get_error_message(error_message:Exception, error_detail:sys)->str:
        """
        error_message: Exception Object
        error_detail: object of sys module
        This method will return the details about the error message in a particular format.
        """
        _,_,exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occurred in script: {file_name} in line {line_number}: {error_message}."
        return error_message
    
    def __str__(self) -> str:
        return self.error_message
    
    def __repr__(self) -> str:
        return CCDefaultException.__name__.str()

    
