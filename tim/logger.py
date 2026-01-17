import logging


logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

x = 2

# # import level wise 
# logging.debug(f"The value of x is {x}")
# logging.info("info")

# logging.warning("warninggg")
# logging.error("errorrrr")
# logging.critical("criticialllll")

try: 
    1/0
except ZeroDivisionError as e:
    # logging.error("zero dividion error", exc_info=True)
    logging.exception("zero dividion error")