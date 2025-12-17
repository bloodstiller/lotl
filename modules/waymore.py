#!/usr/bin/env python3

from utils.runner import run as run_command

def run(cfg, log):
    log.info("Running Waymore")
    out = cfg.output / "waymore"
    outfile = out / "waymoreURLS.txt"

    out.mkdir(exist_ok=True)

    cmd = [
        "waymore",
        "-i", cfg.target_url,
        "-mode", "U",
        "-oU", str(outfile),
        "-lcc", "1"
    ]

    if cfg.proxy:
        cmd.extend(["-p", cfg.proxy])
        

    run_command(cmd, log)
