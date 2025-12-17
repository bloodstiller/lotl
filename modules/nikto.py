#!/usr/bin/env python3

from utils.runner import run as run_command

def run(cfg, log):
    log.info("Running Nikto web scan")
    out = cfg.output / "nikto"
    outfile = out / "nikto.txt"

    out.mkdir(exist_ok=True)

    cmd = [
        "nikto",
        "-h", cfg.target_url,
        "-output", str(outfile)
    ]

    run_command(cmd, log)
