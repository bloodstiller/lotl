#!/usr/bin/env python3

from utils.runner import run as run_command

def run(cfg, log):
    log.info("Running Katana Crawler Scan")
    out = cfg.output / "katana"
    outfile = out / "katana.txt"

    out.mkdir(exist_ok=True)

    cmd = [
        "katana",
        "-u", cfg.target_url, 
        "-o", str(outfile)
    ]

    if cfg.proxy:
        cmd.extend(["-proxy", cfg.proxy])

    run_command(cmd, log)
