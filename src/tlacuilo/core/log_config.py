from uvicorn.config import LOGGING_CONFIG

LOGGING_CONFIG = LOGGING_CONFIG.copy()

LOGGING_CONFIG["loggers"] = dict(LOGGING_CONFIG["loggers"])

LOGGING_CONFIG["loggers"]["tlacuilo"] = {
    "handlers": ["default"],
    "level": "INFO",
    "propagate": False,
}
