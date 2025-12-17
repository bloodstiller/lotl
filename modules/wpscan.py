#!/usr/bin/env python3

import os
from utils.runner import run as run_command

def run(cfg, log):
    token = os.getenv("WPSCAN_API_TOKEN")
    if not token:
        log.warning("WPScan API token not set")
        return

    log.info("Running WPScan")
    out = cfg.output / "wpscan"
    out.mkdir(exist_ok=True)

    cmd = [
        "wpscan",
        "--url", cfg.target_url,
        "--random-user-agent",
        "--api-token", token,
        "-o", str(out / "wpscan.txt")
    ]


    run_command(cmd, log)
