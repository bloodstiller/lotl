#!/usr/bin/env python3

from utils.runner import run as run_command
from pathlib import Path
import os

def run(cfg, log):
    log.info("Running Nuclei scan")

    out = cfg.output / "nuclei"
    outfile = out / "nuclei.txt"

    out.mkdir(exist_ok=True)

    templates = os.getenv(
        "NUCLEI_TEMPLATES",
        str(Path.home() / "nuclei-templates/http")
    )

    if not Path(templates).exists():
        log.warning(f"Nuclei templates not found: {templates}")
        return

    cmd = [
        "nuclei",
        "-u", cfg.target_url,
        "-t", templates,
        "-o", str(outfile),
        "-severity", "low,medium,high,critical"
    ]


    run_command(cmd, log)

   # nuclei -u "https://www.ofwat.gov.uk" -t ~/nuclei-templates/http/technologies/ --proxy http://127.0.0.1:8080
