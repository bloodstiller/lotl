#!/usr/bin/env python3

from utils.runner import run as run_command

def run(cfg, log):
    log.info("Running WhatWeb")
    out = cfg.output / "whatweb"
    out.mkdir(exist_ok=True)

    outfile = out / "tech.txt"

    cmd = [
        "whatweb",
        cfg.target_url,
        "-a", "3",
        
        "--log-verbose", str(outfile)
    ]

    if cfg.proxy:
        cmd.extend(["--proxy", cfg.proxy])

    run_command(cmd, log)

    data = outfile.read_text(errors="ignore").lower()
    return data
