import logging

def main() -> None:
    #set starting point of log level what to show
    logging.basicConfig(level=logging.DEBUG,
                        format=" %(asctime)s - %(levelname)s - %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        filename="basic.log"
                        )

    logging.debug("This is a debug message")
    logging.info("This is and info message")
    logging.warning("This is warning message")
    logging.error("This is warning message")
    logging.critical("This is warning message")



if __name__ == "__main__":
    main()