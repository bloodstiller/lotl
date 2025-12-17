#!/usr/bin/env python3

import logging
from pathlib import Path

# Optional: colored output
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Dummy:
        RED = GREEN = YELLOW = RESET = RESET_ALL = ""
    Fore = Style = Dummy()

def setup_logger(cfg):
    """
    Creates a logger that logs to both console and file.
    """
    log_file = cfg.output / f"{cfg.job}.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Create logger
    logger = logging.getLogger(cfg.job)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False  # Avoid double logs

    # File handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))
    logger.addHandler(fh)

    # Console handler
    ch = logging.StreamHandler()
    # Change to (logging.info) to reduce verbose logging
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(ch)

    # Save original methods
    _info = logger.info
    _warning = logger.warning
    _error = logger.error
    
    # Add convenience colored methods
    def info(msg):
        _info(f"{Fore.GREEN}[+] {msg}{Style.RESET_ALL}")
    
    def warning(msg):
        _warning(f"{Fore.YELLOW}[!] {msg}{Style.RESET_ALL}")
    
    def error(msg):
        _error(f"{Fore.RED}[-] {msg}{Style.RESET_ALL}")
    
    logger.info_colored = info
    logger.warn_colored = warning
    logger.error_colored = error
    
    # Replace methods with colored versions
    logger.info = info
    logger.warning = warning
    logger.error = error

    return logger


