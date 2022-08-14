import logging
from socket import socket, AF_INET, SOCK_DGRAM


class SplunkHandler(logging.Handler):
    """
    logging handler for sending logs to splunk
    """        
    def __init__(self):
        logging.Handler.__init__(self)
        self.s = socket(AF_INET, SOCK_DGRAM, 0)

    def emit(self, record):
        msg: logging.LogRecord = self.format(record)
        msg = f"<1>{msg}".encode('utf-8')
        self.s.sendto(msg, ('', 9900))
        pass