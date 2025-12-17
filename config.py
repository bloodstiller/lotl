#!/usr/bin/env python3

import argparse
from pathlib import Path

class Config:
    def __init__(self, args):
        self.domain = args.domain
        self.subdomain = args.subdomain
        self.https = args.https
        self.job = args.job
        self.output = Path("scans") / self.job

        proto = "https" if self.https else "http"
        host = f"{self.subdomain}.{self.domain}" if self.subdomain else self.domain
        self.target_url = f"{proto}://{host}"
        self.target_host = host

        self.output.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def from_args():
        p = argparse.ArgumentParser(description="Modular Enumeration Framework")
        p.add_argument("-d", "--domain", required=True)
        p.add_argument("-s", "--subdomain")
        p.add_argument("--http", dest="https", action="store_false")
        p.add_argument("-j", "--job", required=True)
        return Config(p.parse_args())
