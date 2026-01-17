import logging

logging.basicConfig(level=logging.DEBUG, 
                    filename="log.log", 
                    filemode="w", 
                    format="%(asctime)s - %(levelname)s - %(message)s")


logger = logging.getLogger(__name__)

handler = logging.FileHandler('test.log')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("Test custom")
