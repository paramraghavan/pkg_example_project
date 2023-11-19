import traceback

def printStackTrace(message:str) -> str:
   traceback_error_msg = traceback.format_exc()
   trace:str = f'{80*"-"}\n{message}:\n{80*"-"}\n{traceback_error_msg}{80*"-"}'
   return trace
