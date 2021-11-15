# Logging with Scrapy

# debug information can be useful, but is often too verbose
# can adjust the level of logging by adding a line to the settings.py file:
# LOG_LEVEL = 'Error'

# hierarchy of logging levels:
# CRITICAL
# ERROR
# WARNING
# DEBUG
# INFO

# if logging is set to ERROR, only CRITICAL and ERROR logs will be displayed
# if logging is set to INFO, all logs will be displayed, and so on

# can control where the logs go, to output to a separate logfile run:
# $ scrapy crawl articles -s LOG_FILE=wiki.log

