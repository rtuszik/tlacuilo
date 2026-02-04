import logging

from escpos import printer

from tlacuilo.core import config

logger = logging.getLogger(__name__)


def get_printer():
    logger.info("Defining Printer")

    p = printer_conn()
    logger.info("printer connected")
    printer_check(p)
    return p


def printer_conn():
    if config.CONNECTION_METHOD == "Network":
        try:
            p = printer.Network(
                config.PRINTER_IP,
                timeout=10,
            )
            logger.info("Printer Network Yes Yes")
        except:
            logger.error("Unable to Connect")

    elif config.CONNECTION_METHOD == "USB":
        try:
            p = printer.Usb(0x04B8, 0x0202)
            logger.info("Printer USB Yes Yes")
        except:
            logger.error("Unable to Connect")
    return p


def printer_check(Printer):

    paper_state = Printer.paper_status()
    if paper_state == 2:
        logger.info("Paper is adequate")
        return
    if paper_state == 1:
        logger.info("Paper ending")
        return

    if paper_state == 0:
        logger.info("No Paper")
        return
