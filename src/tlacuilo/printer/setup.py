import logging

from escpos import printer

from tlacuilo.core import config

logger = logging.getLogger(__name__)


def get_printer():
    logger.info("Defining Printer")

    p = printer_conn()

    try:
        run_checks(p)
    except Exception as e:
        logger.error(f"Printer Says No:{e}")

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


def run_checks(Printer):
    try:
        check_online(Printer)
    except Exception as e:
        logger.error(f"Online Check Failed:{e}")

    try:
        check_paper(Printer)
    except Exception as e:
        logger.error(f"Paper Check Failed:{e}")


def check_online(Printer):
    try:
        Printer.is_online()
    except Exception as e:
        logger.error(f"Printer Not Online{e}")
    return


def check_paper(Printer):
    paper_state = Printer.paper_status()
    if paper_state == 2:
        logger.debug("Paper is adequate")
        return True
    if paper_state == 1:
        logger.warning("Paper ending")
        return True

    if paper_state == 0:
        logger.error("No Paper")
        return False
