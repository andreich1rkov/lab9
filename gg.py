import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")



logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")