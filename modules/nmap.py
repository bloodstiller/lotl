#!/usr/bin/env python3

from utils.runner import run as run_command

def run(cfg, log):
    log.info("Running Nmap")
    out = cfg.output / "nmap"

    out.mkdir(exist_ok=True)

    tcpScan = [
        "sudo", "nmap",
        "-sV", "-sC", "-O", "-T3",
        "-oA", str(out / "tcp"),
        cfg.target_host
    ]

    udpScan = [
        "sudo", "nmap",
        "-sU", "--top-ports=100",
        "-oA", str(out / "udp"),
        cfg.target_host
    ]

    run_command(tcpScan, log)
    run_command(udpScan, log)
