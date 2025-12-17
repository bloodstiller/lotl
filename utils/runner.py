#!/usr/bin/env python3

import subprocess

def run(cmd, log, timeout=1800):
    log.debug(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
            text=True
        )

        if result.stdout:
            for line in result.stdout.splitlines():
                log.debug(line)
        
        if result.stderr:
            for line in result.stderr.splitlines():
                log.debug(line)

        return True
    except subprocess.TimeoutExpired:
        log.warning("Command timed out")
        return False
