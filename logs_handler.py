import logging

# Configures loggers for stage acknowledgment
class MediaMonksLogger():
 
    def __init__(self, loggername:str, stream_logs: bool = True) -> None:
 
        self.stream_logs = stream_logs
        self.loggername = loggername
 
        # setup basic logging configuration
        logging.basicConfig(
            filename='logfile.log',
            filemode='a',  # append new logs
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
 
        # Gets or creates a logger
        self.logger = logging.getLogger(self.loggername)
 
        # set log level
        self.logger.setLevel(logging.DEBUG)
 
        # console logs handler
        if self.stream_logs is True:
            self.stream_handler = logging.StreamHandler()
            self.stream_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(self.stream_handler)