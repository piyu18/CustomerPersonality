import os, sys
class CustomException(Exception):
    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message = CustomException.get_detailed_error_message(error_message=error_message, error_detail=error_detail)
    
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:
        _, _, exec_tb = error_detail.exc_info()
        exception_block_line_no = exec_tb.tb_frame.f_lineno
        try_block_line_no = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = (f"""
                Error occurred in script:
                [{file_name}] at try block line no: [{try_block_line_no}]
                and exception block line no: [{exception_block_line_no}]
                error message: [{error_message}]

                         """)
        return error_message

    def __str__(self):
        return self.error_message
    
    def __repr__(self)->str:
        return CustomException.__name__.str()