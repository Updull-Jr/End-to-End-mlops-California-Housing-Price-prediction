import os
import sys

class HousingException(Exception): # inheriting python exception class to our own custon exception class
    
    def __init__(self, error_message:Exception, error_detail:sys):
        #error_msg ~ will be type of exception, it'll be the object/instance of exception
        # error_detail ~ helps show system related errors, where the exception occured, which file/line 
            #couses the error.

        super().__init__(error_message) #passing the error_message to the parent class i.e. Exception(error_message)
        self.error_message = HousingException.get_detailed_error_message(error_message =error_message, error_detail= error_detail) 


          #let's also customie the error_detail msg.
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:

            """
            error_message : Exception object
            error_detail : object or sys module
            """
            _,_ ,exec_tb = error_detail.exc_info()
            line_number = exec_tb.tb_frame.f_lineno
            file_name = exec_tb.tb_frame.f_code.co_filename
            error_message = f"Error occured in scrip: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
            return error_message

    def __str__(self):
        return self.error_message


    def __repr__(self) -> str:
        return HousingException.__name__.str()
            

            
# sys.exc_info() ~ This function returns the old-style representation of the handled exception. 
#  If an exception e is currently handled (so exception() would return e), exc_info() 
#   returns the tuple (type(e), e, e.__traceback__). That is,a tuple containing the type of the 
#    exception (a subclass of BaseException), the exception itself, an a traceback object which typically 
#     encapsulates the call stack at the point where the exception last occurred.

# filename ~ For syntax errors - the file name where the error occurred.
# lineno ~ For syntax errors - the line number where the error occurred.
 
